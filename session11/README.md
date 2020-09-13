# Dokumentation


```console

C:\projects\git\pyshb_programmierkurs\session11>

>python -m venv python
>python/Scripts/activate
(python) > 

```


```console

(python) >pip install -U sphinx

```


```console


(python) >sphinx-quickstart
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

```python


import os
import sys
sys.path.insert(0, os.path.abspath('.'))


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]


html_theme = 'classic'

```


```rst
Module demolib
==============
.. automodule:: demolib
   :members:
```




```console

(python) >make html

```




```python

import random

class ValueList:
    """create a list with size of count and with random
    values between minvalue and maxvalue

    Args:
        count (int): size of list
        minvalue (int, optional): min random value. Defaults to 0.
        maxvalue (int, optional): max random value. Defaults to 1000.

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
        """        
        return max(self._values)

    def getMinValue(self):
        """return the smallest value from the list

        Returns:
            int: the smallest value in the list
        """        
        return min(self._values)

    def getSum(self):
        """return the sum over all values in the list

        Returns:
            int: sum over all values
        """        
        result = 0
        for value in self._values:
            result += value
        return result
        
if __name__ == "__main__":
    mylist = ValueList(15, 0, 2)
    print(mylist.getValues())

```
