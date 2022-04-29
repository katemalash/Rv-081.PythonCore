import unittest 
import calc


class CalcTest(unittest.TestCase):
    def test_addit(self):
        self.assertEqual(calc.addit(1, 9), 10)
    
    def test_substr(self):
        self.assertEqual(calc.substr(8, 2), 6)
    
    def test_mult(self):
        self.assertEqual(calc.mult(5, 7), 35)
    
    def test_div(self):
        self.assertEqual(calc.div(70, 2), 35)

if __name__ == '__main__':
    unittest.main()