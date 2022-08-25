from datetime import datetime
from models.buy_sell_action import BuySellAction
import yahoo_fin.stock_info as si

from models.stock import Stock
from models.user import User
from services.market_service import MarketService


class BuySellActionService:

    def make_postion(stock:Stock,quantity,buy_sell_type,user:User):
        # MarketService.market_open()
        if buy_sell_type == "BUY":
            order_cost = stock.current_price * quantity
            if user.money >= order_cost:
                user.money -= order_cost
                return BuySellAction(stock,stock.current_price,quantity,buy_sell_type,datetime.now(),user)
            else:
                raise Exception("Not enough money")


    def close_position(stock:Stock,user:User,quantity=None):
        # MarketService.market_open()
        user.money += stock.current_price * quantity
        return quantity
