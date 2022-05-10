import deposit
import unittest

class DepositTest(unittest.TestCase):
    def test_deposit(self):
        self.assertEqual(deposit.deposit_calc(100,10,10),f"Year {10} = {259.4}")

if __name__ == "__main__":
    unittest.main()

