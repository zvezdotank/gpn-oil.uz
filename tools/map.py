# -*- coding: utf-8 -*-
"""Собирает статичную картинку карты офиса.

Раньше на странице контактов стоял встроенный виджет Яндекса: внешний
iframe, который тянет свой скрипт, тайлы и счётчики уже после загрузки
страницы. Это самый тяжёлый элемент на странице и единственный, ради
которого браузер посетителя ходил на чужой домен.

Здесь карта собирается один раз на сборке из тайлов OpenStreetMap и
кладётся к себе в img/. В момент открытия страницы наружу не уходит
ни одного запроса.

Карта не просто перекрашена — она пересобрана. Тайлы OSM рисуют весь
город одинаково подробно, и на картинке в пол-экрана это каша. Из кадра
убрано всё, что не помогает понять «где это»: дома, мелкие подписи,
значки заведений. Осталось пять вещей, по которым место узнают:
стадион «Старт», Салар, Кичик халка йўли, Мустакиллик и железная дорога.
Река нарисована оранжевым — после метки офиса это единственное тёплое
пятно на холодном кадре.

Требование лицензии OSM: под картой обязательна подпись
«© OpenStreetMap» со ссылкой на openstreetmap.org/copyright.
Она стоит в разметке страницы контактов.

Запуск: python3 tools/map.py
"""
import io
import math
import os
import time
import urllib.request

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img")
CACHE = os.path.join(ROOT, "tools", "map-cache")

LAT, LON = 41.3230571, 69.312125
ZOOM = 17
COLS, ROWS = 11, 6         # вчетверо подробнее нужного, потом уменьшаем вдвое
TILE = 256
UA = "gpn-oil.uz static map builder (contact page, one-off build)"


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ─────────────────────────────────────────────────────────────────────────
# Перекраска
#
# У OpenStreetMap каждый тип объекта нарисован своим конкретным цветом,
# поэтому цвета подменяются прицельно: каждый пиксель относится к
# ближайшему цвету исходной палитры и заменяется на парный ему. Разбор
# по оттенку, который пробовали до этого, оказался слишком грубым — под
# «жёлто-оранжевые дороги» попадали контуры зданий и подписи.
#
# Цвета исходной палитры взяты не из документации, а замером по самим
# тайлам этого куска города: у шестидесяти тайлов посчитана гистограмма,
# и в список попало всё, что занимает заметную долю кадра.
ANCHORS = [
    ("LAND", "f2efe9 e0dfdf ededed f6f6f6 dedddd dad9d9 d4d3d3 cccbcb eeeeee "
             "ede9e6 e4e3e3 dddcdc d2d1d1 cecdcd f2dad9 fff1d9 dddde8 ffe4ce"),
    ("BUILD",      "d9d0c9 dcc6c0 d8cec7 d6cdc6 d4cbc4"),
    ("BUILD_EDGE", "c2b5aa c9bdb4 c6bbb1 c8bbb1"),
    ("GREEN",      "dffce2 cdebb0 add19e c8d7ab c7c7b4"),
    ("PITCH",      "88e0be 92d4b6"),
    ("WATER",      "aad3df b5d0d0"),
    ("RAILAREA",   "ebdbe8"),
    ("RAIL",       "707070 717171"),
    ("MAJOR",      "e892a2 f9b29c"),      # магистраль и шоссе
    ("PRIMARY",    "fcd6a4"),             # главная улица
    ("SECOND",     "f7fabf ffffe5"),      # второстепенная и третьестепенная
    ("ROAD",       "ffffff"),
    ("ROAD_EDGE",  "c5c5c5 aaaaaa c5c4c4 c5c5c4 c6c6c6"),
    ("LABEL",      "333333 000000"),
    ("POI",        "0092da 734a08 dd366e ac39ac"),
]
SRC, KEY = [], []
for _role, _hexes in ANCHORS:
    for _h in _hexes.split():
        SRC.append(rgb(_h))
        KEY.append(_role)
SRC = np.array(SRC, dtype=np.int32)
KEY = np.array(KEY)

