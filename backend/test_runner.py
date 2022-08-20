import unittest

from models.stock_wrapper import StockWrapper
from services.stock_service import StockService


class TestApp(unittest.TestCase):
    # def setUp(self):
    #     self.stock_service = StockService()
    #     stock_to_find = self.stock_service.findStock("DNN")
    #     self.stock_wrapper = StockWrapper(stock_to_find)

    def testApp(self):
        self.stock_service = StockService()
        stock_to_find = self.stock_service.findStock("DNN")
        self.stock_wrapper = StockWrapper(stock_to_find)
        self.assertEqual(1.0499999523162842, self.stock_wrapper.stock.stock)

if __name__ == "__main__":
    unittest.main()