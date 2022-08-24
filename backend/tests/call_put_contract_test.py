import unittest

from time import sleep
from models.stock import Stock
from services.call_put_contract_service import CallPutContractService
from services.call_put_option_service import CallPutOptionService
from services.stock_service import StockService

class TestCallPutContract(unittest.TestCase):
    def setUp(self):
        self.amazon_stock = StockService.make_stock("AMZN")
        self.google_stock = StockService.make_stock("GOOGL")

    @unittest.skip("cumbersome test")
    def test_can_find_calls(self):
        calls = CallPutContractService.find_calls(self.google_stock.ticker)
        print(calls)

    @unittest.skip("PASSES cumbersome test")
    def test_can_make_contract(self):
        contract = CallPutContractService.make_contract("GOOGL220826C00055000",self.google_stock,"CALL")
        self.assertEqual("2022-08-26",contract.expires)
    
    # @unittest.skip("PASSES cumbersome test")
    def test_can_update_c_price(self):
        contract = CallPutContractService.make_contract("GOOGL220826C00055000",self.google_stock,"CALL")
        init_c = contract.current_contract_value
        print(init_c)
        sleep(1000)
        contract.fetch_c_price()
        updated_c = contract.current_contract_value
        print(updated_c)
