def ausgabe():
    with open("speisekarte.txt", mode='r') as file:
        print(file.read())
    file.close()

def printCard(dictionary):

    # Alle Speisen mit ihren Presien werden ausgedruckt.
    for name, preis in dictionary.items():
        print(name, ":", preis, "Cent")

    print("--------------------")

def removeFromCard(dictionary):

    # print content of 'speisekarte'
    index = 0
    nameList = {}
    for name in dictionary:
        if name != "Speisename":
            print(index,":", name)
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
                            dictionary.pop(nameList.get(eingabe))
                            boolean = 0

    print("--------------------")
    return dictionary

# handles the adding of content into 'speisekarte'
def addToCard(dictionary):
    print("Sie koennen mit der 'Enter'-Taste diesen Menu verlassen!")

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

        dictionary[name] = preis

        print(name + " wurde zur Speisekarte hinzugefügt!")
    except TypeError:
        pass

    print("--------------------")
    return dictionary

def readFile(dictionary):
    try:
        with open("speisekarte.txt", mode='r') as file:
            for line in file:
                dictionary[line.split(",")[0]] = line.split(",")[1].split('\n')[0]
        file.close()

    except FileNotFoundError:
        print("speisekarte.txt wurde nicht gefunden! Es wird mit einer leeren Speisekarte gearbeitet!")
    except IOError:
        print("Could not read file! CRITICAL ERROR")

    return dictionary


def writeFile(dictionary):

    try:
        with open("speisekarte.txt", mode='w') as file:
            for name,preis in speisekarte.items():
                if name != "Speisename":
                    file.write(f'{name},{preis}\n')
        file.close()
    except :
        print("Die Datei konnte nicht geschrieben werden!")

# starts here
option = "b"
speisekarte = {'Speisename': 'Preis in'}

print("Willkommen zum Speisekarten Manager!")
speisekarte = readFile(speisekarte)

# Main menu
while option != "e":
    print("Bitte waehlen Sie eine der unteren Optionen aus:")
    print("Speisekarte anzeigen (a)")
    print("Neues Gericht hinzufuegen (n)")
    print("Gericht loeschen (1)")
    print("Programmende (e)")

    option = input()

    if option == "a":
        printCard(speisekarte)
    elif option == "n":
        speisekarte = addToCard(speisekarte)
    elif option == "1":
        speisekarte = removeFromCard(speisekarte)
    elif option != "e":
        print("UNBEKANNTE OPTION")

writeFile(speisekarte)


# text at close
print("Programm wird geschlossen!")

