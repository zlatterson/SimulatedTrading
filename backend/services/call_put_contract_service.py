from yahoo_fin import options
import yahoo_fin.stock_info as si
import pandas as pd
from models.call_put_contract import CallPutContract
from models.call_put_option import CallPutOption
from services.market_service import MarketService

class CallPutContractService:

    def find_calls(ticker):
        return options.get_calls(ticker)

    def find_puts(ticker):
        return options.get_puts(ticker)

    def find_contract(contract_name):
        # MarketService.market_open()
        return options.get_options_chain(contract_name)
    
    def make_contract(contract_name, stock, call_put_type):
        # MarketService.market_open()
        contract = CallPutContractService.find_contract(contract_name)
        c_price = CallPutContractService.calc_c_simulated_price(contract)
        expire_date = contract["puts"].loc[0][1]
        strike_price = contract["calls"].loc[4][1]
        return CallPutContract(contract_name,stock,call_put_type,c_price,strike_price,expire_date)

    # returns the midpoint between buy price and ask price
    def calc_c_simulated_price(contract):
        return (contract["calls"].loc[2][1] + contract["calls"].loc[3][1]) / 2
    
