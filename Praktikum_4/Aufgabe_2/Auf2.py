wort = "test wort"
def scopes1():
    wort = "scopes wort"
    def do_nonlocal():
        # Das "Wort" bezieht sich auf "Wort" von scopes1 Funktion
        nonlocal wort
        wort = "nonlocal wort"
        print("in scopes: " + wort)
    do_nonlocal()

    def do_global():
        # # Das "Wort" bezieht sich auf "Wort" von Main
        global wort
        wort = "global wort"
        print("in do-global: " + wort)
    do_global()
    do_nonlocal()


def scopes():
    wort = "scopes Wort"
    print("in scopes: " + wort)

    def do_local():
        wort = "local wort"
        print("in do-local: " + wort)
    do_local()
    print("in scopes: " + wort)

    def do_nonlocal():
        wort = "nonlocal wort"
        print("in do-nonlocal: " + wort)
    do_nonlocal()



print("im Hauptprogramm: " + wort)
scopes()
scopes1()
print("im Hauptprogramm: " + wort)
print(";)")