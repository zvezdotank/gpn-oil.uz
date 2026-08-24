# -*- coding: utf-8 -*-
"""Номенклатура склада. Один источник для русской и узбекской сборок.

Данные — из перечня клиента «Перечень ГПН ИЮЛЬ 01.07.2026» (лежит рядом,
в tools/). Ничего не досочиняем: если класс вязкости не читается прямо из
названия марки, в колонке стоит прочерк.

Группировка на сайте не повторяет группировку прайса. Прайс собран по типу
базового масла — синтетика, полусинтетика, минералка: это логика склада и
закупки. Человек ищет масло по технике и по узлу, поэтому здесь позиции
разложены по применению, а тип базы стоит подписью у самой позиции.

Каждая позиция — кортеж (название, класс, фасовки, наличие):
  наличие True  — есть на складе в Ташкенте, так в перечне;
  наличие False — возят под заказ, в перечне такой позиции нет.

Фасовки — числа из перечня, единица измерения задаётся группой: масла в
литрах, смазки в килограммах.
"""

# ── Моторные, легковой транспорт ─────────────────────────────────────────

# Звёздочка в перечне у части G-Energy означает поставку под заказ.
# У Long Life она стоит только на канистрах 1 и 4 л, а на бочке 205 л её нет,
# поэтому у позиции оставлена одна фасовка — та, что точно на складе.
G_ENERGY = [
    ("G-Energy Synthetic Far East 0W-20", "SAE 0W-20 · синтетика", "4", True),
    ("G-Energy Synthetic Long Life 10W-40", "SAE 10W-40 · синтетика", "205", True),
    ("G-Energy Synthetic Super Start 5W-30", "SAE 5W-30 · синтетика", "1 / 4 / 5 / 48 / 205", False),
    ("G-Energy Synthetic Super Start 5W-40", "SAE 5W-40 · синтетика", "4 / 205", False),
    ("G-Energy Synthetic Active 5W-40", "SAE 5W-40 · синтетика", "4", False),
    ("G-Energy Expert L 10W-40", "SAE 10W-40 · API SL · полусинтетика", "1 / 4 / 5 / 20 / 48 / 205", False),
]

GPN_LIGHT = [
    ("Gazpromneft Premium L 10W-40", "SAE 10W-40 · полусинтетика", "1 / 4 / 5 / 48 / 205", True),
    ("Gazpromneft Super 10W-40", "SAE 10W-40 · полусинтетика", "4 / 5 / 48 / 205", True),
    ("Gazpromneft Standard 10W-40", "SAE 10W-40 · полусинтетика", "4 / 5 / 205", True),
    ("Gazpromneft Ecogas 10W-40", "SAE 10W-40 · полусинтетика · для ГБО", "4 / 205", True),
    ("Gazpromneft Super 15W-40", "SAE 15W-40 · минеральное", "4 / 5 / 205", True),
    ("Gazpromneft Standard 15W-40", "SAE 15W-40 · минеральное", "4 / 5 / 205", True),
    ("Gazpromneft Ecogas 15W-40", "SAE 15W-40 · минеральное · для ГБО", "4", True),
    ("Gazpromneft Standard 20W-50", "SAE 20W-50 · минеральное", "1 / 4 / 5 / 48 / 205", True),
]

# ── Моторные, грузовая техника и дизели ──────────────────────────────────

G_PROFI = [
    ("G-Profi MSK 5W-30", "SAE 5W-30 · синтетика", "20", True),
    ("G-Profi MSI PLUS 15W-40", "SAE 15W-40 · синтетика", "20", True),
    ("G-Profi CNG LA 10W-40", "SAE 10W-40 · полусинтетика · для газовых двигателей", "20 / 205", True),
    ("G-Profi CNG 15W-40", "SAE 15W-40 · минеральное · для газовых двигателей", "20 / 205", True),
    ("G-Profi CNG LA 15W-40", "SAE 15W-40 · минеральное · для газовых двигателей", "20 / 205", True),
]

GPN_DIESEL = [
    ("Gazpromneft Diesel Premium 5W-40", "SAE 5W-40 · полусинтетика", "205", True),
    ("Gazpromneft Diesel Premium 10W-40", "SAE 10W-40 · полусинтетика", "20 / 205", True),
    ("Gazpromneft Diesel Extra 10W-40", "SAE 10W-40 · полусинтетика", "5 / 20 / 205", True),
    ("Gazpromneft Diesel Premium 15W-40", "SAE 15W-40 · минеральное", "5 / 20 / 205", True),
    ("Gazpromneft Diesel Extra 15W-40", "SAE 15W-40 · минеральное", "5 / 20 / 205", True),
    ("Gazpromneft Diesel Extra 20W-50", "SAE 20W-50 · минеральное", "5 / 20 / 205", True),
    ("Gazpromneft HD 50", "SAE 50 · минеральное", "20 / 50", True),
]

