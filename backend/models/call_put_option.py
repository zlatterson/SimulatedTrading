from models.stock import Stock
import pandas as pd

from models.user import User

class CallPutOption:
    def __init__(self,contract_name:str,stock:Stock,n_contracts:int,buy_sell_type:str,call_put_type:str,bought_contract_value:float,user:User,id=None):
        self.contract_name = contract_name
        self.ticker = stock.ticker
        self.buy_sell_type = buy_sell_type
        self.call_put_type = call_put_type
        self.n_contracts = n_contracts
        self.bought_contract_value = bought_contract_value
        self.current_contract_value = None
        self.user = user
        self.id = id

    def get_current_contract_value():
        pass
    def get_bought_contracts_price():
        pass
    def get_current_contracts_price():
        pass


    def get_running_p_l():
        pass
    def get_running_p_l_percentage():
        pass
# contract(100 stocks) value is based on the greeks and stock price and iv
# profit is is how much you close the contract vs how much u paid for it
