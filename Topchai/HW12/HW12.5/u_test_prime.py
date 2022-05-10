import prime_cheker
import unittest

class PrimeTest(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(prime_cheker.is_prime(2000),False)

if __name__ == "__main__":
    unittest.main()