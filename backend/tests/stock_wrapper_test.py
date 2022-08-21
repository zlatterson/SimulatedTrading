import unittest
from models.stock_wrapper import StockWrapper
from services.stock_service import StockService

class TestStockWrapper(unittest.TestCase):
    def setUp(self):
        self.stock_service = StockService()
        stock_to_find = self.stock_service.findStock("DNN")
        self.stock_wrapper = StockWrapper(stock_to_find)

    def test_stock_wrapper_can_get_price(self):
        self.assertEqual(1.0499999523162842, self.stock_wrapper.stock.stock)
    
    def test_can_get_last_access(self):
        self.assertEqual(102121, self.stock_service.findOptions("GOOGL"))