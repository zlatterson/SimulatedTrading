import unittest

from models.stock_wrapper import StockWrapper
from services.stock_service import StockService


class TestStock(unittest.TestCase):
        def setUp(self):
            self.stock_wrapper = StockWrapper()
            self.stock_service = StockService()

        def testApp(self):
            self.stock_wrapper.stock = self.stock_service.findStock("DNN")
            self.assertEqual(10, )