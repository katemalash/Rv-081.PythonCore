import u_test_checker
import unittest

yearTestS = unittest.TestSuite()
yearTestS.addTest(unittest.makeSuite(u_test_checker.YearTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(yearTestS)