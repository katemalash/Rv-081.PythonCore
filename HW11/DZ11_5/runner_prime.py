import uTestDZ8_4
import unittest


calcTestS = unittest.TestSuite()
calcTestS.addTest(unittest.makeSuite(uTestDZ8_4.TestPrime))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestS)
