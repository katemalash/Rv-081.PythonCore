from validationDate import *
import unittest


class ValidationDateTest(unittest.TestCase):

    def test_validation_date(self):
        self.assertEqual(validation_date(29, 2, 2032), True)

    def test_year_leap(self):
        self.assertEqual(is_year_leap(2032), True)
