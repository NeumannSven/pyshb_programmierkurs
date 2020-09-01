# Tests

Ein Test ist eine Methode um zu überprüfen, ob ein Algorithmus mit den gegebenen Argumenten das erwartete Ergebnis zurückgibt.

Als Erstes erstellen wir eine Klasse mit verschiedenen Methoden, die wir dann testen können.

```python

import random

class ValueList:
    """create a list with size of count and with random
    values between minvalue and maxvalue

    Args:
        count (int): size of list
        minvalue (int, optional): min random value. Defaults to 0.
        maxvalue (int, optional): max random value. Defaults to 1000.

    >>> mylist = ValueList(3)
    >>> mylist.getMaxValue()
    5
    >>> mylist.getMinValue()
    1

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



## assert
In Python gibt es ist die eingebaute assert Funktion, mit dieser Funktion können Ergebnisse oder Ausdrücke überprüft werden.
Wenn die Funktion ein False zurück liefert oder der Ausdruck nicht wahr ist, wird eine "AssertionError" Exception geschmissen.
Ansonsten wird nichts ausgegeben.

```python

if __name__ == "__main__":
    mylist = ValueList(15, 0, 2)
    print(mylist.getValues())
    assert mylist.getMaxValue() == 2
    assert mylist.getMinValue() == 0 
    assert mylist.getSum() < 15

```



## unittest

```python

import unittest
import demolib

class Test(unittest.TestCase):

    def setUp(self):
        self.mylist = demolib.ValueList(15, 0, 2)
        
    def tearDown(self):
        pass

    def test_get_max_value(self):
        self.assertEqual(self.mylist.getMaxValue(), 2)

    def test_get_min_value(self):
        self.assertEqual(self.mylist.getMinValue(), 0)
        

if __name__ == "__main__":
    unittest.main()

```



## doctest


```python

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


if __name__ == "__main__":
    import doctest
    doctest.testmod()

```
