import calc
import unittest


class CalcTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.arithmetic_operation(2, 3, '+'), 5)

    def test_dif(self):
        self.assertEqual(calc.arithmetic_operation(2, 3, '-'), -1)

    def test_mult(self):
        self.assertEqual(calc.arithmetic_operation(2, 3, '*'), 6)

    def test_div(self):
        self.assertEqual(calc.arithmetic_operation(6, 3, '/'), 2.0)


if __name__ == '__main__':
    unittest.main()
