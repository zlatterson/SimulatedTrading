from models.call_put_contract import CallPutContract
from models.stock import Stock
import pandas as pd

from models.user import User

class CallPutOption():
    def __init__(self,call_put_contract:CallPutContract,n_contracts:int,buy_sell_type:str,bought_c_price:float,bought_contracts_value:float,user:User,id=None):
        self.call_put_contract = call_put_contract
        self.buy_sell_type = buy_sell_type
        self.n_contracts = n_contracts
        self.bought_c_price = bought_c_price
        self.bought_contracts_value = bought_contracts_value

        self.pseudo_premium = call_put_contract.stock.current_price - call_put_contract.k
        self.current_contracts_value = call_put_contract.current_contract_value * self.n_contracts
        self.running_pl = (self.bought_contracts_value * self.n_contracts - self.current_contracts_value) - self.pseudo_premium
        self.running_pl_percentage = self.running_pl / self.bought_contracts_value * 100
        
        self.user = user
        self.id = id