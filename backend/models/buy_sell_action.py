from datetime import datetime
from models.stock import Stock
from models.user import User

class BuySellAction():
    """
    TODO:
    Change bought_price to average_price
    Add funtionality to dynamically change average price
    """
    
    def __init__(self,stock:Stock,init_price:float,quantity:int,buy_sell_type:str,timestamp,user:User,id=None):
        self.stock = stock
        self.buy_sell_type = buy_sell_type
        self.quantity = quantity
        self.average_price = init_price
        self.history = [str(timestamp),{"Type":buy_sell_type,"Price":init_price,"Quantity":quantity}]
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
        return self.average_price * self.quantity

    @property
    def running_pl(self):
        """Returns running profit or loss.
        """
        return self.current_total_price - self.bought_total_price
    @property
    def running_pl_percentage(self):
        """Returns running profit or loss as percentage.
        """
        return (self.running_pl / self.quantity) / self.average_price * 100

    def calc_new_average_price(self,buy_quantity):
        return ((self.average_price * self.quantity) + (self.stock.current_price * buy_quantity)) / (self.quantity + buy_quantity)
    
    def buy(self,buy_quantity):
        potential_average_price = self.calc_new_average_price(buy_quantity)
        from services.buy_sell_action_service import BuySellActionService
        self.quantity += BuySellActionService.buy_order(self.stock,self.user,buy_quantity)
        self.average_price = potential_average_price
        self.invoice("BUY",buy_quantity)


    def sell(self,sell_quantity=None):
        if sell_quantity==None:
            sell_quantity = self.quantity
        if sell_quantity <= self.quantity:
            from services.buy_sell_action_service import BuySellActionService
            self.quantity -= BuySellActionService.sell_order(self.stock,self.user,sell_quantity)
            self.invoice("SELL",sell_quantity)
    
    def invoice(self,transaction_type,quantity):
        self.history.extend((str(datetime.now()),{"Type":transaction_type,"Stock Price":self.stock.current_price,"Quantity":quantity}))