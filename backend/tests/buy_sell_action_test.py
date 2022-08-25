import unittest
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from time import sleep

from services.stock_service import StockService
class TestBuySellAction(unittest.TestCase):
    def setUp(self):
        self.amazon_stock = StockService.make_stock("AMZN")
        self.google_stock = StockService.make_stock("GOOGL")
        self.user = User("william100","William",32001)

    @unittest.skip("market open dependent")
    def test_can_make_position(self):
        position = BuySellActionService.make_postion(self.google_stock,20,"BUY",self.user)
        print(position.current_price)
        print("total value:", position.bought_value)
        sleep(10)
        self.google_stock.fetch_price()
        print("total value now:", position.current_value)
        print(position.current_price)
        print(position.running_pl)
        print(position.running_pl_percentage)

    @unittest.skip("market open dependent")
    def test_can_make_position(self):
        position = BuySellActionService.make_postion(self.google_stock,20,"BUY",self.user)
        print(position.current_price)
        print("total value:", position.bought_total_price)
        sleep(10)
        self.google_stock.fetch_price()
        print("total value now:", position.current_total_price)
        print(position.current_price)
        print(position.running_pl)
        print(position.running_pl_percentage)

    @unittest.skip("market open dependent")
    def test_can_close_position(self):
        print(self.user.money)
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,10000,"BUY",self.user)
        dnn.current_price = 2
        position.close()
        print(self.user.money)

    # @unittest.skip("market open dependent")
    def test_can_close_quantity_on_position(self):
        print(self.user.money)
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,20000,"BUY",self.user)
        dnn.current_price = 2
        position.close(17000)
        print(self.user.money)