import uTestDZ8_2
import unittest


calcTestS = unittest.TestSuite()
calcTestS.addTest(unittest.makeSuite(uTestDZ8_2.DepositTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestS)