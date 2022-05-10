import year_checker
import unittest

class YearTest(unittest.TestCase):
    def test_leap(self):
        self.assertEqual(year_checker.is_year_leap(2000),True)

if __name__ == "__main__":
    unittest.main()