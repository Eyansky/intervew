import unittest
from Palindromes import Palindromes

class TestPalindromes(unittest.TestCase):
    """
        set up
    """
    def setUp(self):
        """
            code that is executed before each test
        """
        self.data1 = "madam"
        self.data2 = "level"
        self.data3 = "nurses run"

        self.error1 = "eyansky"
        self.error2 = "ian eyansky"
        self.error3 = "Yule msee!!"

    def test_Palindrome(self):
        """
            Test for good palindrome
        """
        


if __name__ == '__main__':
    unittest.main()