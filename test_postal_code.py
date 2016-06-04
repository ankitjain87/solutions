import unittest
from postal_code import is_valid


class TestPostalCode(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_valid_1(self):
        self.assertEqual(is_valid("EC1A 1BB"), "Valid")

    def test_is_valid_2(self):
        self.assertEqual(is_valid("DN55 1PT"), "Valid")

    def test_is_valid_3(self):
        self.assertEqual(is_valid("M1 1AE"), "Valid")

    def test_is_valid_4(self):
        self.assertEqual(is_valid("A11A 1BB"), "Invalid")

    def test_is_valid_5(self):
        self.assertEqual(is_valid("1AA 1BB"), "Invalid")


if __name__ == '__main__':
    unittest.main()
