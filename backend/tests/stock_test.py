import unittest
from models.stock import Stock

class TestStockWrapper(unittest.TestCase):
    def setUp(self):
        self.stock = Stock("DNN")

    def test_stock_currency_can_only_be_enum(self):
        self.stock()
