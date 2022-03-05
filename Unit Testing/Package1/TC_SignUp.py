import unittest


class SignUp(unittest.TestCase):
    def test_signUp_by_email(self):
        print("This is Sign Up By Email")
        self.assertTrue(True)

    def test_signUp_by_facebook(self):
        print("This is Sign Up by Facebook")
        self.assertTrue(True)

    def test_signUp_by_twitter(self):
        print("This is Sign Up By Twitter")
        self.assertTrue(True)

    def test_signUp_by_gmail(self):
        print("This is Sign Up By Gmail")
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
