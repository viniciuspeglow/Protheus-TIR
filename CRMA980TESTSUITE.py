import unittest

from CRMA980TESTCASE import CRMA980

suite = unittest.TestSuite()

suite.addTest(CRMA980('test_CRMA980_001'))
suite.addTest(CRMA980('test_CRMA980_002'))
suite.addTest(CRMA980('test_CRMA980_003'))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)