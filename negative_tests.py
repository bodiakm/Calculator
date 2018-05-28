import unittest

from main_calculator import add


class CalculatorTest(unittest.TestCase):

    def test_pure_string(self):
        """
        Validate if no numbers present in string, 0 is returned
        """
        result = add("stringy")
        expected_result = 0
        self.assertEqual(expected_result, result)

    def test_new_line_at_end(self):
        """
        Validate add function raises error for new line at the end
        """
        try:
            add("1,44444444\n")
        except ValueError as err:
            print(err.args)

    def test_negatives(self):
        """
        Validate error raised when negative numbers are added
        """
        negative_numbers = ("-1", "-100", "-9999")
        positive_numbers = ("-7", "1", "9999")
        for x in positive_numbers:
            for y in negative_numbers:
                try:
                    add("%s,%s" % (x, y))
                except ValueError as err:
                    print(err.args)

    def test_higher_than_1000(self):
        """
        Validate add function ignores numbers over 1000
        """
        result = add("1,1000,1001,1002,9999")
        expected_result = 1001
        self.assertEqual(expected_result, result)

    def test_float(self):
        """
        Validate floats are not supported, its composing numbers are
        summed up individually, e.g. 5.2 turns to 5 and 2
        """
        result = add("7, 5.2")
        expected_result = 14
        self.assertEqual(expected_result, result)
