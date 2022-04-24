import DZ8_1
import unittest


class CalcTest(unittest.TestCase):
    def setUp(self):
        print("Test start")

    def test_add(self):
        self.assertEqual(DZ8_1.arithmetic(1, 2, "+"), 3)

    def test_sub(self):
        self.assertEqual(DZ8_1.arithmetic(3, 3, "-"), 0)

    def test_div(self):
        self.assertEqual(DZ8_1.arithmetic(6, 2, "/"), 3)

    def test_mul(self):
        self.assertEqual(DZ8_1.arithmetic(3, 3, "*"), 9)
