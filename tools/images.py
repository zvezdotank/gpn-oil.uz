# -*- coding: utf-8 -*-
"""Готовит картинки сайта одним конвейером.

Снимки собраны из разных источников: часть — пресс-фото завода, часть —
съёмка склада, часть — рендеры. У них разная температура, насыщенность
и яркость, и на странице это читается как случайный сток. Поэтому все
проходят одну обработку: нормализация гистограммы, приглушение цвета
и общий холодный тон. После неё разные кадры выглядят одним набором.

Мелкие исходники и рекламные баннеры с текстом сюда не берём — они
дешевят страницу сильнее, чем помогает наличие картинки.
"""
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
from PIL import Image, ImageEnhance, ImageOps
import os

SRC = _os.path.join(ROOT, "tools", "photo-src")
OUT = _os.path.join(ROOT, "img")
TINT = (0, 92, 185)          # фирменный синий Газпромнефти


def unify(im):
    im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageEnhance.Color(im).enhance(0.70)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    im = Image.blend(im, Image.new("RGB", im.size, TINT), 0.05)
    return ImageEnhance.Brightness(im).enhance(1.02)


def crop_to(im, ratio):
    w, h = im.size
    if w / h > ratio:
        nw = int(h * ratio)
        return im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    nh = int(w / ratio)
    y = int((h - nh) * 0.40)
    return im.crop((0, y, w, y + nh))


# Страницы, где вёрстка просит промежуточный размер между полным и половинным.
MD = {"hero", "company", "company-office", "gpn", "grease", "price", "products"}


def save(im, name, width, q=78, qa=55):
    """Пишет каждый размер сразу в WebP и AVIF.

    Раньше AVIF делались отдельным ручным шагом, и это уже приводило к тому,
    что после замены снимка страница показывала старую картинку: браузер
    берёт из <picture> первый подходящий источник, а это AVIF.
    """
    r = im.size[0] / im.size[1]
    width = min(width, im.size[0])

    def write(w, suffix=""):
        v = im.resize((w, round(w / r)), Image.LANCZOS)
        v.save(os.path.join(OUT, name + suffix + ".webp"), "WEBP", quality=q, method=6)
        v.save(os.path.join(OUT, name + suffix + ".avif"), "AVIF", quality=qa)
        return v.size

    big = write(width)
    if name in MD and width > 960:
        write(960, "-md")
    write(max(400, width // 2), "-sm")
    return big


# исходник, имя, соотношение, ширина. Только крупные и «неглянцевые» кадры.
JOBS = [
    ("plant-1.jpg",      "hero",            1.34, 1400),   # линия розлива канистр
    ("lab-tester.jpg",   "podbor",          1.36,  900),   # испытание масла в лаборатории
    ("oils-row.jpeg",    "company",         1.34, 1200),   # специалисты у бочки
    ("tank-farm.jpg",    "products",        1.78, 1400),   # парк резервуаров завода

    # карточки каталога
    ("industrial.jpg",   "cat-industrial",  1.9,   800),
    ("canister.jpg",     "cat-gpn",         1.9,  1200),
    ("g-energy-1.jpg",   "cat-g-energy",    1.9,  1024),
    ("grease-photo.png", "cat-grease",      1.9,  1280),
    ("reductor.jpg",     "cat-transmission",1.9,  1200),
    ("coolant.jpg",      "cat-fluids",      1.9,  1200),

    # шапки страниц
    ("industrial.jpg",   "industrial",      2.6,   800),
    ("hydraulic.jpeg",   "hydralic",        2.6,  1200),
    ("reductor.jpg",     "reductor",        2.6,  1200),
    ("compressor.jpg",   "compressor",      2.6,  1024),
    ("grease-photo.png", "grease",          2.6,  1280),
    ("canister.jpg",     "gpn",             2.6,  1400),
    ("g-energy-1.jpg",   "g-energy",        2.6,  1024),
    ("coolant.jpg",      "fluids",          2.6,  1200),
    ("hero-warehouse.jpg","price",          2.6,  1400),
    ("oils-row.jpeg",    "company-office",  2.6,  1400),
]

for src, name, ratio, width in JOBS:
    im = Image.open(os.path.join(SRC, src)).convert("RGB")
    print(name, save(unify(crop_to(im, ratio)), name, width))

# Логотипы заказчиков: у исходников фон то белый, то прозрачный, то тёмный.
# Кладём все на одну белую карточку одного размера — тогда ряд не рябит.
# Цвет оставляем в файле, обесцвечивание делает css, чтобы на наведении
# логотип возвращался в свой цвет.
LOGOS = [("logo-ngmk.jpg", "logo-ngmk"), ("logo-ee.png", "logo-enter"),
         ("logo-ttb.png", "logo-ttz"), ("logo-ahac.jpg", "logo-ahangaran"),
         ("logo-nc.png", "logo-cement")]

for src, name in LOGOS:
    im = Image.open(os.path.join(SRC, src)).convert("RGBA")
    # тёмные подложки в исходниках инвертируем в белый фон
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    flat = Image.alpha_composite(bg, im).convert("RGB")
    if sum(flat.resize((1, 1)).getpixel((0, 0))) < 240:      # фон тёмный
        flat = ImageOps.invert(flat)
    card = Image.new("RGB", (360, 180), (255, 255, 255))
    flat.thumbnail((280, 108), Image.LANCZOS)
    card.paste(flat, ((360 - flat.size[0]) // 2, (180 - flat.size[1]) // 2))
    card.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=88, method=6)
    print(name, (360, 180))

for junk in ("cat-industrial-sm", "hero-sm"):
    pass
total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith(".webp"))
print("вес картинок: %.0f КБ" % (total / 1024))
