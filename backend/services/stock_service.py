from models.stock import Stock
import yahoo_fin.stock_info as si
import pandas as pd

class StockService:


    def find_stock_price(ticker):
        ticker_prices = []
        try:
            market_status = si.get_market_status()
            if market_status == "PRE":
                price = si.get_premarket_price(ticker)
                ticker_prices.append({ticker:price})
                return price
            elif market_status == "POST":
                price = si.get_premarket_price(ticker)
                ticker_prices.append({ticker:price})
                return price
            else: 
                price = si.get_live_price(ticker)
                ticker_prices.append({ticker:price})
                return price
        except:
            return print('find_stock_price: error') 

    def make_stock(ticker):
        return Stock(ticker,si.get_company_info(ticker).loc["longBusinessSummary"].Value[:75]+"...", StockService.find_stock_price(ticker))


    # check if stock exists in db?