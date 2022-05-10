import u_test_calc
import unittest

calcTestS = unittest.TestSuite()
calcTestS.addTest(unittest.makeSuite(u_test_calc.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestS)