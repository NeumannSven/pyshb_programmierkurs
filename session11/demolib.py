'''
Created on 14.09.2020

@author: neumann
'''
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
        result = 0
        for value in self._values:
            result += value
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
