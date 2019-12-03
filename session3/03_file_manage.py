# Funktion für Pfadangaben importieren
import pathlib
# Funktionen zum Dateien verwalten importieren
import shutil
# Funktionen zum Dateien löschen importieren
import os
# Funktionen für Zeitstempel importieren
import datetime as dt

# aktuellen Pfad als Objekt holen
pfad = pathlib.Path.cwd()
# Unterverzeichnis für alte Logdateien als Objekt anlegen
alte_logs = pfad / "logs"
# Logdatei als Pfadobjekt anlegen
logdatei = pathlib.Path("rechner_ausgabe.txt")

# prüfen, ob das Unterverzeichnis exisistiert und gegebenenfalls erzeugen
if not alte_logs.exists():
    alte_logs.mkdir()

# Logdatei in das Unterverzeichnis kopieren
shutil.copy2(logdatei, alte_logs)
# Logdatei im Unterverzeichnis umbenennen mit Zeitstempel
shutil.move(alte_logs / logdatei,
            alte_logs / f"rechner_ausgabe_{dt.datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
# Original Logdatei löschen
# os.remove(logdatei)

# Alte Logs komprimieren
shutil.make_archive(alte_logs / "logs", "zip", alte_logs)
