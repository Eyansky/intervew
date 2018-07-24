import unittest
from Reverser import checkintergers, checkstrings, checksatisfacton 

class TestPalindromes(unittest.TestCase):
    """
        set up
    """
    def setUp(self):
        """
            code that is executed before each test
        """
        self.data1 = [5,6,3,56,67,34]
        self.data2 = ["ian","mwangi","msee"]
        self.data3 = ["ian","eyansky",254,345]


    def test_intergers(self):
        """
            Test for passing intergers test and reversing the integers
        """
       
        self.assertEqual(checkintergers(self.data1), [34, 67, 56, 3, 6, 5])
    
    def test_bad_intergers(self):
        """
            Test for failing intergers test 
        """
       
        self.assertEqual(checkintergers(self.data3), "They are not all integers!!")

    def test_strings(self):
        """
            Test for passing strings test and converting to uppercase
        """
       
        self.assertEqual(checkstrings(self.data2), ['IAN', 'MWANGI', 'MSEE'])
    
    def test_bad_strings(self):
        """
            Test for failing intergers test 
        """
       
        self.assertEqual(checkstrings(self.data3), "They are not all strings!!")
    
    def test_checksatisfacton(self):
        """
            Test if it will return the same list when all they dont satisfy the two requirements
        """
       
        self.assertEqual(checksatisfacton(self.data3), ["ian","eyansky",254,345])


if __name__ == '__main__':
    unittest.main()