# Палитра сайта. Дома и мелкие площадки уводим в цвет фона: на карте
# такого размера застройка читается как рябь, а не как информация —
# человек смотрит сюда, чтобы понять «где это примерно», маршрут он
# всё равно строит в своём приложении.
PAL = dict(
    LAND="F8FAFB",        # --surface-2
    BUILD="F8FAFB",       # дома убраны
    BUILD_EDGE="F8FAFB",
    GREEN="EDF2EE",       # парки — едва заметный холодный зелёный
    PITCH="CFE6F7",       # --on-blue, поля стадионов
    WATER="E0700C",       # --accent, Салар
    RAILAREA="E9EDF1",    # полоса отвода железной дороги
    RAIL="0C1A24",        # --ink, рельсы
    MAJOR="0A1C28",       # --navy, магистрали
    PRIMARY="24485D",     # главные улицы
    SECOND="E4E9ED",      # второстепенные — почти фон
    ROAD="FFFFFF",
    ROAD_EDGE="DFE4E8",   # --rule, кромка улиц
    LABEL="F8FAFB",       # подписи OSM стираем, вместо них свои
    POI="F8FAFB",         # значки заведений тоже
    MARK="0A1C28",        # обод метки офиса
    MARK_DOT="E0700C",    # сердцевина метки
)

INK, MUTED = rgb("0C1A24"), rgb("54636E")

# Подписи. Координаты — в готовой картинке 1200x600, выверены по кадру.
# Угол поворота повторяет направление улицы: 77° — коридор Кичик халка
# йўли и железной дороги, 18° — Мустакиллик.
LABELS = [
    (332, 152, "Стадион «Старт»",  700, 19, 0.00, INK,            0),
    (293, 340, "Салар",            600, 15, 0.10, rgb("C25F06"),  0),
    (548, 450, "Кичик халка йўли", 600, 14, 0.12, MUTED,         77),
    (873, 222, "Мустакиллик",      600, 14, 0.12, MUTED,         18),
    (668, 470, "Железная дорога",  600, 13, 0.12, MUTED,         77),
]


# ─────────────────────────────────────────────────────────────────────────
# Тайлы

# Зеркала. Стиль у всех один — OSM Carto, — поэтому перекраска по цветам
# работает с любым. Основной сервер openstreetmap.org из части сетей
# недоступен, и сборка из-за этого падала целиком.
TILE_HOSTS = [
    "https://tile.openstreetmap.de/%d/%d/%d.png",
    "https://a.tile.openstreetmap.fr/osmfr/%d/%d/%d.png",
    "https://tile.openstreetmap.org/%d/%d/%d.png",
]


def tile_xy(lat, lon, z):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    la = math.radians(lat)
    y = (1 - math.log(math.tan(la) + 1 / math.cos(la)) / math.pi) / 2 * n
    return x, y


def fetch(z, x, y):
    # Тайлы кладём на диск: правка палитры иначе стоит минуты скачивания,
    # а сами тайлы не меняются. Папка в .gitignore, в репозиторий не идёт.
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, "%d-%d-%d.png" % (z, x, y))
    if os.path.exists(path):
        return Image.open(path).convert("RGB")

    last = None
    for host in TILE_HOSTS:
        for attempt in range(3):
            try:
                req = urllib.request.Request(host % (z, x, y), headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=30) as r:
                    data = r.read()
                time.sleep(0.08)      # тайлов под семьдесят, не долбим сервер очередью
                with open(path, "wb") as f:
                    f.write(data)
                return Image.open(io.BytesIO(data)).convert("RGB")
            except Exception as e:    # noqa: BLE001 — причина не важна, важен повтор
                last = e
                time.sleep(0.8 * (attempt + 1))
    raise RuntimeError("не удалось получить тайл %d/%d/%d: %s" % (z, x, y, last))


# ─────────────────────────────────────────────────────────────────────────
# Морфология: отделяем линии от букв

def shift(m, dx, dy):
    """Сдвиг булевой маски с заполнением нулями."""
    out = np.zeros_like(m)
    h, w = m.shape
    xd = slice(max(dx, 0), w + min(dx, 0))
    xs = slice(max(-dx, 0), w + min(-dx, 0))
    yd = slice(max(dy, 0), h + min(dy, 0))
    ys = slice(max(-dy, 0), h + min(-dy, 0))
    out[yd, xd] = m[ys, xs]
    return out


DIRS = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, 2), (2, -1), (1, -2)]


