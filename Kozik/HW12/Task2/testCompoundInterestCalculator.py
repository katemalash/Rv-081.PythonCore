from compoundInterestCalculator import compound_interest_calculator
import unittest


class CompoundInterestCalculatorTest(unittest.TestCase):

    def test_def(self):
        self.assertEqual(compound_interest_calculator(500, 3), 665.5)
