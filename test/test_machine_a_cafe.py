import unittest
from main import Brewer, CreditCardHandler, CreditCard

class TestBrewer(unittest.TestCase):
    def setUp(self):
        self.brewer = Brewer()

    def test_make_a_coffee(self):
        self.assertTrue(self.brewer.make_a_coffee())

    def test_try_pull_water(self):
        self.assertTrue(self.brewer.try_pull_water())

    def test_pour_milk(self):
        self.assertTrue(self.brewer.pour_milk())

    def test_pour_water(self):
        self.assertTrue(self.brewer.pour_water())

    def test_pour_sugar(self):
        self.assertTrue(self.brewer.pour_sugar())

    def test_pour_chocolate(self):
        self.assertTrue(self.brewer.pour_chocolate())


class TestCreditCardHandler(unittest.TestCase):
    def setUp(self):
        self.card_handler = CreditCardHandler()

    def test_try_charge_amount(self):
        self.assertTrue(self.card_handler.try_charge_amount(50))

    def test_refund(self):
        self.card_handler.refund(50)  # No assertion needed, just ensure no exceptions

class TestCreditCard(unittest.TestCase):
    def setUp(self):
        self.credit_card = CreditCard()
        self.card_handler = CreditCardHandler()

    def test_register_card_detected_callback(self):
        self.credit_card.register_card_detected_callback(self.card_handler)
        # We should check the printed output or the internal state change

if __name__ == '__main__':
    unittest.main()