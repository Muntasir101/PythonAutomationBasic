import unittest


class PaymentTest(unittest.TestCase):
    def test_payment_in_dollar(self):
        print("This is Payment in Dollar")
        self.assertTrue(True)

    def test_payment_in_taka(self):
        print("This is Payment in Taka")
        self.assertTrue(True)


if __name__ == "__main___":
    unittest.main()
