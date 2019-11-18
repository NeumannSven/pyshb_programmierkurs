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



## Funktionskopf



## Funktionsrumpf


[Inhalt](../agenda.md)
