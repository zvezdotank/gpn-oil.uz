# -*- coding: utf-8 -*-
"""Собирает статичную картинку карты офиса.

Раньше на странице контактов стоял встроенный виджет Яндекса: внешний
iframe, который тянет свой скрипт, тайлы и счётчики уже после загрузки
страницы. Это самый тяжёлый элемент на странице и единственный, ради
которого браузер посетителя ходил на чужой домен.

Здесь карта собирается один раз на сборке из тайлов OpenStreetMap и
кладётся к себе в img/. В момент открытия страницы наружу не уходит
ни одного запроса.

Требование лицензии OSM: под картой обязательна подпись
«© OpenStreetMap» со ссылкой на openstreetmap.org/copyright.
Она стоит в разметке страницы контактов.

Запуск: python3 tools/map.py
"""
import io
import math
import os
import urllib.request

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "img")

LAT, LON = 41.3230571, 69.312125
ZOOM = 16
COLS, ROWS = 5, 3          # 1280x768 из тайлов по 256, потом режем
TILE = 256
UA = "gpn-oil.uz static map builder (contact page, one-off build)"
BLUE = (0, 92, 185)


def tile_xy(lat, lon, z):
    n = 2 ** z
    x = (lon + 180) / 360 * n
    la = math.radians(lat)
    y = (1 - math.log(math.tan(la) + 1 / math.cos(la)) / math.pi) / 2 * n
    return x, y


def fetch(z, x, y):
    url = "https://tile.openstreetmap.org/%d/%d/%d.png" % (z, x, y)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def build():
    fx, fy = tile_xy(LAT, LON, ZOOM)
    x0, y0 = int(fx) - COLS // 2, int(fy) - ROWS // 2
    canvas = Image.new("RGB", (COLS * TILE, ROWS * TILE), (240, 240, 235))
    for dx in range(COLS):
        for dy in range(ROWS):
            canvas.paste(fetch(ZOOM, x0 + dx, y0 + dy), (dx * TILE, dy * TILE))

    # где на холсте оказалась точка офиса
    px = int((fx - x0) * TILE)
    py = int((fy - y0) * TILE)

    d = ImageDraw.Draw(canvas, "RGBA")
    # мягкий ореол, чтобы метка читалась на пёстром фоне
    d.ellipse((px - 26, py - 26, px + 26, py + 26), fill=BLUE + (46,))
    d.ellipse((px - 11, py - 11, px + 11, py + 11), fill=(255, 255, 255))
    d.ellipse((px - 8, py - 8, px + 8, py + 8), fill=BLUE)

    # Режем до 1200x600: на странице контактов карта занимает колонку около
    # 620 точек, на главной — шире, но карта терпит лёгкую мягкость куда
    # спокойнее фотографии, а лишние килобайты здесь дороже резкости.
    cx, cy = canvas.size[0] // 2, canvas.size[1] // 2
    off_x = px - cx
    canvas = canvas.crop((cx - 600 + off_x // 2, cy - 300, cx + 600 + off_x // 2, cy + 300))
    px -= (cx - 600 + off_x // 2)
    py -= (cy - 300)

    for name, im, q in (("map", canvas, 46),
                        ("map-sm", canvas.resize((600, 300), Image.LANCZOS), 52)):
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q + 20, method=6)
        im.save(os.path.join(OUT, name + ".avif"), "AVIF", quality=q)
    print("карта", canvas.size, "метка в", (px, py))
    for f in ("map.webp", "map.avif", "map-sm.webp", "map-sm.avif"):
        print("  %-14s %5.1f КБ" % (f, os.path.getsize(os.path.join(OUT, f)) / 1024))


if __name__ == "__main__":
    build()
