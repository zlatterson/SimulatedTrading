from datetime import datetime
from yahoo_fin import options
import yahoo_fin.stock_info as si
import pandas as pd
from models.call_put_contract import CallPutContract
from models.call_put_option import CallPutOption
from services.market_service import MarketService

class CallPutOptionService:
    """
    TODO:
    Calculate premium before purchase is made.
    Add SELL type to sell calls
    Add ability to BUY/SELL puts
    """
    def find_calls(ticker):
        return options.get_calls(ticker)

    def find_puts(ticker):
        return options.get_puts(ticker)

    def find_contract(contract_name):
        return options.get_options_chain(contract_name)
    
    def make_position(contract:CallPutContract,buy_sell_type,n_contracts,user):
        MarketService.market_open()
        if buy_sell_type == "BUY":
            order_cost = contract.current_contract_value * n_contracts
            if user.money >= order_cost:
                user.money -= order_cost
                return CallPutOption(contract,n_contracts,buy_sell_type,contract.current_c_price,contract.current_contract_value,datetime.now(),user)
            else:
                raise Exception("Not enough money")

    # returns the midpoint between buy price and ask price
    def calc_c_simulated_price(contract):
        return (contract["calls"].loc[2][1] + contract["calls"].loc[3][1]) / 2
    
    def calc_contracts_value_USD(contract_value, n_contracts):
        return contract_value * n_contracts * 100
