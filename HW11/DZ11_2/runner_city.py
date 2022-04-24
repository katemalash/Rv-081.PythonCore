import uTestDZ7_3
import unittest


calcTestS = unittest.TestSuite()
calcTestS.addTest(unittest.makeSuite(uTestDZ7_3.TestCity))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestS)
