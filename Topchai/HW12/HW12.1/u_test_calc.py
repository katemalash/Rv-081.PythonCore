import calc
import unittest

class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1,2),3)
        
    def test_sub(self):
        self.assertEqual(calc.sub(3,1),2)
        
    def test_mul(self):
        self.assertEqual(calc.mul(3,2),6)
        
    def test_div(self):
        self.assertEqual(calc.div(4,2),2)

if __name__ == "__main__":
    unittest.main()

