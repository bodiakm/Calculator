import unittest
from main_calculator import add


class CalculatorTest(unittest.TestCase):

    def test_no_numbers(self):
        """
        Validates that if an empty string is passed 0 is returned
        """
        result = add("")
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_one_number(self):
        for x in ("0", "1", "10", "9999"):
            result = add(x)
            expected_result = int(float(x))
            self.assertEqual(expected_result, result)

    def test_two_numbers(self):
        result = add("7, 5")
        expected_result = 12
        self.assertEqual(expected_result, result)

    def test_two_numbers_extended(self):
        """
        Adds negatives and 0 to the addition
        """
        numbers = ("0", "1", "9999")
        for x in numbers:
            for y in numbers:
                result = add("%s,%s" % (x, y))
                expected_result = int(float(x)) + int(float(y))
        self.assertEqual(expected_result, result)

    def test_ten_numbers(self):
        """
        Validate that the program accepts and performs correct
        addition on a string containing more than 2 numbers
        """
        x = range(0, 10)
        result = add("%s" % x)
        expected_result = 45
        self.assertEqual(expected_result, result)

    def test_new_line(self):
        """
        Validate add function handles a new line correctly
        """
        result = add("1\n2,3")
        expected_result = 6
        self.assertEqual(expected_result, result)

    def test_different_delimiters(self):
        """
        Validate function handles different delimiters OK
        """
        result = add("//[;]\n1;2*&$^#W[]<\}{>")
        expected_result = 3
        self.assertEqual(expected_result, result)