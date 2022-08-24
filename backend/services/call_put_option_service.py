from yahoo_fin import options
import yahoo_fin.stock_info as si
import pandas as pd
from models.call_put_option import CallPutOption

class CallPutOptionService:

    def __init__(self,ticker):
        self.ticker = ticker
    
    def find_calls(ticker):
        return options.get_calls(ticker)

    def find_puts(ticker):
        return options.get_puts(ticker)

    def find_contract(contract_name):
        return options.get_options_chain(contract_name)
    
    def make_position(contract_name,buy_sell_type,call_put_type,stock,n_contracts,user):
        market_status = si.get_market_status()
        if market_status != "REGULAR":
            return print("Not open")
        contract_value = CallPutOptionService.calc_bid_ask_simulated_value(CallPutOptionService.find_contract(contract_name))
        if buy_sell_type == "BUY":
            bought_contracts_price = CallPutOptionService.calc_contracts_value_USD(contract_value,n_contracts)
            if user.money >= bought_contracts_price:
                user.money -= bought_contracts_price
                return CallPutOption(contract_name,stock,n_contracts,buy_sell_type,call_put_type,contract_value,user)
            else:
                return print("Not enought money")
        #TODO: add SELL type

    # returns the midpoint between buy price and ask price
    def calc_bid_ask_simulated_value(contract):
        return (contract["calls"].loc[2][1] + contract["calls"].loc[3][1]) / 2
    
    def calc_contracts_value_USD(contract_value, n_contracts):
        return contract_value * n_contracts * 100
