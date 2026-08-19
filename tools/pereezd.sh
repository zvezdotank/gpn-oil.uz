#!/bin/bash
# Проверка состояния сайта gpn-oil.uz.
#
# Переезд закончен 18.08.2026: домен делегирован на Cloudflare, записи
# проксируются, сертификат выдаёт Cloudflare (Universal SSL), источник —
# GitHub Pages. Сертификат самого GitHub не используется и не появится:
# их проверка домена не проходила, от неё отказались сознательно.
#
# Работает в сетях, где подменяют DNS (отельный вайфай, публичные точки).
# Обычный порт 53 не используется вообще: адреса спрашиваются через DoH
# по HTTPS, сертификат проверяется прямым TLS-соединением. И то и другое
# защищено шифрованием, местная сеть подделать ответ не может.
#
# Запуск:  bash tools/pereezd.sh
#          bash tools/pereezd.sh -w    следить, проверка каждые 5 минут

OLD_IP=176.57.64.226                  # прежний хостинг Tilda
GH_IPS="185.199.108.153 185.199.109.153 185.199.110.153 185.199.111.153"
ORIGIN=185.199.108.153               # GitHub Pages, источник за Cloudflare

check() {
  echo "──────────────────────────────────────────────────────────"
  echo "  gpn-oil.uz — $(date '+%d.%m.%Y %H:%M:%S')"
  echo "──────────────────────────────────────────────────────────"
  echo
  echo "АДРЕСА ДОМЕНА (через HTTPS, подмена невозможна)"

  n_new=0; n_old=0; n_quiet=0; n_bare=0

  for pair in "Google|https://dns.google/resolve" \
              "Cloudflare|https://cloudflare-dns.com/dns-query" \
              "AdGuard|https://dns.adguard-dns.com/resolve" \
              "dns.sb|https://doh.sb/dns-query"; do
    name="${pair%%|*}"; url="${pair##*|}"
    answer=$(curl -s --max-time 12 -H 'accept: application/dns-json' \
             "$url?name=gpn-oil.uz&type=A" 2>/dev/null | python3 -c '
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(1)
a = [x for x in d.get("Answer", []) if x.get("type") == 1]
if not a:
    sys.exit(1)
print(",".join(sorted(x["data"] for x in a)), min(x["TTL"] for x in a))
' 2>/dev/null)

    if [ -z "$answer" ]; then
      printf "  %-11s не ответил\n" "$name"; n_quiet=$((n_quiet+1)); continue
    fi

    ips="${answer%% *}"; ttl="${answer##* }"

    if [ "$ips" = "$OLD_IP" ]; then
      printf "  %-11s СТАРЫЙ Tilda      %-21s TTL %s\n" "$name" "$ips" "$ttl"
      n_old=$((n_old+1))
    elif echo "$ips" | grep -qE '^(104\.|172\.6)'; then
      printf "  %-11s через Cloudflare  %-21s TTL %s\n" "$name" "$ips" "$ttl"
      n_new=$((n_new+1))
    elif echo "$ips" | grep -q '185\.199\.1'; then
      printf "  %-11s GitHub напрямую   %-21s TTL %s\n" "$name" "185.199.108-111.153" "$ttl"
      n_bare=$((n_bare+1))
    else
      printf "  %-11s непонятно         %-21s TTL %s\n" "$name" "$ips" "$ttl"
      n_old=$((n_old+1))
    fi
  done

  echo
  echo "СЕРТИФИКАТ (то, что видит браузер)"

  n_cert=0
  cn=$(echo | openssl s_client -connect gpn-oil.uz:443 -servername gpn-oil.uz 2>/dev/null \
       | openssl x509 -noout -subject 2>/dev/null | sed 's/.*CN *= *//')
  vr=$(curl -s -o /dev/null --max-time 20 https://gpn-oil.uz/ -w '%{ssl_verify_result}' 2>/dev/null)
  if [ "$vr" = "0" ] && echo "$cn" | grep -q 'gpn-oil\.uz'; then
    printf "  выписан на %s, цепочка проверена\n" "$cn"; n_cert=1
  elif [ -n "$cn" ]; then
    printf "  ВНИМАНИЕ: %s, проверка цепочки вернула %s\n" "$cn" "$vr"
  else
    printf "  нет ответа\n"
  fi

  echo
  echo "ПЕРЕВОД С HTTP НА HTTPS"
  code=$(curl -sI --max-time 20 http://gpn-oil.uz/ 2>/dev/null | head -1 | awk '{print $2}')
  if [ "$code" = "301" ] || [ "$code" = "308" ]; then
    echo "  есть, код $code"
  else
    echo "  ВНИМАНИЕ: http отдал $code — проверьте Always Use HTTPS в Cloudflare"
  fi

  echo
  echo "ИСТОЧНИК НА GITHUB (в обход Cloudflare, по адресу напрямую)"
  code=$(curl -sk -o /dev/null --max-time 20 -w '%{http_code}' \
         --resolve "gpn-oil.uz:443:$ORIGIN" https://gpn-oil.uz/ 2>/dev/null)
  if [ "$code" = "200" ]; then
    echo "  главная отдаётся, код 200"
  else
    echo "  ВНИМАНИЕ: код $code — сайт на GitHub не отдаётся"
  fi

  echo
  echo "──────────────────────────────────────────────────────────"

  if [ "$n_new" -gt 0 ] && [ "$n_old" -eq 0 ] && [ "$n_bare" -eq 0 ] && [ "$n_cert" -gt 0 ]; then
    echo "  ВСЁ В ПОРЯДКЕ. Домен идёт через Cloudflare, сертификат рабочий."
  elif [ "$n_bare" -gt 0 ]; then
    echo "  ВНИМАНИЕ: домен указывает на GitHub напрямую, минуя Cloudflare."
    echo
    echo "  Значит проксирование выключено — в панели Cloudflare, DNS →"
    echo "  Records, тучки у записей A, AAAA и www стали серыми. Пока так,"
    echo "  сертификата на домен нет: GitHub отдаёт общий *.github.io."
    echo "  Включите оранжевые тучки."
  elif [ "$n_old" -gt 0 ] && [ "$n_new" -gt 0 ]; then
    echo "  РАСХОЖДЕНИЕ: часть мира видит старый сайт на Tilda."
    echo
    echo "  Проверьте делегирование: whois gpn-oil.uz | grep 'Name Server'"
    echo "  Должны быть alexa.ns.cloudflare.com и colin.ns.cloudflare.com."
  elif [ "$n_old" -gt 0 ] && [ "$n_new" -eq 0 ]; then
    echo "  Все видят старый сайт на Tilda. Домен ушёл с Cloudflare —"
    echo "  проверьте name-серверы в панели Billur."
  elif [ "$n_new" -gt 0 ] && [ "$n_cert" -eq 0 ]; then
    echo "  Адреса правильные, но с сертификатом беда — смотрите строку выше."
    echo "  В Cloudflare: SSL/TLS → Overview, режим должен быть Full."
  else
    echo "  Ничего не ответило. Похоже, нет интернета вообще."
  fi
  echo "──────────────────────────────────────────────────────────"
}

if [ "$1" = "-w" ]; then
  while true; do
    clear; check; echo; echo "  Следующая проверка через 5 минут. Ctrl+C — выйти."
    sleep 300
  done
else
  check
fi
