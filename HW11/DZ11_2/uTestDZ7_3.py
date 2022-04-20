import DZ7_3
import unittest


class TestCity(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_Ukraine(self):
        self.assertEqual(DZ7_3.info_countries("Kiev"), "Ukraine")

    def test_USA(self):
        self.assertEqual(DZ7_3.info_countries("New-York"), "USA")

