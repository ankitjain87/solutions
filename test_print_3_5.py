import unittest
from print_numbers import print_number


class TestPN(unittest.TestCase):

    def setUp(self):
        pass

    def test_print_numbers_3(self):
        self.assertEqual(print_number(3), "1 2 Three")

    def test_print_numbers_5(self):
        self.assertEqual(print_number(5), "1 2 Three 4 Five")

    def test_print_numbers_3_5(self):
        self.assertEqual(print_number(15), "1 2 Three 4 Five Three 7 8 Three Five 11 Three 13 14 ThreeFive")


if __name__ == '__main__':
    unittest.main()
