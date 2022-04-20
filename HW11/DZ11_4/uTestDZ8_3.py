import DZ8_3
import unittest


class TestDate(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_Date1(self):
        self.assertEqual(DZ8_3.date(28, 2, 1904), True)

    def test_Date2(self):
        self.assertEqual(DZ8_3.date(16, 7, 2004), True)

