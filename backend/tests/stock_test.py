import unittest
from models.stock import Stock
from services.stock_service import StockService

class TestStock(unittest.TestCase):
    def setUp(self):
        self.stock = StockService.make_stock("AMZN")

    def test_stock_can_be_made(self):
        print(self.stock.current_price)
        print(self.stock.fetch_price())