def linear_only(m, length=15):
    """Оставляет в маске только вытянутые линии, выбрасывая мелкие кляксы.

    Так отделяются кромки улиц от букв: подписи OSM нарисованы теми же
    серыми, что и обочины с рельсами, и по цвету их не различить. Зато
    улица тянется через весь кадр, а самый длинный штрих буквы — десяток
    точек. Маску сначала стачивают вдоль восьми направлений, потом
    наращивают обратно: выживает только то, что было длинным хотя бы
    в одном из них.
    """
    keep = np.zeros_like(m)
    for dx, dy in DIRS:
        e = m.copy()
        for k in range(1, length):
            e &= shift(m, -k * dx, -k * dy)
        d = e.copy()
        for k in range(1, length):
            d |= shift(e, k * dx, k * dy)
        keep |= d
    return keep


# ─────────────────────────────────────────────────────────────────────────
# Подписи

def _font(weight, size):
    """Тот же IBM Plex, что на сайте.

    В fonts/ лежит woff2, а Pillow его не читает, поэтому распаковываем
    в ttf рядом с кэшем тайлов. Держать отдельную копию шрифта в репозитории
    не хочется: после пересборки набора символов подписи на карте разъехались
    бы со шрифтом страницы.
    """
    os.makedirs(CACHE, exist_ok=True)
    ttf = os.path.join(CACHE, "plex-%d.ttf" % weight)
    src = os.path.join(ROOT, "fonts", "plex-%d.woff2" % weight)
    if not os.path.exists(ttf) or os.path.getmtime(ttf) < os.path.getmtime(src):
        from fontTools.ttLib import TTFont
        f = TTFont(src)
        f.flavor = None
        f.save(ttf)
    return ImageFont.truetype(ttf, size)


def text_layer(text, font, fill, track_em):
    """Слово с разрядкой и белым ореолом на прозрачном слое.

    Ореол нужен всегда: подпись ложится и на белое поле, и на тёмную
    магистраль, и без него на дороге она пропадает.
    """
    pad = 6
    sp = font.size * track_em
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    widths = [probe.textlength(ch, font=font) for ch in text]
    w = int(sum(widths) + sp * (len(text) - 1)) + pad * 2
    h = int(font.size * 1.9) + pad * 2
    layer = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    d = ImageDraw.Draw(layer)
    for halo in (True, False):
        x = pad
        for ch, cw in zip(text, widths):
            if halo:
                for ox in (-2, -1, 0, 1, 2):
                    for oy in (-2, -1, 0, 1, 2):
                        if ox or oy:
                            d.text((x + ox, pad + oy), ch, font=font,
                                   fill=(255, 255, 255, 240))
            else:
                d.text((x, pad), ch, font=font, fill=fill)
            x += cw + sp
    return layer


def put_label(base, x, y, text, font, fill, track_em, angle):
    """Ставит подпись центром в точку, при необходимости повернув её."""
    layer = text_layer(text, font, fill, track_em)
    if angle:
        layer = layer.rotate(angle, resample=Image.BICUBIC, expand=True)
    base.alpha_composite(layer, (int(x - layer.width / 2), int(y - layer.height / 2)))


# ─────────────────────────────────────────────────────────────────────────

