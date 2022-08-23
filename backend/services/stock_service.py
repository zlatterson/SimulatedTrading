from models.stock import Stock
import yahoo_fin.stock_info as si
import pandas as pd

class StockService:

    def __init__(self,ticker):
        self.ticker = ticker

    def find_stock_price(ticker):
        try:
            if si.get_market_status() == "PRE":
                return si.get_premarket_price(ticker)
            else: return si.get_premarket_price(ticker)
        except:
            return print('hi') 

    def make_stock(ticker):
        try:
            return Stock(ticker,si.get_company_info(ticker).loc["longBusinessSummary"].Value, StockService.find_stock_price(ticker))
        except:
            return print('hi')

    # check if stock exists in db?