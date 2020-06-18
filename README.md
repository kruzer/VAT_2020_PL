# Tabela - baza danych nowych stawek VAT 2020 

Repozytorium gromadzi pliki z różnych źródeł zawierające powiązanie kodów kreskowych z nowymi stawkami VAT

## Jak to działa
Pliki csv mają 2 istotne kolumny rozdzielone przecinkiem:
* pierwsza zawiera kod EAN, 
* a druga nową stawkę, 

Stawki VAT mogą przybrać wartości:
* 5%
* 8%
* 23%

Pliki źródłowe csv znajdują się w katalogu sources. Po ich aktualizacji można wygenerować jeden zbiorczy plik, którzy będzie się charakeryzował tym, że:
* nie będzie zawierał duplikatów
* będzie zawierał tylko kody EAN z poprawną sumą kontrolną (https://www.gs1.org/services/how-calculate-check-digit-manually) GTIN-8 GTIN-12 GTIN-13 GTIN-14
* nie będzie zawierał kodów, dla których podano różne wartości VAT
