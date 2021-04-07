
# Schnelle Dokumentation zum RM-Simulator in Deutsch
# Implementiert in Python


# Alle 29 Befehle und deren Funktion nach Kategorien sortiert
#Start
INI		00			{}
#Laden
LDK		<zahl>		{Lade <zahl> in Akku}
LDA		<adresse>	{Lade Wert aus <adresse> in Akku}
LDP		<adresse>	{Lade Wert aus Adresse, auf die <adresse> zeigt}
#Speichern
STA		<adresse>	{Speichere Akku in <adresse>}
STP		<adresse>	{Speichere Akku in Adresse, auf die <adresse> zeigt}
#Springen
JMP		<anker>		{unbedingter Sprung nach <anker>}
JEZ		<anker>		{Sprung nach <anker>, falls Akku=0}
JLZ		<anker>		{Sprung nach <anker>, falls Akku<0}
JGZ		<anker>		{Sprung nach <anker>, falls Akku>0}
JNE		<anker>		{Sprung nach <anker>, falls Akku<>0}
JLE		<anker>		{Sprung nach <anker>, falls Akku<=0}
JGE		<anker>		{Sprung nach <anker>, falls Akku>=0}
#Anker
ANC		<anker>		{Ankerpunkt mit Bezeichnung <anker>}
#Eingabe, Ausgabe
INP		<adresse>	{Eingabe nach <adresse>}
OUT		<adresse>	{Ausgabe aus <adresse>}
#Operationen
ADK		<zahl>		{Addiere <zahl> zu Akku}
ADA		<adresse>	{Addiere Wert aus <adresse> zu Akku}
ADP		<adresse>	{Addiere Wert aus Adresse, auf die <adresse> zeigt, zu Akku}
SUK		<zahl>		{Subtrahiere <zahl> von Akku}
SUA		<adresse>	{Subtrahiere Wert aus <adresse> von Akku}
SUP		<adresse>	{Subtrahiere Wert aus Adresse, auf die <adresse> zeigt, von Akku}
MUK		<zahl>		{Multipliziere <zahl> mit Akku}
MUA		<adresse>	{Multipliziere Wert aus <adresse> mit Akku}
MUP		<adresse>	{Multipliziere Wert aus Adresse, auf die <adresse> zeigt, mit Akku}
DIK		<zahl>		{Dividiere Akku durch <zahl>}
DIA		<adresse>	{Dividiere Akku durch Wert aus <adresse>}
DIP		<adresse>	{Dividiere Akku durch Wert aus Adresse, auf die <adresse> zeigt}
#Ende
HLT		99			{Programm beenden}


# Befehlsstruktur und Eigenschaften derer
- 1 Befehl pro Zeile
- Freizeilen erlaubt
- Zeilenkommentar beginnend mit "#"
- Befehl ist immer ein STR und mit einem Freizeichen " " von der Übergabe (immer INT / FLOAT) getrennt
- Nach der Übergabe können mit (mindestens einem Freizeichen " " getrennt) Kommentare ergänzt werden
- INT können zwischen zwei Ziffern maximal einen Bodenstrich "_" enthalten
- INT können beliebig viele Nullen "0" enthalten (auch davor)


# Beispielcode zur Berechnung der Fakultät

# Fakultät berechnen

# Eingabe x
INP 01
# Fall 0 und 1 abfangen
LDA 01
JEZ 1_1
SUK 1
JEZ 1_1
# Eingabe x in 02 speichern
LDA 01 #x
STA 02 #x'

# x! berechnen
ANC 3_3
LDA 01
SUK 1
JEZ 2_2
STA 01
MUA 02
STA 02
JMP 3_3

# wenn 0 oder 1, dann x anzeigen
ANC 1_1
OUT 01
HLT 99
# sonst ergebnis von x!
ANC 2_2
OUT 02
HLT 99


# Verwendung über Konsole/Terminal
python rm_interpreter.py [.rm Datei] [optional -p|-w]

# Übergabeparameter
[.rm Datei]: Datei mit beschriebenem RM-Assembler Code
[-p|-w]: "-p" zeigt alle Zwischenschritte im Format "STAT: [Akkumulator Inhalt] [Befehlszähler Wert]" an; "-w" pausiert zusätzlich und wartet auf ENTER

# Eingaben im Code
Bei "INP: " wird eine Eingabe als INT / FLOAT erwartet


# Bemerkungen
Der Befehl "HLT 99" terminiert das Programm.
Wenn dieser Befehl nicht spätestens am Ende steht, ensteht ein "IndexOutOfRange" Fehler. Das Programm terminiert trotzdem ...




