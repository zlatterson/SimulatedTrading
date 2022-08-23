class Stock:
    def __init__(self,ticker:str,summary:str=None,current_price:float=None,id=None):
        self.ticker = ticker
        self.summary = summary
        self.currency = "USD"
        self.current_price = current_price
        self.id = id
        # Will only input ticker and get summary, price
        # Will have a live price

    def fetch_price(self):
        from services.stock_service import StockService
        self.current_price = StockService.find_stock_price(self.ticker)