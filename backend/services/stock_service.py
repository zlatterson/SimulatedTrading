from models.stock_wrapper import StockWrapper
import yahoo_fin.stock_info as si

class StockService:
    def __init__(self):
        self.self = self

    def findStock(self,ticker):
        try:
            print(StockWrapper(si.get_live_price(ticker)).stock)
            print(StockWrapper(si.get_live_price(ticker)).last_access)
            return StockWrapper(si.get_live_price(ticker))
        except:
            return print('hi')