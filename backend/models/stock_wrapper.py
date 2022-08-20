from datetime import datetime


class StockWrapper:
    def __init__(self,stock):
        self.stock = stock
        self.last_access = datetime.now()
