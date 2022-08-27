from models.stock import Stock
import pandas as pd

from models.user import User

class CallPutContract():
    def __init__(self,contract_name:str,stock:Stock,call_put_type:str,k:float,expires,id=None,current_c_price=None):
        self.contract_name = contract_name
        self.stock = stock
        self.call_put_type = call_put_type
        self.k = k
        self.expires = expires
        self.current_c_price = current_c_price
        self.id = id
 
    @property
    def current_contract_value(self):
        """Returns value of one contract
        """
        return self.current_c_price * 100
    
    def fetch_c_price(self):
        from services.call_put_contract_service import CallPutContractService
        updated_contract = CallPutContractService.find_contract(self.contract_name)
        updated_price = CallPutContractService.calc_c_simulated_price(updated_contract)
        self.current_c_price = updated_price