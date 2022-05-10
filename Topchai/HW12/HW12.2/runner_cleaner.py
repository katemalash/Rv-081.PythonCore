import u_test_cleaner
import unittest

cleanerTestS = unittest.TestSuite()
cleanerTestS.addTest(unittest.makeSuite(u_test_cleaner.CleanerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(cleanerTestS)