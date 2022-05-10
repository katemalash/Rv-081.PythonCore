import string_cleaner
import unittest

class CleanerTest(unittest.TestCase):
    def test_cleaner(self):
        self.assertEqual(string_cleaner.duplicate_check("adsadsads"),"ads")
        

if __name__ == "__main__":
    unittest.main()

