logdatei = open("rechner_ausgabe.txt", "a+")

eingabe = ""

while eingabe != "x":
    eingabe = input("Bitte ein Zeichen eingeben: ")

    if eingabe == 'x':
        print("Programm Ende")
        break
    elif eingabe == 'm':
        print("Multiplizieren")
        zahl_eingabe = input("Bitte zwei Zahlen eingeben: ")
        if ',' in zahl_eingabe or '.' in zahl_eingabe or not " " in zahl_eingabe:
            continue
        teile = zahl_eingabe.split()
        ausgabe = f"Das Ergebnis ist: {teile[0]} mal {teile[1]} = {int(teile[0]) * int(teile[1])}"
        print(ausgabe)
    elif eingabe == 'a':
        print("Addieren")
        zahl_eingabe = input("Bitte zwei Zahlen eingeben: ")
        if ',' in zahl_eingabe or '.' in zahl_eingabe or not " " in zahl_eingabe:
            continue
        teile = zahl_eingabe.split()
        ausgabe = f"Das Ergebnis ist: {teile[0]} plus {teile[1]} = {int(teile[0]) + int(teile[1])}"
        print(ausgabe)
    else:
        print("Auswahl nicht unterstüzt")
        ausgabe = ""

    if ausgabe:
        logdatei.write(ausgabe)
        logdatei.write("\n")

logdatei.close()

print("Ende")
