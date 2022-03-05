import unittest


class Login(unittest.TestCase):
    def test_loginBy_email(self):
        print("This is Login by Email Test")
        self.assertTrue(True)

    def test_loginBy_facebook(self):
        print("This is Login by Facebook")
        self.assertTrue(True)

    def test_login_by_twitter(self):
        print("This is Login by Twitter")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
