import uTestDZ8_3
import unittest


calcTestS = unittest.TestSuite()
calcTestS.addTest(unittest.makeSuite(uTestDZ8_3.TestDate))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestS)
