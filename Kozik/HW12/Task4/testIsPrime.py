from isPrime import is_prime
import unittest


class TestIsPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(is_prime(11), True)
