
def removeNachspeise(nachspeise, **kwargs):
    # print content of 'speisekarte'
    index = 0
    nameList = {}
    for name in nachspeise:
        if name != "Speisename":
            print(index, ":", name)
            nameList[index] = name
            index += 1

    if index == 0:
        print("Ihre Speisekarte beinhaltet keine Gerichte!")
    else:
        print("Sie koennen mit der 'Enter'-Taste diesen Menu verlassen!")
        print("Bitte geben Sie die Nummer des Gerichtes ein, den Sie entfernen moechten: ", end='')

        eingabe = input()

        if eingabe != "":
            boolean = bool

            while boolean:
                # check for exit condition
                if eingabe == "":
                    boolean = 0
                else:
                    # try to remove, in it does not work, then redefine 'eingabe'
                    try:
                        eingabe = int(eingabe)
                    except ValueError or KeyError:
                        print("Ihre Eingabe ist keine Zahl!")
                        print("Bitte geben Sie eine Zahl ein: ", end='')
                        eingabe = input()
                    else:
                        if 0 <= eingabe or eingabe <= index:
                            nachspeise.pop(nameList.get(eingabe))
                            boolean = 0

    print("--------------------")
    return nachspeise


def removeGetraenk(getraenk, **kwargs):
    # print content of 'speisekarte'
    index = 0
    nameList = {}
    for name in getraenk:
        if name != "Speisename":
            print(index, ":", name)
            nameList[index] = name
            index += 1

    if index == 0:
        print("Ihre Speisekarte beinhaltet keine Gerichte!")
    else:
        print("Sie koennen mit der 'Enter'-Taste diesen Menu verlassen!")
        print("Bitte geben Sie die Nummer des Gerichtes ein, den Sie entfernen moechten: ", end='')

        eingabe = input()

        if eingabe != "":
            boolean = bool

            while boolean:
                # check for exit condition
                if eingabe == "":
                    boolean = 0
                else:
                    # try to remove, in it does not work, then redefine 'eingabe'
                    try:
                        eingabe = int(eingabe)
                    except ValueError or KeyError:
                        print("Ihre Eingabe ist keine Zahl!")
                        print("Bitte geben Sie eine Zahl ein: ", end='')
                        eingabe = input()
                    else:
                        if 0 <= eingabe or eingabe <= index:
                            getraenk.pop(nameList.get(eingabe))
                            boolean = 0

    print("--------------------")
    return getraenk


def removehauptspeis(hauptspeise, **kwargs):
    # print content of 'speisekarte'
    index = 0
    nameList = {}
    for name in hauptspeise:
        if name != "Speisename":
            print(index, ":", name)
            nameList[index] = name
            index += 1

    if index == 0:
        print("Ihre Speisekarte beinhaltet keine Gerichte!")
    else:
        print("Sie koennen mit der 'Enter'-Taste diesen Menu verlassen!")
        print("Bitte geben Sie die Nummer des Gerichtes ein, den Sie entfernen moechten: ", end='')

        eingabe = input()

        if eingabe != "":
            boolean = bool

            while boolean:
                # check for exit condition
                if eingabe == "":
                    boolean = 0
                else:
                    # try to remove, in it does not work, then redefine 'eingabe'
                    try:
                        eingabe = int(eingabe)
                    except ValueError or KeyError:
                        print("Ihre Eingabe ist keine Zahl!")
                        print("Bitte geben Sie eine Zahl ein: ", end='')
                        eingabe = input()
                    else:
                        if 0 <= eingabe or eingabe <= index:
                            hauptspeise.pop(nameList.get(eingabe))
                            boolean = 0

    print("--------------------")
    return hauptspeise


