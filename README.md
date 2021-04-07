# register-machine-simulator
A simulator for a register machine as an code interpreter written in Python.

## How to use
```
py rm_interpreter.py [absolute path to rm file] [optional -p or -w]
```

## ToDo

* [ ] __**english readme**__

## Deutsche README

### Alle 29 Befehle und deren Funktion nach Kategorien sortiert

#### Start, Ende

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`INI` | 00 | Nur intern notwendig, sonst keine Funktion
`HTL` | 99 | Programm beenden

#### Laden

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`LDK` | *zahl* | Lade *zahl* in Akku
`LDA` | *adresse* | Lade Wert aus *adresse* in Akku
`LDP` | *adresse* | Lade Wert aus Adresse, auf die *adresse* zeigt in Akku

#### Speichern

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`STA` | *adresse* | Speichere Akku in *adresse*
`STP` | *adresse* | Speichere Akku in Adresse, auf die *adresse* zeigt

#### Anker

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`ANC` | *anker* | Ankerpunkt mit ID *anker*

#### Springen

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`JMP` | *anker* | Unbedingter Sprung nach *anker*
`JEZ` | *anker* | Sprung nach *anker*, falls Akku = 0
`JLZ` | *anker* | Sprung nach *anker*, falls Akku < 0
`JGZ` | *anker* | Sprung nach *anker*, falls Akku > 0
`JNE` | *anker* | Sprung nach *anker*, falls Akku != 0
`JLE` | *anker* | Sprung nach *anker*, falls Akku <= 0
`JGE` | *anker* | Sprung nach *anker*, falls Akku >= 0

#### Eingabe, Ausgabe

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`INP` | *adresse* | Eingabe in *adresse* speichern
`OUT` | *adresse* | Wert aus *adresse* ausgeben

#### Operationen

Befehl | Parameter | Beschreibung
------ | --------- | ------------
`ADK` | *zahl* | Addiere *zahl* zu Akku
`ADA` | *adresse* | Addiere Wert aus *adresse* zu Akku
`ADP` | *adresse* | Addiere Wert aus Adresse, auf die *adresse* zeigt, zu Akku
`SUK` | *zahl* | Subtrahiere *zahl* von Akku
`SUA` | *adresse* | Subtrahiere Wert aus *adresse* von Akku
`SUP` | *adresse* | Subtrahiere Wert aus Adresse, auf die *adresse* zeigt, von Akku
`MUK` | *zahl* | Multipliziere *zahl* mit Akku
`MUA` | *adresse* | Multipliziere Wert aus *adresse* mit Akku
`MUP` | *adresse* | Multipliziere Wert aus Adresse, auf die *adresse* zeigt, mit Akku
`DIK` | *zahl* | Dividiere Akku durch *zahl>
`DIA` | *adresse* | Dividiere Akku durch Wert aus *adresse>
`DIP` | *adresse* | Dividiere Akku durch Wert aus Adresse, auf die *adresse* zeigt

### Befehlsstruktur und Eigenschaften derer

* 1 Befehl pro Zeile
* Freizeilen erlaubt
* Zeilenkommentar beginnend mit `#`
* Befehl ist immer ein STR und mit einem Freizeichen ` `&nbsp;von der Übergabe (immer INT / FLOAT) getrennt
* Nach der Übergabe können mit (mindestens einem Freizeichen ` `&nbsp;getrennt) Kommentare ergänzt werden
* INT können zwischen zwei Ziffern maximal einen Bodenstrich `_` enthalten
* INT können beliebig viele Nullen `0` enthalten (auch davor)

### Verwendung über Konsole/Terminal

```
python rm_interpreter.py [.rm Datei] [optional -p|-w]
```

Übergabeparameter

* [.rm Datei]: Datei mit beschriebenem RM-Assembler Code
* [-p|-w]: `-p` zeigt alle Zwischenschritte im Format `STAT: [Akkumulator Inhalt] [Befehlszähler Wert]` an; `-w` pausiert zusätzlich und wartet auf ENTER

### Eingaben im Code

Bei `INP: ` wird eine Eingabe als INT / FLOAT erwartet

### Bemerkungen

Der Befehl `HLT 99` terminiert das Programm.

Wenn dieser Befehl nicht spätestens am Ende steht, ensteht ein "*IndexOutOfRange*" Fehler. *Das Programm terminiert dann trotzdem ...*

