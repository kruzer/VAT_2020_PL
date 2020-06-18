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

Z repozytorium można pobrać gotowy plik VAT2020.csv, albo sklonować całe repozytorium, dodać kolejne pliki do katalogu sources i uruchomić skrypt:
```
./generuj.sh
```
co stworzy plik VAT2020.csv, który można zaimportować do swojego systemu.
Jeśli w źródłach znajdują się te same kody z różnymi stawkami, to pozycje te można podejrzeć komendą:
```
./pokaz_bledy.sh
```
## Źródła danych
Dane pochodzą z plików udostępnionych w różnych miejscach (np. http://www.symplex.eu/?q=node/465) i nadsyłanych przez użytkowników
Jeśli masz zweryfikowane dane zawierające nowe stawki dla kodów EAN możesz je przesłać mailem na lnt @ 3lance.pl albo zrobić pull request.
## Zastrzeżenia
Zebrane tutaj stawki pochodzą z różnych źródeł i mogą zawierać błędy, możesz z nich korzystać tylko na własną odpowiedzialność
