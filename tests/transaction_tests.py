import unittest
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant

class TestTransaction(unittest.TestCase):

    def setUp(self):
        self.tag1 = Tag("food", True, 1)
        self.merchant1 = Merchant("Tesco", True, 5)
        self.transaction1 = Transaction(5000, self.tag1, self.merchant1, 2020-10-20, 1)
        self.transaction2 = Transaction(5000, self.tag1, self.merchant1, '20201020', 1)

    def test_transaction_has_amount(self):
        self.assertEqual(5000, self.transaction1.amount)

    def test_transaction_has_tag_object(self):
        self.assertEqual(self.tag1, self.transaction1.tag)

    def test_extract_tag_details(self):
        self.assertEqual("food", self.transaction1.tag.spending_type)

    def test_extract_tag_id(self):
        self.assertEqual(1, self.transaction1.tag.id)

    def test_extract_tag_active(self):
        self.assertEqual(True, self.transaction1.tag.active)

    def test_transaction_has_merchant_object(self):
        self.assertEqual(self.merchant1, self.transaction1.merchant)

    def test_extract_merchant_details(self):
        self.assertEqual("Tesco", self.transaction1.merchant.name)

    def test_extract_merchant_id(self):
        self.assertEqual(5, self.transaction1.merchant.id)

    def test_extract_merchant_active(self):
        self.assertEqual(True, self.transaction1.merchant.active)

    def test_transaction_has_date(self):
        self.assertEqual(2020-10-20, self.transaction1.date)

    def test_transaction_has_readable_date(self):
        self.assertEqual('20201020', self.transaction2.date)
    # this isn't testing the correct formatting of date though; is only testing that the string '20201020' is what is in place of date attribute.


    

