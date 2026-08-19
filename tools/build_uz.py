# -*- coding: utf-8 -*-
"""Узбекская версия сайта gpn-oil.uz — каталог /uz/.

Адреса зеркалят русские: /industrial ↔ /uz/industrial. Стили, скрипты
и картинки общие, отдельно только тексты. Разовый скрипт, на выходе статика.
"""
import os as _os
ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import io, os
from PIL import Image as _Image

OUT = ROOT
UZDIR = os.path.join(OUT, "uz")
SITE = "https://gpn-oil.uz"
TG = "https://t.me/GPN_OIL_UZ"
INSTA = "https://instagram.com/gpn_oil.uz"
SALESHUB = "https://sales-hub.uz/?utm_source=gpn-oil.uz&utm_medium=referral&utm_campaign=footer"

_DIMS = {}


def dim(name):
    if name not in _DIMS:
        _DIMS[name] = _Image.open(os.path.join(OUT, "img", name + ".webp")).size
    return _DIMS[name]


def srcset(name, w):
    parts = ["/img/%s-sm.webp %dw" % (name, max(400, w // 2))]
    if os.path.exists(os.path.join(OUT, "img", name + "-md.webp")):
        parts.append("/img/%s-md.webp 960w" % name)
    parts.append("/img/%s.webp %dw" % (name, w))
    return ", ".join(parts)


NAV = [
    ("/uz/products", "Mahsulotlar", "products"),
    ("/uz/podbor", "Moy tanlash", "podbor"),
    ("/uz/otrasli", "Tarmoqlar", "otrasli"),
    ("/uz/price", "Narxlar", "price"),
    ("/uz/docs", "Hujjatlar", "docs"),
    ("/uz/company", "Kompaniya", "company"),
    ("/uz/contacts", "Aloqa", "contacts"),
]

HEAD = """<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="uz" href="{canonical}">
<link rel="alternate" hreflang="ru" href="{ruhref}">
<link rel="alternate" hreflang="x-default" href="{ruhref}">
<meta name="theme-color" content="#0d2b45">{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Gazpromneft Oʻzbekiston">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{ogdesc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimage}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta property="og:locale" content="uz_UZ">
<link rel="icon" href="/img/logo-mark.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/plex-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/plex-700.woff2" as="font" type="font/woff2" crossorigin>{preload}
<link rel="stylesheet" href="/site.css?v=22">
<script type="speculationrules">
{{"prefetch":[{{"source":"document","where":{{"href_matches":"/*"}},"eagerness":"moderate"}}]}}
</script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-4VH1EV5FQB');</script>
{jsonld}</head>
<body>

<div class="topbar">
  <div class="wrap topbar__in">
    <span>«Gazpromneft — moylash materiallari»ning Oʻzbekiston Respublikasidagi rasmiy distribyutori</span>
    <div class="topbar__right">
      <span>Du–Ju, 09:00–18:00</span>
      <span class="lang"><a class="lang__off" href="{rupath}" hreflang="ru" lang="ru">RU</a><span>/</span><span class="lang__on">UZ</span></span>
    </div>
  </div>
</div>

<header class="masthead">
  <div class="wrap masthead__in">
    <a class="brand" href="/uz/" aria-label="Gazpromneft Oʻzbekiston — bosh sahifa">
      <img class="brand__logo" src="/img/logo-mark.svg" alt="Gazpromneft — Smart Energy Eco Trade, Oʻzbekistondagi distribyutor" width="221" height="78">
    </a>
    <nav class="nav" id="nav" aria-label="Asosiy menyu">
{nav}
    </nav>
    <div class="masthead__right">
      <a class="tel" href="tel:+998935048490">+998 93 504 84 90<span>savdo boʻlimi</span></a>
      <a class="btn btn--accent btn--sm" href="/uz/price#zayavka">Narxlarni olish</a>
      <button class="burger" type="button" aria-label="Menyu" aria-expanded="false" aria-controls="nav"><i></i><i></i><i></i></button>
    </div>
  </div>
</header>
"""

MGR = """
<aside class="mgr" id="mgr" aria-label="Menejer bilan bogʻlanish">
  <button class="mgr__close" type="button" id="mgrClose" aria-label="Oynani yigʻish">&times;</button>
  <div class="mgr__top">
    <button class="mgr__head" type="button" id="mgrToggle" aria-expanded="false" aria-controls="mgrBody">
      <img class="mgr__ava" src="/img/manager.webp" srcset="/img/manager.webp 128w, /img/manager-2x.webp 256w" sizes="44px" alt="Timur Yarullin, korporativ menejer" width="128" height="128" loading="lazy" decoding="async">
      <span class="mgr__who">
        <b>Timur Yarullin</b>
        <span>korporativ menejer</span>
      </span>
      <span class="mgr__chev" aria-hidden="true"></span>
    </button>
    <a class="mgr__call" href="tel:+998908085972" aria-label="Menejerga qoʻngʻiroq qilish">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M5 3h3.5l1.8 4.4-2.2 1.6a12 12 0 0 0 6.9 6.9l1.6-2.2 4.4 1.8V19a2 2 0 0 1-2.2 2A17 17 0 0 1 3 5.2 2 2 0 0 1 5 3z"/></svg>
    </a>
  </div>
  <div class="mgr__body" id="mgrBody">
    <a class="mgr__row" href="tel:+998908085972">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M5 3h3.5l1.8 4.4-2.2 1.6a12 12 0 0 0 6.9 6.9l1.6-2.2 4.4 1.8V19a2 2 0 0 1-2.2 2A17 17 0 0 1 3 5.2 2 2 0 0 1 5 3z"/></svg>
      +998 90 808 59 72</a>
    <a class="mgr__row mgr__row--tg" href="__TG__" rel="noopener">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M21.2 4.3 2.9 11.2c-.8.3-.8 1.4 0 1.7l4.6 1.5 1.7 5c.2.7 1.1.9 1.6.3l2.4-2.6 4.6 3.4c.6.4 1.4.1 1.6-.6l3-14c.2-.8-.6-1.5-1.2-1.6z"/><path d="M7.5 14.4 18.6 6.6l-7.9 9.1"/></svg>
      Telegramga yozish</a>
    <a class="mgr__row" href="/uz/price#zayavka">
      <svg viewBox="0 0 24 24" aria-hidden="true" stroke-linejoin="round"><path d="M5 3h14v18l-7-4-7 4z"/></svg>
      Ariza qoldirish</a>
    <p class="mgr__hours">Du–Ju, 09:00–18:00. Texnikaga moy tanlash, narxlar va Toshkentdagi ombordagi mavjudlik.</p>
  </div>
</aside>
""".replace("__TG__", TG)

CTA = """
<section class="cta">
  <div class="wrap cta__in">
    <div class="cta__body">
      <b>Bugun hisob-kitob yoki narxlar kerakmi?</b>
      <p>Texnik mutaxassis Du–Ju, 09:00–18:00 aloqada. Telegramda 15 daqiqada javob beramiz.</p>
    </div>
    <div class="cta__actions">
      <a class="btn btn--white" href="tel:+998908085972">+998 90 808 59 72</a>
      <a class="btn btn--onDark" href="{tg}" rel="noopener">Telegramga yozish</a>
    </div>
  </div>
</section>
"""

TAIL = """
<footer class="footer">
  <div class="wrap">
    <div class="footer__in">
      <div class="footer__col footer__brand">
        <img class="footer__logo" src="/img/logo-mark.svg" alt="Gazpromneft" width="221" height="78" loading="lazy">
        <span>«Smart Energy Eco Trade» MChJ — «Gazpromneft» moylash materiallarining Oʻzbekiston Respublikasidagi rasmiy distribyutori.</span>
      </div>
      <div class="footer__col">
        <b>Mahsulotlar</b>
        <a href="/uz/products">Butun katalog</a>
        <a href="/uz/industrial">Industrial moylar</a>
        <a href="/uz/gpn">Gazpromneft motor moylari</a>
        <a href="/uz/g-energy">G-Energy</a>
        <a href="/uz/transmission">Transmissiya moylari</a>
        <a href="/uz/grease">Plastik moylar</a>
        <a href="/uz/fluids">SOJ va suyuqliklar</a>
        <a href="/uz/analogi">Import markalar analoglari</a>
      </div>
      <div class="footer__col">
        <b>Kompaniya</b>
        <a href="/uz/company">Kompaniya haqida</a>
        <a href="/uz/dostavka">Yetkazib berish va toʻlov</a>
        <a href="/uz/price">Narxlar</a>
        <a href="/uz/docs">Hujjatlar</a>
        <a href="/uz/contacts">Aloqa</a>
      </div>
      <div class="footer__col">
        <b>Aloqa</b>
        <a href="tel:+998908085972">+998 90 808 59 72</a>
        <a href="tel:+998935048490">+998 93 504 84 90</a>
        <a href="mailto:t.yarulin@s-energy.uz">t.yarulin@s-energy.uz</a>
        <a href="{tg}" rel="noopener">Telegram</a>
        <a href="{insta}" rel="noopener">Instagram</a>
        <span>Toshkent, Oʻzbekiston</span>
      </div>
    </div>
    <div class="footer__legal">
      <span>© 2026 «Smart Energy Eco Trade» MChJ</span>
      <span>Gazpromneft, G-Profi, G-Energy — huquq egasining savdo belgilari.</span>
      <span>Sayt va reklama — <a href="{saleshub}" rel="noopener">Sales HUB</a></span>
    </div>
  </div>
</footer>
"""

ORG_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Smart Energy Eco Trade","legalName":"«Smart Energy Eco Trade» MChJ","alternateName":["Gazpromneft Oʻzbekiston","Gazpromneft Uzbekistan","GPN Uzbekistan","Газпромнефть Узбекистан","Смарт Энерджи Эко Трейд"],"foundingDate":"2023-04-27","foundingLocation":{"@type":"Place","name":"Toshkent, Oʻzbekiston"},"url":"https://gpn-oil.uz/uz/","logo":"https://gpn-oil.uz/img/logo-mark.svg","description":"«Gazpromneft — moylash materiallari»ning Oʻzbekiston Respublikasidagi rasmiy distribyutori","areaServed":"UZ","address":{"@type":"PostalAddress","addressLocality":"Toshkent","addressCountry":"UZ"},"contactPoint":[{"@type":"ContactPoint","telephone":"+998908085972","contactType":"sales","name":"Timur Yarullin, korporativ menejer","email":"t.yarulin@s-energy.uz","availableLanguage":["uz","ru"]}],"sameAs":["https://instagram.com/gpn_oil.uz","https://t.me/GPN_OIL_UZ"]}
</script>
"""


def crumbs_ld(items):
    parts = ['{"@type":"ListItem","position":%d,"name":"%s","item":"%s%s"}' % (i, n, SITE, u)
             for i, (n, u) in enumerate(items, 1)]
    return ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}\n'
            '</script>\n' % ",".join(parts))


def products_ld(rows, path, img, brand="Gazpromneft"):
    """Toifadagi haqiqiy pozitsiyalar roʻyxati.

    Saytda narxlar yoʻq — ular soʻrov boʻyicha, — shuning uchun narxli Offer
    oʻylab topilmaydi. Faqat haqiqat belgilanadi: nomi, brendi, tavsifi,
    qadoqlanishi, mavjudligi va sotuvchisi.
    """
    if not rows:
        return ""
    items = []
    for i, r in enumerate(rows, 1):
        name = r[0].replace('"', "'")
        spec = " · ".join(str(x).replace('"', "'") for x in r[1:] if x)
        b = "G-Energy" if name.startswith("G-Energy") else brand
        items.append(
            '{"@type":"ListItem","position":%d,"item":{"@type":"Product",'
            '"name":"%s","brand":{"@type":"Brand","name":"%s"},'
            '"description":"%s","image":"%s/img/%s.webp","url":"%s%s",'
            '"offers":{"@type":"Offer","availability":"https://schema.org/InStock",'
            '"priceCurrency":"UZS","areaServed":"UZ","url":"%s%s",'
            '"seller":{"@type":"Organization","name":"Smart Energy Eco Trade"}}}}'
            % (i, name, b, spec, SITE, img, SITE, path, SITE, path))
    return ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"ItemList",'
            '"itemListOrder":"https://schema.org/ItemListUnordered",'
            '"numberOfItems":%d,"itemListElement":[%s]}\n</script>\n'
            % (len(items), ",".join(items)))


def faq_html(items):
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
         preload=None, preload_sizes="100vw", jsonld="", noindex=False,
         ogtitle=None, ogdesc=None, cta=True):
    nav = "\n".join('      <a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if k == active else "", l)
                    for h, l, k in NAV)
    pre = ""
    if preload:
        name = preload.split("/")[-1].replace(".webp", "")
        pre = ('\n<link rel="preload" as="image" type="image/avif" href="%s" imagesrcset="%s" imagesizes="%s" fetchpriority="high">'
               % (preload.replace('.webp', '.avif'), srcset(name, dim(name)[0]).replace('.webp', '.avif'), preload_sizes))
    rupath = "/" if path == "/uz/" else path[3:]
    html = (HEAD.format(title=title, desc=desc, nav=nav, canonical=SITE + path,
                        ruhref=SITE + rupath, rupath=rupath,
                        ogtitle=ogtitle or title, ogdesc=ogdesc or desc,
                        ogimage=SITE + ogimage, preload=pre, jsonld=jsonld,
                        robots='\n<meta name="robots" content="noindex">' if noindex else "")
            + body + MGR
            + (CTA.format(tg=TG) if cta else "")
            + TAIL.format(insta=INSTA, saleshub=SALESHUB, tg=TG)
            + '\n<script src="/site.js?v=22" defer></script>\n</body>\n</html>\n')
    os.makedirs(os.path.dirname(os.path.join(UZDIR, fname)) or UZDIR, exist_ok=True)
    io.open(os.path.join(UZDIR, fname), "w", encoding="utf-8").write(html)


NEEDS = [
    "Industrial moylar (gidravlika, reduktor, kompressor)",
    "Yuk va maxsus texnika uchun motor moylari",
    "Yengil transport uchun motor moylari",
    "Transmissiya moylari",
    "Plastik moylar",
    "Antifriz, tormoz suyuqligi, SOJ",
    "Bilmayman — texnikaga tanlab berish kerak",
]


def leadform(source, title, sub, button, cls="", preset=None, anchor=None):
    opts = "\n".join('            <option%s>%s</option>' % (' selected' if n == preset else '', n)
                     for n in NEEDS)
    return """      <form class="leadform%s"%s method="post" action="https://gpn-relay.zvezdotank.workers.dev/">
        <b>%s</b>
        <p>%s</p>
        <input class="trap" type="text" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="_form" value="%s">
        <input type="hidden" name="_next" value="uz">
        <label><span>Nima kerak</span>
          <select name="need">
%s
          </select>
        </label>
        <label><span>Telefon yoki Telegram</span>
          <input name="phone" type="tel" placeholder="+998" autocomplete="tel" required>
        </label>
        <label><span>Texnika, moy markasi yoki hajmi <em style="font-style:normal;color:#8b9db0">— majburiy emas</em></span>
          <textarea name="task" rows="2" placeholder="Masalan: Komatsu PC300, hozir Shell Tellus 46, yiliga 2000 litrga yaqin"></textarea>
        </label>
        <button type="submit">%s</button>
        <small>Ish vaqtida javob beramiz, Du–Ju 09:00–18:00. Tanlash bepul va hech narsaga majbur qilmaydi.</small>
      </form>""" % (cls, (' id="%s"' % anchor) if anchor else "", title, sub, source, opts, button)


CATS = [
    ("/uz/industrial", "Industrial moylar", "cat-industrial",
     "Gidravlik, reduktor, kompressor, turbina moylari va issiqlik tashuvchilar"),
    ("/uz/gpn", "Gazpromneft motor moylari", "cat-gpn",
     "Tijorat transporti, maxsus texnika va avtoparklar uchun"),
    ("/uz/g-energy", "G-Energy motor moylari", "cat-g-energy",
     "Yengil transport uchun sintetika va yarim sintetika"),
    ("/uz/grease", "Plastik moylar", "cat-grease",
     "Litiy, kalsiy, yuqori haroratli moylar va Steelgrease"),
    ("/uz/transmission", "Transmissiya moylari", "cat-transmission",
     "MUK, AUK, koʻpriklar va gidrokuchaytirgich uchun, ATF ham bor"),
    ("/uz/fluids", "Texnik suyuqliklar va SOJ", "cat-fluids",
     "Antifrizlar, tormoz suyuqliklari, moylab-sovutuvchi suyuqliklar"),
]



def picture(name, w, inner_img):
    """AVIF первым источником, webp — запасным. Кто не умеет AVIF (старые
    Safari и часть андроидов), получит webp, разметка одна на всех."""
    return ('<picture><source type="image/avif" srcset="%s" sizes="%s">%s</picture>'
            % (srcset(name, w).replace(".webp", ".avif"), _sizes_of(inner_img), inner_img))


def _sizes_of(tag):
    import re as _re
    m = _re.search(r'sizes="([^"]*)"', tag)
    return m.group(1) if m else "100vw"


def cards_html(indent="        "):
    out = []
    for href, name, img, text in CATS:
        w, h = dim(img)
        out.append("""%s<a class="card" href="%s">
%s  <picture><source type="image/avif" srcset="%s" sizes="(max-width:640px) 100vw, (max-width:1080px) 50vw, 33vw"><source type="image/webp" srcset="%s" sizes="(max-width:640px) 100vw, (max-width:1080px) 50vw, 33vw"><img class="card__media" src="/img/%s.webp" alt="%s Gazpromneft" width="%d" height="%d" loading="lazy" decoding="async"></picture>
%s  <div class="card__title">%s</div>
%s  <div class="card__text">%s</div>
%s</a>""" % (indent, href, indent, srcset(img, w).replace(".webp", ".avif"), srcset(img, w), img, name, w, h, indent, name, indent, text, indent))
    return "\n".join(out)


ASIDE_REQUEST = """        <div class="callout">
          <b>Narx va mavjudlikni soʻrash</b>
          <p>Ish vaqtida Telegramda 15 daqiqada javob beramiz.</p>
          <a class="btn btn--orange" href="#zayavka">Ariza qoldirish</a>
          <a class="btn btn--onDark" href="tel:+998935048490">+998 93 504 84 90</a>
          <a class="btn btn--onDark" href="%s" rel="noopener">Telegramga yozish</a>
        </div>""" % TG


def aside_other(current):
    links = "\n".join('            <a href="%s">%s</a>' % (h, n) for h, n, _, _ in CATS if h != current)
    return """        <div class="asidebox">
          <b>Boshqa toifalar</b>
          <div>
%s
          </div>
        </div>""" % links


def table(rows):
    body = ["""          <div class="table__row">
            <b>%s</b>
            <span><span class="table__label">Qovushqoqlik sinfi: </span>%s</span>
            <span><span class="table__label">Qadoq: </span>%s</span>
            <div class="table__files"><a href="/uz/docs">TDS · MSDS</a></div>
          </div>""" % r for r in rows]
    return """        <div class="table">
          <div class="table__head">
            <div>Nomi</div><div>Qovushqoqlik sinfi</div><div>Qadoq</div><div>Hujjatlar</div>
          </div>
%s
        </div>
        <p class="table__note">Asosiy pozitsiyalar koʻrsatilgan. Toʻliq roʻyxat va narxlar — menejerdan soʻrov boʻyicha.</p>""" % "\n".join(body)


CHECKLIST = """        <div class="checklist">
          <b>Javob aniq boʻlishi uchun arizada nima yozish kerak</b>
          <span>Texnika yoki uzelning markasi va modeli</span>
          <span>Hozir qanday moy quyilgan — marka yoki ruxsatnoma</span>
          <span>Taxminiy hajm: bir marta quyishga yoki bir yilga</span>
          <span>Kerakli qadoq: kanistr, bochka, kub sigʻim</span>
        </div>"""


def category(path, fname, crumb, h1, title, desc, lead, img, alt,
             rows=None, chips=None, longread=None, parent=None,
             uses=None, faq=None, preset=None):
    items = [("Bosh sahifa", "/uz/"), ("Mahsulotlar", "/uz/products")]
    ch = '<a href="/uz/">Bosh sahifa</a><span>/</span><a href="/uz/products">Mahsulotlar</a><span>/</span>'
    if parent:
        items.append(parent)
        ch += '<a href="%s">%s</a><span>/</span>' % (parent[1], parent[0])
    items.append((crumb, path))
    ch += '<b>%s</b>' % crumb

    hero = ""
    if img:
        iw, ih = dim(img)
        hero = '''    <div class="pagehero">
      <picture><source type="image/avif" srcset="%s" sizes="100vw"><source type="image/webp" srcset="%s" sizes="100vw"><img src="/img/%s.webp" alt="%s" width="%d" height="%d" fetchpriority="high" decoding="async"></picture>
    </div>
''' % (srcset(img, iw).replace(".webp", ".avif"), srcset(img, iw), img, alt, iw, ih)

    chips_html = ""
    if chips:
        chips_html = '\n        <div class="chips">\n' + "\n".join(
            '          <a class="chip" href="%s">%s</a>' % (u, n) for n, u in chips) + '\n        </div>'

    if rows:
        content = table(rows)
    else:
        tiles = "\n".join('          <div><b>%s</b><span>%s</span></div>' % (n, t) for n, t in (uses or []))
        content = """        <h2 style="font-size:24px;margin-top:8px">Bu toifada nimani tanlaymiz</h2>
        <div class="uses">
%s
        </div>
%s
%s""" % (tiles, CHECKLIST,
         leadform("Ariza (uz): " + crumb, "Tanlab berish va narx",
                  "Tanlov, ombordagi mavjudlik bilan narxlar va texnik tavsifni yuboramiz.",
                  "Tanlov va narxlarni olish", preset=preset))

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
          <h2>Koʻp beriladigan savollar</h2>
        </div>
%s""" % faq_html(faq)

    body = """
<main>
  <nav class="wrap crumbs" aria-label="Yoʻl">
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
""" % (ch, hero, h1, lead, chips_html, content, long_html, ASIDE_REQUEST,
       leadform("Yon paneldan ariza (uz): " + crumb, "Narxni soʻrash",
                "Telegramda javob beramiz yoki qoʻngʻiroq qilamiz.",
                "Ariza yuborish", cls=" leadform--aside", preset=preset, anchor="zayavka"),
       aside_other(path))

    page(path, fname, title, desc, body, active="products",
         preload=("/img/%s.webp" % img) if img else None,
         jsonld=crumbs_ld(items) + (faq_ld(faq) if faq else "")
                       + products_ld(rows, path, img))


INDUSTRIAL_ROWS = [
    ("Gazpromneft Hydraulic HLP 32", "ISO VG 32", "20 / 50 / 205 l"),
    ("Gazpromneft Hydraulic HLP 46", "ISO VG 46", "20 / 50 / 205 l"),
    ("Gazpromneft Hydraulic HLP 68", "ISO VG 68", "20 / 205 l"),
    ("Gazpromneft Reductor CLP 150", "ISO VG 150", "20 / 205 l"),
    ("Gazpromneft Reductor CLP 220", "ISO VG 220", "20 / 205 l"),
    ("Gazpromneft Compressor Oil 46", "ISO VG 46", "20 / 205 l"),
    ("Gazpromneft Turbine Oil 32", "ISO VG 32", "205 l"),
    ("Gazpromneft Termoil 26", "ISO VG 32", "205 l"),
]

category("/uz/industrial", "industrial.html", "Industrial moylar",
         "Toshkentda Gazpromneft industrial moylari",
         "Oʻzbekistonda Gazpromneft industrial moylari",
         "Toshkentdagi ombordan Gazpromneft industrial moylari: gidravlik HLP 32/46/68, reduktor CLP, kompressor va turbina moylari. Partiyaga sifat pasporti.",
         "Gidravlik, reduktor, kompressor, turbina va transformator moylari, issiqlik tashuvchilar. Toshkentdagi omborda mavjud, qadoq 20 litrdan kub sigʻimgacha, har bir partiyaga sifat pasporti beriladi.",
         "industrial", "Gazpromneft industrial moylari ombordagi bochkalarda",
         rows=INDUSTRIAL_ROWS,
         chips=[("Gidravlik", "/uz/hydralic"), ("Reduktor", "/uz/reductor"),
                ("Kompressor", "/uz/compressor"), ("Plastik moylar", "/uz/grease"), ("SOJ", "/uz/fluids")],
         longread=("Import markalarni tanlash va almashtirish",
                   "Shell Tellus, Mobil DTE, Total Azolla va boshqa markalarga analogni ISO VG qovushqoqlik sinfi, tozalik darajasi va uskuna ishlab chiqaruvchisining talablari boʻyicha tanlaymiz. Oʻtishda tavsiflar solishtirmasi va tizimni yuvish boʻyicha tavsiyalarni beramiz — <a href=\"/uz/analogi\" style=\"color:var(--blue);font-weight:600\">moslik jadvaliga</a> qarang."))

category("/uz/hydralic", "hydralic.html", "Gidravlik moylar",
         "Toshkentda Gazpromneft gidravlik moylari",
         "Oʻzbekistonda Gazpromneft gidravlik moylari — HLP 32, 46, 68",
         "Toshkentdagi ombordan Gazpromneft Hydraulic HLP 32, 46 va 68. Qadoq 20, 50 va 205 litr, sifat pasporti, import analoglarni tanlash.",
         "Karyer, qurilish va sanoat texnikasining gidravlik tizimlari uchun Gazpromneft Hydraulic seriyasi. ISO VG 32, 46 va 68 sinflari, qadoq 20 litrdan kub sigʻimgacha.",
         "hydralic", "Karyer texnikasi gidravlikasi — Gazpromneft gidravlik moylari",
         rows=INDUSTRIAL_ROWS[:3], parent=("Industrial moylar", "/uz/industrial"),
         longread=("Import gidravlik moyni nima bilan almashtirish mumkin",
                   "Shell Tellus S2 M, Mobil DTE 20 va Total Azolla ZS ISO VG sinfi va tozalik darajasi boʻyicha tanlanadi. Oʻtishdan oldin tavsiflar solishtirmasini va tizimni yuvish boʻyicha tavsiyani beramiz."))

category("/uz/reductor", "reductor.html", "Reduktor moylari",
         "Toshkentda Gazpromneft reduktor moylari",
         "Oʻzbekistonda Gazpromneft reduktor moylari — CLP 150, CLP 220",
         "Toshkentdagi ombordan Gazpromneft Reductor CLP 150 va CLP 220 reduktor moylari. Qadoq 20 va 205 litr, sifat pasporti, yuklama va haroratga qarab tanlash.",
         "Sanoat reduktorlari va uzatmalari uchun Gazpromneft Reductor seriyasi. ISO VG 150 va 220 sinflari, qadoq 20 va 205 litr, Toshkentdagi omborda mavjud.",
         "reductor", "Sanoat reduktori — Gazpromneft reduktor moylari",
         rows=INDUSTRIAL_ROWS[3:5], parent=("Industrial moylar", "/uz/industrial"),
         longread=("Reduktor moyini qanday tanlash kerak",
                   "Qovushqoqlik sinfi aylanma tezlik, tishga tushadigan yuklama va uzelning ish haroratiga qarab tanlanadi. Zarbali yuklama katta yoki harorat 90 °C dan yuqori boʻlsa, kuchaytirilgan qoʻshimchalar paketi kerak — tanlashda aytamiz."))

category("/uz/compressor", "compressor.html", "Kompressor moylari",
         "Toshkentda Gazpromneft kompressor moylari",
         "Oʻzbekistonda Gazpromneft kompressor moylari — Compressor Oil 46",
         "Toshkentdagi ombordan Gazpromneft Compressor Oil kompressor moylari. Qadoq 20 va 205 litr, sifat pasporti, vint va porshenli kompressorlarga tanlash.",
         "Vint va porshenli kompressorlar uchun moylar. ISO VG 46 sinfi, qadoq 20 va 205 litr, Toshkentdagi omborda mavjud.",
         "compressor", "Vint kompressorlari — Gazpromneft kompressor moylari",
         rows=INDUSTRIAL_ROWS[5:6], parent=("Industrial moylar", "/uz/industrial"),
         longread=("Kompressorda almashtirish oraligʻi",
                   "Vint kompressorida moy resursi haydash harorati va maydondagi changga bogʻliq. Oʻzbekiston yozida oraliq odatda pasportdagidan qisqaroq — faqat ishlash soatiga emas, namuna tahliliga qarang."))

category("/uz/gpn", "gpn.html", "Gazpromneft motor moylari",
         "Toshkentda Gazpromneft motor moylari",
         "Oʻzbekistonda Gazpromneft motor moylari",
         "Yuk transporti, avtobuslar va maxsus texnika uchun Gazpromneft va G-Profi motor moylari. Toshkentdagi ombor, ruxsatnomalar boʻyicha tanlash, har partiyaga hujjatlar.",
         "Tijorat transporti, maxsus texnika va avtoparklar uchun. Dvigatel ishlab chiqaruvchisining ruxsatnomasi va ish sharoitiga qarab tanlaymiz, Toshkentdagi ombordan sifat pasporti bilan yetkazamiz.",
         "gpn", "Gazpromneft motor moylari ishlab chiqarish liniyasi",
         preset="Yuk va maxsus texnika uchun motor moylari",
         uses=[("Yuk mashinalari va tortqilar", "MAN, Scania, Volvo, Mercedes-Benz ruxsatnomalari boʻyicha dizel moylari"),
               ("Karyer va qurilish texnikasi", "Chang va yuqori haroratda ishlash uchun"),
               ("Avtobuslar va kommunal texnika", "Tez-tez toʻxtaydigan shahar rejimi"),
               ("Qishloq xoʻjaligi texnikasi", "Aralash park uchun universal moylar")],
         faq=[("Import moy oʻrniga Gazpromneft toʻgʻri keladimi?",
               "Ha, agar SAE qovushqoqlik sinfi, API yoki ACEA darajasi va dvigatel ishlab chiqaruvchisining ruxsatnomasi mos kelsa. Hozir quyilgan markani yuboring — tavsiflar boʻyicha solishtiramiz va solishtirma bayonnomasini beramiz."),
              ("Buxgalteriya va tender uchun hujjatlar berasizmi?",
               "Ha. Yetkazib berish shartnoma asosida, hisob-faktura, tovar-transport hujjatlari va partiyaga sifat pasporti bilan. Tender uchun buyurtmachi talabiga qarab toʻliq paket yigʻamiz."),
              ("Qanchalik tez joʻnatasiz?",
               "Toshkentdagi omborda bor pozitsiyalarni ariza tushgandan keyin 24 soat ichida joʻnatamiz. Yetkazib berish Oʻzbekiston boʻylab kelishuv asosida.")],
         longread=("Qanday tanlaymiz",
                   "Avtoparklar uchun belgilangan narx va joʻnatish jadvali bilan yillik spetsifikatsiya tayyorlaymiz. Import markadan oʻtishda texnik mutaxassis ruxsatnoma va qovushqoqlik sinfini solishtirib, tavsiflar bayonnomasini beradi."))

category("/uz/g-energy", "g-energy.html", "G-Energy motor moylari",
         "Toshkentda G-Energy motor moylari",
         "Oʻzbekistonda G-Energy motor moylari",
         "Yengil transport uchun G-Energy motor moylari: sintetika va yarim sintetika. Toshkentdagi ombordan rasmiy yetkazib berish, qadoq 1 litrdan, partiyaga hujjatlar.",
         "Yengil transport uchun sintetika va yarim sintetika. Toshkentdagi ombordan rasmiy mahsulot, qadoq bir litrlik kanistrdan bochkagacha, har partiyaga sifat pasporti.",
         "g-energy", "G-Energy — yengil transport uchun motor moylari",
         preset="Yengil transport uchun motor moylari",
         uses=[("Servis markazlari va STO", "Sintetika va yarim sintetika, keng tarqalgan qovushqoqliklar"),
               ("Avtotovarlar doʻkonlari", "Chakana javon uchun 1, 4 va 5 litrlik qadoq"),
               ("Korporativ avtoparklar", "Belgilangan narx bilan muntazam joʻnatish"),
               ("Taksi va karsheringlar", "Ogʻir shahar rejimi uchun moylar")],
         faq=[("G-Energy Gazpromneftdan nimasi bilan farq qiladi?",
               "Bu bitta ishlab chiqaruvchining ikki liniyasi: G-Energy yengil transportga, Gazpromneft liniyasi tijorat va sanoat texnikasiga moʻljallangan. Qoʻshimchalar paketi va ruxsatnomalari bilan farq qiladi."),
              ("Chakana savdo qilasizmi?",
               "Biz Toshkentdagi ombordan optom ishlaymiz. Doʻkon va servislar uchun alohida shartlar bor — menejerga yozing."),
              ("Asl mahsulotni qalbakidan qanday ajratish mumkin?",
               "Biz rasmiy distribyutormiz va mahsulotni toʻgʻridan-toʻgʻri ishlab chiqaruvchi zavodlaridan olib kelamiz. Har bir partiyada sifat pasporti bor, hujjatlarni yetkazib berishga ilova qilamiz.")],
         longread=("Kimga yetkazamiz",
                   "Servis markazlari, doʻkonlar va korporativ avtoparklarga. Muntazam joʻnatishlarda narxni davrga belgilaymiz va omborda kelishilgan zaxirani saqlaymiz."))

category("/uz/g-energy-retail", "g-energy-retail.html", "G-Energy — chakana tarmoq",
         "Oʻzbekistonda chakana savdo uchun G-Energy",
         "G-Energy chakana tarmoq — doʻkon va STO uchun shartlar",
         "Oʻzbekiston boʻylab avtotovarlar doʻkonlari, STO va shoxobchalarga G-Energy motor moylari. Optom shartlar, savdoni qoʻllab-quvvatlash.",
         "Avtotovarlar doʻkonlari, servislar va shoxobchalar uchun shartlar: optom narxlar, Toshkentdagi ombordan joʻnatish, savdoni qoʻllab-quvvatlash va firma materiallari.",
         None, None,
         preset="Yengil transport uchun motor moylari",
         uses=[("Avtotovarlar doʻkonlari", "Hududdagi talabga mos qadoq va qovushqoqliklar"),
               ("Servislar va STO", "Almashtirish uchun bochka va kanistrlarda moy"),
               ("Shoxobchalar", "Vitrina pozitsiyalari va firma materiallari"),
               ("Internet-doʻkonlar", "Toshkentdagi ombordan joʻnatish")],
         faq=[("Qanday hajmdan ishlaysiz?",
               "Shartlar tanlab olish hajmi va muntazamligiga bogʻliq — alohida kelishamiz. Oqimingizni yozing, hisoblab beramiz."),
              ("Assortiment tanlashda yordam berasizmi?",
               "Ha. Umumiy narxlar roʻyxati boʻyicha emas, hududingizdagi mashinalar parkiga qarab roʻyxat tuzamiz.")],
         longread=("Hamkorga nima beramiz",
                   "Tanlab olish hajmiga qarab optom narx, shartnoma boʻyicha muddatli toʻlov, Oʻzbekiston boʻylab yetkazib berish va savdo nuqtasiga firma materiallari."))

category("/uz/transmission", "transmission.html", "Transmissiya moylari",
         "Toshkentda Gazpromneft transmissiya moylari",
         "Oʻzbekistonda Gazpromneft transmissiya moylari",
         "MUK, AUK, koʻpriklar va gidrokuchaytirgich uchun Gazpromneft transmissiya moylari, ATF ham bor. Toshkentdagi ombordan yetkazib berish, ruxsatnomalar boʻyicha tanlash.",
         "MUK, AUK, koʻpriklar va gidrokuchaytirgich uchun, ATF ham bor. SAE qovushqoqlik sinfi, API darajasi va uzel ishlab chiqaruvchisining ruxsatnomasi boʻyicha tanlaymiz.",
         None, None,
         preset="Transmissiya moylari",
         uses=[("MUK va tarqatuvchi qutilar", "SAE qovushqoqligi boʻyicha GL-4 va GL-5 sinflari"),
               ("Avtomatik uzatmalar qutisi", "Ishlab chiqaruvchi talabiga mos ATF suyuqliklari"),
               ("Yetakchi koʻpriklar va reduktorlar", "Yuqori yuklama va changli sharoitlar uchun"),
               ("Gidrokuchaytirgichlar", "Maxsus gidrokuchaytirgich suyuqliklari")],
         faq=[("Koʻprikka qanday moy kerakligini qanday bilish mumkin?",
               "Texnika qoʻllanmasi boʻyicha: API GL-4 yoki GL-5 sinfi, SAE qovushqoqligi va zadirga qarshi qoʻshimchalar talabi. Hujjat boʻlmasa, marka va modelni ayting — katalog boʻyicha tanlaymiz."),
              ("Butun parkni bitta moy bilan yopish mumkinmi?",
               "Koʻpincha ha. Aralash parklar uchun roʻyxatni bitta pozitsiya maksimal uzelni yopadigan qilib tuzamiz: omborda qoldiq kam va notoʻgʻri quyish xavfi past.")],
         longread=("Qanday tanlaymiz",
                   "Aralash parklar uchun roʻyxatni bitta moy imkon qadar koʻp uzelni yopadigan qilib tuzamiz — buyurtmachining omborida kamroq pozitsiya qoladi."))

category("/uz/grease", "grease.html", "Plastik moylar",
         "Toshkentda Gazpromneft plastik moylari",
         "Oʻzbekistonda Gazpromneft plastik moylari",
         "Gazpromneft plastik moylari: litiy, kalsiy, yuqori haroratli va Steelgrease. Toshkentdagi ombor, kartrijdan bochkagacha qadoq, partiyaga hujjatlar.",
         "Litiy, kalsiy, yuqori haroratli moylar va Steelgrease liniyasi. Kartrijdan bochkagacha qadoq, Toshkentdagi omborda mavjud, har partiyaga sifat pasporti.",
         "grease", "Podshipnikdagi plastik moy — Gazpromneft moylari",
         preset="Plastik moylar",
         uses=[("Dumalanish va sirpanish podshipniklari", "Umumiy maqsadli litiy moylari"),
               ("Yuqori haroratlar", "Metallurgiya, sement va shisha ishlab chiqarish"),
               ("Nam va yuvish", "Yuvilishga chidamli kalsiy va kompleks moylar"),
               ("Ochiq uzellar va arqonlar", "Karyer texnikasi uchun adgeziv tarkiblar")],
         faq=[("Litol-24 oʻrniga nima ishlatish mumkin?",
               "Nega ushlab turmaganiga bogʻliq. Harorat yuqori boʻlsa — boshqa quyultirgich, yuvilib ketsa — suvga chidamli moy, yuklama katta boʻlsa — zadirga qarshi qoʻshimchali tarkib kerak. Uzelni tasvirlang, tanlaymiz."),
              ("Qanday qadoqda yetkazasiz?",
               "Kartrijdan bochkagacha. Aniq pozitsiya boʻyicha qadoqni tanlash paytida aniqlaymiz.")],
         longread=("Qanday tanlaymiz",
                   "Uzeldagi harorat, yuklama va nam yoki abraziv borligiga qarab. Universal moy ushlab turmay qolgan joyda odatda moylash chastotasini emas, quyultirgichni oʻzgartirish kerak."))

category("/uz/fluids", "fluids.html", "Texnik suyuqliklar va SOJ",
         "Toshkentda Gazpromneft texnik suyuqliklari va SOJ",
         "Gazpromneft antifrizlari, tormoz suyuqliklari va SOJ",
         "Toshkentdagi ombordan Gazpromneft antifrizlari, tormoz suyuqliklari va moylab-sovutuvchi suyuqliklari. Qadoq 1 litrdan kub sigʻimgacha, partiyaga hujjatlar.",
         "Antifrizlar, tormoz suyuqliklari, moylab-sovutuvchi suyuqliklar. Qadoq bir litrdan kub sigʻimgacha, Toshkentdagi omborda mavjud, har partiyaga sifat pasporti.",
         "fluids", "Metallga ishlov berishda moylab-sovutuvchi suyuqlik",
         preset="Antifriz, tormoz suyuqligi, SOJ",
         uses=[("Antifrizlar", "Texnika ishlab chiqaruvchisi talabi va mintaqa iqlimiga qarab"),
               ("Moylab-sovutuvchi suyuqliklar", "Zagotovka materiali va ishlov turiga qarab"),
               ("Tormoz suyuqliklari", "Yuk va yengil transport uchun DOT sinflari"),
               ("Yuvish tarkiblari", "Bir markadan boshqasiga oʻtish uchun")],
         faq=[("Texnikamizga qaysi antifriz toʻgʻri keladi?",
               "Ishlab chiqaruvchi talabiga qaraymiz — karboksilat, lobrid yoki anʼanaviy tarkib, hamda mintaqadagi haroratga. Texnika markasini ayting, tanlaymiz."),
              ("SOJni qanday tanlash kerak?",
               "Zagotovka materiali, ishlov turi va uskunaga qarab. Hamma narsaga mos universal suyuqlik boʻlmaydi: poʻlatda yaxshi ishlagani alyuminiyga toʻgʻri kelmasligi mumkin.")],
         longread=("Qanday tanlaymiz",
                   "Ishlab chiqarish uchun — zagotovka materiali va ishlov turiga mos SOJ, avtoparklar uchun — texnika talabi va mintaqa iqlimiga mos antifriz."))

print("uz: toifalar tayyor")

# ------------------------------------------------------------- bosh sahifa
HOME_FAQ = [
 ("Import moyni Gazpromneftga almashtirsa boʻladimi?",
  "Ha. Analogni qovushqoqlik sinfi, tozalik darajasi va uskuna ishlab chiqaruvchisining ruxsatnomasi boʻyicha tanlaymiz — Shell, Mobil, Total, Castrol va boshqa markalar uchun. Tavsiflar solishtirmasi va oʻtishdan oldin tizimni yuvish boʻyicha tavsiyani ilova qilamiz."),
 ("Yetkazib berishga qanday hujjatlar berasiz?",
  "Shartnoma, hisob-faktura, tovar-transport hujjatlari va partiyaga sifat pasporti. Tender uchun buyurtmachi talabiga qarab distribyutorlik xati va muvofiqlik sertifikatlarini ham yigʻamiz."),
 ("Qanchalik tez joʻnata olasiz?",
  "Toshkentdagi ombordagi pozitsiyalarni ariza tushgandan keyin 24 soat ichida joʻnatamiz. Kerakli pozitsiya boʻlmasa, muddatni darhol aytamiz — choʻzmaymiz."),
 ("Mahsulot asl ekaniga qanday ishonch hosil qilish mumkin?",
  "«Smart Energy Eco Trade» MChJ — «Gazpromneft — moylash materiallari»ning Oʻzbekistondagi rasmiy distribyutori. Ishlab chiqaruvchi zavodlari bilan toʻgʻridan-toʻgʻri ishlaymiz, har partiyada sifat pasporti bor."),
 ("Tanlash qancha turadi?",
  "Bepul. Texnik mutaxassis texnika roʻyxatini koʻrib chiqadi, pozitsiyalarni tanlaydi va yillik hajmni hisoblaydi — bu alohida xizmat emas, ishimizning bir qismi."),
 ("Viloyatlardagi korxonalar bilan ishlaysizmi?",
  "Ha, Toshkent, Samarqand, Buxoro, Navoiy va Fargʻona vodiysiga yetkazib beramiz. Yetkazib berish shartlarini ariza paytida kelishamiz."),
]

home = """
<main>

  <section class="hero">
    <div class="wrap hero__grid">
      <div class="hero__body">
        <span class="hero__badge">Toshkentda ombor · 24 soatda joʻnatish</span>
        <h1>Gazpromneft Oʻzbekiston&nbsp;— Toshkentdagi ombordan moylash materiallari</h1>
        <p class="hero__lead">Texnikangizga moy tanlab, ombordagi mavjudlik bilan narxlarni 15 daqiqada yuboramiz. 24 soatda joʻnatish, buxgalteriya va tender uchun toʻliq hujjatlar paketi.</p>
        <div class="hero__actions">
          <a class="btn btn--orange" href="tel:+998908085972">Qoʻngʻiroq qiling: +998 90 808 59 72</a>
          <a class="btn btn--onDark" href="#zayavka">Tanlov va narxlarni olish</a>
        </div>
        <div class="trust">
          <span>Rasmiy distribyutor</span>
          <span>Partiyaga sifat pasporti</span>
          <span>Oʻzbekiston boʻylab yetkazish</span>
        </div>
      </div>
      <div class="hero__shot"><picture><source type="image/avif" srcset="/img/hero-sm.avif 700w, /img/hero-md.avif 960w, /img/hero.avif 1400w" sizes="(max-width:900px) 100vw, 45vw"><source type="image/webp" srcset="/img/hero-sm.webp 700w, /img/hero-md.webp 960w, /img/hero.webp 1400w" sizes="(max-width:900px) 100vw, 45vw"><img src="/img/hero.webp" alt="Gazpromneft moylarini quyish liniyasi" width="{herow}" height="{heroh}" fetchpriority="high" decoding="async"></picture></div>
    </div>
  </section>

  <div class="stats">
    <div class="wrap stats__in">
      <div class="stats__item"><div class="stats__num">3 yil</div><div class="stats__label">Oʻzbekistonga yetkazib beramiz</div></div>
      <div class="stats__item"><div class="stats__num">600+</div><div class="stats__label">omborda pozitsiya</div></div>
      <div class="stats__item"><div class="stats__num">24 soat</div><div class="stats__label">arizadan joʻnatishgacha</div></div>
      <div class="stats__item"><div class="stats__num">NKMK, UzAuto</div><div class="stats__label">buyurtmachilarimiz orasida</div></div>
    </div>
  </div>

  <section class="section" id="products">
    <div class="wrap">
      <div class="section__head">
        <div>
          <h2>Mahsulotlar</h2>
          <p class="section__sub">Toshkentdagi ombordan Gazpromneft, G-Profi va G-Energy toʻliq liniyasi</p>
        </div>
        <a class="section__link" href="/uz/products">Butun katalog →</a>
      </div>
      <div class="cards">
{cards}
      </div>
    </div>
  </section>

  <section class="split">
    <div class="split__body">
      <h2>Uskunangizga moy tanlab beramiz</h2>
      <p>Texnika roʻyxatini yoki hozirgi moy markalarini yuboring — texnik mutaxassis analoglar bilan tanlov va yillik hajm hisobini tayyorlaydi.</p>
      <div class="steps">
        <div class="step"><b>1</b><span>Texnika roʻyxatini formada, Telegramda yoki telefon orqali yuborasiz</span></div>
        <div class="step"><b>2</b><span>Tanlov, TDS va tijorat taklifini olasiz</span></div>
        <div class="step"><b>3</b><span>Toshkentdagi ombordan joʻnatamiz, Oʻzbekiston boʻylab yetkazamiz</span></div>
      </div>
      <div class="split__actions">
        <a class="btn btn--navy" href="#zayavka">Ariza yuborish</a>
        <a class="btn btn--outline" href="/uz/podbor">Tanlash qanday oʻtadi</a>
      </div>
    </div>
    <picture><source type="image/avif" srcset="/img/podbor-sm.avif 450w, /img/podbor.avif 900w" sizes="(max-width:900px) 100vw, 50vw"><source type="image/webp" srcset="/img/podbor-sm.webp 450w, /img/podbor.webp 900w" sizes="(max-width:900px) 100vw, 50vw"><img class="split__media" src="/img/podbor.webp" alt="Gazpromneft laboratoriyasi: moyni to'rt sharli ishqalanish mashinasida sinash" width="{podborw}" height="{podborh}" loading="lazy" decoding="async"></picture>
  </section>

  <section class="section section--tight" id="industries">
    <div class="wrap">
      <div class="section__head">
        <div><h2>Tarmoqlar</h2><p class="section__sub">Turli ishlab chiqarishlarda odatda nima kerak boʻladi</p></div>
        <a class="section__link" href="/uz/otrasli">Barcha tarmoqlar →</a>
      </div>
      <div class="tiles">
        <a class="tile" href="/uz/hydralic"><b>Kon sanoati</b><span>Karyer texnikasi gidravlikasi, KMK uchun reduktor moylari</span></a>
        <a class="tile" href="/uz/grease"><b>Metallurgiya</b><span>Issiqlikka chidamli moylar, SOJ, issiqlik tashuvchilar</span></a>
        <a class="tile" href="/uz/gpn"><b>Transport va logistika</b><span>Yuk texnikasi va avtobuslar parki uchun motor moylari</span></a>
        <a class="tile" href="/uz/industrial"><b>Energetika</b><span>Turbina va transformator moylari</span></a>
      </div>
    </div>
  </section>

  <section class="section section--tight section--grey">
    <div class="wrap seo">
      <div class="seo__text">
        <h2>Oʻzbekistonda Gazpromneft moylash materiallarini qayerdan sotib olish mumkin</h2>
        <p>«Smart Energy Eco Trade» MChJ Gazpromneft, G-Profi va G-Energy mahsulotlarini Toshkent, Samarqand, Buxoro, Navoiy va Fargʻona vodiysi korxonalariga yetkazib beradi. Omborda doimiy ravishda HLP 32, 46 va 68 gidravlik moylari, CLP reduktor moylari, yuk va karyer texnikasi uchun motor moylari, plastik moylar va antifrizlar bir litrdan kub sigʻimgacha qadoqda mavjud.</p>
        <p>Sanoat korxonalari uchun belgilangan narx bilan yillik spetsifikatsiya tayyorlaymiz, yetkazib berishni shartnoma asosida rasmiylashtiramiz va tender jarayonlari uchun toʻliq hujjatlar paketini beramiz. Texnik mutaxassislar aniq uskunaga moy tanlashga va import markalardan Gazpromneft mahsulotiga oʻtishga yordam beradi.</p>
      </div>
      <aside class="callout">
        <b>Narxlar roʻyxatini olish</b>
        <p>Dolzarb narxlar va ombordagi mavjudlikni 15 daqiqada yuboramiz.</p>
        <a class="btn btn--orange" href="#zayavka">Ariza qoldirish</a>
        <a class="btn btn--onDark" href="tel:+998908085972">+998 90 808 59 72</a>
        <a class="btn btn--onDark" href="{tg}" rel="noopener">Telegramga yozish</a>
        <small>Timur Yarullin, korporativ menejer.</small>
      </aside>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section__head"><div><h2>Bizga ishonishadi</h2></div></div>
      <div class="logos">
        <img src="/img/logo-ngmk.webp" alt="Navoiy kon-metallurgiya kombinati" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-enter.webp" alt="Enter Engineering" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-ttz.webp" alt="V. L. Galperin nomidagi Toshkent quvur zavodi" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-ahangaran.webp" alt="Akhangarancement" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-cement.webp" alt="Namangan Sement" width="400" height="400" loading="lazy" decoding="async">
      </div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section__head">
        <div>
          <h2>Nega bizdan olishadi</h2>
          <p class="section__sub">Taʼminotchi birinchi yetkazib berishdan oldin odatda nimani tekshiradi</p>
        </div>
      </div>
      <div class="why">
        <div class="why__item"><b>Rasmiy distribyutor</b><span>Mahsulot vositachilar orqali emas, toʻgʻridan-toʻgʻri ishlab chiqaruvchi zavodlaridan keladi. Har partiyaga sifat pasporti.</span></div>
        <div class="why__item"><b>Texnik mutaxassis tanlaydi</b><span>Texnika roʻyxatini koʻrib chiqamiz, pozitsiyalarni tanlaymiz va yillik hajmni hisoblaymiz. Bepul va majburiyatsiz.</span></div>
        <div class="why__item"><b>Import markalarni almashtirish</b><span>Shell, Mobil, Total va Castrol analoglarini tavsiflar solishtirmasi bilan tanlaymiz.</span></div>
        <div class="why__item"><b>Toshkentda ombor</b><span>Mavjud pozitsiyalarni 24 soatda joʻnatamiz. Boʻlmaganini choʻzmasdan, muddatini darhol aytamiz.</span></div>
        <div class="why__item"><b>Tender uchun hujjatlar</b><span>Shartnoma, hisob-faktura, sifat pasporti, sertifikatlar va distribyutorlik xati. Paketni buyurtmachi talabiga qarab yigʻamiz.</span></div>
        <div class="why__item"><b>Yillik spetsifikatsiyalar</b><span>Doimiy ehtiyoji bor korxonalar uchun narxni davrga belgilaymiz — har yetkazishni qaytadan kelishish shart emas.</span></div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--grey">
    <div class="wrap">
      <div class="section__head"><div><h2>Koʻp beriladigan savollar</h2></div></div>
      <div class="faqgrid">
{faqhtml}
      <aside class="faqside">
        <picture>
          <source type="image/avif" srcset="/img/barrel-sm.avif 400w, /img/barrel.avif 800w" sizes="(max-width:900px) 100vw, 340px">
          <source type="image/webp" srcset="/img/barrel-sm.webp 400w, /img/barrel.webp 800w" sizes="(max-width:900px) 100vw, 340px">
          <img src="/img/barrel.webp" alt="Omborda 205 litrli Gazpromneft moy bochkasi" width="800" height="1067" loading="lazy" decoding="async">
        </picture>
        <div class="faqside__cap">
          <b>Bochka va kubda yetkazamiz</b>
          <span>Qadoqlash 20 litrdan kub idishlargacha. Doimiy ehtiyoj uchun narxni bir yilga belgilaymiz — har yetkazishni qaytadan kelishish shart emas.</span>
        </div>
      </aside>
      </div>
    </div>
  </section>

  <section class="formband" id="zayavka">
    <div class="wrap formband__in">
      <div class="formband__body">
        <h2>Texnika roʻyxatini yuboring — tanlov va narxlarni qaytaramiz</h2>
        <p class="formband__lead">Artikul va qovushqoqlik sinflarini bilish shart emas. Qanday texnika borligini va unga hozir nima quyilishini yozsangiz kifoya — qolganini texnik mutaxassis qiladi.</p>
        <div class="formband__list">
          <span>Import markalar analoglari bilan tanlov va yillik hajm hisobi</span>
          <span>Toshkentdagi omborda haqiqiy mavjudlik bilan narxlar</span>
          <span>TDS texnik tavsifi va MSDS xavfsizlik pasporti</span>
          <span>Buxgalteriya va tender uchun toʻliq hujjatlar paketi</span>
        </div>
        <div class="formband__alt">
          <span>Telefon orqali tezroq:</span>
          <a href="tel:+998908085972">+998 90 808 59 72</a>
          <span>yoki</span>
          <a href="{tg}" rel="noopener">Telegramga yozing</a>
        </div>
      </div>
{form}
    </div>
  </section>

  <section class="section section--tight" id="where">
    <div class="wrap">
      <div class="section__head">
        <div>
          <h2>Bizni qayerdan topasiz</h2>
          <p class="section__sub">Ofis va ombor Toshkentda — ariza kelgandan keyin bir kun ichida joʻnatamiz</p>
        </div>
        <a class="section__link" href="/uz/contacts">Barcha aloqalar →</a>
      </div>
      <div class="findus">
        <div class="findus__info">
          <div class="findus__row"><b>Manzil</b><span>Toshkent, Mirzo Ulugʻbek tumani</span></div>
          <div class="findus__row"><b>Ish vaqti</b><span>Du–Ju, 09:00–18:00</span></div>
          <div class="findus__row"><b>Korporativ menejer</b><a href="tel:+998908085972">+998 90 808 59 72</a><span>Timur Yarullin</span></div>
          <div class="findus__row"><b>Savdo boʻlimi</b><a href="tel:+998935048490">+998 93 504 84 90</a></div>
          <div class="findus__row"><b>Pochta</b><a href="mailto:t.yarulin@s-energy.uz">t.yarulin@s-energy.uz</a></div>
          <a class="btn btn--outline" href="https://yandex.uz/maps/?ll=69.312125%2C41.3230571&amp;z=17&amp;pt=69.312125,41.3230571" rel="noopener">Marshrut tuzish</a>
        </div>
        <div class="map">
        <picture>
          <source type="image/avif" srcset="/img/map-sm.avif 600w, /img/map.avif 1200w" sizes="(max-width:900px) 100vw, 50vw">
          <source type="image/webp" srcset="/img/map-sm.webp 600w, /img/map.webp 1200w" sizes="(max-width:900px) 100vw, 50vw">
          <img src="/img/map.webp" alt="Smart Energy Eco Trade ofisi Toshkentda xaritada" width="1200" height="600" loading="lazy" decoding="async">
        </picture>
        <div class="map__go">
          <span class="map__hint">Yoʻnalishni ochish:</span>
          <a class="btn btn--outline btn--sm" href="https://yandex.uz/maps/?ll=69.312125%2C41.3230571&amp;z=17&amp;pt=69.312125,41.3230571,pm2rdm" rel="noopener" target="_blank">Yandex Xarita</a>
          <a class="btn btn--outline btn--sm" href="https://www.google.com/maps/search/?api=1&amp;query=41.3230571%2C69.312125" rel="noopener" target="_blank">Google Xarita</a>
          <a class="btn btn--outline btn--sm" href="https://maps.apple.com/?ll=41.3230571,69.312125&amp;q=Smart%20Energy%20Eco%20Trade" rel="noopener" target="_blank">Apple Xarita</a>
        </div>
        <p class="map__attr">&copy; <a href="https://www.openstreetmap.org/copyright" rel="noopener nofollow" target="_blank">OpenStreetMap</a></p>
      </div>
      </div>
    </div>
  </section>

</main>
""".format(tg=TG, cards=cards_html(), herow=dim("hero")[0], heroh=dim("hero")[1],
           podborw=dim("podbor")[0], podborh=dim("podbor")[1], faqhtml=faq_html(HOME_FAQ),
           form=leadform("Bosh sahifadan ariza (uz)", "15 daqiqada tanlov va narxlar",
                         "Ikkita maydonni toʻldiring — qolganini oʻzimiz aniqlaymiz.",
                         "Tanlov va narxlarni olish"))

page("/uz/", "index.html", "Gazpromneft Oʻzbekiston — moylarning rasmiy distribyutori",
     "Gazpromneft Oʻzbekiston: industrial, motor va transmissiya moylari, plastik moylar, texnik suyuqliklar. Toshkentda ombor, 24 soatda joʻnatish.",
     home, preload="/img/hero.webp", preload_sizes="(max-width:900px) 100vw, 45vw",
     jsonld=ORG_LD + faq_ld(HOME_FAQ), cta=False,
     ogtitle="Gazpromneft Oʻzbekiston — rasmiy distribyutor")

# ------------------------------------------------------------- mahsulotlar
products = """
<main>
  <nav class="wrap crumbs" aria-label="Yoʻl">
    <a href="/uz/">Bosh sahifa</a><span>/</span><b>Mahsulotlar</b>
  </nav>

  <div class="wrap page">
    <div class="pagehero">
      <picture><source type="image/avif" srcset="/img/products-sm.avif 700w, /img/products-md.avif 960w, /img/products.avif 1400w" sizes="100vw"><source type="image/webp" srcset="/img/products-sm.webp 700w, /img/products-md.webp 960w, /img/products.webp 1400w" sizes="100vw"><img src="/img/products.webp" alt="Gazpromneft moylash materiallari zavodining rezervuar parki" width="{pw}" height="{ph}" fetchpriority="high" decoding="async"></picture>
    </div>
    <div class="page__head">
      <h1>Oʻzbekistonda Gazpromneft mahsulotlari</h1>
      <p class="page__lead">Toshkentdagi ombordan 600 dan ortiq pozitsiya: industrial va motor moylari, transmissiya moylari, plastik moylar, antifrizlar va SOJ. Har partiyaga sifat pasporti, tenderlar uchun toʻliq hujjatlar paketi.</p>
    </div>

    <div class="cards">
{cards}
    </div>

    <div class="section__head" style="margin-top:44px">
      <div>
        <h2>Industrial moylar vazifasi boʻyicha</h2>
        <p class="section__sub">Pozitsiyalar roʻyxati va qovushqoqlik sinflari bilan alohida sahifalar</p>
      </div>
    </div>
    <div class="tiles">
      <a class="tile" href="/uz/hydralic"><b>Gidravlik</b><span>Gazpromneft Hydraulic HLP 32, 46, 68</span></a>
      <a class="tile" href="/uz/reductor"><b>Reduktor</b><span>Gazpromneft Reductor CLP 150, 220</span></a>
      <a class="tile" href="/uz/compressor"><b>Kompressor</b><span>Gazpromneft Compressor Oil 46</span></a>
      <a class="tile" href="/uz/industrial"><b>Turbina va issiqlik tashuvchilar</b><span>Turbine Oil 32, Termoil 26</span></a>
    </div>

    <div class="layout" style="margin-top:40px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Uskunaga qarab tanlash</h2>
          <p>Aynan nima kerakligini bilmasangiz, texnika roʻyxatini yoki hozirgi moy markalarini yuboring. Texnik mutaxassis analoglar bilan pozitsiyalarni tanlaydi, yillik hajmni hisoblaydi va TDS ilova qiladi. Tanlash bepul va hech narsaga majbur qilmaydi.</p>
          <p>Shuningdek: <a href="/uz/podbor" style="color:var(--blue);font-weight:600">tanlash qanday oʻtadi</a>, <a href="/uz/analogi" style="color:var(--blue);font-weight:600">import markalarni almashtirish jadvali</a> va <a href="/uz/otrasli" style="color:var(--blue);font-weight:600">tarmoqlar boʻyicha yechimlar</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
{catalogform}
      </aside>
    </div>
  </div>
</main>
""".format(cards=cards_html(indent="      "), pw=dim("products")[0], ph=dim("products")[1],
           catalogform=leadform("Katalogdan ariza (uz)", "Kerakli pozitsiyani topmadingizmi?",
                                "Nima kerakligini yozing — mavjudligini tekshirib, narxini yuboramiz.",
                                "Ariza yuborish", cls=" leadform--aside", anchor="zayavka"))

page("/uz/products", "products.html", "Gazpromneft mahsulotlari — moylar katalogi",
     "Toshkentdagi ombordan Gazpromneft, G-Profi va G-Energy moylash materiallari katalogi: industrial, motor, transmissiya moylari, plastik moylar, antifrizlar va SOJ.",
     products, active="products", preload="/img/products.webp",
     jsonld=crumbs_ld([("Bosh sahifa", "/uz/"), ("Mahsulotlar", "/uz/products")]))

# ------------------------------------------------------------- oddiy sahifalar
def simple(path, fname, crumb, h1, title, desc, active, blocks, faq=None, img=None, alt=""):
    hero = ""
    if img:
        iw, ih = dim(img)
        hero = '''    <div class="pagehero">
      <picture><source type="image/avif" srcset="%s" sizes="100vw"><source type="image/webp" srcset="%s" sizes="100vw"><img src="/img/%s.webp" alt="%s" width="%d" height="%d" fetchpriority="high" decoding="async"></picture>
    </div>
''' % (srcset(img, iw).replace(".webp", ".avif"), srcset(img, iw), img, alt, iw, ih)
    faq_block = ""
    if faq:
        faq_block = '\n    <div class="longread"><h2>Koʻp beriladigan savollar</h2></div>\n%s' % faq_html(faq)
    body = '''
<main>
  <nav class="wrap crumbs" aria-label="Yoʻl">
    <a href="/uz/">Bosh sahifa</a><span>/</span><b>%s</b>
  </nav>
  <div class="wrap page">
%s    <div class="page__head">
      <h1>%s</h1>
    </div>
%s%s
  </div>
</main>
''' % (crumb, hero, h1, blocks, faq_block)
    page(path, fname, title, desc, body, active=active,
         preload=("/img/%s.webp" % img) if img else None,
         jsonld=crumbs_ld([("Bosh sahifa", "/uz/"), (crumb, path)]) + (faq_ld(faq) if faq else ""))


PODBOR_FAQ = [
 ("Tanlash qancha turadi?", "Hech qancha. Tanlash — taʼminotchining ishi, alohida xizmat emas. Ariza hech narsaga majbur qilmaydi: tanlovni olib, boshqa takliflar bilan solishtirishingiz mumkin."),
 ("Texnikaga hujjat boʻlmasa nima qilish kerak?", "Uzelning markasi va modeli yetarli. Ishlab chiqaruvchi kataloglari boʻyicha qovushqoqlik sinfi va ruxsatnoma talabini topamiz. Model ham nomaʼlum boʻlsa — shildik yoki hozirgi moy yorligʻining surati boʻladi."),
 ("Javob qanchalik tez keladi?", "Ish vaqtida oddiy soʻrovlarga 15 daqiqada. Roʻyxatda oʻnlab texnika boʻlsa, yillik hajm hisobi bilan toʻliq tanlovga bir ish kuni ketadi."),
 ("Sinov partiyasini berasizmi?", "Birinchi yetkazib berish shartlarini alohida kelishamiz — hajm va texnika turini yozing, menejer variant taklif qiladi."),
]

podbor_blocks = '''    <p class="page__lead" style="max-width:760px">Texnika roʻyxatini yoki hozir quyayotgan moy markalarini yuboring — texnik mutaxassis Gazpromneft pozitsiyalarini tanlaydi, yillik hajmni hisoblaydi va ombordagi mavjudlik bilan narxlarni yuboradi. Bepul va majburiyatsiz.</p>

    <div class="why" style="margin-top:28px">
      <div class="why__item"><b>Texnika boʻyicha tanlash</b><span>Marka va model — ishlab chiqaruvchining qovushqoqlik sinfi, API yoki ACEA darajasi va ruxsatnoma talabini topamiz.</span></div>
      <div class="why__item"><b>Analog boʻyicha tanlash</b><span>Hozir nima quyilganini ayting — oʻsha sinf va darajadagi Gazpromneft mahsulotini tanlab, tavsiflar solishtirmasini koʻrsatamiz.</span></div>
      <div class="why__item"><b>Hajm hisobi</b><span>Texnika soni va almashtirish oraligʻiga qarab yillik ehtiyojni hisoblaymiz — byudjetni himoya qilishda qulay.</span></div>
    </div>

    <div class="longread"><h2>Tanlash qanday oʻtadi</h2></div>
    <div class="steps" style="margin-bottom:28px">
      <div class="step"><b>1</b><span>Texnika roʻyxatini yoki hozirgi moy markalarini yuborasiz — quyidagi formada, telefon orqali yoki pochtaga</span></div>
      <div class="step"><b>2</b><span>Texnik mutaxassis ruxsatnoma va qovushqoqlik sinflarini solishtirib, pozitsiyalarni tanlaydi va hajmni hisoblaydi</span></div>
      <div class="step"><b>3</b><span>Analoglar bilan tanlov, TDS texnik tavsifi va ombordagi haqiqiy mavjudlik bilan narxlarni olasiz</span></div>
      <div class="step"><b>4</b><span>Hammasi maʼqul boʻlsa — shartnoma rasmiylashtiramiz va Toshkentdagi ombordan joʻnatamiz</span></div>
    </div>

    <div class="layout">
      <div class="layout__main">
%s
        <div class="longread">
          <h2>Natijada nima olasiz</h2>
          <p>Tanlov jadvalini: har bir texnika uchun Gazpromneft pozitsiyasi, qovushqoqlik sinfi, sifat darajasi va qadogʻi. Unga TDS texnik tavsifi va MSDS xavfsizlik pasportini, import markadan oʻtishda esa asosiy tavsiflar solishtirmasini ilova qilamiz — muhandis tanlov nimaga asoslanganini koʻrsin.</p>
          <p>Pozitsiya koʻp boʻlsa, yillik ehtiyojni alohida hisoblab, belgilangan narx bilan spetsifikatsiya taklif qilamiz. Shuningdek: <a href="/uz/analogi" style="color:var(--blue);font-weight:600">import markalarni almashtirish jadvali</a> va <a href="/uz/price" style="color:var(--blue);font-weight:600">narx shartlari</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % (CHECKLIST, leadform("Tanlashga ariza (uz)", "Texnikani tanlashga yuborish",
                          "Ish vaqtida, odatda 15 daqiqada javob beramiz.",
                          "Tanlovni olish", cls=" leadform--aside", anchor="zayavka"))

simple("/uz/podbor", "podbor.html", "Moy tanlash", "Texnikaga moy tanlash — bepul",
       "Toshkentda texnikaga Gazpromneft moyini tanlash — bepul",
       "Texnikangizga Gazpromneft moyini bepul tanlab beramiz: marka va model yoki import moy analogi boʻyicha. Hajm hisobi, TDS, Toshkentdagi narxlar.",
       "podbor", podbor_blocks, faq=PODBOR_FAQ, img="podbor", alt="Texnikaga moy tanlash")

ANALOG_ROWS = [
 ("Gidravlik, ISO VG 32", "Shell Tellus S2 M 32, Mobil DTE 24, Total Azolla ZS 32", "Gazpromneft Hydraulic HLP 32"),
 ("Gidravlik, ISO VG 46", "Shell Tellus S2 M 46, Mobil DTE 25, Total Azolla ZS 46", "Gazpromneft Hydraulic HLP 46"),
 ("Gidravlik, ISO VG 68", "Shell Tellus S2 M 68, Mobil DTE 26, Total Azolla ZS 68", "Gazpromneft Hydraulic HLP 68"),
 ("Reduktor, ISO VG 150", "Shell Omala S2 G 150, Mobilgear 600 XP 150", "Gazpromneft Reductor CLP 150"),
 ("Reduktor, ISO VG 220", "Shell Omala S2 G 220, Mobilgear 600 XP 220", "Gazpromneft Reductor CLP 220"),
 ("Kompressor, ISO VG 46", "Shell Corena S2 P 46, Mobil Rarus 425", "Gazpromneft Compressor Oil 46"),
 ("Turbina, ISO VG 32", "Shell Turbo T 32, Mobil DTE 797", "Gazpromneft Turbine Oil 32"),
]
analog_rows_html = "\n".join('''        <div class="table__row">
          <b>%s</b>
          <span><span class="table__label">Import markalar: </span>%s</span>
          <span><span class="table__label">Analog: </span><b style="color:var(--blue)">%s</b></span>
        </div>''' % r for r in ANALOG_ROWS)

ANALOG_FAQ = [
 ("Bu rasmiy almashtirish jadvalimi?", "Yoʻq. Bu ISO VG qovushqoqlik sinfi va odatdagi vazifa boʻyicha solishtirma — suhbatni shundan boshlash qulay. Yakuniy tanlov har doim uskuna ishlab chiqaruvchisining ruxsatnomasi va uzelning ish sharoiti boʻyicha qilinadi, shuning uchun aniq texnikaga alohida tanlov tayyorlaymiz."),
 ("Oʻtishda tizimni yuvish kerakmi?", "Nima quyilganiga va tizim holatiga bogʻliq. Bir turdagi va yaqin sinfdagi moylar orasida oʻtishda odatda yuvish shart emas, moy turi oʻzgarsa yoki ifloslanish katta boʻlsa — kerak. Tavsiyani tanlovda beramiz."),
 ("Tizimdagi eski moy qoldigʻi bilan nima qilish kerak?", "Mos moylarning kichik qoldigʻi joiz, lekin tanlovda qanchasini qoldirish mumkinligini va bu nimaga taʼsir qilishini har doim koʻrsatamiz. Moslik shubhali boʻlsa — toʻliq almashtirishni taklif qilamiz."),
 ("Tavsiflar solishtirmasini qogʻozda berasizmi?", "Ha. Tanlovga asosiy koʻrsatkichlar solishtirmasini ilova qilamiz: 40 va 100 °C dagi qovushqoqlik, qovushqoqlik indeksi, alangalanish va qotish harorati, tozalik darajasi."),
]

analogi_blocks = '''    <p class="page__lead" style="max-width:820px">Shell, Mobil, Total, Castrol va boshqa markalarni Gazpromneft mahsulotiga almashtirishni qovushqoqlik sinfi, tozalik darajasi va uskuna ishlab chiqaruvchisining talablari boʻyicha tanlaymiz. Quyida asosiy industrial guruhlar boʻyicha solishtirma — undan boshlash qulay.</p>

    <div class="table" style="margin-top:24px;--cols:1.1fr 1.6fr 1.3fr">
      <div class="table__head">
        <div>Guruh va sinf</div><div>Import markalar</div><div>Gazpromneft analogi</div>
      </div>
%s
    </div>
    <p class="table__note">Bu qovushqoqlik sinfi va odatdagi vazifa boʻyicha solishtirma, rasmiy almashtirish jadvali emas. Aniq uskunaga tanlovni texnik mutaxassis qiladi — ruxsatnoma va uzelning ish sharoitiga qarab.</p>

    <div class="layout" style="margin-top:40px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Almashtirishni qanday tanlaymiz</h2>
          <p>Avval uskuna ishlab chiqaruvchisining talabiga qaraymiz: qovushqoqlik sinfi, sifat darajasi va ruxsatnoma. Keyin ish sharoitiga: uzeldagi harorat, maydondagi chang, nam borligi, smena rejimi. Faqat shundan keyin pozitsiyani tanlab, asosiy tavsiflar boʻyicha hozir quyilganidan yomon emasligini tekshiramiz.</p>
          <p>Oʻtishda tavsiflar solishtirmasi va tizimni yuvish boʻyicha tavsiyalarni ilova qilamiz. Butun park boʻyicha almashtirish ketayotgan korxonalarda oʻtishni bosqichlarga boʻlamiz — hammasini birdan oʻzgartirmaslik uchun.</p>
          <h2>Nimadan boshlash kerak</h2>
          <p>Hozir sotib olayotgan markalar roʻyxati yetarli — qadoq va taxminiy yillik hajm bilan. Solishtirma tayyorlash va narxni hisoblash uchun shu kifoya. Roʻyxat boʻlmasa, <a href="/uz/podbor" style="color:var(--blue);font-weight:600">texnika boʻyicha tanlashdan</a> boshlang.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % (analog_rows_html, leadform("Analoglarga ariza (uz)", "Moylar roʻyxatini yuborish",
                                 "Gazpromneft mahsuloti bilan solishtirma va narxlarni yuboramiz.",
                                 "Analoglarni tanlash", cls=" leadform--aside", anchor="zayavka"))

simple("/uz/analogi", "analogi.html", "Import moylar analoglari",
       "Import moylarni Gazpromneftga almashtirish",
       "Shell, Mobil, Total oʻrniga Gazpromneft — analoglar jadvali",
       "Import moylar va Gazpromneft moslik jadvali: Shell Tellus, Mobil DTE, Total Azolla, Mobilgear. Toshkentda almashtirishni tanlab beramiz.",
       "products", analogi_blocks, faq=ANALOG_FAQ)

INDUSTRIES = [
 ("Kon sanoati va KMK", "Karyer ekskavatorlari, samosvallar, maydalash majmualari",
  "Yuqori tozalikdagi HLP gidravlik moylari, maydalagich uzatmalari uchun CLP reduktor moylari, chang va zarbali yuklamada ishlaydigan uzellarga issiqlikka chidamli moylar.", "/uz/hydralic"),
 ("Metallurgiya", "Prokat stanlari, pechlar, konveyer liniyalari",
  "Issiqlikka chidamli plastik moylar, issiqlik tashuvchilar, mexanik ishlov uchun SOJ va yuqori yuklamali uzatmalar uchun reduktor moylari.", "/uz/grease"),
 ("Sement zavodlari", "Tegirmonlar, aylanuvchi pechlar, maydalagichlar",
  "Tegirmon uzatmalari uchun reduktor moylari, ochiq tishli uzatmalar uchun adgeziv moylar, yordamchi uskunalar uchun gidravlika.", "/uz/reductor"),
 ("Transport va logistika", "Magistral tortqilar, avtobuslar, kommunal texnika",
  "MAN, Scania, Volvo va Mercedes-Benz ruxsatnomalari boʻyicha motor moylari, koʻprik va qutilar uchun transmissiya moylari, mintaqa iqlimiga mos antifrizlar.", "/uz/gpn"),
 ("Qishloq xoʻjaligi", "Traktorlar, kombaynlar, nasos stansiyalari",
  "Aralash park uchun universal motor moylari, transmissiya va gidravlik moylar, dalada ishlaydigan uzellar uchun moylar.", "/uz/transmission"),
 ("Energetika", "Turbinalar, transformatorlar, kompressor stansiyalari",
  "Turbina va transformator moylari, vint va porshenli mashinalar uchun kompressor moylari, issiqlik tashuvchilar.", "/uz/compressor"),
 ("Mashinasozlik", "Stanoklar parki, ishlov berish markazlari",
  "Zagotovka materiali va ishlov turiga mos SOJ, yoʻnaltiruvchi va shpindel moylari, presslar uchun gidravlika.", "/uz/fluids"),
 ("Qurilish", "Ekskavatorlar, pogruzchiklar, beton nasoslari",
  "Sovuqda ham, issiqda ham ishlaydigan texnika uchun gidravlik moylar, dizellar uchun motor moylari, sharnir va barmoqlar uchun moylar.", "/uz/industrial"),
]
ind_html = "\n".join('''        <a class="tile" href="%s">
          <b>%s</b>
          <span style="color:var(--muted-2);font-size:13px">%s</span>
          <span>%s</span>
        </a>''' % (u, n, sub, t) for n, sub, t, u in INDUSTRIES)

otrasli_blocks = '''    <p class="page__lead" style="max-width:820px">Oʻzbekiston boʻylab sanoat korxonalari, avtoparklar va servis markazlariga moylash materiallarini yetkazib beramiz. Quyida — koʻproq ishlaydigan tarmoqlarimiz va ularda odatda nima kerak boʻlishi.</p>

    <div class="tiles" style="grid-template-columns:repeat(4,1fr);margin-top:28px">
%s
    </div>

    <div class="layout" style="margin-top:40px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Tarmoq boʻyicha tanlash narxlar roʻyxati boʻyicha sotishdan nimasi bilan farq qiladi</h2>
          <p>Bitta moy karyerda va sexda oʻzini har xil tutadi. Karyerda chang va zarbali yuklama hal qiladi, sexda — harorat barqarorligi va zichlagichlar bilan moslik, trassada — smena rejimi va yoqilgʻi sifati. Shuning uchun umumiy narxlar roʻyxatini yubormaymiz, balki texnika qayerda va qanday ishlashini soʻraymiz.</p>
          <p>Doimiy ehtiyoji bor korxonalar uchun yillik spetsifikatsiya tayyorlaymiz: pozitsiyalar roʻyxati, hajmlar va davrga belgilangan narx. Bu har yetkazishni qaytadan kelishish zaruratini olib tashlaydi va byudjetni kurs tebranishidan himoya qiladi.</p>
          <h2>Sanoat buyurtmachilari uchun hujjatlar</h2>
          <p>Yetkazib berish shartnoma asosida toʻliq paket bilan ketadi: hisob-faktura, tovar-transport hujjatlari, partiyaga sifat pasporti. Tender jarayonlari uchun qoʻshimcha ravishda muvofiqlik sertifikatlari va distribyutorlik xatini yigʻamiz.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % (ind_html, leadform("Tarmoq sahifasidan ariza (uz)", "Ishlab chiqarishingizga tanlash",
                         "Tarmoq va texnikani yozing — tanlov va narxlarni qaytaramiz.",
                         "Tanlovni olish", cls=" leadform--aside", anchor="zayavka"))

simple("/uz/otrasli", "otrasli.html", "Tarmoqlar", "Tarmoqlar boʻyicha moylash materiallari",
       "Tarmoqlar boʻyicha Gazpromneft moylash materiallari",
       "Tarmoqqa qarab Gazpromneft moylarini tanlash: kon sanoati, metallurgiya, sement, transport, energetika, mashinasozlik. Toshkentdagi ombordan.",
       "otrasli", otrasli_blocks, img="industrial", alt="Sanoat ishlab chiqarishi — Gazpromneft moylash materiallari")

DOST_FAQ = [
 ("Qanchalik tez joʻnatasiz?", "Toshkentdagi omborda bor pozitsiyalarni ariza kelishilgandan keyin 24 soat ichida joʻnatamiz. Pozitsiya boʻlmasa, yetkazib berish muddatini darhol aytamiz — choʻzmaymiz va imkonsizni vaʼda qilmaymiz."),
 ("Viloyatlarga yetkazasizmi?", "Ha, Toshkent, Samarqand, Buxoro, Navoiy, Fargʻona vodiysi va boshqa hududlarga yetkazamiz. Shartlar hajm va manzilga bogʻliq, ariza paytida kelishamiz."),
 ("Oʻzimiz olib keta olamizmi?", "Ha, Toshkentdagi ombordan. Mashina navbatda turmasligi uchun joʻnatish vaqtini oldindan kelishamiz."),
 ("Toʻlov qanday boʻladi?", "Shartnoma va hisob asosida, pul oʻtkazish orqali. Doimiy buyurtmachilar uchun alohida shartlar mumkin — alohida muhokama qilinadi."),
 ("Yuk bilan qanday hujjatlar keladi?", "Hisob-faktura, tovar-transport hujjatlari va partiyaga sifat pasporti. Tender va kirish nazorati uchun qoʻshimcha ravishda muvofiqlik sertifikatlari va distribyutorlik xatini tayyorlaymiz."),
]

dostavka_blocks = '''    <p class="page__lead" style="max-width:820px">Toshkentda ombor, ariza kelishilgandan keyin 24 soat ichida joʻnatish, Oʻzbekiston boʻylab yetkazib berish. Buxgalteriya va tender jarayonlari uchun toʻliq hujjatlar paketi bilan shartnoma asosida ishlaymiz.</p>

    <div class="why" style="margin-top:28px">
      <div class="why__item"><b>24 soatda joʻnatish</b><span>Omborda bor pozitsiyalar uchun. Boʻlmaganining muddatini darhol aytamiz.</span></div>
      <div class="why__item"><b>Oʻzbekiston boʻylab yetkazish</b><span>Toshkent, Samarqand, Buxoro, Navoiy, Fargʻona vodiysi va boshqa hududlar.</span></div>
      <div class="why__item"><b>Oʻzi olib ketish</b><span>Toshkentdagi ombordan, joʻnatish vaqtini oldindan kelishamiz.</span></div>
      <div class="why__item"><b>Shartnoma asosida</b><span>Har yetkazishga hisob, hisob-faktura va tovar-transport hujjatlari.</span></div>
      <div class="why__item"><b>Sifat pasporti</b><span>Har partiyaga. Kirish nazorati va tenderlar uchun — toʻliq hujjatlar paketi.</span></div>
      <div class="why__item"><b>Yillik spetsifikatsiyalar</b><span>Doimiy buyurtmachilar uchun davrga belgilangan narx va joʻnatish jadvali.</span></div>
    </div>

    <div class="layout" style="margin-top:40px">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Yetkazib berish qanday oʻtadi</h2>
          <p>Siz ariza yuborasiz — pozitsiyalar roʻyxati yoki tanlash uchun texnika. Menejer mavjudlik va narxni tasdiqlaydi, kerak boʻlsa texnik mutaxassis tanlov tayyorlaydi. Keyin hisob chiqaramiz, muddatlarni kelishamiz va ombordan joʻnatamiz.</p>
          <p>Katta hajm va muntazam yetkazishlar uchun jadval bilan spetsifikatsiya rasmiylashtiramiz: unda pozitsiyalar, hajmlar va davrga narx qayd etiladi. Bu format buyurtmachiga ham, bizga ham qulay — har reysga kamroq kelishuv.</p>
          <h2>Qadoqlar</h2>
          <p>Bir litrlik kanistrdan kub sigʻimgacha yetkazamiz: 1, 4, 5, 10 va 20 litrlik kanistrlar, 205 litrlik bochkalar, kub sigʻimlar. Plastik moylar boʻyicha — kartrijdan bochkagacha. Aniq pozitsiya boʻyicha qadoqni tanlash paytida aniqlaymiz, u mahsulotga bogʻliq.</p>
        </div>
      </div>
      <aside class="layout__aside">
%s
      </aside>
    </div>
''' % leadform("Yetkazish boʻyicha savol (uz)", "Muddat va shartlarni aniqlash",
               "Pozitsiya va manzilni yozing — muddat va narxni hisoblaymiz.",
               "Ariza yuborish", cls=" leadform--aside", anchor="zayavka")

simple("/uz/dostavka", "dostavka.html", "Yetkazib berish va toʻlov", "Yetkazib berish va toʻlov",
       "Yetkazib berish va toʻlov — Gazpromneft moylari",
       "Toshkentdagi ombordan 24 soatda joʻnatish, Oʻzbekiston boʻylab yetkazish, oʻzi olib ketish, shartnoma asosida ishlash. Har partiyaga hisob-faktura va sifat pasporti.",
       "company", dostavka_blocks, faq=DOST_FAQ)

# ------------------------------------------------------------- narxlar
PRICE_FAQ = [
 ("Nega narxlar toʻgʻridan-toʻgʻri saytda yoʻq?", "Narx tanlab olish hajmi, qadoq va joʻnatish shartlariga bogʻliq: bitta pozitsiya kanistrda va kub sigʻimda har xil turadi. Aniq raqamlar bilan narxlar roʻyxatini soʻrov boʻyicha oʻsha kuni yuboramiz."),
 ("Narxni bir yilga belgilash mumkinmi?", "Doimiy ehtiyoji bor korxonalar uchun belgilangan narx bilan yillik spetsifikatsiya tayyorlaymiz — bu kurs tebranishidan himoya qiladi va har yetkazishni qaytadan kelishish zaruratini olib tashlaydi."),
 ("Yetkazib berish bilan qanday hujjatlar keladi?", "Shartnoma, hisob-faktura, tovar-transport hujjatlari va partiyaga sifat pasporti. Tender uchun qoʻshimcha ravishda muvofiqlik sertifikatlari va distribyutorlik xatini yigʻamiz."),
]

price_body = """
<main>
  <nav class="wrap crumbs" aria-label="Yoʻl">
    <a href="/uz/">Bosh sahifa</a><span>/</span><b>Narxlar</b>
  </nav>

  <div class="wrap page">
    <div class="layout">
      <div class="layout__main">
        <h1>Gazpromneft moylash materiallari narxlari</h1>
        <p class="page__lead">Narxlar roʻyxatini soʻrov boʻyicha yuboramiz: narx hajm, qadoq va joʻnatish shartlariga bogʻliq, shuning uchun saytda qatʼiy narxlar yoʻq. Toshkentdagi ombordagi mavjudlik bilan dolzarb hujjatni ish vaqtida 15 daqiqada yuboramiz.</p>

{priceform}

        <div class="longread">
          <h2>Narx nimaga bogʻliq</h2>
          <p>Qiymatga tanlab olish hajmi, qadoq (kanistr, bochka, kub sigʻim), joʻnatish davriyligi va toʻlov shartlari taʼsir qiladi. Yillik ehtiyoji bor korxonalarga belgilangan narxli spetsifikatsiya foydaliroq: u kurs tebranishidan himoya qiladi va har yetkazishni qaytadan kelishish zaruratini olib tashlaydi.</p>
          <h2>Buxgalteriya va tender uchun hujjatlar</h2>
          <p>Shartnoma asosida toʻliq paket bilan yetkazamiz: hisob-faktura, tovar-transport hujjatlari, partiyaga sifat pasporti, muvofiqlik sertifikatlari va distribyutorlik xati. Tender jarayonlari uchun buyurtmachi talabiga qarab majmua yigʻamiz.</p>
        </div>
{pricefaq}
      </div>

      <aside class="layout__aside">
{aside}
        <div class="asidebox">
          <b>Ommabop pozitsiyalar</b>
          <div>
            <a href="/uz/hydralic">Gidravlik HLP 32, 46, 68</a>
            <a href="/uz/reductor">Reduktor CLP 150, 220</a>
            <a href="/uz/gpn">Yuk texnikasi uchun motor moylari</a>
            <a href="/uz/grease">Plastik moylar</a>
            <a href="/uz/fluids">Antifrizlar va SOJ</a>
          </div>
        </div>
      </aside>
    </div>
  </div>
</main>
""".format(aside=ASIDE_REQUEST, pricefaq=faq_html(PRICE_FAQ),
           priceform=leadform("Narxlar roʻyxatiga soʻrov (uz)", "Narxlar roʻyxatini olish",
                              "Toshkent omboridagi mavjudlik bilan dolzarb narxlarni yuboramiz.",
                              "Narxlarni olish", anchor="zayavka"))

page("/uz/price", "price.html", "Oʻzbekistonda Gazpromneft moylash materiallari narxlari",
     "Oʻzbekistonda Gazpromneft moy va moylari narxlari. Narx hajm va qadoqqa bogʻliq — Toshkent omboridagi mavjudlik bilan dolzarb narxlarni 15 daqiqada yuboramiz.",
     price_body, active="price",
     jsonld=crumbs_ld([("Bosh sahifa", "/uz/"), ("Narxlar", "/uz/price")]) + faq_ld(PRICE_FAQ))

# ------------------------------------------------------------- kompaniya
company_body = """
<main>
  <nav class="wrap crumbs" aria-label="Yoʻl">
    <a href="/uz/">Bosh sahifa</a><span>/</span><b>Kompaniya haqida</b>
  </nav>

  <div class="wrap intro">
    <div class="intro__body">
      <h1>«Smart Energy Eco Trade» MChJ</h1>
      <p>«Gazpromneft — moylash materiallari»ning Oʻzbekiston Respublikasidagi rasmiy distribyutori. Mamlakat boʻylab sanoat korxonalari, avtoparklar va servis markazlariga moy, plastik moylar va texnik suyuqliklar yetkazib beramiz.</p>
      <p>Ishlab chiqaruvchi zavodlari bilan toʻgʻridan-toʻgʻri ishlaymiz: har bir partiya sifat pasporti bilan keladi, texnik mutaxassislar esa mahsulot tanlashga va import markalardan oʻtishga yordam beradi.</p>
    </div>
    <picture><source type="image/avif" srcset="/img/company-sm.avif 600w, /img/company-md.avif 960w, /img/company.avif 1200w" sizes="(max-width:900px) 100vw, 50vw"><source type="image/webp" srcset="/img/company-sm.webp 600w, /img/company-md.webp 960w, /img/company.webp 1200w" sizes="(max-width:900px) 100vw, 50vw"><img class="intro__media" src="/img/company.webp" alt="Gazpromneft mutaxassislari moy bochkasi yonida" width="1200" height="896" fetchpriority="high" decoding="async"></picture>
  </div>

  <div class="stats">
    <div class="wrap stats__in">
      <div class="stats__item"><div class="stats__num">2023</div><div class="stats__label">yetkazib berish boshlangan yil</div></div>
      <div class="stats__item"><div class="stats__num">600+</div><div class="stats__label">assortiment pozitsiyasi</div></div>
      <div class="stats__item"><div class="stats__num">12 hudud</div><div class="stats__label">yetkazib berish geografiyasi</div></div>
      <div class="stats__item"><div class="stats__num">100%</div><div class="stats__label">rasmiy mahsulot</div></div>
    </div>
  </div>

  <section class="section section--tight">
    <div class="wrap">
      <div class="section__head"><div><h2>Hujjatlar va maqom</h2></div></div>
      <div class="why">
        <div class="why__item"><b>Distribyutorlik maqomi</b><span>«Gazpromneft — moylash materiallari»ning Oʻzbekiston Respublikasidagi rasmiy distribyutori. Xatni soʻrov boʻyicha, jumladan tender uchun beramiz.</span></div>
        <div class="why__item"><b>Muvofiqlik sertifikatlari</b><span>Yetkazilayotgan mahsulotga. Yetkazishga ilova qilamiz yoki kirish nazorati uchun oldindan yuboramiz.</span></div>
        <div class="why__item"><b>Partiyaga sifat pasporti</b><span>Har bir partiya ishlab chiqaruvchi zavodning haqiqiy koʻrsatkichlari bilan sifat pasporti bilan keladi.</span></div>
        <div class="why__item"><b>Yetkazib berish shartnomasi</b><span>Hisob-faktura va tovar-transport hujjatlari bilan shartnoma asosida ishlaymiz.</span></div>
        <div class="why__item"><b>TDS va MSDS hujjatlari</b><span>Texnik tavsiflar va xavfsizlik pasportlari — <a href="/uz/docs" style="color:var(--blue)">hujjatlar boʻlimida</a> yoki soʻrov boʻyicha.</span></div>
        <div class="why__item"><b>Tender uchun paket</b><span>Aniq xarid talabiga qarab majmua yigʻamiz, distribyutorlik xati ham kiradi.</span></div>
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0">
    <div class="wrap">
      <div class="section__head"><div><h2>Bizga ishonishadi</h2></div></div>
      <div class="logos">
        <img src="/img/logo-ngmk.webp" alt="Navoiy kon-metallurgiya kombinati" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-enter.webp" alt="Enter Engineering" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-ttz.webp" alt="V. L. Galperin nomidagi Toshkent quvur zavodi" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-ahangaran.webp" alt="Akhangarancement" width="400" height="400" loading="lazy" decoding="async">
        <img src="/img/logo-cement.webp" alt="Namangan Sement" width="400" height="400" loading="lazy" decoding="async">
      </div>
    </div>
  </section>

  <section class="section section--tight" style="padding-top:0">
    <div class="wrap layout">
      <div class="layout__main">
        <div class="longread" style="padding-top:0">
          <h2>Ishni qanday boshlash kerak</h2>
          <p>Birinchi qadam — texnika roʻyxati yoki hozir sotib olayotgan moylar roʻyxati bilan ariza. Texnik mutaxassis tanlov tayyorlaydi, menejer — mavjudlik bilan narxlar va shartnoma loyihasini. Keyin Toshkentdagi ombordan joʻnatamiz, odatda bir kun ichida.</p>
          <p>Batafsil: <a href="/uz/podbor" style="color:var(--blue);font-weight:600">tanlash qanday oʻtadi</a>, <a href="/uz/dostavka" style="color:var(--blue);font-weight:600">yetkazib berish va toʻlov</a>, <a href="/uz/docs" style="color:var(--blue);font-weight:600">TDS va MSDS hujjatlari</a>.</p>
        </div>
      </div>
      <aside class="layout__aside">
{companyform}
      </aside>
    </div>
  </section>
</main>
"""

page("/uz/company", "company.html", "Kompaniya haqida — Smart Energy Eco Trade",
     "«Smart Energy Eco Trade» MChJ — 2023 yildan Gazpromneft moylash materiallarining Oʻzbekistondagi rasmiy distribyutori. 12 hududga yetkazib beramiz.",
     company_body.format(companyform=leadform("«Kompaniya» sahifasidan ariza (uz)", "Ishni boshlash",
                                              "Nima kerakligini yozing — tanlov va narx bilan qaytamiz.",
                                              "Ariza yuborish", cls=" leadform--aside", anchor="zayavka")),
     active="company", preload="/img/company.webp", preload_sizes="(max-width:900px) 100vw, 50vw",
     jsonld=crumbs_ld([("Bosh sahifa", "/uz/"), ("Kompaniya haqida", "/uz/company")]))

# ------------------------------------------------------------- hujjatlar
DOCS = [
    ("Gazpromneft Hydraulic HLP 46", "Industrial", "02.2026"),
    ("Gazpromneft Reductor CLP 220", "Industrial", "02.2026"),
    ("G-Profi MSI Plus 15W-40", "Motor", "01.2026"),
    ("G-Profi GT 10W-40", "Motor", "01.2026"),
    ("G-Energy Synthetic Active 5W-40", "Motor", "12.2025"),
    ("Gazpromneft Grease L EP 2", "Plastik moylar", "11.2025"),
    ("Gazpromneft Antifreeze SF 40", "Suyuqliklar", "11.2025"),
]
docs_rows = "\n".join("""      <div class="table__row" data-name="{n} {c}">
        <b>{n}</b>
        <span><span class="table__label">Toifa: </span>{c}</span>
        <span><span class="table__label">Yangilangan: </span>{d}</span>
        <div class="table__files table__files--btn"><a href="#zapros">TDS soʻrash</a><a href="#zapros">MSDS soʻrash</a></div>
      </div>""".format(n=n, c=c, d=d) for n, c, d in DOCS)

docs_body = """
<main class="wrap page" style="padding-top:32px">
  <nav class="crumbs" style="padding-top:0" aria-label="Yoʻl">
    <a href="/uz/">Bosh sahifa</a><span>/</span><b>Hujjatlar</b>
  </nav>
  <div class="page__head">
    <h1>TDS va MSDS hujjatlari</h1>
    <p class="page__lead">Gazpromneft, G-Profi va G-Energy mahsulotlariga texnik tavsiflar va xavfsizlik pasportlari. Kerakli hujjat roʻyxatda boʻlmasa — quyida soʻrang, ish kuni davomida yuboramiz.</p>
  </div>

  <div class="search">
    <input id="docsearch" type="search" placeholder="Mahsulot nomi boʻyicha qidirish" aria-label="Mahsulot nomi boʻyicha qidirish" autocomplete="off">
  </div>

  <div class="table table--docs" id="docstable">
    <div class="table__head"><div>Mahsulot</div><div>Toifa</div><div>Yangilangan</div><div>Hujjatlar</div></div>
%s
  </div>
  <p class="table__note" id="docsempty" hidden>Hech narsa topilmadi — hujjatni quyida soʻrang, ish kuni davomida yuboramiz.</p>

  <div class="layout" style="margin-top:40px">
    <div class="longread" style="padding-top:0">
      <h2>Roʻyxatda yoʻq hujjat kerakmi</h2>
      <p>Kutubxona toʻldirib borilmoqda. Kerakli TDS yoki MSDS bu yerda boʻlmasa — mahsulot nomini yozing, faylni ish kuni davomida yuboramiz. Shu bilan birga pozitsiya omborda bor-yoʻqligini va qanday qadoqda ekanini aytamiz.</p>
      <p>Hujjat tender yoki kirish nazorati uchun kerak boʻlsa, buni darhol ayting: toʻliq paket yigʻamiz — partiyaga sifat pasporti, muvofiqlik sertifikati va distribyutorlik xati.</p>
    </div>
%s
  </div>
</main>
""" % (docs_rows, leadform("Hujjat soʻrovi (uz)", "Hujjat soʻrash",
                           "Mahsulot nomini yozing — TDS va MSDS yuboramiz.",
                           "Hujjat soʻrash", cls=" leadform--aside", anchor="zapros"))

page("/uz/docs", "docs.html", "Gazpromneft mahsulotlariga TDS va MSDS hujjatlari",
     "Gazpromneft, G-Profi, G-Energy moy va moylariga texnik tavsiflar (TDS) va xavfsizlik pasportlari (MSDS). Kerakli hujjatni soʻrov boʻyicha yuboramiz.",
     docs_body, active="docs",
     jsonld=crumbs_ld([("Bosh sahifa", "/uz/"), ("Hujjatlar", "/uz/docs")]))

# ------------------------------------------------------------- aloqa
LOCAL_LD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LocalBusiness","name":"Smart Energy Eco Trade — Gazpromneft Oʻzbekiston","url":"https://gpn-oil.uz/uz/contacts","image":"https://gpn-oil.uz/img/og.jpg","telephone":"+998908085972","email":"t.yarulin@s-energy.uz","address":{"@type":"PostalAddress","addressLocality":"Toshkent","addressRegion":"Mirzo Ulugʻbek tumani","postalCode":"100000","addressCountry":"UZ"},"geo":{"@type":"GeoCoordinates","latitude":41.3230571,"longitude":69.312125},"hasMap":"https://yandex.uz/maps/?ll=69.312125%2C41.3230571&z=17","openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"18:00"}],"priceRange":"$$","sameAs":["https://instagram.com/gpn_oil.uz","https://t.me/GPN_OIL_UZ"]}
</script>
"""

contacts_body = """
<main>
  <nav class="wrap crumbs" aria-label="Yoʻl">
    <a href="/uz/">Bosh sahifa</a><span>/</span><b>Aloqa</b>
  </nav>
  <div class="wrap contacts" style="padding-top:12px">
    <div class="contacts__col">
      <h1>Aloqa</h1>
      <h2 style="font-size:19px;font-weight:600;color:var(--muted)">Savdo boʻlimi va texnik mutaxassis</h2>
      <div class="calls">
        <a class="call" href="tel:+998908085972">+998 90 808 59 72<span>Timur Yarullin · korporativ menejer</span></a>
        <a class="call" href="tel:+998935048490">+998 93 504 84 90<span>savdo boʻlimi</span></a>
        <a class="call call--tg" href="{tg}" rel="noopener">Telegram<span>@GPN_OIL_UZ · 15 daqiqada javob</span></a>
      </div>
      <dl class="meta">
        <div class="meta__item"><dt>Pochta</dt><dd><a href="mailto:t.yarulin@s-energy.uz">t.yarulin@s-energy.uz</a></dd></div>
        <div class="meta__item"><dt>Ish vaqti</dt><dd>Du–Ju, 09:00–18:00</dd></div>
        <div class="meta__item"><dt>Manzil</dt><dd>Toshkent, Mirzo Ulugʻbek tumani</dd></div>
        <div class="meta__item"><dt>Kompaniya</dt><dd>«Smart Energy Eco Trade» MChJ</dd></div>
        <div class="meta__item"><dt>Instagram</dt><dd><a href="{insta}" rel="noopener">@gpn_oil.uz</a></dd></div>
      </dl>
    </div>

    <div class="contacts__col">
      <div class="map">
        <picture>
          <source type="image/avif" srcset="/img/map-sm.avif 600w, /img/map.avif 1200w" sizes="(max-width:900px) 100vw, 50vw">
          <source type="image/webp" srcset="/img/map-sm.webp 600w, /img/map.webp 1200w" sizes="(max-width:900px) 100vw, 50vw">
          <img src="/img/map.webp" alt="Smart Energy Eco Trade ofisi Toshkentda xaritada" width="1200" height="600" loading="lazy" decoding="async">
        </picture>
        <div class="map__go">
          <span class="map__hint">Yoʻnalishni ochish:</span>
          <a class="btn btn--outline btn--sm" href="https://yandex.uz/maps/?ll=69.312125%2C41.3230571&amp;z=17&amp;pt=69.312125,41.3230571,pm2rdm" rel="noopener" target="_blank">Yandex Xarita</a>
          <a class="btn btn--outline btn--sm" href="https://www.google.com/maps/search/?api=1&amp;query=41.3230571%2C69.312125" rel="noopener" target="_blank">Google Xarita</a>
          <a class="btn btn--outline btn--sm" href="https://maps.apple.com/?ll=41.3230571,69.312125&amp;q=Smart%20Energy%20Eco%20Trade" rel="noopener" target="_blank">Apple Xarita</a>
        </div>
        <p class="map__attr">&copy; <a href="https://www.openstreetmap.org/copyright" rel="noopener nofollow" target="_blank">OpenStreetMap</a></p>
      </div>

      <div class="asidebox" style="padding:26px">
        <h2 style="font-size:19px">Biz bilan qanday ishlash mumkin</h2>
        <div style="gap:14px;color:var(--muted);font-size:15px;line-height:1.6">
          <span><b style="color:var(--ink)">1. Ariza.</b> Qoʻngʻiroq qiling yoki formani toʻldiring — texnikani yoki kerakli pozitsiyalarni yozing.</span>
          <span><b style="color:var(--ink)">2. Tanlov va hisob.</b> Texnik mutaxassis tanlov, menejer — mavjudlik bilan narxlar va shartnoma tayyorlaydi.</span>
          <span><b style="color:var(--ink)">3. Joʻnatish.</b> Toshkentdagi ombordan, odatda bir kun ichida. Oʻzbekiston boʻylab yetkazish yoki oʻzi olib ketish.</span>
        </div>
      </div>

      <form class="form" id="zayavka" method="post" action="https://gpn-relay.zvezdotank.workers.dev/">
        <b>Ariza qoldirish</b>
        <input class="trap" type="text" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true">
        <input type="hidden" name="_form" value="Aloqa sahifasidan ariza (uz)">
        <input type="hidden" name="_next" value="uz">
        <div class="form__fields">
          <label class="field"><span>Ism</span><input name="name" autocomplete="name"></label>
          <label class="field"><span>Telefon</span><input name="phone" type="tel" placeholder="+998" autocomplete="tel" required></label>
          <label class="field"><span>Nimani tanlash kerak yoki qancha hajm kerak</span><textarea name="task" rows="3"></textarea></label>
        </div>
        <button type="submit">Ariza yuborish</button>
        <small>Ariza darhol menejerga tushadi, ish vaqtida javob beramiz.</small>
      </form>
    </div>
  </div>
</main>
""".format(tg=TG, insta=INSTA)

page("/uz/contacts", "contacts.html", "Aloqa — Gazpromneft Oʻzbekiston, Smart Energy Eco Trade",
     "Korporativ menejer va savdo boʻlimi telefonlari, Telegram, pochta va ariza formasi. Toshkent, Du–Ju 09:00 dan 18:00 gacha.",
     contacts_body, active="contacts",
     jsonld=LOCAL_LD + crumbs_ld([("Bosh sahifa", "/uz/"), ("Aloqa", "/uz/contacts")]))

# ------------------------------------------------------------- xizmat sahifalari
page("/uz/spasibo", "spasibo.html", "Ariza yuborildi — Gazpromneft Oʻzbekiston",
     "Ariza qabul qilindi, menejer ish vaqtida bogʻlanadi.", """
<main class="wrap note">
  <h1>Rahmat, arizani qabul qildik</h1>
  <p>Menejer roʻyxatni koʻrib chiqadi va ish vaqtida javob beradi — Du–Ju 09:00 dan 18:00 gacha. Savol shoshilinch boʻlsa, qoʻngʻiroq qiling — darhol javob beramiz.</p>
  <div class="empty__actions">
    <a class="btn btn--blue" href="tel:+998908085972">+998 90 808 59 72</a>
    <a class="btn btn--outline" href="/uz/">Bosh sahifaga qaytish</a>
  </div>
</main>
""", noindex=True)

page("/uz/oshibka", "oshibka.html", "Ariza yuborilmadi — Gazpromneft Oʻzbekiston",
     "Forma arizani yubora olmadi. Biz bilan bevosita bogʻlaning.", """
<main class="wrap note">
  <h1>Ariza yuborilmadi</h1>
  <p>Bizning tomonda nimadir ishlamay qoldi va forma arizani uzata olmadi. Vaqt yoʻqotmaslik uchun qoʻngʻiroq qiling — darhol javob beramiz.</p>
  <div class="empty__actions">
    <a class="btn btn--blue" href="tel:+998908085972">+998 90 808 59 72</a>
    <a class="btn btn--outline" href="tel:+998935048490">+998 93 504 84 90</a>
  </div>
</main>
""", noindex=True)

print("uz: sahifalar tayyor")
