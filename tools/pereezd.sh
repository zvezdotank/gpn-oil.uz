#!/bin/bash
# Проверка переезда gpn-oil.uz на GitHub Pages.
#
# Работает в сетях, где подменяют DNS (отельный вайфай, публичные точки).
# Обычный порт 53 не используется вообще: адреса спрашиваются через DoH
# по HTTPS, сертификат проверяется прямым TLS-соединением. И то и другое
# защищено шифрованием, местная сеть подделать ответ не может.
#
# Запуск:  bash tools/pereezd.sh
#          bash tools/pereezd.sh -w    следить, проверка каждые 5 минут

OLD_IP=176.57.64.226
NEW_IPS="185.199.108.153 185.199.109.153 185.199.110.153 185.199.111.153"
FIRST_IP=185.199.108.153

check() {
  echo "──────────────────────────────────────────────────────────"
  echo "  gpn-oil.uz — $(date '+%d.%m.%Y %H:%M:%S')"
  echo "──────────────────────────────────────────────────────────"
  echo
  echo "АДРЕСА ДОМЕНА (через HTTPS, подмена невозможна)"

  n_new=0; n_old=0; n_quiet=0

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
      printf "  %-11s СТАРЫЙ сайт   %-19s TTL %s\n" "$name" "$ips" "$ttl"
      n_old=$((n_old+1))
    elif echo "$ips" | grep -q '185\.199\.1'; then
      printf "  %-11s новый сайт    %-19s TTL %s\n" "$name" "185.199.108-111.153" "$ttl"
      n_new=$((n_new+1))
    else
      printf "  %-11s непонятно     %-19s TTL %s\n" "$name" "$ips" "$ttl"
      n_old=$((n_old+1))
    fi
  done

  echo
  echo "СЕРТИФИКАТ (прямое TLS-соединение с GitHub)"

  n_cert=0
  for ip in $NEW_IPS; do
    cn=$(echo | openssl s_client -connect "$ip:443" -servername gpn-oil.uz 2>/dev/null \
         | openssl x509 -noout -subject 2>/dev/null | sed 's/.*CN *= *//')
    if [ -z "$cn" ]; then
      printf "  %-17s нет ответа\n" "$ip"
    elif echo "$cn" | grep -q 'gpn-oil\.uz'; then
      printf "  %-17s ВЫПУЩЕН на gpn-oil.uz\n" "$ip"; n_cert=$((n_cert+1))
    else
      printf "  %-17s пока общий (%s)\n" "$ip" "$cn"
    fi
  done

  echo
  echo "САЙТ НА GITHUB (в обход DNS, по адресу напрямую)"
  code=$(curl -sk -o /dev/null --max-time 20 -w '%{http_code}' \
         --resolve "gpn-oil.uz:443:$FIRST_IP" https://gpn-oil.uz/ 2>/dev/null)
  if [ "$code" = "200" ]; then
    echo "  главная отдаётся, код 200"
  else
    echo "  ВНИМАНИЕ: код $code — сайт на GitHub не отдаётся"
  fi

  echo
  echo "──────────────────────────────────────────────────────────"

  if [ "$n_new" -gt 0 ] && [ "$n_old" -eq 0 ] && [ "$n_cert" -gt 0 ]; then
    echo "  ПЕРЕЕЗД ЗАВЕРШЁН."
    echo
    echo "  Осталось одно действие руками: на GitHub в Settings → Pages"
    echo "  поставить галочку Enforce HTTPS. После неё всё."
  elif [ "$n_new" -gt 0 ] && [ "$n_old" -eq 0 ]; then
    echo "  Адреса разошлись везде, ждём сертификат."
    echo
    echo "  GitHub выпускает его сам, обычно за минуты. Если через час"
    echo "  сертификат всё ещё общий — на GitHub в Settings → Pages"
    echo "  сотрите значение в поле Custom domain, впишите gpn-oil.uz"
    echo "  заново и сохраните. Это запускает проверку принудительно."
  elif [ "$n_new" -gt 0 ] && [ "$n_old" -gt 0 ]; then
    echo "  РАСКОЛ СЕРВЕРОВ ЖИВ: часть мира видит новый сайт, часть старый."
    echo
    echo "  Само не лечится — ns3 и ns4 у Billur держат отдельный файл зоны"
    echo "  и не забирают правки. Сертификат GitHub тоже не выпустит, пока"
    echo "  так. Что делать — в файле tools/pismo-billur.txt"
  elif [ "$n_old" -gt 0 ] && [ "$n_new" -eq 0 ]; then
    echo "  Пока все видят старый сайт. Если правку в панели вы только что"
    echo "  сохранили — это нормально, подождите час."
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
