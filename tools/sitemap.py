# -*- coding: utf-8 -*-
"""Собирает sitemap.xml по готовым страницам.

Раньше карта сайта велась руками. Она пережила несколько правок структуры
и осталась верной по составу, но `lastmod` у всех сорока одного адреса
застыл на дате первой сборки — и после большой правки текстов поисковик
не видел причины перечитывать страницы. Плюс любая новая страница попадала
бы в индекс только если про неё вспомнили.

Здесь состав берётся из самих файлов: адрес — из canonical, языковые пары —
из hreflang, страницы с noindex пропускаются. Дата правки — по времени
изменения файла, а не «сегодня»: иначе после каждой пересборки все адреса
объявлялись бы изменёнными, и подсказка обесценивается.

Приоритет расставлен по смыслу: главная, витрина и категории важнее
служебных страниц. Это подсказка, а не команда, но пусть будет осмысленной.

Запуск: python3 tools/sitemap.py (вызывается из build_ru.py в конце сборки)
"""
import datetime
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://gpn-oil.uz"

PRIORITY = [
    (("/", "/uz/"), "1.0"),
    (("/products", "/uz/products", "/price", "/uz/price",
      "/contacts", "/uz/contacts"), "0.9"),
    (("/podbor", "/uz/podbor", "/analogi", "/uz/analogi"), "0.8"),
]
DEFAULT_PRIORITY = "0.7"
LOW = ("/blog", "/dostavka", "/uz/dostavka", "/docs", "/uz/docs")


def priority(path):
    for paths, value in PRIORITY:
        if path in paths:
            return value
    if path in LOW:
        return "0.6"
    return DEFAULT_PRIORITY


def collect():
    pages = []
    for f in sorted(glob.glob(os.path.join(ROOT, "*.html"))
                    + glob.glob(os.path.join(ROOT, "uz", "*.html"))):
        t = open(f, encoding="utf-8").read()
        if re.search(r'<meta name="robots" content="[^"]*noindex', t):
            continue
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', t)
        if not canon:
            continue
        url = canon.group(1)
        alts = re.findall(r'<link rel="alternate" hreflang="([^"]*)" href="([^"]*)"', t)
        mod = datetime.date.fromtimestamp(os.path.getmtime(f)).isoformat()
        pages.append((url, alts, mod))
    # Главная и узбекская главная — первыми, дальше в алфавитном порядке:
    # порядок в файле ни на что не влияет, но так его удобно читать глазами.
    pages.sort(key=lambda p: (p[0] not in (SITE + "/", SITE + "/uz/"), p[0]))
    return pages


def build():
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
           ' xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    pages = collect()
    for url, alts, mod in pages:
        path = url.replace(SITE, "") or "/"
        out.append("  <url>")
        out.append("    <loc>%s</loc>" % url)
        for code, href in alts:
            out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (code, href))
        out.append("    <lastmod>%s</lastmod>" % mod)
        out.append("    <priority>%s</priority>" % priority(path))
        out.append("  </url>")
    out.append("</urlset>")
    path = os.path.join(ROOT, "sitemap.xml")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return len(pages)


if __name__ == "__main__":
    print("карта сайта: %d адресов" % build())
