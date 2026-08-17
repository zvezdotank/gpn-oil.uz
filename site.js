/* Весь скрипт сайта: мобильное меню, окно менеджера, поиск по документам,
   аналитика. Один файл с defer — на отрисовку первого экрана не влияет. */

/* ---------- Аналитика: загрузка счётчика ----------
   Библиотека gtag.js весит больше, чем весь остальной сайт вместе с
   картинками, и в критическом пути ей делать нечего. Очередь dataLayer
   заведена инлайном в <head>, поэтому всё, что случилось до загрузки
   библиотеки, не теряется — она разберёт очередь сама, включая просмотр
   страницы с правильным адресом и источником перехода.

   Грузим по первому из двух событий: человек что-то сделал или страница
   догрузилась. Сайт грузится быстрее секунды, так что счётчик почти всегда
   успевает; при этом на скорость отрисовки он не влияет вообще. */
(function () {
  var ID = 'G-4VH1EV5FQB';
  var done = false;

  function load() {
    if (done) return;
    done = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ID;
    document.head.appendChild(s);
  }

  ['pointerdown', 'keydown', 'touchstart', 'scroll'].forEach(function (t) {
    window.addEventListener(t, load, { once: true, passive: true });
  });
  if (document.readyState === 'complete') setTimeout(load, 0);
  else window.addEventListener('load', function () { setTimeout(load, 0); });
})();

/* ---------- Аналитика: целевые действия ----------
   Считаем то, ради чего сайт существует: звонок, телеграм, отправленную
   заявку. Ключевые события в GA4 — phone_click, telegram_click,
   generate_lead. К каждому идёт параметр place: без него видно «было
   40 звонков», но не видно, откуда именно звонят — из шапки, из окна
   менеджера или из подвала, — а это ровно то, что нужно, чтобы решать,
   что усиливать. */
(function () {
  window.gpnTrack = function (name, params) {
    try { window.gtag('event', name, params || {}); } catch (e) {}
  };

  function place(el) {
    if (el.closest('.mgr')) return 'Окно менеджера';
    if (el.closest('.formnote')) return 'Сбой формы';
    if (el.closest('.topbar')) return 'Верхняя полоса';
    if (el.closest('.masthead')) return 'Шапка';
    if (el.closest('.hero')) return 'Первый экран';
    if (el.closest('.cta')) return 'Полоса «нужен расчёт»';
    if (el.closest('.footer')) return 'Подвал';
    if (el.closest('.findus')) return 'Блок контактов';
    return 'Тело страницы';
  }
  window.gpnPlace = place;

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var p = { place: place(a) };

    if (href.indexOf('tel:') === 0) {
      p.number = href.slice(4);
      window.gpnTrack('phone_click', p);
    } else if (href.indexOf('mailto:') === 0) {
      window.gpnTrack('email_click', p);
    } else if (href.indexOf('t.me/') !== -1) {
      window.gpnTrack('telegram_click', p);
    } else if (href.indexOf('instagram.com') !== -1) {
      window.gpnTrack('instagram_click', p);
    } else if (href.indexOf('yandex.') !== -1) {
      window.gpnTrack('map_click', p);
    } else if (a.classList.contains('lang__off')) {
      // на какой язык ушли и с какой страницы: если узбекскую версию
      // включают часто — её стоит развивать, если почти никогда — нет
      window.gpnTrack('lang_switch', {
        lang_to: (a.getAttribute('lang') || '').toUpperCase(),
        from_page: location.pathname
      });
    }
  }, true);

  // Начатая, но брошенная форма — отдельный сигнал: если form_start сильно
  // больше generate_lead, дело не в трафике, а в самой форме.
  var started = [];
  document.addEventListener('focusin', function (e) {
    var form = e.target.closest && e.target.closest('.leadform, .form');
    if (!form || started.indexOf(form) !== -1) return;
    started.push(form);
    var src = form.querySelector('[name="_form"]');
    window.gpnTrack('form_start', { form_name: src ? src.value : 'Форма' });
  });
})();

/* ---------- Мобильное меню ----------
   Кнопка рисуется только здесь: без скрипта раскрыть список нечем,
   а показывать нерабочую кнопку хуже, чем не показывать. */
(function () {
  var burger = document.querySelector('.burger');
  var nav = document.getElementById('nav');
  if (!burger || !nav) return;

  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Клик по пункту закрывает меню: якорные ссылки иначе прокручивают
  // страницу под раскрытым списком.
  nav.addEventListener('click', function (e) {
    if (e.target.closest('a')) {
      nav.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });
})();

/* ---------- Плавающее окно менеджера ----------
   Само не разворачивается и не выпрыгивает по таймеру: посетитель открывает
   его, когда готов. Крестик не прячет окно совсем, а сворачивает в кружок
   с фотографией: канал связи не должен пропадать без возможности вернуть. */
(function () {
  var box = document.getElementById('mgr');
  if (!box) return;
  var toggle = document.getElementById('mgrToggle');
  var close = document.getElementById('mgrClose');

  var store = {
    get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };

  if (store.get('mgrMin') === '1') box.classList.add('is-min');

  toggle.addEventListener('click', function () {
    // из свёрнутого состояния первый клик разворачивает обратно в визитку
    if (box.classList.contains('is-min')) {
      box.classList.remove('is-min');
      store.set('mgrMin', '0');
      return;
    }
    var open = box.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open && window.gpnTrack) window.gpnTrack('manager_open', {});
  });

  close.addEventListener('click', function () {
    box.classList.remove('is-open');
    box.classList.add('is-min');
    toggle.setAttribute('aria-expanded', 'false');
    store.set('mgrMin', '1');
  });

  // Esc сворачивает раскрытое окно, но не прячет его совсем.
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && box.classList.contains('is-open')) {
      box.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.focus();
    }
  });

  // Пока человек заполняет форму, окно уезжает: оно висит ровно над кнопкой
  // отправки и в этот момент только мешает. Когда форма уходит из виду —
  // возвращается. Считаем именно видимые формы, а не сальдо событий:
  // первый вызов наблюдателя приходит сразу на все цели и увёл бы счётчик
  // в минус.
  var forms = document.querySelectorAll('.leadform, .form');
  if (forms.length && 'IntersectionObserver' in window) {
    var seen = [];
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var i = seen.indexOf(e.target);
        if (e.isIntersecting && i === -1) seen.push(e.target);
        if (!e.isIntersecting && i !== -1) seen.splice(i, 1);
      });
      box.classList.toggle('is-away', seen.length > 0);
    }, { threshold: 0.35 });
    Array.prototype.forEach.call(forms, function (f) { io.observe(f); });
  }
})();

