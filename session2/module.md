[Inhalt](../agenda.md)

# Module


## Standard Bibliothek
Python liefert eine mächtige Standard Bibliothek mit. In der Python Shell kann eine Liste der
installierten Modulen mittels der help() Funktion aufgelistet werden.

```idle
>>> help()
help> modules

Please wait a moment while I gather a list of all available modules...

```

Mehr Informationen gibt es in der Python Documentation (F1) unter Library Reference


## Module verwenden
Hat man ein Modul gefunden in dem die gewünschten Funktionen enthalten sind, kann dieses in das eigene
Programm importiert werden.

```python
import sys
print(sys.version)

```


## Eigene Module schreiben

```python
# mymodule.py

def myfunction(txt):
  print(txt)
  
```


## Eigene Module verwenden

```python
# mymodprog.py

import mymodule

myfunction('Hallo Welt!')



[Inhalt](../agenda.md)
