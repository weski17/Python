def defaultparameter(semester,studiengang ,firstname= "Wael", lastname = "Eskeif"):
    print(firstname,lastname,studiengang,semester)

print("____Defaultparameter_____")
defaultparameter(1,"Informatik")
print()

def positionsparameter(firstname , semester , studiengang , lastname):
    print(firstname , lastname ,studiengang , semester)

print("____Positionsparameter_____")
positionsparameter(firstname="Wael",lastname="Eskeif",studiengang="Informatik",semester= 1)
print()

def benannteParameter(firstname, lastname , studiengang , semester):
    print(firstname , lastname , studiengang , semester)

print("____Benannteparameter_____")
benannteParameter("Wael","Eskeif","Informatik",1)
print()


def dictionaryPa(**kwargs):
    for key, value in kwargs.items():
        print(value, end= " ")

print("____Dictionary**_____"),
dictionaryPa(firstname = "Wael", lastname="Eskeif" , studiengang = "Informatik", semester = 1 )

print()

def tupleF(*args):
    full = ""
    for i in args:
        full = full+ " "+i
    return full
print()
print("____unpacking übernehmen____")
print(tupleF("Wael","Eskeif","Informatik",))
def unbacking(a,b,c):
    """Diese Funktion gibt das Produkt aus drei Zahlen zurück"""
    return(a+" "+b+" "+c)

values=["Wael","Eskeif","Informatik"]
print()
print("___Unpacking übergeben___")
print(unbacking(*values))