# Масла для больших стационарных, тепловозных и судовых дизелей. В перечне
# клиента М-10В2 и М-16Г2ЦС попали в индустриальные, но это моторные масла,
# и человек ищет их именно среди моторных.
GPN_MARINE = [
    ("Gazpromneft М-10В2", "—", "205", True),
    ("Gazpromneft М-14В2", "—", "205", True),
    ("Gazpromneft М-16Г2ЦС", "—", "205", True),
]

# ── Трансмиссионные ──────────────────────────────────────────────────────

ATF = [
    ("Gazpromneft ATF DX III", "Dexron III", "1 / 4 / 205", True),
    ("G-Box ATF DX III", "Dexron III", "205", True),
    ("G-Box ATF DX VI", "Dexron VI", "1", True),
]

MKPP = [
    ("Gazpromneft GL-4 75W-80", "SAE 75W-80 · API GL-4", "1 / 205", True),
    ("Gazpromneft GL-4 75W-90", "SAE 75W-90 · API GL-4", "1", True),
    ("Gazpromneft GL-4 80W-90", "SAE 80W-90 · API GL-4", "1 / 4 / 20 / 205", True),
    ("Gazpromneft GL-5 75W-90", "SAE 75W-90 · API GL-5", "1 / 205", True),
    ("Gazpromneft GL-5 80W-90", "SAE 80W-90 · API GL-5", "1 / 4 / 20 / 205", True),
    ("Gazpromneft GL-5 85W-140", "SAE 85W-140 · API GL-5", "1 / 4 / 20 / 205", True),
]

UTTO = [
    ("G-Special UTTO 10W-30", "SAE 10W-30", "205", True),
]

# ── Индустриальные ───────────────────────────────────────────────────────

HYDRAULIC = [
    ("Gazpromneft Hydraulic HLP 32", "ISO VG 32 · HLP", "20 / 50 / 205", True),
    ("Gazpromneft Hydraulic HLP 46", "ISO VG 46 · HLP", "20 / 50 / 205", True),
    ("Gazpromneft Hydraulic HLP 68", "ISO VG 68 · HLP", "20 / 205", True),
    ("Gazpromneft Hydraulic HVLP 15", "ISO VG 15 · HVLP", "20", True),
    ("Gazpromneft Hydraulic HVLP 32", "ISO VG 32 · HVLP", "205", True),
    ("Gazpromneft Hydraulic HVLP 46", "ISO VG 46 · HVLP", "20 / 205", True),
    ("Gazpromneft Hydraulic HVLP 68", "ISO VG 68 · HVLP", "20 / 205", True),
    ("Gazpromneft Гидравлик 32", "ISO VG 32 · HL", "20 / 205", True),
    ("Gazpromneft Гидравлик 46", "ISO VG 46 · HL", "20 / 205", True),
    ("Gazpromneft Гидравлик 68", "ISO VG 68 · HL", "20 / 205", True),
]

REDUCTOR = [
    ("Gazpromneft Reductor CLP 68", "ISO VG 68 · минеральное", "205", True),
    ("Gazpromneft Reductor CLP 100", "ISO VG 100 · минеральное", "205", True),
    ("Gazpromneft Reductor CLP 150", "ISO VG 150 · минеральное", "20 / 205", True),
    ("Gazpromneft Reductor CLP 220", "ISO VG 220 · минеральное", "20 / 205", True),
    ("Gazpromneft Reductor CLP 320", "ISO VG 320 · минеральное", "20 / 205", True),
    ("Gazpromneft Reductor CLP 460", "ISO VG 460 · минеральное", "205", True),
    ("Gazpromneft Reductor CLP 680", "ISO VG 680 · минеральное", "205", True),
    ("Gazpromneft Reductor F Synth 150", "ISO VG 150 · синтетика", "205", True),
    ("Gazpromneft Reductor F Synth 220", "ISO VG 220 · синтетика", "205", True),
    ("Gazpromneft Reductor F Synth 320", "ISO VG 320 · синтетика", "205", True),
    ("Gazpromneft Reductor F Synth 460", "ISO VG 460 · синтетика", "205", True),
    ("Gazpromneft Reductor PAO Synth 460", "ISO VG 460 · синтетика на ПАО", "205", True),
]

