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
        Validate add function raises error for new line at the end
        """
        negative_numbers = ("-1", "-100", "-9999")
        positive_numbers = ("-7", "1", "9999")
        for x in positive_numbers:
            for y in negative_numbers:
                try:
                    add("%s,%s" % (x, y))
                except ValueError as err:
                    print(err.args)
