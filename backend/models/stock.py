from models.currency import Currency

class Stock:
    def __init__(self,ticker:str,stock_name:str=None,currency=Currency,current_price:float=None,id=None):
        self.ticker = ticker
        self.stock_name = stock_name
        self.currency = currency
        self.current_price = current_price
        self.id = id
        # Will only input ticker and get price?