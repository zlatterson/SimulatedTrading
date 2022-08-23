class Stock:
    def __init__(self,ticker:str,summary:str,current_price:float,id=None):
        self.ticker = ticker
        self.summary = summary
        self.currency = "USD"
        self.current_price = current_price
        self.id = id

    def fetch_price(self):
        from services.stock_service import StockService
        self.current_price = StockService.find_stock_price(self.ticker)