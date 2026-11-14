# Trener Lambdina

Aplikacja do nauki hebrajszczyzny biblijnej według podręcznika T. O. Lambdina
(*Wprowadzenie do hebrajszczyzny biblijnej*, wyd. polskie). Trzy poziomy do wyboru:

| Poziom | Lekcje | Zawartość | Tryby |
|---|---|---|---|
| I | 1–24 | 308 słów z pełną wokalizacją | Fiszki · Quiz · Zdania · Frazy · Lista |
| II | 25–37 | 405 form do rozbioru, słownik, paradygmaty | Rozbiór (fiszka / quiz) · Słownik · Paradygmaty · Lista |
| III | 38–55 | 357 form do rozbioru, słownik, paradygmaty | Rozbiór (fiszka / quiz) · Słownik · Paradygmaty · Lista |

## Jak używać

Cała aplikacja to jeden plik: **`index.html`**. Wystarczy go pobrać i otworzyć w przeglądarce
(komputer lub telefon). Nie wymaga instalacji ani internetu — czcionki hebrajskie są wbudowane.

- **Postęp** („umiem", statystyki quizów) zapisuje się w przeglądarce, w której aplikacja jest otwarta.
  Na innym urządzeniu lub w innej przeglądarce licznik jest osobny.
- **Przenoszenie postępu:** na stronie wyboru poziomu są przyciski *Zapisz postęp do pliku*
  i *Wczytaj postęp z pliku*.
- **Quiz** to sesje po 10, 20 lub 30 pytań z podsumowaniem: wynik, lista błędów do powtórki,
  procent opanowanego materiału.
- **Zgłaszanie błędów:** przycisk *⚑ Zgłoś błąd* tworzy gotowe zgłoszenie z miejscem,
  w którym jest użytkownik (poziom, tryb, hasło na ekranie).

## Ustawienia zgłoszeń

W `src/shell.html` jest blok `CONFIG`:

```js
const CONFIG = {
  reportEmail: "",      // adres, na który mają trafiać zgłoszenia (pusty = sam przycisk „Skopiuj zgłoszenie")
  reportFormUrl: "",    // link do formularza Google (opcjonalnie)
  formFields: { what: "", desc: "", contact: "", context: "" },  // identyfikatory pól entry.XXXX
  ...
};
```

Po zmianie trzeba złożyć plik od nowa (niżej).

## Budowa repozytorium

```
index.html                       gotowa aplikacja (powstaje z build.py)
build.py                         składa index.html z części w src/
src/shell.html                   powłoka: strona tytułowa, wybór poziomu, zapis postępu, zgłoszenia
src/fonts.css                    czcionki wbudowane (Frank Ruhl Libre, Spectral, Inter)
src/poziom1_lekcje_1-24.html     trener podstawowy
src/poziom2_lekcje_25-37.html    trener zaawansowany
src/poziom3_lekcje_38-55.html    trener zaawansowany
```

Po każdej zmianie w `src/`:

```
python3 build.py
```

Skrypt nie potrzebuje żadnych dodatkowych bibliotek.

## Źródła i prawa

Słownictwo, formy i ćwiczenia pochodzą z polskiego wydania podręcznika Lambdina; tłumaczenia zdań
w trybie *Zdania* sporządzono pomocniczo. Materiał służy do nauki własnej. Czcionki: Frank Ruhl Libre,
Spectral i Inter (licencja SIL Open Font License).