/* ---------- Поиск по таблице документов ----------
   Список короткий и целиком лежит в разметке, поэтому фильтруем на месте. */
(function () {
  var input = document.getElementById('docsearch');
  var table = document.getElementById('docstable');
  var empty = document.getElementById('docsempty');
  if (!input || !table) return;

  var rows = Array.prototype.slice.call(table.querySelectorAll('.table__row'));

  input.addEventListener('input', function () {
    var q = input.value.trim().toLowerCase();
    var shown = 0;
    rows.forEach(function (row) {
      var hit = !q || (row.getAttribute('data-name') || row.textContent).toLowerCase().indexOf(q) !== -1;
      row.hidden = !hit;
      if (hit) shown++;
    });
    if (empty) empty.hidden = shown !== 0;
  });
})();

/* ---------- Вопрос-ответ ----------
   Открытым остаётся только один вопрос. Свежие браузеры делают это сами
   по атрибуту name у <details>, здесь — подстраховка для остальных. */
(function () {
  var items = document.querySelectorAll('.faq details');
  if (items.length < 2) return;
  // если браузер понимает name у details, он уже всё сделал
  if ('name' in document.createElement('details')) return;

  Array.prototype.forEach.call(items, function (d) {
    d.addEventListener('toggle', function () {
      if (!d.open) return;
      Array.prototype.forEach.call(items, function (other) {
        if (other !== d) other.open = false;
      });
    });
  });
})();

/* ---------- Отправка форм ----------
   Обычный POST при недоступном приёмнике показывает человеку ошибку браузера,
   и заявка просто теряется. Отправляем сами и, если не дошло, показываем
   телефон и телеграм прямо в форме — контакт не должен пропадать из-за того,
   что у нас что-то не работает. */
(function () {
  var forms = document.querySelectorAll('.leadform, .form');
  if (!forms.length || !window.fetch) return;

  var TEL = '+998 90 808 59 72';
  var TEL_HREF = 'tel:+998908085972';
  var TG = 'https://t.me/GPN_OIL_UZ';
  var UZ = document.documentElement.lang === 'uz';

  var TEXT = UZ ? {
    sending: 'Yuborilmoqda…',
    fail: 'Ariza yuborilmadi — bizning tomonda nosozlik. Iltimos, qoʻngʻiroq qiling yoki Telegramga yozing, darhol javob beramiz.',
    done: 'Rahmat, arizani qabul qildik. Ish vaqtida javob beramiz.'
  } : {
    sending: 'Отправляем…',
    fail: 'Заявка не ушла — сбой на нашей стороне. Позвоните или напишите в Telegram, ответим сразу.',
    done: 'Спасибо, заявку приняли. Ответим в рабочее время.'
  };

  function notice(form, html, ok) {
    var box = form.querySelector('.formnote');
    if (!box) {
      box = document.createElement('p');
      box.className = 'formnote';
      form.appendChild(box);
    }
    box.className = 'formnote' + (ok ? ' formnote--ok' : ' formnote--fail');
    box.innerHTML = html;
  }

  Array.prototype.forEach.call(forms, function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type=submit], button');
      var label = btn ? btn.textContent : '';
      if (btn) { btn.disabled = true; btn.textContent = TEXT.sending; }

      var src = form.querySelector('[name="_form"]');
      var need = form.querySelector('[name="need"]');
      var about = {
        form_name: src ? src.value : 'Форма',
        product: need ? need.value : ''
      };

      fetch(form.action, { method: 'POST', body: new FormData(form), mode: 'cors' })
        .then(function (r) {
          if (!r.ok && r.type !== 'opaque') throw new Error('bad status');
          // приёмник сам уводит на страницу «спасибо». Уходим не сразу:
          // сначала даём счётчику отправить заявку, иначе переход обрывает
          // запрос и половина конверсий не доезжает. Ждём максимум 900 мс —
          // человека нельзя держать из-за аналитики.
          var gone = false;
          var go = function () {
            if (gone) return;
            gone = true;
            window.location.href = (UZ ? '/uz/spasibo' : '/spasibo');
          };
          if (window.gpnTrack) {
            about.event_callback = go;
            window.gpnTrack('generate_lead', about);
            setTimeout(go, 900);
          } else {
            go();
          }
        })
        .catch(function () {
          if (window.gpnTrack) window.gpnTrack('form_error', about);
          notice(form, TEXT.fail + ' <a href="' + TEL_HREF + '">' + TEL +
                 '</a> · <a href="' + TG + '" rel="noopener">Telegram</a>', false);
          if (btn) { btn.disabled = false; btn.textContent = label; }
        });
    });
  });
})();
