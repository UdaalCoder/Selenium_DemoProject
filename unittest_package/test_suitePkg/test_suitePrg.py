import  unittest
#step1
from unittest_package.test_fixtures import TestFixEx
from unittest_package.test_skipprg import TestSkip

#step 2
testcase1 = unittest.TestLoader().loadTestsFromTestCase(TestFixEx)
testcase2 = unittest.TestLoader().loadTestsFromTestCase(TestSkip)

#step 3
suite = unittest.TestSuite([testcase1,testcase2])

#step 4
unittest.TextTestRunner().run(suite)