import u_test_deposit
import unittest

depositTestS = unittest.TestSuite()
depositTestS.addTest(unittest.makeSuite(u_test_deposit.DepositTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(depositTestS)