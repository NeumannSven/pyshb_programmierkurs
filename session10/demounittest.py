'''
Created on 01.09.2020

@author: neumann
'''
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
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
