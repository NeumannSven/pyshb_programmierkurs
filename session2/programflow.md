[Inhalt](../agenda.md)

# Programmfluss
Ein Python Script kann von oben nach unten abgearbeitet werden, aber es gibt meistens Situationen die besonders
behandelt werden müssen um dann eine Entscheidung herbeizuführen der den Programmfluss verändert.


## Bedingungen
Ein Zeichen kann z.B. von der Tastaur eingelesen werden, dieses Zeichen kann dann eine Bedingung für das weitere
Ausführen des Programms oder bei der Eingabe eines "x" die Beendigung des Programms hervorrufen.

### if
```python
eingabe = input("Bitte ein Zeichen eingeben: ")

if eingabe == 'x':
    print("Programm Ende")
    
print("Ende")

```

### elif
```python
eingabe = input("Bitte ein Zeichen eingeben: ")

if eingabe == 'x':
    print("Programm Ende")
elif eingabe == 'm':
    print("Multiplizieren")
elif eingabe == 'a':
    print("Addieren")
    
print("Ende")

```
### else
```python
eingabe = input("Bitte ein Zeichen eingeben: ")

if eingabe == 'x':
    print("Programm Ende")
elif eingabe == 'm':
    print("Multiplizieren")
elif eingabe == 'a':
    print("Addieren")
else:
    print("Auswahl nicht unterstüzt")
    
print("Ende")

```

## Schleifen

### for 


### while


[Inhalt](../agenda.md)
