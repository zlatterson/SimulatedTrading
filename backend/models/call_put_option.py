from models.stock import Stock
import pandas as pd

class CallPutOption:
    def __init__(self,contract_name:str,stock:Stock,n_contracts:int,call_put_type:str,id=None):
        self.ticker = stock.ticker
        self.type = call_put_type
        self.contract_name = contract_name
        self.n_contracts = n_contracts
        self.bought_contract_price = None
        self.current_contract_value = None
        self.id = id
# contract(100 stocks) value is based on the greeks and stock price and iv
# profit is is how much you close the contract vs how much u paid for it

# simulated contract price will be directly in between bid and ask price
    def fetch_contract(self):
        from services.call_put_option_service import CallPutOptionService
        return CallPutOptionService.find_contract(self.contract_name)
    
    #returns the middlepoint value between bid and ask
    def calc_contract_simulated_value(self):
        contract = self.fetch_contract()
        if(self.type == "CALL"):
            return ((contract["calls"].loc[2][1] + contract["calls"].loc[3][1]) / 2)
        elif(self.type == "PUT"):
            return ((contract["puts"].loc[2][1] + contract["puts"].loc[3][1]) / 2)
