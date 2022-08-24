import unittest

from models.call_put_option import CallPutOption
from models.stock import Stock
from models.user import User
from services.call_put_option_service import CallPutOptionService
from services.stock_service import StockService

class TestCallPut(unittest.TestCase):
    def setUp(self):
        self.stock = StockService.make_stock("AMZN")
        self.google_stock = StockService.make_stock("GOOGL")
        self.user = User("Daniel100","Daniel",32100.5)

    @unittest.skip("cumbersome test")
    def _can_have_a_call_put_type(self):
        cpo = CallPutOption(self.stock,"PUT")
        self.assertEqual("PUT",cpo.call_put_type)
    
    @unittest.skip("cumbersome test")
    def _can_get_calls(self):
        print(self.stock.current_price)
        calls = CallPutOptionService.find_calls("GOOGL")
        print(calls)
        # self.assertEqual()

    @unittest.skip("cumbersome test")
    def test_can_get_call_contract_price(self):
        # contract_price = CallPutOptionService.find_contract("GOOGL220826C00075000")
        # print(contract_price)
        google_call = CallPutOption("GOOGL220826C00075000",self.google_stock,1,"BUY","CALL",self.user)
        self.assertTrue(100 > google_call.calc_contract_simulated_value())
    
    @unittest.skip("outdated test")
    def test_can_get_a_put_price(self):
        worst_put_in_history = CallPutOption("GOOGL220826P00070000", self.google_stock,1,"BUY","PUT",self.user)
        print(worst_put_in_history.calc_contract_simulated_value())

    def test_can_get_call_put_valeu(self):
        # worst_put_in_history = CallPutOption("GOOGL220826P00070000", self.google_stock,1,"BUY","PUT",self.user)
        res = CallPutOptionService.indv_tester("GOOGL220826P00070000")
        print(res)
        google_stock = StockService.make_stock("GOOGL")
        call_position = CallPutOptionService.make_position("GOOGL220826C00075000","BUY","CALL",google_stock,2,self.user)
        print(call_position)