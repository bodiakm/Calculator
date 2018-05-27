import unittest

from main_calculator import add


class CalculatorTest(unittest.TestCase):

    def test_addition_no_numbers(self):
        result = add()
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_addition_one_number(self):
        for x in (0, 1, 10, 9999, 2.0, "44"):
            result = add(x)
            expected_result = int(x)
        self.assertEqual(expected_result, result)

    def test_addition_two_numbers(self):
        result = add(7,5)
        expected_result = 12
        self.assertEqual(expected_result, result)

    def test_addition_two_numbers_extended(self):
        """
        Adds more integers, floats and number strings
        """
        numbers = (0, 1, 10, 9999, 2.0, "44")
        for x in numbers:
            for y in numbers:
                result = add(x,y)
                expected_result = int(x) + int(y)
        self.assertEqual(expected_result, result)

    def test_addition_three_numbers(self):
        # Needs improvement
        try:
            add(1,2,3)
        except:
            TypeError

    def test_addition_string(self):
        # Needs improvement
        try:
            add(1,"stringy")
        except:
            ValueError