zahl = 7
wort = "Wael"
list = [1,2,3,"Wael"]
liste1 = [1,2,3]
def mecanismuslist(liste):

    liste = [4,5,6]
    if  liste1 is not liste :
        print("Call by Value")
    else:
        print("Call by Refernence")

def mechanismus(datentyp):
    print("Vor: ",datentyp)
    if type(datentyp)== type(int()):
        datentyp = datentyp+1
        if datentyp is zahl:
            print("Call by Reference")
        else:
            print("Call by Value")

    elif type(datentyp) == type(str()):
       datentyp = datentyp + " Eskeif"
       if datentyp is wort:
           print("Call by Reference")
       else:
           print("Call by Value")

    else:
        datentyp[3] = "Eskeif"
        if datentyp is list:
            print("Call by Reference")
        else:
            print("Call by Value")
print("___Integer---")
mechanismus(zahl)
print("Nach: ",zahl)
print("___String---")
mechanismus(wort)
print("Nach: ",wort)
print("___Liste---")
mechanismus(list)
print("Nach: ",list)
print("___NewList---")
print("Vor:", liste1)
mecanismuslist(liste1)
print("Nach" , liste1)
