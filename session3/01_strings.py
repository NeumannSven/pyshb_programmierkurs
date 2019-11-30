eingabe = ""

while eingabe != "x":
    eingabe = input("Bitte ein Zeichen eingeben: ")

    if eingabe == 'x':
        print("Programm Ende")
    elif eingabe == 'm':
        print("Multiplizieren")
        zahl_eingabe = input("Bitte zwei Zahlen eingeben: ")
        teile = zahl_eingabe.split()
        print(f"Das Ergebnis ist: {teile[0]} mal {teile[1]} = {int(teile[0]) * int(teile[1])}")
    elif eingabe == 'a':
        print("Addieren")
        zahl_eingabe = input("Bitte zwei Zahlen eingeben: ")
        teile = zahl_eingabe.split()
        print(f"Das Ergebnis ist: {teile[0]} plus {teile[1]} = {int(teile[0]) + int(teile[1])}")
    else:
        print("Auswahl nicht unterstüzt")

print("Ende")
