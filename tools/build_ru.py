# -*- coding: utf-8 -*-
"""Сборка сайта gpn-oil.uz. Адреса страниц повторяют адреса действующего
сайта на Tilda — иначе при переезде теряются позиции. Разовый скрипт,
на выходе обычная статика."""
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import io, os

OUT = ROOT
SITE = "https://gpn-oil.uz"
TG = "https://t.me/GPN_OIL_UZ"
INSTA = "https://instagram.com/gpn_oil.uz"
SALESHUB = "https://sales-hub.uz/?utm_source=gpn-oil.uz&utm_medium=referral&utm_campaign=footer"

from PIL import Image as _Image
_DIMS = {}


def dim(name):
    if name not in _DIMS:
        _DIMS[name] = _Image.open(os.path.join(OUT, "img", name + ".webp")).size
    return _DIMS[name]


NAV = [
    ("/products", "Продукция", "products"),
    ("/podbor", "Подбор масла", "podbor"),
    ("/otrasli", "Отрасли", "otrasli"),
    ("/price", "Цены", "price"),
    ("/docs", "Документация", "docs"),
    ("/company", "О компании", "company"),
    ("/contacts", "Контакты", "contacts"),
]

HEAD = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">{alternates}
<meta name="theme-color" content="#0d2b45">{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Газпромнефть Узбекистан">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{ogdesc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimage}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="ru_RU">
<link rel="icon" href="/img/logo-mark.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/plex-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/plex-700.woff2" as="font" type="font/woff2" crossorigin>{preload}
<link rel="stylesheet" href="/site.css?v=6">
{jsonld}</head>
<body>

<div class="topbar">
  <div class="wrap topbar__in">
    <span>Официальный дистрибьютор «Газпромнефть — смазочные материалы» в Республике Узбекистан</span>
    <div class="topbar__right">
      <span>Пн–Пт, 09:00–18:00</span>
      <span class="lang"><span class="lang__on">RU</span><span>/</span>{uzlink}</span>
    </div>
  </div>
</div>

<header class="masthead">
  <div class="wrap masthead__in">
    <a class="brand" href="/" aria-label="Газпромнефть Узбекистан — на главную">
      <img class="brand__logo" src="/img/logo-mark.svg" alt="Gazpromneft — Smart Energy Eco Trade, дистрибьютор в Узбекистане" width="221" height="78">
    </a>
    <nav class="nav" id="nav" aria-label="Основная навигация">
{nav}
    </nav>
    <div class="masthead__right">
      <a class="tel" href="tel:+998935048490">+998 93 504 84 90<span>отдел продаж</span></a>
      <a class="btn btn--accent btn--sm" href="/price#zayavka">Получить прайс</a>
      <button class="burger" type="button" aria-label="Меню" aria-expanded="false" aria-controls="nav"><i></i><i></i><i></i></button>
    </div>
  </div>
</header>
"""

MGR = """
<aside class="mgr" id="mgr" aria-label="Связаться с менеджером">
  <button class="mgr__close" type="button" id="mgrClose" aria-label="Свернуть окно менеджера">&times;</button>
  <div class="mgr__top">
    <button class="mgr__head" type="button" id="mgrToggle" aria-expanded="false" aria-controls="mgrBody">
      <img class="mgr__ava" src="/img/manager.webp" srcset="/img/manager.webp 128w, /img/manager-2x.webp 256w" sizes="44px" alt="Тимур Яруллин, корпоративный менеджер" width="128" height="128" loading="lazy" decoding="async">
      <span class="mgr__who">
        <b>Тимур Яруллин</b>
        <span>корпоративный менеджер</span>
      </span>
      <span class="mgr__chev" aria-hidden="true"></span>
    </button>
    <a class="mgr__call" href="tel:+998908085972" aria-label="Позвонить менеджеру">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M5 3h3.5l1.8 4.4-2.2 1.6a12 12 0 0 0 6.9 6.9l1.6-2.2 4.4 1.8V19a2 2 0 0 1-2.2 2A17 17 0 0 1 3 5.2 2 2 0 0 1 5 3z"/></svg>
    </a>
  </div>
  <div class="mgr__body" id="mgrBody">
    <a class="mgr__row" href="tel:+998908085972">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M5 3h3.5l1.8 4.4-2.2 1.6a12 12 0 0 0 6.9 6.9l1.6-2.2 4.4 1.8V19a2 2 0 0 1-2.2 2A17 17 0 0 1 3 5.2 2 2 0 0 1 5 3z"/></svg>
      +998 90 808 59 72</a>
    <a class="mgr__row mgr__row--tg" href="__TG__" rel="noopener">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M21.2 4.3 2.9 11.2c-.8.3-.8 1.4 0 1.7l4.6 1.5 1.7 5c.2.7 1.1.9 1.6.3l2.4-2.6 4.6 3.4c.6.4 1.4.1 1.6-.6l3-14c.2-.8-.6-1.5-1.2-1.6z"/><path d="M7.5 14.4 18.6 6.6l-7.9 9.1"/></svg>
      Написать в Telegram</a>
    <a class="mgr__row" href="/price#zayavka">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M5 3h14v18l-7-4-7 4z"/></svg>
      Оставить заявку</a>
    <a class="mgr__row" href="mailto:t.yarulin@s-energy.uz">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14"/><path d="m3 6 9 7 9-7"/></svg>
      t.yarulin@s-energy.uz</a>
    <p class="mgr__hours">Пн–Пт, 09:00–18:00. Подбор под оборудование, прайс и наличие на складе в Ташкенте.</p>
  </div>
</aside>
""".replace("__TG__", TG)

CTA = """
<section class="cta">
  <div class="wrap cta__in">
    <div class="cta__body">
      <b>Нужен расчёт или прайс сегодня?</b>
      <p>Технический специалист на связи Пн–Пт, 09:00–18:00. Ответ в Telegram — в течение 15 минут.</p>
    </div>
    <div class="cta__actions">
      <a class="btn btn--white" href="tel:+998908085972">+998 90 808 59 72</a>
      <a class="btn btn--onDark" href="{tg}" rel="noopener">Написать в Telegram</a>
    </div>
  </div>
</section>
"""

TAIL = """
<footer class="footer">
  <div class="wrap">
    <div class="footer__in">
      <div class="footer__col footer__brand">
        <img class="footer__logo" src="/img/logo-footer.svg" alt="Gazpromneft" width="221" height="78" loading="lazy">
        <span>ООО «Smart Energy Eco Trade» — официальный дистрибьютор смазочных материалов «Газпромнефть» в Республике Узбекистан.</span>
      </div>
      <div class="footer__col">
        <b>Продукция</b>
        <a href="/products">Весь каталог</a>
        <a href="/industrial">Индустриальные масла</a>
        <a href="/gpn">Моторные масла Газпромнефть</a>
        <a href="/g-energy">G-Energy</a>
        <a href="/transmission">Трансмиссионные масла</a>
        <a href="/grease">Пластичные смазки</a>
        <a href="/fluids">СОЖ и жидкости</a>
        <a href="/analogi">Аналоги импортных марок</a>
      </div>
      <div class="footer__col">
        <b>Компания</b>
        <a href="/company">О компании</a>
        <a href="/dostavka">Доставка и оплата</a>
        <a href="/price">Цены</a>
        <a href="/docs">Документация</a>
        <a href="/blog">Блог</a>
        <a href="/contacts">Контакты</a>
      </div>
      <div class="footer__col">
        <b>Контакты</b>
        <a href="tel:+998908085972">+998 90 808 59 72</a>
        <a href="tel:+998935048490">+998 93 504 84 90</a>
        <a href="mailto:t.yarulin@s-energy.uz">t.yarulin@s-energy.uz</a>
        <a href="{tg}" rel="noopener">Telegram</a>
        <a href="{insta}" rel="noopener">Instagram</a>
        <span>Ташкент, Узбекистан</span>
      </div>
    </div>
    <div class="footer__legal">
      <span>© 2026 ООО «Smart Energy Eco Trade»</span>
      <span>Gazpromneft, G-Profi, G-Energy — товарные знаки правообладателя.</span>
      <span>Сайт и продвижение — <a href="{saleshub}" rel="noopener">Sales HUB</a></span>
    </div>
  </div>
</footer>
"""

ORG_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Smart Energy Eco Trade","alternateName":"Газпромнефть Узбекистан","url":"https://gpn-oil.uz/","logo":"https://gpn-oil.uz/img/logo-mark.svg","description":"Официальный дистрибьютор «Газпромнефть — смазочные материалы» в Республике Узбекистан","areaServed":"UZ","address":{"@type":"PostalAddress","addressLocality":"Ташкент","addressCountry":"UZ"},"contactPoint":[{"@type":"ContactPoint","telephone":"+998908085972","contactType":"sales","name":"Тимур Яруллин, корпоративный менеджер","email":"t.yarulin@s-energy.uz","availableLanguage":["ru","uz"]},{"@type":"ContactPoint","telephone":"+998935048490","contactType":"customer service","availableLanguage":["ru","uz"]}],"sameAs":["https://instagram.com/gpn_oil.uz"]}
</script>
"""


def crumbs_ld(items):
    parts = []
    for i, (name, url) in enumerate(items, 1):
        parts.append('{"@type":"ListItem","position":%d,"name":"%s","item":"%s%s"}' % (i, name, SITE, url))
    return ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}\n'
            '</script>\n' % ",".join(parts))



def faq_html(items):
    """Вопрос-ответ на <details>: работает без скрипта, раскрыт для поисковика."""
    out = ['        <div class="faq">']
    for q, a in items:
        out.append('          <details name="faq">\n            <summary>%s</summary>\n            <p>%s</p>\n          </details>' % (q, a))
    out.append('        </div>')
    return "\n".join(out)


def faq_ld(items):
    q = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}'
                 % (a.replace('"', "'"), b.replace('"', "'")) for a, b in items)
    return ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}\n</script>\n' % q)


def page(path, fname, title, desc, body, active=None, ogimage="/img/og.jpg",
         preload=None, jsonld="", noindex=False, ogtitle=None, ogdesc=None, cta=True, formhref="/price#zayavka",
         preload_sizes="100vw"):
    nav = "\n".join(
        '      <a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if key == active else "", label)
        for href, label, key in NAV)
    pre = ''
    if preload:
        name = preload.split("/")[-1].replace(".webp", "")
        w = dim(name)[0]
        pre = ('\n<link rel="preload" as="image" href="%s" imagesrcset="%s" imagesizes="%s" fetchpriority="high">'
               % (preload, srcset(name, w), preload_sizes))
    uzpath = "/uz/" if path == "/" else "/uz" + path
    has_uz = os.path.exists(os.path.join(OUT, "uz", fname))
    html = (HEAD.format(title=title, desc=desc, nav=nav, tg=TG,
                        canonical=SITE + path,
                        alternates=('\n<link rel="alternate" hreflang="ru" href="%s">'
                                    '\n<link rel="alternate" hreflang="uz" href="%s">'
                                    '\n<link rel="alternate" hreflang="x-default" href="%s">'
                                    % (SITE + path, SITE + uzpath, SITE + path)) if has_uz else "",
                        uzlink=('<a class="lang__off" href="%s" hreflang="uz" lang="uz">UZ</a>' % uzpath)
                                if has_uz else '<span class="lang__off" style="opacity:.45">UZ</span>',
                        ogtitle=ogtitle or title, ogdesc=ogdesc or desc,
                        ogimage=SITE + ogimage, preload=pre, jsonld=jsonld,
                        robots='\n<meta name="robots" content="noindex">' if noindex else "")
            + body + MGR
            + (CTA.format(tg=TG) if cta else "")
            + TAIL.format(insta=INSTA, saleshub=SALESHUB, tg=TG)
            + '\n<script src="/site.js?v=6" defer></script>\n</body>\n</html>\n')
    with io.open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    return len(html)


