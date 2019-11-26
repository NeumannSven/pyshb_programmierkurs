[Inhalt](../agenda.md)

# Funktionen

Ein Rechteck erzeugen und ausdrucken.

```python
# functions.py

rechteck = ""
breite = 20
hoehe = 5

# Linie Oben
rechteck += "+"
for i in range(breite):
    rechteck += "-"
rechteck += "+\n"


# Linie Rechts und Links 
for i in range(hoehe):
    rechteck += "|" + (breite)*" " + "|\n"
    

rechteck += "+"
# Linie Unten
for i in range(breite):
    rechteck += "-"
rechteck += "+\n"
    
    
print(rechteck)
```

Zwei verschieden große Rechtecke ausdrucken.

```python
# functions.py

rechteck = ""
breite = 20
hoehe = 5

# Linie Oben
rechteck += "+"
for i in range(breite):
    rechteck += "-"
rechteck += "+\n"

# Linie Rechts und Links 
for i in range(hoehe):
    rechteck += "|" + (breite)*" " + "|\n"
    
rechteck += "+"
# Linie Unten
for i in range(breite):
    rechteck += "-"
rechteck += "+\n"
        
print(rechteck)

rechteck = ""
breite = 40
hoehe = 10

# Linie Oben
rechteck += "+"
for i in range(breite):
    rechteck += "-"
rechteck += "+\n"


# Linie Rechts und Links 
for i in range(hoehe):
    rechteck += "|" + (breite)*" " + "|\n"
    

rechteck += "+"
# Linie Unten
for i in range(breite):
    rechteck += "-"
rechteck += "+\n"
    
print(rechteck)

```

Eleganter geht das so

```python

# functions.py

def createRechteck(breite, hoehe):
    rechteck = ""

    # Linie Oben
    rechteck += "+"
    for i in range(breite):
        rechteck += "-"
    rechteck += "+\n"

    # Linie Rechts und Links 
    for i in range(hoehe):
        rechteck += "|" + (breite)*" " + "|\n"
        
    rechteck += "+"
    # Linie Unten
    for i in range(breite):
        rechteck += "-"
    rechteck += "+\n"
            
    print(rechteck)

createRechteck(20, 5)
createRechteck(40, 10)
```

## Funktionskopf

### Funktion mit Positionsargumenten

```python

def createRechteck(breite, hoehe):

```

### Funktion mit Positionsargumente

```python

def createRechteck(breite, hoehe):

```

### Funktion mit Schlüsselwort-Argumente

```python

def createRechteck(breite=10, hoehe=10):

```

## Funktionskörper

```python
    rechteck = ""

    # Linie Oben
    rechteck += "+"
    for i in range(breite):
        rechteck += "-"
    rechteck += "+\n"

    # Linie Rechts und Links 
    for i in range(hoehe):
        rechteck += "|" + (breite)*" " + "|\n"
        
    rechteck += "+"
    # Linie Unten
    for i in range(breite):
        rechteck += "-"
    rechteck += "+\n"
            
    print(rechteck)
```

## Functionsaufruf

```python
createRechteck(20, 5)
createRechteck(40, 10)

```

[Inhalt](../agenda.md)
