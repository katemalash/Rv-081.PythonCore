import u_test
import unittest


calcTestS = unittest.TestSuite()
calcTestS.addTest(unittest.makeSuite(u_test.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestS)
