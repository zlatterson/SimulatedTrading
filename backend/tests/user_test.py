from time import sleep
import unittest
from models.stock import Stock
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.stock_service import StockService

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("william100","William",32001)
        self.AMZN = StockService.make_stock("AMZN")
        self.GOOGL = StockService.make_stock("GOOGL")

    def test_user_can_own_stock(self):
        print("initial money:", self.user.money)
        position = BuySellActionService.make_postion(self.GOOGL,20,"BUY",self.user)
        print("current money:", self.user.money)
        print(position.average_price)