from models.stock_wrapper import StockWrapper
import yahoo_fin.stock_info as si

class StockService:
    def __init__(self):
        self.self = self

    def findStock(self,ticker):
        try:
            return StockWrapper(si.get_analysts_info(ticker))
        except:
            return print('hi')