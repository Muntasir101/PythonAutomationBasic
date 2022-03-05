import unittest

from Package1.TC_LoginTest import Login
from Package1.TC_SignUp import SignUp

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnTest import PaymentReturn

# Get all the tests method from LoginTest | SignUp Test | PaymentTest | PaymentReturnTest

test_case1 = unittest.TestLoader().loadTestsFromTestCase(Login)
test_case2 = unittest.TestLoader().loadTestsFromTestCase(SignUp)
test_case3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
test_case4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

# Creating Sanity Test Suite - Include "Login Test" & "SignUp Test"

# sanity_test_suite = unittest.TestSuite([test_case1, test_case2])
# unittest.TextTestRunner().run(sanity_test_suite)

# Creating Functional Test Suite

# functional_test_suite = unittest.TestSuite([test_case3, test_case4])
# unittest.TextTestRunner().run(functional_test_suite)

# Creating Master Test Suite

master_test_suite = unittest.TestSuite([test_case1, test_case2, test_case3, test_case4])
unittest.TextTestRunner(verbosity=2).run(master_test_suite)
