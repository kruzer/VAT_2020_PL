#!/bin/sh
export LC_ALL=C
echo "Tworzenie wspólnej bazy"
cat sources/*.csv | tr -d '\r' | sort -n | uniq | ./ean_checksum.py > wszystkie.csv
wc wszystkie.csv
echo "Podsumowanie rozbieżności"
./duble.py < wszystkie.csv > rozbieznosci.csv
wc rozbieznosci.csv
echo "Pomijanie rozbieżnych wartości"
grep -v -x -f  rozbieznosci.csv wszystkie.csv > VAT2020.csv
wc VAT2020.csv
