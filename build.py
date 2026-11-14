#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Składa index.html — jeden samowystarczalny plik aplikacji — z części w katalogu src/.

    python3 build.py

src/shell.html                  powłoka: strona tytułowa, wybór poziomu, zapis postępu, zgłoszenia
src/fonts.css                   czcionki wbudowane (woff2 w base64), dzięki nim aplikacja działa offline
src/poziom1_lekcje_1-24.html    trener podstawowy
src/poziom2_lekcje_25-37.html   trener zaawansowany
src/poziom3_lekcje_38-55.html   trener zaawansowany
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
LEVELS = {
    "l1": "poziom1_lekcje_1-24.html",
    "l2": "poziom2_lekcje_25-37.html",
    "l3": "poziom3_lekcje_38-55.html",
}

shell = (SRC / "shell.html").read_text(encoding="utf-8")
fonts = (SRC / "fonts.css").read_text(encoding="utf-8")

# trenery wchodzą do pliku jako base64 — chroni to znaki hebrajskie i znaczniki przed uszkodzeniem
blobs = ",\n    ".join(
    '%s: "%s"' % (key, base64.b64encode((SRC / name).read_bytes()).decode("ascii"))
    for key, name in LEVELS.items()
)

for marker in ("/*FONTS*/", "/*B64*/"):
    assert shell.count(marker) == 1, "brak znacznika %s w src/shell.html" % marker

out = shell.replace("/*FONTS*/", fonts).replace("/*B64*/", "\n    " + blobs + "\n  ")
(ROOT / "index.html").write_text(out, encoding="utf-8")
print("index.html: %.2f MB" % ((ROOT / "index.html").stat().st_size / 1024 / 1024))
