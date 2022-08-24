import unittest

from models.call_put_option import CallPutOption
from models.stock import Stock
from models.user import User
from services.call_put_contract_service import CallPutContractService
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
    
    @unittest.skip("outdated test")
    def test_can_create_call_position(self):
        google_stock = StockService.make_stock("GOOGL")
        print("user money:", self.user.money)
        call_position = CallPutOptionService.make_position("GOOGL220826C00075000","BUY","CALL",google_stock,2,self.user)
        print("user money after purchase:", self.user.money)
        print("bought contract price:", call_position.bought_c_price)
        self.assertTrue(call_position.bought_c_price > 10.475)

    @unittest.skip("outdated test")
    def test_cannot_create_position_without_enough_money(self):
        google_stock = StockService.make_stock("GOOGL")
        call_position = CallPutOptionService.make_position("GOOGL220826C00075000","BUY","CALL",google_stock,20,self.user)
        self.assertEqual(call_position, None)
    
    # @unittest.skip("test since contract class added")
    def test_cannot_create_position_without_enough_money(self):
        google_stock = StockService.make_stock("GOOGL")
        google_call_contract = CallPutContractService.make_contract("GOOGL220826C00055000",google_stock,"CALL")
        print("user money before call: ",self.user.money)
        user_google_call = CallPutOptionService.make_position(google_call_contract,"BUY",2,self.user)
        print("user money after call: ", self.user.money)