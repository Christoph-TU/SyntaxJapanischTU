# Japanisches Mini Wörterbuch

Dieses Wörterbuch sammelt häufig genutzte Wörter und Satzfragmente, die oftmals in Hiragana notiert werden. Es beinhaltet außerdem alle Partikel, um einen umfassenden Überblick zu bieten, welche Satzfunktionen sie jeweils einnehmen könnten.

## Struktur

Die eigentlichen Wörter befinden sich in der Datei `entries.json`, welche die wichtigste Datei dieses Projekts ist. Das Python-Skript `generate_dictionary.py` erzeugt in Verbindung mit der LaTeX-Vorlage `template.tex` ein TeX-Dokument, welches anschließend zu einem PDF kompiliert wird.

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

Alle Felder sind optional. Das Skript erzeugt automatisch ein Hiragana aus dem Namen, wenn es ausgeführt wird. Zusätzlich werden alle Einträge alphabetisch geordnet, wenn das Skript ausgeführt wird. Daher ist es wichtig, die Datei zu speichern, bevor das Skript ausgeführt wird, um das versehentliche Löschen von Einträgen zu vermeiden.

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

Am besten währe es einen Pull Request zu stellen, um Fehler zu korrigieren oder neue Einträge hinzuzufügen. Bitte führe vor dem Erstellen des Pull Requests zuerst das Python-Skript aus, um sicherzustellen, dass die Einträge geordnet sind.

Sollte dies nicht möglich sein, sende die überarbeitete Entries-Liste per E-Mail oder Whatsapp.