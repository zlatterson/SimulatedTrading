import unittest

from models.call_put_option import CallPutOption
from models.stock import Stock
from services.call_put_option_service import CallPutOptionService
from services.stock_service import StockService

class TestCallPut(unittest.TestCase):
    def setUp(self):
        self.stock = StockService.make_stock("AMZN")
        self.google_stock = StockService.make_stock("GOOGL")

    def _can_have_a_call_put_type(self):
        CPO = CallPutOption(self.stock,"PUT")
        self.assertEqual("PUT",CPO.call_put_type)
    
    def _can_get_calls(self):
        print(self.stock.current_price)
        calls = CallPutOptionService.find_calls("GOOGL")
        print(calls)
        # self.assertEqual()
    def test_can_get_call_contract_price(self):
        # contract_price = CallPutOptionService.find_contract("GOOGL220826C00075000")
        # print(contract_price)
        google_call = CallPutOption("GOOGL220826C00075000",self.google_stock,1,"CALL")
        self.assertTrue(100 > google_call.calc_contract_simulated_value())

    def test_can_get_a_put_price(self):
        CallPutOptionService.find_puts("")