COMPRESSOR = [
    ("Gazpromneft Compressor Oil 46", "ISO VG 46 · минеральное", "20 / 205", True),
    ("Gazpromneft Compressor Oil 68", "ISO VG 68 · минеральное", "205", True),
    ("Gazpromneft Compressor Oil 100", "ISO VG 100 · минеральное", "205", True),
    ("Gazpromneft Compressor Oil 150", "ISO VG 150 · минеральное", "20 / 205", True),
    ("Gazpromneft Compressor Oil 220", "ISO VG 220 · минеральное", "205", True),
    ("Gazpromneft Compressor S Synth-46", "ISO VG 46 · синтетика", "20 / 205", True),
    ("Gazpromneft Compressor S Synth-68", "ISO VG 68 · синтетика", "205", True),
    ("Gazpromneft Compressor S Synth-100", "ISO VG 100 · синтетика", "205", True),
    ("Gazpromneft Compressor S Synth-150", "ISO VG 150 · синтетика", "205", True),
    ("Gazpromneft Compressor F Synth-46", "ISO VG 46 · синтетика", "20", True),
    ("Gazpromneft КС-19п", "—", "205", True),
]

# Turbine Oil 32 в перечне склада нет — на складе турбинные ТП-22 и ТП-30.
# Позицию оставляем с пометкой «под заказ»: она в линейке производителя
# и на неё приходят запросы.
TURBINE = [
    ("Gazpromneft ТП-22", "—", "205", True),
    ("Gazpromneft ТП-30", "—", "205", True),
    ("Gazpromneft Turbine Oil 32", "ISO VG 32", "—", False),
]

TRANSFORMER = [
    ("Gazpromneft ГК м.1", "—", "205", True),
]

INDUSTRIAL_GP = [
    ("Gazpromneft И-20А", "—", "205", True),
    ("Gazpromneft И-40А", "—", "205", True),
    ("Gazpromneft И-50А", "—", "205", True),
]

FORM_OIL = [
    ("Gazpromneft Form Oil 135", "—", "205", True),
]

HTO = [
    ("Gazpromneft HTO 32", "ISO VG 32", "205", True),
]

WHITE_OIL = [
    ("Gazpromneft White Oil 15 T", "—", "205", True),
]

# ── Смазки, фасовка в килограммах ────────────────────────────────────────

GREASE = [
    ("Gazpromneft Grease L EP-00", "NLGI 00 · литиевая", "18", True),
    ("Gazpromneft Grease L EP-0", "NLGI 0 · литиевая", "18", True),
    ("Gazpromneft Grease L EP 1", "NLGI 1 · литиевая", "18 / 180", True),
    ("Gazpromneft Grease L EP 2", "NLGI 2 · литиевая", "0,4 / 18 / 180", True),
    ("Gazpromneft Grease L EP 3", "NLGI 3 · литиевая", "18", True),
    ("Gazpromneft Grease LX EP 2", "NLGI 2 · литиевый комплекс", "18 / 180", True),
    ("Gazpromneft Grease Synth LX EP 2", "NLGI 2 · синтетическая", "18 / 180", True),
    ("Gazpromneft Premium Grease EP 1", "NLGI 1", "18", True),
    ("Gazpromneft Premium Grease EP 2", "NLGI 2", "0,4", True),
    ("Gazpromneft ЕР-2", "NLGI 2", "18", True),
    ("Gazpromneft ЕР-3", "NLGI 3", "18", True),
    ("Gazpromneft Литол-24", "—", "0,1 / 0,8 / 18 / 170", True),
]

# ── Технические жидкости ─────────────────────────────────────────────────

BRAKE = [
    ("Gazpromneft DOT 4", "DOT 4", "0,45", True),
    ("G-Energy Expert DOT 4", "DOT 4", "0,45", True),
]


# Пояснения в колонке класса переводим по словарю: сами обозначения
# (SAE, ISO VG, NLGI, API, Dexron) международные и остаются как есть.
UZ = {
    "синтетика": "sintetika",
    "синтетическая": "sintetik",
    "синтетика на ПАО": "PAO asosidagi sintetika",
    "полусинтетика": "yarim sintetika",
    "минеральное": "mineral",
    "для ГБО": "gaz balonli uskunalar uchun",
    "для газовых двигателей": "gaz dvigatellari uchun",
    "литиевая": "litiyli",
    "литиевый комплекс": "litiy kompleksi",
}
UNIT_UZ = {"л": "l", "кг": "kg"}


def _grade(g, lang):
    if lang == "ru":
        return g
    return " · ".join(UZ.get(part, part) for part in g.split(" · "))


def _pack(s, unit):
    return "—" if s == "—" else "%s %s" % (s, unit)


def rows(items, unit="л", lang="ru"):
    """Готовит позиции к вёрстке: перевод пояснений и единица у фасовок."""
    u = unit if lang == "ru" else UNIT_UZ.get(unit, unit)
    return [(n, _grade(g, lang), _pack(p, u), stock) for n, g, p, stock in items]


def groups(pairs, unit="л", lang="ru"):
    """То же для страницы, разбитой на подразделы: [(подзаголовок, позиции)]."""
    return [(title, rows(items, unit, lang)) for title, items in pairs]


def count(*lists):
    return sum(len(x) for x in lists)
