
def Geldwechsler():
    dictMuenzen = {}

    preis = (float(input("Den Preis eingaben: ")))
    while preis < 0:
        print("ungueltige Eingabe")
        preis = (float(input("Geben Sie den Preis erneut ein: ")))

    betrag =(float(input("Gegebenden Betrag eingeben: ")))
    # Control
    while betrag < preis :
        print("Der Betrag muss goesser als " + str(preis) +" sein")
        betrag = (float(input("Geben Sie den Betrag erneut ein: ")))


    fin = False

    print("Die zur verfuegung stehenden Muenzen sind: ")
    while not fin:


        try:
            muenzen = int(input("1,2,5,10,20,50 ct"
                        "\nBitte Muenzart eingeben: "))
        except ValueError:
            print("something went wrong")
            break
            exit


        while not (muenzen == 1 or muenzen == 2 or muenzen == 5 or muenzen == 10 or muenzen == 20 or muenzen == 50):
            try:
                muenzen = int(input("ungueltige einagbe, bitte erneut versuchen: "))
            except ValueError:
                print("something went wrong")
                exit
                break


        anzahl = int(input(" Bitte anzhal der " + str(muenzen) + " angeben: "))
        while anzahl < 0:
           anzahl = int(input("ungueltige einagbe, bitte erneut versuchen: "))
        dictMuenzen.update({muenzen: anzahl})

        exit = input("Fertig = f / mehr Eingeben = Enter \n")
        if (exit == "f" or exit == "F"):
               fin = True
        else:
            continue



    sortedDictMuenzen = dict(sorted(dictMuenzen.items(), key=lambda item: item[1] ))

    wechselGeld = betrag - preis
    print("Wechselgeld: " + str(wechselGeld))

    #Greedy
    for difference in sortedDictMuenzen:
        count = 0
        while (wechselGeld - int(difference)) >= 0:
            if int(sortedDictMuenzen[difference]) > 0:
                wechselGeld = wechselGeld - int(difference)
                sortedDictMuenzen[difference] = (int(sortedDictMuenzen[difference]) -1)
                count = count+1
            else:
                break
        print(str(difference) + " ct muenzen")
        print(str(count) + " wurden benoetigt\n")
        if wechselGeld == 0:
            break

    if wechselGeld != 0:
        print("nicht genuegend muenzen vorhanden")

    print(wechselGeld)

    print(dictMuenzen)
    print(sortedDictMuenzen)

Geldwechsler()

