import unittest
from Palindromes import palindromes 

class TestPalindromes(unittest.TestCase):
    """
        set up
    """
    def setUp(self):
        """
            code that is executed before each test
        """
        self.data1 = "madam"
        self.data2 = "nurses run"

        self.error1 = "eyansky"

    def test_Palindrome(self):
        """
            Test for good palindrome
        """
       
        self.assertEqual(palindromes(self.data1), "It is a Palindrome!!")

    def test_whitespace_Palindrome(self):
        """
            Test for palindrome with white spaces
        """
       
        self.assertEqual(palindromes(self.data2), "It is a Palindrome!!")
    
    def test_bad_Palindrome(self):
        """
            Test for bad palindrome 
        """
       
        self.assertEqual(palindromes(self.error1), "It is not a Palindrome!!")


if __name__ == '__main__':
    unittest.main()