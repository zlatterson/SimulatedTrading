class Stock:
    def __init__(self,ticker,summary,id=None,current_price=None):
        self.ticker = ticker
        self.summary = summary
        self.current_price = current_price
        self.currency = "USD"
        self.id = id

    def fetch_price(self):
        from services.stock_service import StockService
        self.current_price = StockService.find_stock_price(self.ticker)