# --------------------------------------------------------------- каталог
CATS = [
    ("/industrial", "Индустриальные масла", "cat-industrial",
     "Гидравлические, редукторные, компрессорные, турбинные, теплоносители"),
    ("/gpn", "Моторные масла Газпромнефть", "cat-gpn",
     "Для коммерческого транспорта, спецтехники и автопарков"),
    ("/g-energy", "Моторные масла G-Energy", "cat-g-energy",
     "Синтетика и полусинтетика для легкового транспорта"),
    ("/grease", "Пластичные смазки", "cat-grease",
     "Литиевые, кальциевые, высокотемпературные, Steelgrease"),
    ("/transmission", "Трансмиссионные масла", "cat-transmission",
     "Для МКПП, АКПП, мостов и ГУР, включая ATF"),
    ("/fluids", "Технические жидкости и СОЖ", "cat-fluids",
     "Антифризы, тормозные жидкости, смазочно-охлаждающие жидкости"),
]

CARD_IMG = {
    "cat-industrial": (650, 342), "cat-gpn": (760, 400), "cat-g-energy": (730, 384),
    "cat-grease": (760, 399), "cat-transmission": (760, 399), "cat-fluids": (760, 399),
}



def srcset(name, w):
    """Три ступени вместо двух: без промежуточной телефон с плотным экраном
    тянет самую большую картинку, потому что выбрать больше нечего."""
    parts = ["/img/%s-sm.webp %dw" % (name, max(400, w // 2))]
    if os.path.exists(os.path.join(OUT, "img", name + "-md.webp")):
        parts.append("/img/%s-md.webp 960w" % name)
    parts.append("/img/%s.webp %dw" % (name, w))
    return ", ".join(parts)


def cards_html(indent="        "):
    out = []
    for href, name, img, text in CATS:
        w, h = dim(img)
        alt = name if ("Газпромнефть" in name or "G-Energy" in name) else name + " Газпромнефть"
        out.append("""%s<a class="card" href="%s">
%s  <img class="card__media" src="/img/%s.webp" srcset="%s" sizes="(max-width:640px) 100vw, (max-width:1080px) 50vw, 33vw" alt="%s" width="%d" height="%d" loading="lazy" decoding="async">
%s  <div class="card__title">%s</div>
%s  <div class="card__text">%s</div>
%s</a>""" % (indent, href, indent, img, srcset(img, w), alt, w, h, indent, name, indent, text, indent))
    return "\n".join(out)


ASIDE_REQUEST = """        <div class="callout">
          <b>Запросить цену и наличие</b>
          <p>Ответим в Telegram в течение 15 минут в рабочее время.</p>
          <a class="btn btn--orange" href="#zayavka">Оставить заявку</a>
          <a class="btn btn--onDark" href="tel:+998935048490">+998 93 504 84 90</a>
          <a class="btn btn--onDark" href="%s" rel="noopener">Написать в Telegram</a>
        </div>""" % TG


def aside_other(current):
    links = "\n".join('            <a href="%s">%s</a>' % (h, n)
                      for h, n, _, _ in CATS if h != current)
    return """        <div class="asidebox">
          <b>Другие категории</b>
          <div>
%s
          </div>
        </div>""" % links


def table(rows):
    """Таблица позиций. Данные — из перечня клиента, ничего не досочиняем."""
    body = []
    for name, grade, pack in rows:
        body.append("""          <div class="table__row">
            <b>%s</b>
            <span><span class="table__label">Класс вязкости: </span>%s</span>
            <span><span class="table__label">Фасовка: </span>%s</span>
            <div class="table__files"><a href="/docs">TDS · MSDS</a></div>
          </div>""" % (name, grade, pack))
    return """        <div class="table">
          <div class="table__head">
            <div>Наименование</div><div>Класс вязкости</div><div>Фасовка</div><div>Документы</div>
          </div>
%s
        </div>
        <p class="table__note">Показаны основные позиции. Полный перечень и цены — по запросу у менеджера.</p>""" % "\n".join(body)


EMPTY = """        <div class="empty">
          <b>Перечень позиций готовим к публикации</b>
          <p>Пришлите модель техники, действующую марку масла или нужный объём — подберём позиции, вышлем прайс с наличием и техническое описание в течение 15 минут в рабочее время.</p>
          <div class="empty__actions">
            <a class="btn btn--blue" href="%s" rel="noopener">Запросить прайс в Telegram</a>
            <a class="btn btn--outline" href="tel:+998935048490">+998 93 504 84 90</a>
          </div>
        </div>""" % TG



NEEDS = [
    "Индустриальные масла (гидравлика, редукторы, компрессоры)",
    "Моторные масла для грузовой техники и спецтехники",
    "Моторные масла для легкового транспорта",
    "Трансмиссионные масла",
    "Пластичные смазки",
    "Антифризы, тормозные жидкости, СОЖ",
    "Не знаю — нужен подбор по технике",
]


def leadform(source, title, sub, button, cls="", preset=None, anchor=None):
    """Форма заявки. Поля короткие: чем меньше полей, тем больше отправок,
    но тип продукта спрашиваем — с ним менеджер отвечает сразу по делу."""
    opts = "\n".join(
        '            <option%s>%s</option>' % (' selected' if n == preset else '', n)
        for n in NEEDS)
    return """      <form class="leadform%s"%s method="post" action="https://gpn-relay.zvezdotank.workers.dev/">
        <b>%s</b>
        <p>%s</p>
        <input class="trap" type="text" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="_form" value="%s">
        <label><span>Что нужно</span>
          <select name="need">
%s
          </select>
        </label>
        <label><span>Телефон или Telegram</span>
          <input name="phone" type="tel" placeholder="+998" autocomplete="tel" required>
        </label>
        <label><span>Техника, марка масла или объём <em style="font-style:normal;color:#8b9db0">— необязательно</em></span>
          <textarea name="task" rows="2" placeholder="Например: Komatsu PC300, сейчас Shell Tellus 46, около 2000 л в год"></textarea>
        </label>
        <button type="submit">%s</button>
        <small>Ответим в рабочее время, Пн–Пт с 09:00 до 18:00. Подбор бесплатный и ни к чему не обязывает.</small>
      </form>""" % (cls, (' id="%s"' % anchor) if anchor else "", title, sub, source, opts, button)


def category(path, fname, crumb, h1, title, desc, lead, img, img_size, alt,
             rows=None, chips=None, longread=None, active="products", parent=None,
             uses=None, faq=None, preset=None):
    crumb_items = [("Главная", "/"), ("Продукция", "/products")]
    if parent:
        crumb_items.append(parent)
    crumb_items.append((crumb, path))
    crumb_html = '<a href="/">Главная</a><span>/</span><a href="/products">Продукция</a><span>/</span>'
    if parent:
        crumb_html += '<a href="%s">%s</a><span>/</span>' % (parent[1], parent[0])
    crumb_html += '<b>%s</b>' % crumb

    # Фото ставим только там, где есть достойный кадр. Мелкий или рекламный
    # снимок дешевит страницу сильнее, чем помогает её оживить, — тогда
    # страница просто начинается с заголовка.
    if img:
        iw, ih = dim(img)
        hero_block = """    <div class="pagehero">
      <img src="/img/%s.webp" srcset="%s" sizes="100vw" alt="%s" width="%d" height="%d" fetchpriority="high" decoding="async">
    </div>
""" % (img, srcset(img, iw), alt, iw, ih)
    else:
        hero_block = ""

    chips_html = ""
    if chips:
        chips_html = '\n        <div class="chips">\n' + "\n".join(
            '          <a class="chip" href="%s">%s</a>' % (u, n) for n, u in chips) + '\n        </div>'
    if rows:
        content = table(rows)
    else:
        # Перечня позиций нет — но пустая страница выкидывает человека обратно
        # в выдачу. Показываем, под какие задачи подбираем, и просим заявку.
        tiles = "\n".join(
            '          <div><b>%s</b><span>%s</span></div>' % (n, t) for n, t in (uses or []))
        content = """        <h2 style="font-size:24px;margin-top:8px">Что подбираем в этой категории</h2>
        <div class="uses">
%s
        </div>
        <div class="checklist">
          <b>Что написать в заявке, чтобы ответ был точным</b>
          <span>Марка и модель техники или узла</span>
          <span>Какое масло залито сейчас — марка или допуск</span>
          <span>Примерный объём: на одну заправку или на год</span>
          <span>Нужная фасовка: канистра, бочка, кубовая ёмкость</span>
        </div>
%s""" % (tiles, leadform(("Заявка со страницы: " + crumb), "Подобрать и узнать цену",
                         "Пришлём подбор, прайс с наличием и техническое описание.",
                         "Получить подбор и прайс", preset=preset))
    long_html = ""
    if longread:
        long_html = """
        <div class="longread">
          <h2>%s</h2>
          <p>%s</p>
        </div>""" % longread
    if faq:
        long_html += """
        <div class="longread">
          <h2>Частые вопросы</h2>
        </div>
%s""" % faq_html(faq)

    body = """
<main>
  <nav class="wrap crumbs" aria-label="Хлебные крошки">
    %s
  </nav>

  <div class="wrap page">
%s    <div class="layout">
      <div class="layout__main">
        <h1>%s</h1>
        <p class="page__lead">%s</p>
%s
%s%s
      </div>

      <aside class="layout__aside">
%s
%s
%s
      </aside>
    </div>
  </div>
</main>
""" % (crumb_html, hero_block, h1, lead, chips_html, content, long_html,
       ASIDE_REQUEST,
       leadform("Заявка из сайдбара: " + crumb, "Запросить цену", "Ответим в Telegram или перезвоним.",
                "Отправить заявку", cls=" leadform--aside", preset=preset, anchor="zayavka"),
       aside_other(path))

    return page(path, fname, title, desc, body, active=active, formhref="#zayavka",
                ogimage="/img/og.jpg",
                preload=("/img/%s.webp" % img) if img else None,
                jsonld=crumbs_ld(crumb_items) + (faq_ld(faq) if faq else ""))


INDUSTRIAL_ROWS = [
    ("Gazpromneft Hydraulic HLP 32", "ISO VG 32", "20 / 50 / 205 л"),
    ("Gazpromneft Hydraulic HLP 46", "ISO VG 46", "20 / 50 / 205 л"),
    ("Gazpromneft Hydraulic HLP 68", "ISO VG 68", "20 / 205 л"),
    ("Gazpromneft Reductor CLP 150", "ISO VG 150", "20 / 205 л"),
    ("Gazpromneft Reductor CLP 220", "ISO VG 220", "20 / 205 л"),
    ("Gazpromneft Compressor Oil 46", "ISO VG 46", "20 / 205 л"),
    ("Gazpromneft Turbine Oil 32", "ISO VG 32", "205 л"),
    ("Gazpromneft Termoil 26", "ISO VG 32", "205 л"),
]

category("/industrial", "industrial.html", "Индустриальные масла",
         "Индустриальные масла Газпромнефть в Ташкенте",
         "Индустриальные масла Газпромнефть в Ташкенте и Узбекистане",
         "Индустриальные масла Gazpromneft со склада в Ташкенте: гидравлические HLP 32/46/68, редукторные CLP, компрессорные и турбинные. Паспорт качества на партию.",
         "Гидравлические, редукторные, компрессорные, турбинные и трансформаторные масла, теплоносители. Наличие на складе в Ташкенте, фасовка от 20 л до кубовых ёмкостей, паспорт качества на каждую партию.",
         "industrial", (800, 449),
         "Индустриальные масла Газпромнефть в бочках на складе",
         rows=INDUSTRIAL_ROWS,
         chips=[("Гидравлические", "/hydralic"), ("Редукторные", "/reductor"),
                ("Компрессорные", "/compressor"), ("Смазки", "/grease"), ("СОЖ", "/fluids")],
         longread=("Подбор и замена импортных марок",
                   "Подбираем аналоги Shell Tellus, Mobil DTE, Total Azolla и других марок по классу вязкости ISO VG, уровню очистки и требованиям производителя оборудования. При переходе предоставляем протокол сравнения характеристик и рекомендации по промывке системы — смотрите <a href=\"/analogi\" style=\"color:var(--blue);font-weight:600\">таблицу соответствий</a>."))

category("/hydralic", "hydralic.html", "Гидравлические масла",
         "Гидравлические масла Газпромнефть в Ташкенте",
         "Гидравлические масла Газпромнефть — HLP 32, 46, 68",
         "Гидравлические масла Gazpromneft Hydraulic HLP 32, 46 и 68 со склада в Ташкенте. Фасовка 20, 50 и 205 л, подбор аналогов Shell Tellus и Mobil DTE.",
         "Серия Gazpromneft Hydraulic для гидросистем карьерной, строительной и промышленной техники. Классы ISO VG 32, 46 и 68, фасовка от 20 л до кубовых ёмкостей.",
         "hydralic", (1200, 674),
         "Гидравлика карьерной техники — гидравлические масла Газпромнефть",
         rows=INDUSTRIAL_ROWS[:3],
         parent=("Индустриальные масла", "/industrial"),
         longread=("Чем заменить импортное гидравлическое масло",
                   "Shell Tellus S2 M, Mobil DTE 20 и Total Azolla ZS подбираются по классу ISO VG и уровню очистки. Даём протокол сравнения характеристик и рекомендации по промывке системы перед переходом."))

category("/reductor", "reductor.html", "Редукторные масла",
         "Редукторные масла Газпромнефть в Ташкенте",
         "Редукторные масла Газпромнефть — CLP 150 и CLP 220",
         "Редукторные масла Gazpromneft Reductor CLP 150 и CLP 220 со склада в Ташкенте. Фасовка 20 и 205 л, паспорт качества на партию, подбор по нагрузке и температуре.",
         "Серия Gazpromneft Reductor для промышленных редукторов и приводов. Классы ISO VG 150 и 220, фасовка 20 и 205 л, наличие на складе в Ташкенте.",
         "reductor", (1200, 674),
         "Промышленный редуктор — редукторные масла Газпромнефть",
         rows=INDUSTRIAL_ROWS[3:5],
         parent=("Индустриальные масла", "/industrial"),
         longread=("Как подобрать редукторное масло",
                   "Класс вязкости выбирается по окружной скорости, нагрузке на зуб и рабочей температуре узла. При высокой ударной нагрузке или температуре выше 90 °C нужен продукт с усиленным пакетом противозадирных присадок — подскажем на подборе."))

category("/compressor", "compressor.html", "Компрессорные масла",
         "Компрессорные масла Газпромнефть в Ташкенте",
         "Компрессорные масла Газпромнефть в Узбекистане",
         "Компрессорные масла Gazpromneft Compressor Oil со склада в Ташкенте. Фасовка 20 и 205 л, паспорт качества на партию, подбор под винтовые и поршневые компрессоры.",
         "Масла для винтовых и поршневых компрессоров. Класс ISO VG 46, фасовка 20 и 205 л, наличие на складе в Ташкенте.",
         "compressor", (1024, 575),
         "Винтовые компрессоры — компрессорные масла Газпромнефть",
         rows=INDUSTRIAL_ROWS[5:6],
         parent=("Индустриальные масла", "/industrial"),
         longread=("Интервал замены в компрессоре",
                   "Ресурс масла в винтовом компрессоре зависит от температуры нагнетания и запылённости воздуха на площадке. В условиях Узбекистана летом интервал обычно короче паспортного — ориентируйтесь на анализ пробы, а не только на наработку."))

category("/gpn", "gpn.html", "Моторные масла Газпромнефть",
         "Моторные масла Газпромнефть в Ташкенте",
         "Моторные масла Газпромнефть в Узбекистане со склада в Ташкенте",
         "Моторные масла Gazpromneft и G-Profi для грузового транспорта, автобусов и спецтехники. Склад в Ташкенте, подбор по допускам производителя, документы на каждую партию.",
         "Для коммерческого транспорта, спецтехники и автопарков. Подбираем по допускам производителя двигателя и условиям эксплуатации, поставляем со склада в Ташкенте с паспортом качества на каждую партию.",
         "gpn", (1200, 673),
         "Производство моторных масел Газпромнефть",
                  preset="Моторные масла для грузовой техники и спецтехники",
         uses=[("Грузовики и тягачи", "Дизельные масла по допускам MAN, Scania, Volvo, Mercedes-Benz"),
               ("Карьерная и строительная техника", "Для работы в пыли и на высоких температурах"),
               ("Автобусы и коммунальная техника", "Городской цикл с частыми остановками"),
               ("Сельхозтехника", "Универсальные масла для смешанного парка")],
         faq=[("Подойдёт ли Газпромнефть вместо импортного масла?",
               "Да, если совпадают класс вязкости SAE, уровень API или ACEA и допуск производителя двигателя. Пришлите марку, которая залита сейчас, — сверим по характеристикам и дадим протокол сравнения."),
              ("Дадите документы для бухгалтерии и тендера?",
               "Да. Поставка идёт по договору со счётом-фактурой, товарно-транспортными документами и паспортом качества на партию. Для тендерных процедур собираем пакет под требования заказчика."),
              ("Как быстро отгружаете?",
               "Позиции, которые есть на складе в Ташкенте, отгружаем в течение 24 часов с момента заявки. Доставка по Узбекистану — по договорённости.")],
         longread=("Как подбираем",
                   "Для автопарков готовим годовую спецификацию с фиксированной ценой и графиком отгрузок. При переходе с импортных марок технический специалист сверяет допуски и класс вязкости и выдаёт протокол сравнения характеристик."))

category("/g-energy", "g-energy.html", "Моторные масла G-Energy",
         "Моторные масла G-Energy в Ташкенте",
         "Моторные масла G-Energy в Узбекистане",
         "Моторные масла G-Energy для легкового транспорта: синтетика и полусинтетика. Официальная поставка со склада в Ташкенте, фасовки от 1 л, документы на партию.",
         "Синтетика и полусинтетика для легкового транспорта. Официальная продукция со склада в Ташкенте, фасовки от литровой канистры до бочки, паспорт качества на каждую партию.",
         "g-energy", (1024, 575),
         "G-Energy — моторные масла для легкового транспорта",
                  preset="Моторные масла для легкового транспорта",
         uses=[("Сервисные центры и СТО", "Синтетика и полусинтетика ходовых вязкостей"),
               ("Магазины автотоваров", "Фасовки 1, 4 и 5 л под розничную полку"),
               ("Корпоративные автопарки", "Регулярные отгрузки по фиксированной цене"),
               ("Такси и каршеринг", "Масла для тяжёлого городского цикла")],
         faq=[("Чем G-Energy отличается от Gazpromneft?",
               "Это две линейки одного производителя: G-Energy рассчитана на легковой транспорт, линейка Gazpromneft — на коммерческую и промышленную технику. Отличаются пакетом присадок и допусками."),
              ("Продаёте в розницу?",
               "Мы работаем оптом со склада в Ташкенте. Для магазинов и сервисов есть отдельные условия — смотрите страницу розничной сети."),
              ("Как отличить оригинал от подделки?",
               "Мы официальный дистрибьютор и возим продукцию напрямую с заводов производителя. На каждую партию есть паспорт качества, документы прикладываем к поставке.")],
         longread=("Кому поставляем",
                   "Сервисным центрам, магазинам и корпоративным автопаркам. Для регулярных отгрузок фиксируем цену на период и держим согласованный запас на складе."))

category("/g-energy-retail", "g-energy-retail.html", "G-Energy — розничная сеть",
         "G-Energy для розницы в Узбекистане",
         "G-Energy для магазинов и СТО в Узбекистане",
         "Поставка моторных масел G-Energy магазинам автотоваров, СТО и АЗС по Узбекистану. Оптовые условия, фирменное оборудование, поддержка продаж.",
         "Условия для магазинов автотоваров, сервисов и АЗС: оптовые цены, отгрузка со склада в Ташкенте, поддержка продаж и фирменные материалы в точку.",
         None, None, None,
                  preset="Моторные масла для легкового транспорта",
         uses=[("Магазины автотоваров", "Ходовые фасовки и вязкости под спрос района"),
               ("Сервисы и СТО", "Масло в бочках и канистрах под замену"),
               ("АЗС", "Витринные позиции и фирменные материалы"),
               ("Интернет-магазины", "Отгрузка со склада в Ташкенте")],
         faq=[("С какого объёма работаете?",
               "Условия зависят от объёма выборки и регулярности — обсуждаем индивидуально. Напишите, какой у вас поток, посчитаем."),
              ("Помогаете с ассортиментом?",
               "Да. Подбираем перечень под парк машин в вашем районе, а не по общему прайсу: в спальном районе и рядом с трассой продаётся разное.")],
         longread=("Что даём партнёру",
                   "Оптовую цену по объёму выборки, отсрочку по договору, доставку по Узбекистану и фирменные материалы в точку продаж. Ассортимент подбираем под парк машин в вашем районе, а не по общему прайсу."))

category("/transmission", "transmission.html", "Трансмиссионные масла",
         "Трансмиссионные масла Газпромнефть в Ташкенте",
         "Трансмиссионные масла Газпромнефть в Узбекистане",
         "Трансмиссионные масла Gazpromneft для МКПП, АКПП, мостов и ГУР, включая ATF. Поставка со склада в Ташкенте, подбор по допускам, документы на партию.",
         "Для МКПП, АКПП, мостов и ГУР, включая ATF. Подбираем по классу вязкости SAE, уровню API и допускам производителя узла, отгружаем со склада в Ташкенте.",
         None, None, None,
                  preset="Трансмиссионные масла",
         uses=[("МКПП и раздаточные коробки", "Масла классов GL-4 и GL-5 по вязкости SAE"),
               ("Автоматические коробки", "Жидкости ATF под требования производителя"),
               ("Ведущие мосты и редукторы", "Для высоких нагрузок и пыльных условий"),
               ("Гидроусилители руля", "Специальные жидкости ГУР")],
         faq=[("Как понять, какое масло нужно в мост?",
               "По руководству на технику: класс API GL-4 или GL-5, вязкость SAE и наличие требования по противозадирным присадкам. Если документации нет, скажите марку и модель — подберём по каталогу."),
              ("Можно ли одним маслом закрыть весь парк?",
               "Часто да. Для смешанных парков мы специально подбираем перечень так, чтобы одна позиция закрывала максимум узлов: меньше остатков на складе и меньше риска залить не то.")],
         longread=("Как подбираем",
                   "Для смешанных парков составляем перечень так, чтобы одно масло закрывало максимум узлов: меньше позиций на складе заказчика и меньше риска залить не то."))

category("/grease", "grease.html", "Пластичные смазки",
         "Пластичные смазки Газпромнефть в Ташкенте",
         "Пластичные смазки Газпромнефть в Узбекистане и Ташкенте",
         "Пластичные смазки Gazpromneft: литиевые, кальциевые, высокотемпературные, Steelgrease. Склад в Ташкенте, фасовки от картриджа до бочки, документы на партию.",
         "Литиевые, кальциевые, высокотемпературные смазки и линейка Steelgrease. Фасовки от картриджа до бочки, наличие на складе в Ташкенте, паспорт качества на каждую партию.",
         "grease", (1200, 674),
         "Пластичная смазка в подшипнике — смазки Газпромнефть",
                  preset="Пластичные смазки",
         uses=[("Подшипники качения и скольжения", "Литиевые смазки общего назначения"),
               ("Высокие температуры", "Металлургия, цементные и стекольные производства"),
               ("Влага и мойка", "Кальциевые и комплексные смазки, стойкие к вымыванию"),
               ("Открытые узлы и канаты", "Адгезионные составы для карьерной техники")],
         faq=[("Чем заменить Литол-24?",
               "Зависит от того, почему он перестал держать. При высокой температуре нужен другой загуститель, при вымывании — водостойкая смазка, при высокой нагрузке — состав с противозадирными присадками. Опишите узел, подберём."),
              ("В какой фасовке поставляете?",
               "От картриджа до бочки. Точные фасовки по конкретной позиции уточним при подборе.")],
         longread=("Как подбираем",
                   "По температуре в узле, нагрузке и наличию влаги или абразива. Там, где универсальная смазка перестаёт держать, обычно нужен переход на другой загуститель, а не увеличение частоты смазывания."))

category("/fluids", "fluids.html", "Технические жидкости и СОЖ",
         "Технические жидкости и СОЖ Газпромнефть в Ташкенте",
         "Антифризы, тормозные жидкости и СОЖ Газпромнефть",
         "Антифризы, тормозные жидкости и смазочно-охлаждающие жидкости Gazpromneft со склада в Ташкенте. Фасовки от 1 л до кубовых ёмкостей, документы на партию.",
         "Антифризы, тормозные жидкости, смазочно-охлаждающие жидкости. Фасовки от литра до кубовых ёмкостей, наличие на складе в Ташкенте, паспорт качества на каждую партию.",
         "fluids", (1200, 674),
         "Смазочно-охлаждающая жидкость при обработке металла",
                  preset="Антифризы, тормозные жидкости, СОЖ",
         uses=[("Антифризы", "Под требования производителя техники и климат региона"),
               ("Смазочно-охлаждающие жидкости", "Под материал заготовки и тип обработки"),
               ("Тормозные жидкости", "Классы DOT для грузового и легкового транспорта"),
               ("Промывочные составы", "Для перехода с одной марки масла на другую")],
         faq=[("Какой антифриз подойдёт для нашей техники?",
               "Смотрим на требование производителя — карбоксилатный, лобридный или традиционный состав, и на температуру в регионе эксплуатации. Скажите марку техники, подберём."),
              ("Как подобрать СОЖ?",
               "По материалу заготовки, типу обработки и оборудованию. Универсальной жидкости под всё не бывает: то, что хорошо работает на стали, может не подойти для алюминия.")],
         longread=("Как подбираем",
                   "Для производств — СОЖ под материал заготовки и тип обработки, для автопарков — антифриз под требования производителя техники и климат региона."))

print("категории готовы")

HOME_FAQ = [('Можно ли заменить импортное масло на Газпромнефть?', 'Да. Подбираем аналог по классу вязкости, уровню очистки и допуску производителя оборудования — для Shell, Mobil, Total, Castrol и других марок. Прикладываем протокол сравнения характеристик и рекомендации по промывке системы перед переходом.'), ('Какие документы даёте на поставку?', 'Договор, счёт-фактуру, товарно-транспортные документы и паспорт качества на партию. Для тендерных процедур собираем пакет под требования заказчика, включая дистрибьюторское письмо и сертификаты соответствия.'), ('Как быстро получится отгрузить?', 'Позиции со склада в Ташкенте отгружаем в течение 24 часов после заявки. Если нужной позиции нет в наличии, сразу скажем срок поставки, а не будем тянуть.'), ('Как убедиться, что продукция оригинальная?', 'ООО «Smart Energy Eco Trade» — официальный дистрибьютор «Газпромнефть — смазочные материалы» в Узбекистане. Работаем напрямую с заводами производителя, на каждую партию есть паспорт качества.'), ('Сколько стоит подбор?', 'Ничего. Технический специалист разбирает перечень техники, подбирает позиции и считает годовой объём бесплатно и без обязательств — это часть нашей работы, а не отдельная услуга.'), ('Работаете с предприятиями в регионах?', 'Да, поставляем в Ташкент, Самарканд, Бухару, Навои и Ферганскую долину. Условия доставки обсуждаем при заявке.')]

# --------------------------------------------------------------- главная
home = """
<main>

  <section class="hero">
    <div class="wrap hero__grid">
      <div class="hero__body">
        <span class="hero__badge">Склад в Ташкенте · отгрузка за 24 часа</span>
        <h1>Газпромнефть Узбекистан&nbsp;— смазочные материалы для предприятий</h1>
        <p class="hero__lead">Подберём масло под вашу технику и пришлём прайс с наличием за 15 минут. Со склада в Ташкенте, отгрузка за 24 часа, полный пакет документов для бухгалтерии и тендера.</p>
        <div class="hero__actions">
          <a class="btn btn--orange" href="tel:+998908085972">Позвонить: +998 90 808 59 72</a>
          <a class="btn btn--onDark" href="#zayavka">Получить подбор и прайс</a>
        </div>
        <div class="trust">
          <span>Официальный дистрибьютор</span>
          <span>Паспорт качества на партию</span>
          <span>Доставка по Узбекистану</span>
        </div>
      </div>
      <img class="hero__media" src="/img/hero.webp" srcset="/img/hero-sm.webp 700w, /img/hero-md.webp 960w, /img/hero.webp 1400w" sizes="(max-width:900px) 100vw, 45vw" alt="Линия розлива масел Газпромнефть" width="{herow}" height="{heroh}" fetchpriority="high" decoding="async">
    </div>
  </section>

  <div class="stats">
    <div class="wrap stats__in">
      <div class="stats__item"><div class="stats__num">9 лет</div><div class="stats__label">поставок в Узбекистане</div></div>
      <div class="stats__item"><div class="stats__num">600+</div><div class="stats__label">позиций на складе</div></div>
      <div class="stats__item"><div class="stats__num">24 часа</div><div class="stats__label">от заявки до отгрузки</div></div>
      <div class="stats__item"><div class="stats__num">НГМК, УзАвто</div><div class="stats__label">среди наших заказчиков</div></div>
    </div>
  </div>

  <section class="section" id="products">
    <div class="wrap">
      <div class="section__head">
        <div>
          <h2>Продукция</h2>
          <p class="section__sub">Полная линейка Gazpromneft, G-Profi и G-Energy со склада в Ташкенте</p>
        </div>
        <a class="section__link" href="/products">Весь каталог →</a>
      </div>
      <div class="cards">
{cards}
      </div>
    </div>
  </section>

  <section class="split">
    <div class="split__body">
      <h2>Подберём масло под ваше оборудование</h2>
      <p>Пришлите список техники или действующие марки масел — технический специалист подготовит подбор с аналогами и расчёт объёма на год.</p>
      <div class="steps">
        <div class="step"><b>1</b><span>Отправляете перечень техники в форме, в Telegram или по телефону</span></div>
        <div class="step"><b>2</b><span>Получаете подбор, TDS и коммерческое предложение</span></div>
        <div class="step"><b>3</b><span>Отгружаем со склада в Ташкенте, доставка по Узбекистану</span></div>
      </div>
      <div class="split__actions">
        <a class="btn btn--navy" href="#zayavka">Отправить заявку</a>
        <a class="btn btn--outline" href="/podbor">Как проходит подбор</a>
      </div>
    </div>
    <img class="split__media" src="/img/podbor.webp" srcset="/img/podbor-sm.webp 390w, /img/podbor.webp 780w" sizes="(max-width:900px) 100vw, 50vw" alt="Оператор на линии розлива масла Газпромнефть" width="{podborw}" height="{podborh}" loading="lazy" decoding="async">
  </section>

  <section class="section section--tight" id="industries">
    <div class="wrap">
      <div class="section__head">
        <div><h2>Отрасли</h2><p class="section__sub">Что обычно нужно на разных производствах</p></div>
        <a class="section__link" href="/otrasli">Все отрасли →</a>
      </div>
      <div class="tiles">
        <a class="tile" href="/hydralic"><b>Горнодобыча</b><span>Гидравлика карьерной техники, редукторные масла ГОК</span></a>
        <a class="tile" href="/grease"><b>Металлургия</b><span>Термостойкие смазки, СОЖ, теплоносители</span></a>
        <a class="tile" href="/gpn"><b>Транспорт и логистика</b><span>Моторные масла для парков грузовой техники и автобусов</span></a>
        <a class="tile" href="/industrial"><b>Энергетика</b><span>Турбинные и трансформаторные масла</span></a>
      </div>
    </div>
  </section>

  <section class="section section--tight section--grey">
    <div class="wrap seo">
      <div class="seo__text">
        <h2>Где купить смазочные материалы Газпромнефть в Узбекистане</h2>
        <p>ООО «Smart Energy Eco Trade» поставляет продукцию Gazpromneft, G-Profi и G-Energy предприятиям Ташкента, Самарканда, Бухары, Навои и Ферганской долины. На складе постоянно доступны гидравлические масла HLP 32, 46 и 68, редукторные масла CLP, моторные масла для грузовой и карьерной техники, пластичные смазки и антифризы в фасовках от 1 литра до кубовых ёмкостей.</p>
        <p>Для промышленных предприятий мы готовим годовые спецификации с фиксированной ценой, оформляем поставку по договору и предоставляем полный пакет документов для участия в тендерных процедурах. Технические специалисты помогают подобрать масло под конкретное оборудование и перейти на продукт Газпромнефть с импортных марок.</p>
      </div>
      <aside class="callout">
        <b>Получить прайс-лист</b>
        <p>Пришлём актуальный прайс и наличие на складе в течение 15 минут.</p>
        <a class="btn btn--orange" href="#zayavka">Оставить заявку</a>
        <a class="btn btn--onDark" href="tel:+998908085972">+998 90 808 59 72</a>
        <small>Тимур Яруллин, корпоративный менеджер.</small>
      </aside>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section__head"><div><h2>Нам доверяют</h2></div></div>
      <div class="logos">
        <img src="/img/logo-ngmk.webp" alt="Навоийский горно-металлургический комбинат" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-enter.webp" alt="Enter Engineering" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-ttz.webp" alt="Ташкентский трубный завод имени В. Л. Гальперина" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-ahangaran.webp" alt="Akhangarancement" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-cement.webp" alt="Namangan Sement" width="360" height="240" loading="lazy" decoding="async">
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section__head">
        <div>
          <h2>Почему берут у нас</h2>
          <p class="section__sub">Что снабженец обычно проверяет перед первой поставкой</p>
        </div>
      </div>
      <div class="why">
        <div class="why__item"><b>Официальный дистрибьютор</b><span>Продукция идёт напрямую с заводов производителя, а не через перекупщиков. На каждую партию — паспорт качества.</span></div>
        <div class="why__item"><b>Подбор техническим специалистом</b><span>Разбираем перечень техники, подбираем позиции и считаем годовой объём. Бесплатно и без обязательств.</span></div>
        <div class="why__item"><b>Замена импортных марок</b><span>Подбираем аналоги Shell, Mobil, Total и Castrol с протоколом сравнения характеристик.</span></div>
        <div class="why__item"><b>Склад в Ташкенте</b><span>То, что есть в наличии, отгружаем за 24 часа. Чего нет — сразу называем срок, а не тянем.</span></div>
        <div class="why__item"><b>Документы для тендера</b><span>Договор, счёт-фактура, паспорт качества, сертификаты и дистрибьюторское письмо. Пакет собираем под требования заказчика.</span></div>
        <div class="why__item"><b>Годовые спецификации</b><span>Для предприятий с постоянной потребностью фиксируем цену на период — не нужно согласовывать каждую поставку заново.</span></div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--grey">
    <div class="wrap" style="max-width:920px">
      <div class="section__head"><div><h2>Частые вопросы</h2></div></div>
{faqhtml}
    </div>
  </section>

  <section class="formband" id="zayavka">
    <div class="wrap formband__in">
      <div class="formband__body">
        <h2>Пришлите перечень техники — вернём подбор и прайс</h2>
        <p class="formband__lead">Не нужно знать артикулы и классы вязкости. Достаточно написать, какая техника и что в неё заливают сейчас — остальное сделает технический специалист.</p>
        <div class="formband__list">
          <span>Подбор с аналогами импортных марок и расчёт объёма на год</span>
          <span>Прайс с фактическим наличием на складе в Ташкенте</span>
          <span>Техническое описание TDS и паспорт безопасности MSDS</span>
          <span>Полный пакет документов для бухгалтерии и тендера</span>
        </div>
        <div class="formband__alt">
          <span>Быстрее по телефону:</span>
          <a href="tel:+998908085972">+998 90 808 59 72</a>
          <span>или</span>
          <a href="{tg}" rel="noopener">напишите в Telegram</a>
        </div>
      </div>
{form}
    </div>
  </section>

</main>
""".format(tg=TG, cards=cards_html(), herow=dim("hero")[0], heroh=dim("hero")[1], podborw=dim("podbor")[0], podborh=dim("podbor")[1], faqhtml=faq_html(HOME_FAQ), form=leadform("Заявка с главной", "Подбор и прайс за 15 минут", "Заполните два поля — остальное уточним сами.", "Получить подбор и прайс"))

page("/", "index.html",
     "Газпромнефть Узбекистан — официальный дистрибьютор масел",
     "Газпромнефть Узбекистан: индустриальные, моторные и трансмиссионные масла, смазки и техжидкости. Склад в Ташкенте, отгрузка за 24 часа, документы для тендера.",
     home, preload="/img/hero.webp", preload_sizes="(max-width:900px) 100vw, 45vw",
     jsonld=ORG_LD + faq_ld(HOME_FAQ), cta=False,
     ogtitle="Газпромнефть Узбекистан — официальный дистрибьютор",
     ogdesc="Официальный дистрибьютор «Газпромнефть — смазочные материалы». Склад в Ташкенте, подбор под оборудование, полный пакет документов.")

# --------------------------------------------------------------- продукция
products = """
<main>
  <nav class="wrap crumbs" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>Продукция</b>
  </nav>

  <div class="wrap page">
    <div class="pagehero">
      <img src="/img/products.webp" srcset="/img/products-sm.webp 700w, /img/products-md.webp 960w, /img/products.webp 1400w" sizes="100vw" alt="Склад смазочных материалов Газпромнефть" width="{pw}" height="{ph}" fetchpriority="high" decoding="async">
    </div>
    <div class="page__head">
      <h1>Продукция Газпромнефть в Узбекистане</h1>
      <p class="page__lead">Более 600 позиций со склада в Ташкенте: индустриальные и моторные масла, трансмиссионные масла, пластичные смазки, антифризы и СОЖ. На каждую партию — паспорт качества, для тендеров готовим полный пакет документов.</p>
    </div>

    <div class="cards">
{cards}
    </div>

    <div class="section__head" style="margin-top:56px">
      <div>
        <h2>Индустриальные масла по назначению</h2>
        <p class="section__sub">Отдельные страницы с перечнем позиций и классами вязкости</p>
      </div>
    </div>
    <div class="tiles">
      <a class="tile" href="/hydralic"><b>Гидравлические</b><span>Gazpromneft Hydraulic HLP 32, 46, 68</span></a>
      <a class="tile" href="/reductor"><b>Редукторные</b><span>Gazpromneft Reductor CLP 150, 220</span></a>
      <a class="tile" href="/compressor"><b>Компрессорные</b><span>Gazpromneft Compressor Oil 46</span></a>
      <a class="tile" href="/industrial"><b>Турбинные и теплоносители</b><span>Turbine Oil 32, Termoil 26</span></a>
    </div>

    <div class="layout" style="margin-top:44px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Подбор под оборудование</h2>
          <p>Если не знаете, что именно нужно, пришлите перечень техники или действующие марки масел. Технический специалист подберёт позиции с аналогами, посчитает годовой объём и приложит TDS. Подбор бесплатный и ни к чему не обязывает.</p>
          <p>Смотрите также <a href="/podbor" style="color:var(--blue);font-weight:600">как проходит подбор</a>, <a href="/analogi" style="color:var(--blue);font-weight:600">таблицу замены импортных марок</a> и <a href="/otrasli" style="color:var(--blue);font-weight:600">решения по отраслям</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
{catalogform}
      </aside>
    </div>
  </div>
</main>
""".format(cards=cards_html(indent="      "), pw=dim("products")[0], ph=dim("products")[1],
           catalogform=leadform("Заявка из каталога", "Не нашли нужную позицию?",
                                "Напишите, что требуется, — проверим наличие и пришлём цену.",
                                "Отправить заявку", cls=" leadform--aside", anchor="zayavka"))

page("/products", "products.html", "Продукция Газпромнефть — каталог масел и смазок",
     "Каталог смазочных материалов Gazpromneft, G-Profi и G-Energy со склада в Ташкенте: индустриальные, моторные, трансмиссионные масла, пластичные смазки, антифризы и СОЖ.",
     products, active="products", preload="/img/products.webp", formhref="#zayavka",
     jsonld=crumbs_ld([("Главная", "/"), ("Продукция", "/products")]))

PRICE_FAQ = [('Почему цен нет прямо на сайте?', 'Цена зависит от объёма выборки, фасовки и условий отгрузки: одна и та же позиция в канистрах и в кубовой ёмкости стоит по-разному. Прайс с актуальными цифрами присылаем по запросу в тот же день.'), ('Можно ли зафиксировать цену на год?', 'Для предприятий с постоянной потребностью готовим годовую спецификацию с фиксированной ценой — это защищает от колебаний курса и снимает необходимость согласовывать каждую поставку заново.'), ('Какие документы приходят с поставкой?', 'Договор, счёт-фактура, товарно-транспортные документы и паспорт качества на партию. Для тендера дополнительно собираем сертификаты соответствия и дистрибьюторское письмо.')]

# --------------------------------------------------------------- цены
price = """
<main>
  <nav class="wrap crumbs" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>Цены</b>
  </nav>

  <div class="wrap page">
    <div class="layout">
      <div class="layout__main">
        <h1>Цены на смазочные материалы Газпромнефть</h1>
        <p class="page__lead">Прайс-лист высылаем по запросу: цена зависит от объёма, фасовки и условий отгрузки, поэтому фиксированного прайса на сайте нет. Актуальный документ с наличием на складе в Ташкенте отправляем в течение 15 минут в рабочее время.</p>

{priceform}

        <div class="longread">
          <h2>От чего зависит цена</h2>
          <p>На стоимость влияют объём выборки, фасовка (канистра, бочка, кубовая ёмкость), периодичность отгрузок и условия оплаты. Для предприятий с годовой потребностью выгоднее спецификация с фиксированной ценой: она защищает от колебаний курса и снимает необходимость согласовывать каждую поставку заново.</p>
          <h2>Документы для бухгалтерии и тендера</h2>
          <p>Поставляем по договору с полным пакетом: счёт-фактура, товарно-транспортные документы, паспорт качества на партию, сертификаты соответствия и дистрибьюторское письмо. Для тендерных процедур собираем комплект под требования заказчика.</p>
        </div>
{pricefaq}
      </div>

      <aside class="layout__aside">
{aside}
        <div class="asidebox">
          <b>Популярные позиции</b>
          <div>
            <a href="/hydralic">Гидравлические HLP 32, 46, 68</a>
            <a href="/reductor">Редукторные CLP 150, 220</a>
            <a href="/gpn">Моторные для грузовой техники</a>
            <a href="/grease">Пластичные смазки</a>
            <a href="/fluids">Антифризы и СОЖ</a>
          </div>
        </div>
      </aside>
    </div>
  </div>
</main>
""".format(tg=TG, aside=ASIDE_REQUEST, pricefaq=faq_html(PRICE_FAQ), priceform=leadform("Запрос прайс-листа", "Получить прайс-лист", "Пришлём актуальный прайс с наличием на складе в Ташкенте.", "Получить прайс", anchor="zayavka"))

page("/price", "price.html", "Цены на масла Газпромнефть в Узбекистане — прайс-лист",
     "Прайс-лист на масла и смазки Gazpromneft в Узбекистане. Цена зависит от объёма и фасовки — пришлём актуальный прайс с наличием на складе в Ташкенте в течение 15 минут.",
     price, active="price",      jsonld=crumbs_ld([("Главная", "/"), ("Цены", "/price")]) + faq_ld(PRICE_FAQ))

# --------------------------------------------------------------- о компании
company = """
<main>
  <nav class="wrap crumbs" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>О компании</b>
  </nav>

  <div class="wrap intro">
    <div class="intro__body">
      <h1>ООО «Smart Energy Eco Trade»</h1>
      <p>Официальный дистрибьютор «Газпромнефть — смазочные материалы» в Республике Узбекистан. Поставляем масла, смазки и технические жидкости предприятиям промышленности, автопаркам и сервисным центрам по всей стране.</p>
      <p>Работаем напрямую с заводами производителя: каждая партия сопровождается паспортом качества, а технические специалисты помогают с подбором продукта и переходом с импортных марок.</p>
    </div>
    <img class="intro__media" src="/img/company.webp" srcset="/img/company-sm.webp 600w, /img/company-md.webp 960w, /img/company.webp 1200w" sizes="(max-width:900px) 100vw, 50vw" alt="Специалисты Газпромнефть у бочки с маслом" width="1200" height="896" fetchpriority="high" decoding="async">
  </div>

  <div class="stats">
    <div class="wrap stats__in">
      <div class="stats__item"><div class="stats__num">2017</div><div class="stats__label">год начала поставок</div></div>
      <div class="stats__item"><div class="stats__num">600+</div><div class="stats__label">позиций ассортимента</div></div>
      <div class="stats__item"><div class="stats__num">12 регионов</div><div class="stats__label">география поставок</div></div>
      <div class="stats__item"><div class="stats__num">100%</div><div class="stats__label">официальная продукция</div></div>
    </div>
  </div>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section__head"><div><h2>Документы и статус</h2></div></div>
      <div class="why">
        <div class="why__item"><b>Дистрибьюторский статус</b><span>Официальный дистрибьютор «Газпромнефть — смазочные материалы» в Республике Узбекистан. Письмо предоставляем по запросу — в том числе для тендерных процедур.</span></div>
        <div class="why__item"><b>Сертификаты соответствия</b><span>На поставляемую продукцию. Прикладываем к поставке или высылаем заранее, если нужны для входного контроля.</span></div>
        <div class="why__item"><b>Паспорт качества на партию</b><span>Каждая партия сопровождается паспортом качества завода-изготовителя с фактическими показателями.</span></div>
        <div class="why__item"><b>Договор поставки</b><span>Работаем по договору со счётом-фактурой и товарно-транспортными документами.</span></div>
        <div class="why__item"><b>Документы TDS и MSDS</b><span>Технические описания и паспорта безопасности — в <a href="/docs" style="color:var(--blue)">разделе документации</a> или по запросу.</span></div>
        <div class="why__item"><b>Пакет для тендера</b><span>Собираем комплект под требования конкретной закупки, включая дистрибьюторское письмо.</span></div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0">
    <div class="wrap">
      <div class="section__head"><div><h2>Нам доверяют</h2></div></div>
      <div class="logos">
        <img src="/img/logo-ngmk.webp" alt="Навоийский горно-металлургический комбинат" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-enter.webp" alt="Enter Engineering" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-ttz.webp" alt="Ташкентский трубный завод имени В. Л. Гальперина" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-ahangaran.webp" alt="Akhangarancement" width="360" height="240" loading="lazy" decoding="async">
        <img src="/img/logo-cement.webp" alt="Namangan Sement" width="360" height="240" loading="lazy" decoding="async">
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0">
    <div class="wrap layout">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Как начать работать</h2>
          <p>Первый шаг — заявка с перечнем техники или списком масел, которые вы закупаете сейчас. Технический специалист готовит подбор, менеджер — прайс с наличием и проект договора. Дальше отгружаем со склада в Ташкенте, обычно в течение суток.</p>
          <p>Подробнее: <a href="/podbor" style="color:var(--blue);font-weight:600">как проходит подбор</a>, <a href="/dostavka" style="color:var(--blue);font-weight:600">доставка и оплата</a>, <a href="/docs" style="color:var(--blue);font-weight:600">документация TDS и MSDS</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
{companyform}
      </aside>
    </div>
  </section>
</main>
"""

page("/company", "company.html", "О компании — Smart Energy Eco Trade, дистрибьютор Газпромнефть",
     "ООО «Smart Energy Eco Trade» — официальный дистрибьютор «Газпромнефть — смазочные материалы» в Узбекистане с 2017 года. Поставки по 12 регионам.",
     body=company.format(companyform=leadform("Заявка со страницы «О компании»", "Начать работу",
                                        "Напишите, что требуется, — вернёмся с подбором и ценой.",
                                        "Отправить заявку", cls=" leadform--aside", anchor="zayavka")),
     active="company", preload="/img/company.webp", preload_sizes="(max-width:900px) 100vw, 50vw",
     formhref="#zayavka",
     jsonld=crumbs_ld([("Главная", "/"), ("О компании", "/company")]))

# --------------------------------------------------------------- документация
DOCS = [
    ("Gazpromneft Hydraulic HLP 46", "Индустриальные", "02.2026", "gazpromneft-hydraulic-hlp-46"),
    ("Gazpromneft Reductor CLP 220", "Индустриальные", "02.2026", "gazpromneft-reductor-clp-220"),
    ("G-Profi MSI Plus 15W-40", "Моторные", "01.2026", "g-profi-msi-plus-15w-40"),
    ("G-Profi GT 10W-40", "Моторные", "01.2026", "g-profi-gt-10w-40"),
    ("G-Energy Synthetic Active 5W-40", "Моторные", "12.2025", "g-energy-synthetic-active-5w-40"),
    ("Gazpromneft Grease L EP 2", "Смазки", "11.2025", "gazpromneft-grease-l-ep-2"),
    ("Gazpromneft Antifreeze SF 40", "Жидкости", "11.2025", "gazpromneft-antifreeze-sf-40"),
]
rows = "\n".join("""      <div class="table__row" data-name="{name} {cat}">
        <b>{name}</b>
        <span><span class="table__label">Категория: </span>{cat}</span>
        <span><span class="table__label">Обновлён: </span>{date}</span>
        <div class="table__files table__files--btn"><a href="#zapros">Запросить TDS</a><a href="#zapros">Запросить MSDS</a></div>
      </div>""".format(name=n, cat=c, date=d, slug=s) for n, c, d, s in DOCS)

docs = """
<main class="wrap page" style="padding-top:40px">
  <nav class="crumbs" style="padding-top:0" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>Документация</b>
  </nav>
  <div class="page__head">
    <h1>Документация TDS и MSDS</h1>
    <p class="page__lead">Технические описания и паспорта безопасности на продукцию Gazpromneft, G-Profi и G-Energy. Если нужного документа нет в списке — запросите его ниже, пришлём в течение рабочего дня.</p>
  </div>

  <div class="search">
    <input id="docsearch" type="search" placeholder="Поиск по названию продукта" aria-label="Поиск по названию продукта" autocomplete="off">
  </div>

  <div class="table table--docs" id="docstable">
    <div class="table__head"><div>Продукт</div><div>Категория</div><div>Обновлён</div><div>Документы</div></div>
%s
  </div>
  <p class="table__note" id="docsempty" hidden>Ничего не нашлось — запросите документ ниже, пришлём в течение рабочего дня.</p>

  <div class="layout" style="margin-top:44px">
    <div class="longread" style="padding-top:0">
      <h2>Нужен документ, которого нет в списке</h2>
      <p>Библиотека пополняется. Если нужного TDS или MSDS здесь нет — напишите название продукта, пришлём файл в течение рабочего дня. Заодно подскажем, есть ли позиция на складе и в какой фасовке.</p>
      <p>Если документ нужен для тендера или входного контроля, скажите об этом сразу: соберём полный пакет — паспорт качества на партию, сертификат соответствия и дистрибьюторское письмо.</p>
    </div>
%s
  </div>
</main>
""" % (rows, leadform("Запрос документа TDS/MSDS", "Запросить документ",
                      "Напишите название продукта — пришлём TDS и MSDS.",
                      "Запросить документ", anchor="zapros"))

page("/docs", "docs.html", "Документация TDS и MSDS на продукцию Газпромнефть",
     "Технические описания (TDS) и паспорта безопасности (MSDS) на масла и смазки Gazpromneft, G-Profi, G-Energy. Скачать PDF или запросить нужный документ в Telegram.",
     docs, active="docs", jsonld=crumbs_ld([("Главная", "/"), ("Документация", "/docs")]))

# --------------------------------------------------------------- блог
POSTS = [
    ("Подбор", "Как подобрать гидравлическое масло для карьерной техники",
     "Класс вязкости, чистота по ISO 4406 и допуски производителей — на что смотреть при выборе."),
    ("Аналоги", "Замена импортных масел на Газпромнефть: таблица соответствий",
     "Сопоставление Shell, Mobil, Total и Castrol с продуктами Gazpromneft по ключевым характеристикам."),
    ("Эксплуатация", "Интервалы замены масла в автопарке: на что смотреть",
     "Как условия эксплуатации в Узбекистане влияют на срок службы моторного масла."),
    ("Индустрия", "Редукторные масла CLP: подбор по нагрузке и температуре",
     "Разбор типовых ошибок при выборе масла для промышленных редукторов."),
    ("Смазки", "Пластичные смазки для высоких температур",
     "Где Литол уже не работает и чем его заменить в металлургии и цементной отрасли."),
    ("Документы", "Какие документы нужны для участия в тендере на поставку масел",
     "Перечень документов, которые мы предоставляем предприятиям-заказчикам."),
]
BLOG_IMG = ["cat-industrial", "cat-transmission", "cat-gpn", "reductor", "cat-grease", "products"]
cards = "\n".join("""    <article class="post">
      <img class="post__media" src="/img/{img}-sm.webp" alt="" width="380" height="200" loading="lazy" decoding="async">
      <div class="post__tag">{tag}</div>
      <h2 class="post__title">{title}</h2>
      <p class="post__lead">{lead}</p>
    </article>""".format(img=BLOG_IMG[i], tag=t, title=ti, lead=le)
    for i, (t, ti, le) in enumerate(POSTS))

blog = """
<main class="wrap page" style="padding-top:40px">
  <nav class="crumbs" style="padding-top:0" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>Блог</b>
  </nav>
  <div class="page__head">
    <h1>Блог</h1>
    <p class="page__lead">Разборы по подбору масел, замене импортных марок и эксплуатации техники в условиях Узбекистана.</p>
  </div>
  <div class="posts">
%s
  </div>
  <div class="layout" style="margin-top:44px">
    <div class="longread" style="padding-top:0">
      <h2>Статьи готовятся к публикации</h2>
      <p>Разборы выходят по мере того, как накапливаются вопросы от заказчиков. Если по вашей технике нужен ответ прямо сейчас — не ждите статью, опишите задачу в форме: технический специалист разберёт её предметно и бесплатно.</p>
      <p>Быстрее всего решаются два типа вопросов: <a href=\"/podbor\" style=\"color:var(--blue);font-weight:600\">подбор под конкретную технику</a> и <a href=\"/analogi\" style=\"color:var(--blue);font-weight:600\">замена импортной марки на аналог</a>.</p>
    </div>
%s
  </div>
</main>
""" % (cards, leadform("Вопрос из блога", "Задать вопрос специалисту",
                       "Опишите технику и задачу — ответим по делу.",
                       "Отправить вопрос", cls=" leadform--aside", anchor="zayavka"))

page("/blog", "blog.html", "Блог — подбор масел и смазок для техники в Узбекистане",
     "Разборы по подбору масел Газпромнефть, замене импортных марок и эксплуатации техники в условиях Узбекистана.",
     blog, active="blog", formhref="#zayavka",
     jsonld=crumbs_ld([("Главная", "/"), ("Блог", "/blog")]))

# --------------------------------------------------------------- контакты
LOCAL_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LocalBusiness","name":"Smart Energy Eco Trade — Газпромнефть Узбекистан","url":"https://gpn-oil.uz/contacts","image":"https://gpn-oil.uz/img/hero.webp","telephone":"+998908085972","email":"t.yarulin@s-energy.uz","address":{"@type":"PostalAddress","addressLocality":"Ташкент","addressCountry":"UZ"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"18:00"}],"priceRange":"$$","sameAs":["https://instagram.com/gpn_oil.uz"]}
</script>
"""

contacts = """
<main>
  <nav class="wrap crumbs" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>Контакты</b>
  </nav>
  <div class="wrap contacts" style="padding-top:12px">
    <div class="contacts__col">
      <h1>Контакты</h1>
      <h2 style="font-size:19px;font-weight:600;color:var(--muted)">Отдел продаж и технический специалист</h2>
      <div class="calls">
        <a class="call" href="tel:+998908085972">+998 90 808 59 72<span>Тимур Яруллин · корпоративный менеджер</span></a>
        <a class="call" href="tel:+998935048490">+998 93 504 84 90<span>отдел продаж</span></a>
        <a class="call call--tg" href="{tg}" rel="noopener">Telegram<span>@GPN_OIL_UZ · ответ за 15 минут</span></a>
      </div>
      <dl class="meta">
        <div class="meta__item"><dt>Почта</dt><dd><a href="mailto:t.yarulin@s-energy.uz">t.yarulin@s-energy.uz</a></dd></div>
        <div class="meta__item"><dt>Время работы</dt><dd>Пн–Пт, 09:00–18:00</dd></div>
        <div class="meta__item"><dt>Адрес</dt><dd>Ташкент, Узбекистан</dd></div>
        <div class="meta__item"><dt>Компания</dt><dd>ООО «Smart Energy Eco Trade»</dd></div>
        <div class="meta__item"><dt>Instagram</dt><dd><a href="{insta}" rel="noopener">@gpn_oil.uz</a></dd></div>
      </dl>
    </div>

    <div class="contacts__col">
      <div class="asidebox" style="padding:30px">
        <h2 style="font-size:19px">Как с нами работать</h2>
        <div style="gap:14px;color:var(--muted);font-size:15px;line-height:1.6">
          <span><b style="color:var(--ink)">1. Заявка.</b> Позвоните или заполните форму — опишите технику или нужные позиции.</span>
          <span><b style="color:var(--ink)">2. Подбор и счёт.</b> Технический специалист готовит подбор, менеджер — прайс с наличием и договор.</span>
          <span><b style="color:var(--ink)">3. Отгрузка.</b> Со склада в Ташкенте, обычно в течение суток. Доставка по Узбекистану или самовывоз.</span>
        </div>
      </div>

      <form class="form" id="zayavka" method="post" action="https://gpn-relay.zvezdotank.workers.dev/">
        <b>Оставить заявку</b>
        <input class="trap" type="text" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="_form" value="Заявка с сайта">
        <div class="form__fields">
          <label class="field"><span>Имя</span><input name="name" autocomplete="name"></label>
          <label class="field"><span>Телефон</span><input name="phone" type="tel" placeholder="+998" autocomplete="tel" required></label>
          <label class="field"><span>Что нужно подобрать или сколько требуется</span><textarea name="task" rows="3"></textarea></label>
        </div>
        <button type="submit">Отправить заявку</button>
        <small>Заявка приходит менеджеру в Telegram, отвечаем в рабочее время.</small>
      </form>
    </div>
  </div>
</main>
""".format(tg=TG, insta=INSTA)

page("/contacts", "contacts.html", "Контакты — Газпромнефть Узбекистан, Smart Energy Eco Trade",
     "Телефоны корпоративного менеджера и отдела продаж, Telegram, почта и форма заявки. Ташкент, Пн–Пт с 09:00 до 18:00.",
     contacts, active="contacts", jsonld=LOCAL_LD + crumbs_ld([("Главная", "/"), ("Контакты", "/contacts")]))

# --------------------------------------------------------------- служебные
page("/spasibo", "spasibo.html", "Заявка отправлена — Газпромнефть Узбекистан",
     "Заявка принята, менеджер свяжется в рабочее время.", """
<main class="wrap note">
  <h1>Спасибо, заявку приняли</h1>
  <p>Менеджер посмотрит перечень и ответит в рабочее время — Пн–Пт с 09:00 до 18:00. Если вопрос срочный, позвоните — ответим сразу.</p>
  <div class="empty__actions">
    <a class="btn btn--blue" href="tel:+998908085972">+998 90 808 59 72</a>
    <a class="btn btn--outline" href="/">Вернуться на главную</a>
  </div>
</main>
""".format(tg=TG), noindex=True)

page("/oshibka", "oshibka.html", "Заявка не отправилась — Газпромнефть Узбекистан",
     "Форма не смогла отправить заявку. Свяжитесь с нами напрямую.", """
<main class="wrap note">
  <h1>Заявка не ушла</h1>
  <p>Что-то сломалось на нашей стороне, и форма не смогла передать заявку. Чтобы не терять время, позвоните — ответим сразу.</p>
  <div class="empty__actions">
    <a class="btn btn--blue" href="tel:+998908085972">+998 90 808 59 72</a>
    <a class="btn btn--outline" href="tel:+998935048490">+998 93 504 84 90</a>
  </div>
</main>
""".format(tg=TG), noindex=True)

page("/404", "404.html", "Страница не найдена — Газпромнефть Узбекистан",
     "Такой страницы нет. Перейдите в каталог продукции или напишите менеджеру.", """
<main class="wrap note">
  <h1>Такой страницы нет</h1>
  <p>Возможно, адрес изменился при обновлении сайта. Загляните в каталог продукции или напишите менеджеру — подскажем, где искать.</p>
  <div class="empty__actions">
    <a class="btn btn--blue" href="/products">Каталог продукции</a>
    <a class="btn btn--outline" href="/contacts">Контакты</a>
  </div>
</main>
""", noindex=True)

print("готово")

# =========================================================== новые страницы

def simple(path, fname, crumb, h1, title, desc, active, blocks, faq=None, img=None, alt=""):
    hero = ""
    if img:
        iw, ih = dim(img)
        hero = '''    <div class="pagehero">
      <img src="/img/%s.webp" srcset="%s" sizes="100vw" alt="%s" width="%d" height="%d" fetchpriority="high" decoding="async">
    </div>
''' % (img, srcset(img, iw), alt, iw, ih)
    faq_block = ""
    if faq:
        faq_block = '''
    <div class="longread"><h2>Частые вопросы</h2></div>
%s''' % faq_html(faq)
    body = '''
<main>
  <nav class="wrap crumbs" aria-label="Хлебные крошки">
    <a href="/">Главная</a><span>/</span><b>%s</b>
  </nav>
  <div class="wrap page">
%s    <div class="page__head">
      <h1>%s</h1>
    </div>
%s%s
  </div>
</main>
''' % (crumb, hero, h1, blocks, faq_block)
    return page(path, fname, title, desc, body, active=active, formhref="#zayavka",
                preload=("/img/%s.webp" % img) if img else None,
                jsonld=crumbs_ld([("Главная", "/"), (crumb, path)]) + (faq_ld(faq) if faq else ""))


# ---------------------------------------------------------------- подбор
PODBOR_FAQ = [
 ("Сколько стоит подбор?",
  "Нисколько. Подбор — часть работы поставщика, а не отдельная услуга. Заявка ни к чему не обязывает: можете взять подбор и сравнить его с другими предложениями."),
 ("Что делать, если документации на технику нет?",
  "Достаточно марки и модели узла. По каталогам производителей мы находим требование по классу вязкости и допуску. Если и модель неизвестна — подойдёт фотография шильдика или этикетки того масла, которое залито сейчас."),
 ("Как быстро придёт ответ?",
  "В рабочее время — в течение 15 минут по простым запросам. Если в перечне десятки единиц техники, на полный подбор с расчётом годового объёма уходит один рабочий день."),
 ("Дадите пробную партию?",
  "Условия первой поставки обсуждаем отдельно — напишите объём и тип техники, менеджер предложит вариант."),
]

podbor_blocks = '''    <p class="page__lead" style="max-width:760px">Пришлите перечень техники или марки масел, которые заливаете сейчас, — технический специалист подберёт позиции Gazpromneft, посчитает годовой объём и пришлёт прайс с наличием. Бесплатно и без обязательств.</p>

    <div class="why" style="margin-top:32px">
      <div class="why__item"><b>Подбор по технике</b><span>Марка и модель — находим требование производителя по классу вязкости, уровню API или ACEA и допуску.</span></div>
      <div class="why__item"><b>Подбор по аналогу</b><span>Скажите, что залито сейчас, — подберём продукт Gazpromneft того же класса и уровня и покажем сравнение характеристик.</span></div>
      <div class="why__item"><b>Расчёт объёма</b><span>Считаем годовую потребность по количеству техники и интервалам замены — с этим удобно защищать бюджет.</span></div>
    </div>

    <div class="longread">
      <h2>Как проходит подбор</h2>
    </div>
    <div class="steps" style="margin-bottom:32px">
      <div class="step"><b>1</b><span>Вы присылаете перечень техники или список действующих марок масел — в форме ниже, по телефону или на почту</span></div>
      <div class="step"><b>2</b><span>Технический специалист сверяет допуски и классы вязкости, подбирает позиции и считает объём</span></div>
      <div class="step"><b>3</b><span>Вы получаете подбор с аналогами, техническое описание TDS и прайс с фактическим наличием на складе</span></div>
      <div class="step"><b>4</b><span>Если всё устраивает — оформляем поставку по договору и отгружаем со склада в Ташкенте</span></div>
    </div>

    <div class="layout">
      <div class="layout__main">
        <div class="checklist">
          <b>Что написать в заявке, чтобы ответ был точным</b>
          <span>Марка и модель техники или узла: двигатель, гидравлика, редуктор, коробка</span>
          <span>Какое масло залито сейчас — марка или допуск с этикетки</span>
          <span>Условия работы: карьер, цех, город, круглосуточная смена</span>
          <span>Примерный объём — на одну заправку или на год</span>
          <span>Нужная фасовка: канистра, бочка, кубовая ёмкость</span>
        </div>
        <div class="longread">
          <h2>Что вы получаете на выходе</h2>
          <p>Таблицу подбора: под каждую единицу техники — позиция Gazpromneft, класс вязкости, уровень качества и фасовка. К ней прикладываем техническое описание TDS и паспорт безопасности MSDS, а при переходе с импортной марки — сравнение ключевых характеристик, чтобы инженер видел, на чём основан выбор.</p>
          <p>Если позиций много, отдельно считаем годовую потребность и предлагаем спецификацию с фиксированной ценой. Смотрите также <a href="/analogi" style="color:var(--blue);font-weight:600">таблицу замены импортных марок</a> и <a href="/price" style="color:var(--blue);font-weight:600">условия по ценам</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % leadform("Заявка на подбор", "Отправить технику на подбор",
               "Ответим в рабочее время, обычно в течение 15 минут.",
               "Получить подбор", cls=" leadform--aside", anchor="zayavka")

simple("/podbor", "podbor.html", "Подбор масла",
       "Подбор масла под технику — бесплатно",
       "Подбор масла Газпромнефть под технику — бесплатно, Ташкент",
       "Бесплатный подбор масел Gazpromneft под вашу технику: по марке и модели или по аналогу импортной марки. Расчёт объёма, TDS, прайс с наличием в Ташкенте.",
       "podbor", podbor_blocks, faq=PODBOR_FAQ, img="podbor",
       alt="Подбор масла под технику")


# ---------------------------------------------------------------- аналоги
ANALOG_ROWS = [
 ("Гидравлические, ISO VG 32", "Shell Tellus S2 M 32, Mobil DTE 24, Total Azolla ZS 32", "Gazpromneft Hydraulic HLP 32"),
 ("Гидравлические, ISO VG 46", "Shell Tellus S2 M 46, Mobil DTE 25, Total Azolla ZS 46", "Gazpromneft Hydraulic HLP 46"),
 ("Гидравлические, ISO VG 68", "Shell Tellus S2 M 68, Mobil DTE 26, Total Azolla ZS 68", "Gazpromneft Hydraulic HLP 68"),
 ("Редукторные, ISO VG 150", "Shell Omala S2 G 150, Mobilgear 600 XP 150", "Gazpromneft Reductor CLP 150"),
 ("Редукторные, ISO VG 220", "Shell Omala S2 G 220, Mobilgear 600 XP 220", "Gazpromneft Reductor CLP 220"),
 ("Компрессорные, ISO VG 46", "Shell Corena S2 P 46, Mobil Rarus 425", "Gazpromneft Compressor Oil 46"),
 ("Турбинные, ISO VG 32", "Shell Turbo T 32, Mobil DTE 797", "Gazpromneft Turbine Oil 32"),
]
analog_rows_html = "\n".join('''        <div class="table__row">
          <b>%s</b>
          <span><span class="table__label">Импортные марки: </span>%s</span>
          <span><span class="table__label">Аналог: </span><b style="color:var(--blue)">%s</b></span>
        </div>''' % r for r in ANALOG_ROWS)

ANALOG_FAQ = [
 ("Это официальная таблица замены?",
  "Нет. Это сопоставление по классу вязкости ISO VG и типовому назначению — с него удобно начинать разговор. Окончательный выбор всегда делается по допуску производителя оборудования и условиям работы узла, поэтому под конкретную технику мы готовим отдельный подбор."),
 ("Нужно ли промывать систему при переходе?",
  "Зависит от того, что было залито и в каком состоянии система. При переходе между маслами одного типа и близкого класса промывка обычно не нужна, при смене типа масла или сильном загрязнении — нужна. Рекомендацию даём в подборе."),
 ("Что делать с остатком старого масла в системе?",
  "Небольшой остаток совместимых масел допустим, но мы всегда указываем в подборе, сколько можно оставить и на что это влияет. Если совместимость под вопросом — предлагаем полную замену."),
 ("Дадите сравнение характеристик на бумаге?",
  "Да. К подбору прикладываем протокол сравнения ключевых показателей: вязкость при 40 и 100 °C, индекс вязкости, температура вспышки и застывания, уровень очистки."),
]

analogi_blocks = '''    <p class="page__lead" style="max-width:820px">Подбираем замену Shell, Mobil, Total, Castrol и других марок на продукцию Gazpromneft — по классу вязкости, уровню очистки и требованиям производителя оборудования. Ниже — сопоставление по основным индустриальным группам, с которого удобно начать.</p>

    <div class="table" style="margin-top:28px;--cols:1.1fr 1.6fr 1.3fr">
      <div class="table__head">
        <div>Группа и класс</div><div>Импортные марки</div><div>Аналог Gazpromneft</div>
      </div>
%s
    </div>
    <p class="table__note">Сопоставление по классу вязкости и типовому назначению, а не официальная таблица замены. Под конкретное оборудование подбор делает технический специалист — по допуску производителя и условиям работы узла.</p>

    <div class="layout" style="margin-top:44px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Как мы подбираем замену</h2>
          <p>Сначала смотрим на требование производителя оборудования: класс вязкости, уровень качества и допуск. Затем — на условия работы: температура в узле, запылённость площадки, наличие влаги, режим смен. Только после этого подбираем позицию и проверяем, что по ключевым характеристикам она не хуже той, что залита сейчас.</p>
          <p>При переходе прикладываем протокол сравнения характеристик и рекомендации по промывке системы. Для предприятий, где замена идёт по всему парку, разносим переход по этапам, чтобы не менять всё разом.</p>
          <h2>С чего начать</h2>
          <p>Достаточно списка марок, которые вы закупаете сейчас, — с фасовками и примерным годовым объёмом. Этого хватит, чтобы подготовить сопоставление и посчитать стоимость. Если списка нет, начните с <a href="/podbor" style="color:var(--blue);font-weight:600">подбора по технике</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % (analog_rows_html,
       leadform("Заявка на подбор аналогов", "Прислать список масел",
                "Пришлём сопоставление с продукцией Gazpromneft и цены.",
                "Подобрать аналоги", cls=" leadform--aside", anchor="zayavka"))

simple("/analogi", "analogi.html", "Аналоги импортных масел",
       "Замена импортных масел на Газпромнефть",
       "Замена Shell, Mobil, Total на Газпромнефть — таблица аналогов",
       "Таблица соответствий импортных масел и Gazpromneft по классу вязкости: Shell Tellus, Mobil DTE, Total Azolla, Mobilgear. Подбор замены под допуск, Ташкент.",
       "products", analogi_blocks, faq=ANALOG_FAQ)


# ---------------------------------------------------------------- отрасли
INDUSTRIES = [
 ("Горнодобыча и ГОК", "Карьерные экскаваторы, самосвалы, дробильно-сортировочные комплексы",
  "Гидравлические масла HLP с высоким уровнем очистки, редукторные CLP для приводов дробилок, термостойкие смазки для узлов, работающих в пыли и под ударной нагрузкой.",
  "/hydralic"),
 ("Металлургия", "Прокатные станы, печи, конвейерные линии",
  "Термостойкие пластичные смазки, теплоносители, СОЖ для механической обработки и редукторные масла для приводов с высокой нагрузкой.",
  "/grease"),
 ("Цементные заводы", "Мельницы, вращающиеся печи, дробилки",
  "Редукторные масла для приводов мельниц, адгезионные смазки для открытых зубчатых передач, гидравлика для вспомогательного оборудования.",
  "/reductor"),
 ("Транспорт и логистика", "Магистральные тягачи, автобусы, коммунальная техника",
  "Моторные масла по допускам MAN, Scania, Volvo и Mercedes-Benz, трансмиссионные масла для мостов и коробок, антифризы под климат региона.",
  "/gpn"),
 ("Сельское хозяйство", "Тракторы, комбайны, насосные станции",
  "Универсальные моторные масла для смешанного парка, трансмиссионные и гидравлические масла, смазки для узлов, работающих в поле.",
  "/transmission"),
 ("Энергетика", "Турбины, трансформаторы, компрессорные станции",
  "Турбинные и трансформаторные масла, компрессорные масла для винтовых и поршневых машин, теплоносители.",
  "/compressor"),
 ("Машиностроение", "Станочный парк, обрабатывающие центры",
  "СОЖ под материал заготовки и тип обработки, направляющие и шпиндельные масла, гидравлика для прессов.",
  "/fluids"),
 ("Строительство", "Экскаваторы, погрузчики, бетононасосы",
  "Гидравлические масла для техники, работающей на морозе и в жару, моторные масла для дизелей, смазки для шарниров и пальцев.",
  "/industrial"),
]
ind_html = "\n".join('''        <a class="tile" href="%s">
          <b>%s</b>
          <span style="color:var(--muted-2);font-size:13px">%s</span>
          <span>%s</span>
        </a>''' % (u, n, sub, t) for n, sub, t, u in INDUSTRIES)

otrasli_blocks = '''    <p class="page__lead" style="max-width:820px">Поставляем смазочные материалы предприятиям промышленности, автопаркам и сервисным центрам по всему Узбекистану. Ниже — отрасли, с которыми работаем чаще всего, и то, что обычно нужно в каждой из них.</p>

    <div class="tiles" style="grid-template-columns:repeat(4,1fr);margin-top:32px">
%s
    </div>

    <div class="layout" style="margin-top:48px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Чем отраслевой подбор отличается от продажи по прайсу</h2>
          <p>Одно и то же масло в карьере и в цеху ведёт себя по-разному. В карьере решает запылённость и ударная нагрузка, в цеху — стабильность температуры и совместимость с уплотнениями, на трассе — режим смен и качество топлива. Поэтому мы не отправляем общий прайс, а спрашиваем, где и как работает техника.</p>
          <p>Для предприятий с постоянной потребностью готовим годовую спецификацию: перечень позиций, объёмы и фиксированная цена на период. Это снимает необходимость согласовывать каждую поставку заново и защищает бюджет от колебаний курса.</p>
          <h2>Документы для промышленных заказчиков</h2>
          <p>Поставка идёт по договору с полным пакетом: счёт-фактура, товарно-транспортные документы, паспорт качества на партию. Для тендерных процедур дополнительно собираем сертификаты соответствия и дистрибьюторское письмо — под требования конкретной закупки.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % (ind_html,
       leadform("Заявка с отраслевой страницы", "Подобрать под ваше производство",
                "Напишите отрасль и технику — вернём подбор и прайс.",
                "Получить подбор", cls=" leadform--aside", anchor="zayavka"))

simple("/otrasli", "otrasli.html", "Отрасли",
       "Смазочные материалы по отраслям",
       "Смазочные материалы по отраслям — Газпромнефть Узбекистан",
       "Подбор масел Gazpromneft под отрасль: горнодобыча, металлургия, цемент, транспорт, энергетика, машиностроение. Поставка со склада в Ташкенте.",
       "otrasli", otrasli_blocks, img="industrial",
       alt="Промышленное производство — смазочные материалы Газпромнефть")


# ---------------------------------------------------------------- доставка
DOST_FAQ = [
 ("Как быстро отгружаете?",
  "Позиции, которые есть на складе в Ташкенте, отгружаем в течение 24 часов после согласования заявки. Если позиции нет в наличии, сразу называем срок поставки — не тянем и не обещаем невозможного."),
 ("Доставляете в регионы?",
  "Да, поставляем в Ташкент, Самарканд, Бухару, Навои, Ферганскую долину и другие регионы. Условия доставки зависят от объёма и адреса, обсуждаем при заявке."),
 ("Можно забрать самовывозом?",
  "Да, со склада в Ташкенте. Время отгрузки согласуем заранее, чтобы машина не стояла в очереди."),
 ("Как происходит оплата?",
  "По договору и счёту, перечислением. Для постоянных заказчиков возможны индивидуальные условия — обсуждаются отдельно."),
 ("Какие документы приходят с грузом?",
  "Счёт-фактура, товарно-транспортные документы и паспорт качества на партию. Для тендеров и входного контроля дополнительно готовим сертификаты соответствия и дистрибьюторское письмо."),
]

dostavka_blocks = '''    <p class="page__lead" style="max-width:820px">Склад в Ташкенте, отгрузка в течение 24 часов после согласования заявки, поставка по всему Узбекистану. Работаем по договору с полным пакетом документов для бухгалтерии и тендерных процедур.</p>

    <div class="why" style="margin-top:32px">
      <div class="why__item"><b>Отгрузка за 24 часа</b><span>Для позиций, которые есть на складе. Чего нет в наличии — сразу называем срок поставки.</span></div>
      <div class="why__item"><b>Доставка по Узбекистану</b><span>Ташкент, Самарканд, Бухара, Навои, Ферганская долина и другие регионы.</span></div>
      <div class="why__item"><b>Самовывоз</b><span>Со склада в Ташкенте, время отгрузки согласуем заранее.</span></div>
      <div class="why__item"><b>Работа по договору</b><span>Счёт, счёт-фактура, товарно-транспортные документы на каждую поставку.</span></div>
      <div class="why__item"><b>Паспорт качества</b><span>На каждую партию. Для входного контроля и тендеров — полный пакет документов.</span></div>
      <div class="why__item"><b>Годовые спецификации</b><span>Фиксированная цена на период и график отгрузок для постоянных заказчиков.</span></div>
    </div>

    <div class="layout" style="margin-top:44px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Как проходит поставка</h2>
          <p>Вы присылаете заявку — перечень позиций или технику для подбора. Менеджер подтверждает наличие и цену, при необходимости технический специалист готовит подбор. Дальше выставляем счёт, согласуем сроки и отгружаем со склада.</p>
          <p>Для крупных объёмов и регулярных поставок оформляем спецификацию с графиком: в ней зафиксированы позиции, объёмы и цена на период. Такой формат удобнее и заказчику, и нам — меньше согласований на каждый рейс.</p>
          <h2>Фасовки</h2>
          <p>Поставляем от литровой канистры до кубовой ёмкости: канистры 1, 4, 5, 10 и 20 л, бочки 205 л, кубовые ёмкости. По смазкам — от картриджа до бочки. Точные фасовки по конкретной позиции уточняем при подборе, они зависят от продукта.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % leadform("Вопрос по доставке", "Уточнить сроки и условия",
               "Напишите позиции и адрес — посчитаем сроки и стоимость.",
               "Отправить заявку", cls=" leadform--aside", anchor="zayavka")

simple("/dostavka", "dostavka.html", "Доставка и оплата",
       "Доставка и оплата",
       "Доставка и оплата масел Газпромнефть по Узбекистану",
       "Отгрузка со склада в Ташкенте за 24 часа, доставка по Узбекистану, самовывоз, работа по договору. Счёт-фактура и паспорт качества на каждую партию.",
       "company", dostavka_blocks, faq=DOST_FAQ)

print("новые страницы готовы")
