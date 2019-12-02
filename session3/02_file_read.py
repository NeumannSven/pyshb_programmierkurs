# Datei zum Lesen öffnen
logdatei = open("rechner_ausgabe.txt", "r")

# Dictionary vorbereiten
anzahl = {"mal": 0,
          "plus": 0}

# zeilenweise durch die Datei gehen
for line in logdatei:
    # Zeile auswerten und Ergebnis im Dictionary speichern
    if "mal" in line:
        anzahl["mal"] += 1
    elif "plus" in line:
        anzahl["plus"] += 1

# Die Auswertung anzeigen
for key, value in anzahl.items():
    print(f"Es wurde {value} mal {key.upper()} gerechnet.")