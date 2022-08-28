class Stock:
    def __init__(self,ticker,summary,id=None,current_price=None):
        self.ticker = ticker
        self.summary = summary
        self._current_price = None
        self.currency = "USD"
        self.id = id

    @property
    def current_price(self):
        return self._current_price

    @current_price.setter
    def current_price(self, value):
        print("setter of x called")
        self._current_price = value

    def fetch_price(self):
        from services.stock_service import StockService
        self.current_price = StockService.find_stock_price(self.ticker)