def build():
    fx, fy = tile_xy(LAT, LON, ZOOM)
    x0, y0 = int(fx) - COLS // 2, int(fy) - ROWS // 2
    canvas = Image.new("RGB", (COLS * TILE, ROWS * TILE), (242, 239, 233))
    for dx in range(COLS):
        for dy in range(ROWS):
            canvas.paste(fetch(ZOOM, x0 + dx, y0 + dy), (dx * TILE, dy * TILE))

    # где на холсте оказалась точка офиса
    px = int((fx - x0) * TILE)
    py = int((fy - y0) * TILE)

    # Считаем в 32 битах: квадрат разницы по трём каналам доходит до 195 000,
    # в 16 бит это не влезает и молча переполняется — первая версия из-за
    # этого увела почти всю карту в тёмный.
    a = np.asarray(canvas).astype(np.int32)
    idx = ((a[:, :, None, :] - SRC[None, None, :, :]) ** 2).sum(3).argmin(2)
    out = np.array([rgb(PAL[k]) for k in KEY], dtype=np.uint8)[idx]
    role = KEY[idx]

    # Подписи и значки OSM убираем совсем — вместо них ставим свои. Прямая
    # замена по цвету стирает только сердцевину букв: их сглаженные края
    # покрашены в тот же серый, что и обочины с рельсами. Разделяет форма.
    cand = np.isin(role, ["ROAD_EDGE", "LABEL", "POI", "RAIL", "BUILD_EDGE", "ROAD"])
    lin = linear_only(cand)
    out[cand & ~lin] = rgb(PAL["LAND"])
    rail = (role == "RAIL") & lin

    # Названия улиц OSM пишет прямо по дороге, обводя буквы белым. Буквы мы
    # стёрли, а обводка осталась светлыми дырами в тёмной полосе: она тянется
    # вдоль дороги и проверку на длину проходит. Затыкаем дыры замыканием.
    # Перед ним — размыкание: полоса дороги шире десятка точек и его
    # переживает, а случайные буквы того же цвета стачиваются. Без этого
    # замыкание слепляет их в чёрные кляксы по всему кадру.
    for which in ("MAJOR", "PRIMARY"):
        m = Image.fromarray((role == which).astype(np.uint8) * 255)
        m = m.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(5))
        m = m.filter(ImageFilter.MaxFilter(17)).filter(ImageFilter.MinFilter(17))
        out[np.asarray(m) > 127] = rgb(PAL[which])

    # Река и рельсы в кадре — волосяные линии, а именно их человек и должен
    # увидеть. Утолщаем маски, но реку не пускаем на магистрали и рельсы,
    # иначе она перерезает мост. Сначала сжатие: одиночные пиксели, попавшие
    # в роль на сглаженных краях, после утолщения стали бы кляксами.
    protect = np.isin(role, ["MAJOR", "PRIMARY"]) | rail
    for which, mask, grow, prot in (("WATER", role == "WATER", 9, protect),
                                    ("RAIL", rail, 3, None)):
        m = Image.fromarray(mask.astype(np.uint8) * 255).filter(ImageFilter.MinFilter(3))
        m = np.asarray(m.filter(ImageFilter.MaxFilter(grow))) > 127
        if prot is not None:
            m = m & ~prot
        out[m] = rgb(PAL[which])

    canvas = Image.fromarray(out)

    # Режем вдвое больший кусок, чем нужно, и только потом уменьшаем.
    # Перекраска привязывает каждый пиксель к одному из полутора десятков
    # цветов и тем самым убивает сглаживание — края букв и линий становятся
    # ступенчатыми. Уменьшение вдвое усредняет соседние пиксели и возвращает
    # плавность, заодно приглушая мелкую рябь.
    W, H = canvas.size
    left = min(max(px - 1200, 0), W - 2400)
    top = min(max(py - 600, 0), H - 1200)
    canvas = canvas.crop((left, top, left + 2400, top + 1200)).resize((1200, 600), Image.LANCZOS)
    px, py = (px - left) // 2, (py - top) // 2

    canvas = canvas.convert("RGBA")
    for x, y, text, weight, size, track, colour, angle in LABELS:
        put_label(canvas, x, y, text, _font(weight, size), colour, track, angle)

    # Метку рисуем последней, иначе она размылась бы вместе с картой.
    d = ImageDraw.Draw(canvas, "RGBA")
    d.ellipse((px - 27, py - 27, px + 27, py + 27), fill=rgb(PAL["MARK"]) + (38,))
    d.ellipse((px - 15, py - 15, px + 15, py + 15), fill=rgb(PAL["MARK"]))
    d.ellipse((px - 11, py - 11, px + 11, py + 11), fill=(255, 255, 255))
    d.ellipse((px - 7, py - 7, px + 7, py + 7), fill=rgb(PAL["MARK_DOT"]))
    canvas = canvas.convert("RGB")

    for name, im, q in (("map", canvas, 52),
                        ("map-sm", canvas.resize((600, 300), Image.LANCZOS), 58)):
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q + 20, method=6)
        im.save(os.path.join(OUT, name + ".avif"), "AVIF", quality=q)
    print("карта", canvas.size, "метка в", (px, py))
    for f in ("map.webp", "map.avif", "map-sm.webp", "map-sm.avif"):
        print("  %-14s %5.1f КБ" % (f, os.path.getsize(os.path.join(OUT, f)) / 1024))


if __name__ == "__main__":
    build()
