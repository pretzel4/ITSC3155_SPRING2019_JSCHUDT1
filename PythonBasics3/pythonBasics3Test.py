import unittest

import pythonBasics3

class TestPythonBasicsOne(unittest.TestCase):

#Test case for ends_with_consonant
    def test_ends_with_consonant(self):

        self.assertEqual(pythonBasics3.ends_with_consonant("Once upon a dark, cold night"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("What did Steve just say"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("I once swam with sharks"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("Do I know how old you are you"), False)

        #Self created cases
        self.assertEqual(pythonBasics3.ends_with_consonant("My friend's name is Keely"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("I'm listening to my favorite music"), True)

        self.assertEqual(pythonBasics3.ends_with_consonant("There's a forest outside"), False)

        # Please add three more test cases following the order above

#Test case for ends_with_number
    def test_ends_with_number(self):

        self.assertEqual(pythonBasics3.ends_with_number("What is 3/10"), True)

        self.assertEqual(pythonBasics3.ends_with_number("It was not a cat"), False)

        self.assertEqual(pythonBasics3.ends_with_number("I once swam with sharks"), False)

        self.assertEqual(pythonBasics3.ends_with_number("Blue plus purple equals 5"), True)

        # Please add three more test cases following the order above

        self.assertEqual(pythonBasics3.ends_with_number("I like the number 6"), True)

        self.assertEqual(pythonBasics3.ends_with_number("5 rockets spinning in space"), False)

        self.assertEqual(pythonBasics3.ends_with_number("1 is a cool number, but I like 5"), True)


#Test case for binary_multiple_of_6
    def test_binary_multiple_of_6(self):

        self.assertEqual(pythonBasics3.binary_multiple_of_6("100101"), False)

        self.assertEqual(pythonBasics3.binary_multiple_of_6("110"), True)

        self.assertEqual(pythonBasics3.binary_multiple_of_6("111111"), False)

        self.assertEqual(pythonBasics3.binary_multiple_of_6("3"), False)



if __name__ == '__main__':

  unittest.main(verbosity=1)

