from models.stock import Stock
import pandas as pd

from models.user import User

class CallPutContract():
    def __init__(self,contract_name:str,stock:Stock,call_put_type:str,current_c_price,k:float,expires,id=None):
        self.contract_name = contract_name
        self.stock = stock
        self.call_put_type = call_put_type
        self.k = k
        self.expires = expires
        self.current_c_price = current_c_price
        self.current_contract_value = current_c_price * 100
        self.id = id
    
    def fetch_c_price(self):
        from services.call_put_contract_service import CallPutContractService
        updated_contract = CallPutContractService.find_contract(self.contract_name)
        updated_price = CallPutContractService.calc_c_simulated_price(updated_contract)
        updated_price = 65
        print(updated_price)
        self.current_c_price = updated_price
