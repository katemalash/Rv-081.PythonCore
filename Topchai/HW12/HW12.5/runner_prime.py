import u_test_prime
import unittest

primeTestS = unittest.TestSuite()
primeTestS.addTest(unittest.makeSuite(u_test_prime.PrimeTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(primeTestS)