def removeVorspeise(vorspeise, **kwargs):
    # print content of 'speisekarte'
    index = 0
    nameList = {}
    for name in vorspeise:
        if name != "Speisename":
            print(index, ":", name)
            nameList[index] = name
            index += 1

    if index == 0:
        print("Ihre Speisekarte beinhaltet keine Gerichte!")
    else:
        print("Sie koennen mit der 'Enter'-Taste diesen Menu verlassen!")
        print("Bitte geben Sie die Nummer des Gerichtes ein, den Sie entfernen moechten: ", end='')

        eingabe = input()

        if eingabe != "":
            boolean = bool

            while boolean:
                # check for exit condition
                if eingabe == "":
                    boolean = 0
                else:
                    # try to remove, in it does not work, then redefine 'eingabe'
                    try:
                        eingabe = int(eingabe)
                    except ValueError or KeyError:
                        print("Ihre Eingabe ist keine Zahl!")
                        print("Bitte geben Sie eine Zahl ein: ", end='')
                        eingabe = input()
                    else:
                        if 0 <= eingabe or eingabe <= index:
                            vorspeise.pop(nameList.get(eingabe))
                            boolean = 0

    print("--------------------")
    return vorspeise


def addMethodvorspeise(vorspeise, **kwargs):
    try:
        print("Bitte geben Sie den Namen Ihres Gerichtes ein:")
        name = input()

        if name == "":
            raise TypeError("CLOSE THIS MENU")

        # making 'preis' a local variable in this method
        preis = 0

        print("Bitte geben Sie den Preis ein (in Cent):")

        boolean = bool
        while boolean:
            try:
                consoleInput = input()

                if consoleInput == "":
                    raise TypeError("CLOSE THIS MENU")

                preis = int(consoleInput)
                boolean = 0

            except ValueError:
                print("Ihre Eingabe ist keine Zahl!")

        vorspeise[name] = preis

        print(name + " wurde zur Speisekarte hinzugefügt!")
    except TypeError:
        pass

    print("--------------------")
    return vorspeise


def addMethodHauptspeise(hauptspeise, **kwargs):
    try:
        print("Bitte geben Sie den Namen Ihres Gerichtes ein:")
        name = input()

        if name == "":
            raise TypeError("CLOSE THIS MENU")

        # making 'preis' a local variable in this method
        preis = 0

        print("Bitte geben Sie den Preis ein (in Cent):")

        boolean = bool
        while boolean:
            try:
                consoleInput = input()

                if consoleInput == "":
                    raise TypeError("CLOSE THIS MENU")

                preis = int(consoleInput)
                boolean = 0

            except ValueError:
                print("Ihre Eingabe ist keine Zahl!")

        hauptspeise[name] = preis

        print(name + " wurde zur Speisekarte hinzugefügt!")
    except TypeError:
        pass

    print("--------------------")
    return hauptspeise


def addMethodGetraenk(getraenk, **kwargs):
    try:
        print("Bitte geben Sie den Namen Ihres Gerichtes ein:")
        name = input()

        if name == "":
            raise TypeError("CLOSE THIS MENU")

        # making 'preis' a local variable in this method
        preis = 0

        print("Bitte geben Sie den Preis ein (in Cent):")

        boolean = bool
        while boolean:
            try:
                consoleInput = input()

                if consoleInput == "":
                    raise TypeError("CLOSE THIS MENU")

                preis = int(consoleInput)
                boolean = 0

            except ValueError:
                print("Ihre Eingabe ist keine Zahl!")

        getraenk[name] = preis

        print(name + " wurde zur Speisekarte hinzugefügt!")
    except TypeError:
        pass

    print("--------------------")
    return getraenk


def addMethodNachspeise(nachspeise, **kwargs):
    try:
        print("Bitte geben Sie den Namen Ihres Gerichtes ein:")
        name = input()

        if name == "":
            raise TypeError("CLOSE THIS MENU")

        # making 'preis' a local variable in this method
        preis = 0

        print("Bitte geben Sie den Preis ein (in Cent):")

        boolean = bool
        while boolean:
            try:
                consoleInput = input()

                if consoleInput == "":
                    raise TypeError("CLOSE THIS MENU")

                preis = int(consoleInput)
                boolean = 0

            except ValueError:
                print("Ihre Eingabe ist keine Zahl!")

        nachspeise[name] = preis

        print(name + " wurde zur Speisekarte hinzugefügt!")
    except TypeError:
        pass

    print("--------------------")
    return nachspeise

