/* Весь скрипт сайта: мобильное меню, окно менеджера, поиск по документам.
   Один файл с defer — на отрисовку первого экрана не влияет. */

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

      fetch(form.action, { method: 'POST', body: new FormData(form), mode: 'cors' })
        .then(function (r) {
          if (!r.ok && r.type !== 'opaque') throw new Error('bad status');
          // приёмник сам уводит на страницу «спасибо»
          window.location.href = (UZ ? '/uz/spasibo' : '/spasibo');
        })
        .catch(function () {
          notice(form, TEXT.fail + ' <a href="' + TEL_HREF + '">' + TEL +
                 '</a> · <a href="' + TG + '" rel="noopener">Telegram</a>', false);
          if (btn) { btn.disabled = false; btn.textContent = label; }
        });
    });
  });
})();
