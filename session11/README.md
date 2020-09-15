# Dokumentation

wie sieht das bei Euch mit der Dokumentation von Software Projekten aus? Wenn Du z. B. ein Python Module einer weiteren Person oder sogar auf einer Plattform wie Github mehreren Anwendern zur Verfügung stellst, dokumentierst Du das Interface oder wie das Modul anzuwenden ist?

In Python gibt es mehrere Module, die Dir die unschönen Fleißarbeit abnehmen. Wir schauen uns den Paket „Sphinx“ an und werden eine Dokumentation für ein Software-Modul generieren.


## Vorbereitung

Erstelle ein neues Verzeichnis Deiner Wahl z. B. "project" und wechsel in das Verzeichnis.

```
c:\User\Benutzer>cd \
C:\>mkdir project
C:\>cd project
```

Dann clone das Repositorie mit "git clone" 

```console
C:\project>git clone https://github.com/NeumannSven/pyshb_programmierkurs.git
Cloning into 'pyshb_programmierkurs'...
remote: Enumerating objects: 232, done.
remote: Counting objects: 100% (232/232), done.
remote: Compressing objects: 100% (193/193), done.
remote: Total 655 (delta 112), reused 99 (delta 32), pack-reused 423
Receiving objects: 100% (655/655), 2.24 MiB | 3.84 MiB/s, done.
Resolving deltas: 100% (336/336), done.

C:\project>
```

Wenn Du nicht mit "virtual environments" arbeiten möchtest, kannst Du diesen Schritt überspringen.
Wechsel in das Verzichnis wo alle Deine "virtual environments" aufbewahren möchtest, hier z. B. "venv".

```console
C:\project>cd \
C:\>mkdir venv
C:\>cd venv
C:\venv>
```

Erzeugen von einer "virtual environment" mit dem Namen "session11"

```console
C:\venv>python -m venv session11
C:\venv>session11\Scripts\activate
(session11) C:\venv> 
```

## Installation

Installieren des "sphinx" Paket

```console
(session11) C:\venv>pip install -U sphinx
```

## Erzeugen von einer Dokumentation

Wechseln in das "seesion11" Verzeichnis des Repositories

```console
(session11) C:\venv>cd \project\pyshb_programmierkurs\session11
(session11) C:\project\pyshb_programmierkurs\session11>

(session11) C:\project\pyshb_programmierkurs\session11>sphinx-quickstart
Welcome to the Sphinx 3.2.1 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

The project name will occur in several places in the built documentation.
> Project name: DemoLib
> Author name(s): Sven Neumann
> Project release []: 1.0.0

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]:

Creating file conf.py.
Creating file index.rst.
Creating file Makefile.
Creating file make.bat.

Finished: An initial directory structure has been created.

You should now populate your master file index.rst and create other documentation
source files. Use the Makefile to build the docs, like so:
   make builder
where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

```

Es wurde dann mehrere Dateien erzeugt. Wichtig sind für uns die Dateien "conf.py" und "index.rst" 

In der Datei "conf.py" kommentieren wir die Zeilen 13-15 aus. 

```python


import os
import sys
sys.path.insert(0, os.path.abspath('.'))
```

Ab der Zeile 34 fügen wir folgendes hinzu. 

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]
```

In der Zeile 53 kann das HTML-Theme festgelegt werden.

```python
html_theme = 'classic'

```

In der Datei "index.rst" wird (ab der Zeile 13) definiert, welche Module dokumentiert werden sollen. 

```rst
Module demolib
==============
.. automodule:: demolib
   :members:
```

Mit dem unten stehenden Befehl, wird die Dokumentation erzeugt.
Diese befindet sich dann im Verzeichnis "_build\html".

```console
(python) >make html
```

Hier das Python Beispiel für das wir eine Dokumentation erzeugen wollen.

```python
import random

class ValueList:
    """create a list with size of count and with random
    values between minvalue and maxvalue

    Args:
        count (int): size of list
        minvalue (int, optional): min random value. Defaults to 0.
        maxvalue (int, optional): max random value. Defaults to 1000.

    >>> mylist = ValueList(15, 0, 2)
    >>> mylist.getMaxValue()
    2
    >>> mylist.getMinValue()
    0

    """   
    def __init__(self, count, minvalue=0, maxvalue=1000): 
        self._values = [random.randrange(minvalue, maxvalue+1) for i in range(count)]

    def getValues(self):
        """return the list of values

        Returns:
            list: list of values
        
            
        """        
        return self._values.copy()

    def getMaxValue(self):
        """return the biggest value from the list 

        Returns:
            int: the biggest value in the list
            
        >>> mylist = ValueList(15, 0, 2)
        >>> mylist.getMaxValue()
        2
            
        """        
        return max(self._values)

    def getMinValue(self):
        """return the smallest value from the list

        Returns:
            int: the smallest value in the list

        >>> mylist = ValueList(15, 0, 2)
        >>> mylist.getMinValue()
        0

        """        
        return min(self._values)

    def getSum(self):
        """return the sum over all values in the list

        Returns:
            int: sum over all values
        """
        #TODO: get das nicht ein bischen besser?        
        result = 0
        for value in self._values:
            result += value
        return result    
```
