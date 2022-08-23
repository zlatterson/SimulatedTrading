from models.stock import Stock
import yahoo_fin.stock_info as si
import pandas as pd

class StockService:

    def __init__(self,ticker):
        self.ticker = ticker

    def find_stock_price(ticker):
        try:
            market_status = si.get_market_status()
            if market_status == "PRE":
                return si.get_premarket_price(ticker)
            elif market_status == "POST":
                return si.get_postmarket_price(ticker)
            else: 
                return si.get_live_price(ticker)
        except:
            return print('find_stock_price: error') 

    def make_stock(ticker):
        return Stock(ticker,si.get_company_info(ticker).loc["longBusinessSummary"].Value, StockService.find_stock_price(ticker))


    # check if stock exists in db?