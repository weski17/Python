import time as zeit  # damit messen wir, wie lange ein Rechenprozess dauert

menue = """a = einlesen
r = ausgeben
n = neues Wort hinzufügen
e = Programmende
l = Wort löschen"""

letztesWort = ""  # globale Variable, die immer das zuletzt hinzugefügte Element speichert

# wir nutzen ein dictionary, wobei der Anfangsbuchtabe der key ist. Falls der
# String mit einer Zahl beginnt, ist "sonstwas" der key. Hinter jedem Key ist eine Liste in der
# die Worte gespeichert werden. Es sind also 53 Positionen, davon 52 fuer Buchstaben
a = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [], "I": [], "J": [], "K": [], "L": [],
     "M": [],
     "N": [], "O": [], "P": [], "Q": [], "R": [], "S": [], "T": [], "U": [], "V": [], "W": [], "X": [], "Y": [],
     "Z": [],
     "a": [], "b": [], "c": [], "d": [], "e": [], "f": [], "g": [], "h": [], "i": [], "j": [], "k": [], "l": [],
     "m": [],
     "n": [], "o": [], "p": [], "q": [], "r": [], "s": [], "t": [], "u": [], "v": [], "w": [], "x": [], "y": [],
     "z": [],
     "sonstwas": []}


# diese Funktion liest die Datei ein und speichert jede Zeile in das dictionary
def einlesen():
    anfang = zeit.time()
    try:
        file = open('dokument.txt', 'r')
        y = file.readlines()
        for x in range(0, len(y), 1):  # liest jede Zeile einzeln ein und speichert diese in der dictionary
            if y[x].replace("\n", "") != "":
                global letztesWort
                letztesWort = y[x].replace("\n", "")  # replace \n, um Zeilenumbrüche zu löschen
                a[pruefen(y[x])].append(letztesWort)  # in dictionary speichern
        f.close()
    except:
        pass  # nichts tun, wenn Datei nicht gefunden
    ende = zeit.time()
    print("Dauer des Einlesens: " + str((ende - anfang) / 1000) + " Sekunden")


# fragt nach einem Buchstaben und gibt dazu alle Worte aus dem dictionary aus
def ausgabe(buchstabe):
    t = 1  # rein dekorative Numerierung
    if buchstabe != "":
        if buchstabe[0].isalpha():  # wenn das Eingabeelement nicht mit Zahl beginnt (Normalfall, Buchstabe)
            for x in a[buchstabe[0]]:
                print(str(t) + ": " + x)
                t = t + 1
        if not buchstabe[0].isalpha():  # wenn das Eingabeelement mit Zahl beginnt (Sonderfall)
            for x in a["sonstwas"]:
                print(str(t) + ": " + x)
                t = t + 1
    print()


# loescht das zuletzt hinzugefügte Wort
def loeschen():
    anfang = zeit.time()
    t = -1  # zaehlervariable
    for x in a[pruefen(letztesWort)]:  # prueft nur die Liste mit dem passenden Anfangsbuchstaben
        t = t + 1
        if x == letztesWort:
            a[pruefen(letztesWort)].pop(t)
            print("Gelöscht wird: " + letztesWort)
    ende = zeit.time()
    print("Dauer des Loeschens: " + str((ende - anfang) / 1000) + " Sekunden")


# prueft, ob ein Wort mit einem Buchstaben anfaengt. Dann kommt das wort in die letzte Position
# des Dictionarys. Sonst wird nur der Anfangsbuchstabe zurückgegeben
def pruefen(wort):
    if wort != "":
        if not wort[0].isalpha():
            return "sonstwas"
        else:
            return wort[0]


# speichert ein neues Element in die Liste des passenden Anfangsbuchstaben
# letztesWort ist global, damit auch ausserhalb vom Methodenscope verändert
def anlegen():
    print("Welches Wort soll angelegt werden?")
    wort = input()
    global letztesWort
    if wort != "":
        letztesWort = wort
        a[pruefen(wort)].append(wort)  # append= in die liste packen
    if wort == "":
        print("Leere Worte werden nicht gespeichert")


# speichern in eine neue Datei
def speichern():
    kopie = ""
    print("Wie soll das neue Dokument heissen?")
    for x in a:
        for y in a[x]:
            kopie = kopie + y + "\n"  # Alle Begriffe in einen String mit Zeilenumbrueche speichern
    file = open(input() + ".txt", 'w')
    file.write(kopie)
    file.close()
    print("Dokument ist gespeichert.")


# das ist unsere Dauerschleie
befehl = a
while befehl != "e":
    print(menue)
    befehl = input()
    if befehl == "a":
        einlesen()
    elif befehl == "n":
        anlegen()
    elif befehl == "r":
        print("Was wollen Sie ausgeben?")
        ausgabe(input())
    elif befehl == "l":
        loeschen()
    elif befehl == "s":
        speichern()
    elif befehl == "e":
        pass
    else:
        print("Ungültige Eingabe - Sie sind weiterhin im Hauptmenü")
print("Programm beendet")



