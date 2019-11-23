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
Oft ist es notwendig viele wiederholungen eines Programmabschnittes ausführen. Dafür werden Schleifen benötigt,
die es in den folgenden Ausführungen gibt.

### while

```python
# loops.py

eingabe = ""

while eingabe != "x":
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

### for 

```python
# forloops.py
for i in range(10):
    print(i)

t = (1,42,6,17,99,23)

for i in t:
    print(i)

l = ["Hallo", "Welt", "!", 42, 23]

for i in l:
    print(i)

```

[Inhalt](../agenda.md)
