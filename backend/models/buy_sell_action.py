from datetime import datetime
from models.stock import Stock
from models.user import User

class BuySellAction():
    def __init__(self,stock:Stock,bought_price:float,quantity:int,buy_sell_type:str,timestamp,user:User,id=None):
        self.stock = stock
        self.buy_sell_type = buy_sell_type
        self.quantity = quantity
        self.bought_price = bought_price
        self.history = [str(timestamp),{"Type":buy_sell_type,"Price":bought_price,"Quantity":quantity}]
        self.user = user
        self.id = id

    @property
    def current_price(self):
        """Gets the live price from Stock.
        """
        return self.stock.current_price

    @property
    def current_total_price(self):
        """Returns the current total value of the asset for position's quantity.
        """
        return self.current_price * self.quantity

    @property
    def bought_total_price(self):
        """Returns the total value of the asset for which the user paid.
        """
        return self.bought_price * self.quantity

    @property
    def running_pl(self):
        """Returns running profit or loss.
        """
        return self.current_total_price - self.bought_total_price
    @property
    def running_pl_percentage(self):
        """Returns running profit or loss as percentage.
        """
        return (self.running_pl / self.quantity) / self.bought_price * 100

    def buy(self,buy_quantity):
        from services.buy_sell_action_service import BuySellActionService
        self.quantity += BuySellActionService.buy_order(self.stock,self.user,buy_quantity)
        self.history.extend((str(datetime.now()),{"Type":"BUY","Price":self.stock.current_price,"Quantity":buy_quantity}))

    def sell(self,sell_quantity=None):
        if sell_quantity==None:
            sell_quantity = self.quantity
        if sell_quantity <= self.quantity:
            from services.buy_sell_action_service import BuySellActionService
            self.quantity -= BuySellActionService.sell_order(self.stock,self.user,sell_quantity)
            self.history.extend((str(datetime.now()),{"Type":"SELL","Price":self.stock.current_price,"Quantity":sell_quantity}))