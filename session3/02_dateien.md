[Inhalt](../agenda.md)

# Dateien Teil 1

Dateien lesen und schreiben funktioniert in Python ohne zusätzliche Module. 
Für weitergehende Dateimanipulation gibt es Module in der Standard-Library.

## Dateien öffnen

Dateien öffnen mit open(). Gibt ein file-Objekt zurück.

```python
f = open("datei.txt", "w") # Datei zum schreiben öffnen, muss existieren
f = open("datei.txt", "w+") # Datei zum schreiben öffnen, wird erstellt
f = open("datei.txt", "a") # Datei zum anhängen öffnen, muss existieren
f = open("datei.txt", "a+") # Datei zum anhängen öffnen, wird erstellt
f = open("datei.txt", "r") # Datei zum lesen öffnen
```

## Dateien schreiben

Text in eine Datei schreiben mit write().

```python
f.write("Hallo Bremen!")
```

Datei abschließen mit close(). Wird spätestens am Ende des Skripts automatisch geschlossen.

```python
f.close()
```

## Dateien lesen

Kompletten Inhalt lesen mit read(). Anzahl Zeichen lesen mit read(x).

Einzelne Zeile lesen mit readline(). Alle Zeilen lesen mit readlines().

```python
i = f.read() # liefert den Inhalt als String
z = f.readlines() # liefert den Inhalt zeilenweise als Liste von Strings
```

Die oberen Funktionen legen den Dateiinhalt komplett im Speicher ab, das kann bei großen Dateien lange dauern.
Effizienter ist es, die Zeilen in einer Schleife einzulesen und zu verarbeiten.

```python
f = open("datei.txt", "r")
for l in f:
    print(l)
```

[Inhalt](../agenda.md)