def aendern_Vorspeis(vorspeise,**kwargs):
    removeVorspeise(vorspeise)
    addMethodvorspeise(vorspeise)
def aendern_Nachspeise(nachspeise, **kwargs):
    removeNachspeise(nachspeise)
    addMethodNachspeise(nachspeise)
def aendern_getraenk(getraenk,**kwargs):
    removeGetraenk(getraenk)
    addMethodGetraenk(getraenk)
def aendern_hauptspeise(hauptspeise,**kwargs):
    removehauptspeis(hauptspeise)
    addMethodHauptspeise(hauptspeise)

def kategorieWahl():
    print("Aus welcher Kategorie möchten Sie entfernen.")
    print("v = Vorspeise")
    print("h = Hauptspeise")
    print("g = Getränk")
    print("n = Nachspeise")


def printCard():
    print("a = Speisekarte anzeigen ")
    print("n = Neues Gericht hinzufuegen ")
    print("l = Gericht loeschen ")
    print("s = Speise ändern")
    print("e = Programmende ")

def printKategorie():
    print("v = Vorspeise")
    print("h = Hauptspeise")
    print("g = Getraenk")
    print("n = Nachspeise")


getraenk = {
}
vorspeise = {
}
hauptspeise = {
}
nachspeise = {

}

speiskarte = {
    "vorspeise": vorspeise,
    "Hauptspeise": hauptspeise,
    "Nachspeise": nachspeise,
    "Getraenk": getraenk
}
cheak_aendern = ""
cheak_katRemove = ""
cheak_Kategorie = ""
cheak_w = ""
option = "s"
cheak = ""
print("Herzlich Willkommen")
while option != "e":
    printCard()
    option = input()
    if option == "a":
        for i in speiskarte:
            print(i, " : ", speiskarte[i])
    elif option == "s":
        for i in speiskarte:
            print(i, " : ", speiskarte[i])
        print("Aus welcher Kategorie moechten Sie ändern")
        printKategorie()
        cheak_aendern = input()
        if cheak_aendern == "v":
             aendern_Vorspeis(vorspeise)
        elif cheak_aendern== "h":
            aendern_hauptspeise(hauptspeise)
        elif cheak_aendern == "g":
             aendern_getraenk(getraenk)
        elif cheak_Kategorie == "n":
             aendern_Nachspeise(nachspeise)
        else:
              pass


    elif option == "n":
        print("w = Weiter")
        cheak_w = input()
        if cheak_w == "w":
            printKategorie()
            cheak_Kategorie = input()
            if cheak_Kategorie == "v":
                addMethodvorspeise(vorspeise)
            elif cheak_Kategorie == "h":
                addMethodHauptspeise(hauptspeise)
            elif cheak_Kategorie == "g":
                addMethodGetraenk(getraenk)
            elif cheak_Kategorie == "n":
                addMethodNachspeise(nachspeise)
            else:
                pass
        else:
            pass

    elif option == "l":
        for i in speiskarte:
            print(i, " : ", speiskarte[i])
        print("Aus welcher Kategorie moechten Sie entfernen")
        printKategorie()
        cheak_katRemove = input()
        if cheak_katRemove == "v":
            removeVorspeise(vorspeise)
        elif cheak_katRemove == "h":
            removehauptspeis(hauptspeise)
        elif cheak_katRemove == "g":
            removeGetraenk(getraenk)
        elif cheak_katRemove == "n":
            removeNachspeise(nachspeise)
        else:
            pass

print("Programm ist beendet")
try:
    with open("speisekarte.txt","w") as file:
     for id, info in speiskarte.items():
         file.write(id+"\n")
         for key in info:
           file.write(key+ " : " + str(info[key])+" Cent"+"\n")
    file.close()

except:
    print("Die Datei konnte nicht geschrieben werden!")
