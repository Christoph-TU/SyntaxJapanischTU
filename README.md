# Japanisches Mini Wörterbuch

Dieses Wörterbuch sammelt häufig genutzte Wörter und Satzfragmente, die oftmals in Hiragana notiert werden. Es beinhaltet außerdem alle Partikel, um einen umfassenden Überblick zu bieten, welche Satzfunktionen sie jeweils einnehmen könnten.

Eine fertig kompilierte PDF-Datei findet sich unter 'dictionary_output.pdf', falls man nur am Inhalt interessiert ist.

Alle Angaben ohne Gewähr.

## Struktur

Die eigentlichen Wörter befinden sich in der Datei `entries.json`, welche die wichtigste Datei dieses Projekts ist. Das Python-Skript `generate_dictionary.py` erzeugt in Verbindung mit der LaTeX-Vorlage `template.tex` ein TeX-Dokument, welches anschließend zu einem PDF kompiliert wird.

## Overleaf
Es ist auch möglich das Wörterbuch komplett auf Overleaf zu berabeiten. Einfach die `entries.json`, `overleaf-main.tex` und `overleaf-python.py` in ein Overleaf Project hineinkopieren und dann Recompile drücken.

### Vorteile
* Falls man sich technisch nicht gut auskennt, ist es einfacher die Einträge zu bearbeiten oder das Pdf Dokument zu verändern.
* Funktioniert universal, da nur ein Webbrowser notwendig ist
  
### Nachteile
* Entries Einträge werden nur beim ausgeben sortiert, die eigentliche Liste bleibt gleich.
* Hiragana wird nicht automatisch generiert.

## Entries

Die Einträge sind im JSON-Format angegeben und können folgende Felder enthalten:

```json
  {
    "name": "",
    "hiragana": "",
    "type": "",
    "code": "",
    "kanji": "",
    "translation": "",
    "chapter": "",
    "misc": ""
  }
```

Alle Felder sind optional. Das Skript erzeugt automatisch Hiragana passend zum Namen, wenn es ausgeführt wird. Zudem werden dabei alle Einträge alphabetisch geordnet. Dabei wird allerdings die alte Liste überschrieben. Daher ist es wichtig, die Datei zuerst zu speichern, bevor das Skript ausgeführt wird, da sonst ungespeicherte Einträgen gelöscht werden könnten.

Hier ist ein Beispiel für einen Eintrag:
```json
  {
    "name": "desu",
    "hiragana": "です",
    "type": "Kop",
    "translation": "Polite form",
    "chapter": "G04",
    "misc": "A wa B desu: A ist b"
  }
```

## Fehlerkorrekturen und neue Einträge

Am besten währe es einen Pull Request zu erstellen, um Fehler zu korrigieren oder neue Einträge hinzuzufügen. Bitte aber zuerst immer das Python-Skript ausführen, um sicherzustellen, dass die Einträge geordnet sind.

Sollte dies nicht möglich sein, sende einfach die überarbeitete Entries-Liste per E-Mail oder Whatsapp.