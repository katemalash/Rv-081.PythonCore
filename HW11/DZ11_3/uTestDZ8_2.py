import DZ8_2
import unittest


class DepositTest(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_dep1(self):
        self.assertEqual(DZ8_2.deposit(1000, 9), 2357.95)

    def test_dep2(self):
        self.assertEqual(DZ8_2.deposit(53821, 4), 78799.33)
