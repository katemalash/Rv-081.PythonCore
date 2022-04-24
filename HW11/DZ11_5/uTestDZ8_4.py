import DZ8_4
import unittest


class TestPrime(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_Prime1(self):
        self.assertEqual(DZ8_4.is_prime(83), True)

    def test_Prime2(self):
        self.assertEqual(DZ8_4.is_prime(96), False)

