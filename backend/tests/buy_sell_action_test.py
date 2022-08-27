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

    @unittest.skip("market open dependent")
    def test_can_sell_by_quantity_on_position(self):
        print(self.user.money)
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,20000,"BUY",self.user)
        dnn.current_price = 2
        position.sell(17000)
        print(position.history)
        print(self.user.money)

    @unittest.skip("market open dependent")
    def test_can_buy_by_quantity_on_position(self):
        print(self.user.money)
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 2
        position.sell(1000)
        position.buy(12345)
        dnn.current_price = 1.02
        position.sell()
        position.buy(100)
        position.buy(100)
        position.buy(23)
        position.sell(300)
        print(position.quantity)
        # print(position.history)
        # print(self.user.money)

    @unittest.skip("market open dependent")
    def test_cannot_sell_more_stock_than_owned(self):
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 2
        position.sell()
        position.buy(100)
        position.buy(100)
        position.buy(23)
        position.sell(300)
        self.assertEqual(223, position.quantity)

    @unittest.skip("market open dependent")
    def test_can_sell_less_stock_than_owned(self):
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 2
        position.sell()
        position.buy(100)
        position.buy(100)
        position.buy(23)
        position.sell(200)
        self.assertEqual(23, position.quantity)

    @unittest.skip("market open dependent")
    def test_can_sell_less_stock_than_owned(self):
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 2
        position.sell()
        position.buy(100)
        position.buy(100)
        position.buy(23)
        position.sell(200)
        self.assertEqual(23, position.quantity)

    @unittest.skip("market open dependent")
    def test(self):
        print("user money:",self.user.money)
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 2
        position.sell()
        position.buy(100)
        position.buy(100)
        position.buy(23)
        position.sell(200)
        print("running p/l:", position.running_pl)
        print("average price:", position.average_price)
        dnn.current_price = 1.54
        print("running p/l:", position.running_pl)
        print("average price:", position.average_price)
        position.buy(12000)
        print("average price:", position.average_price)
        dnn.current_price = 3
        print("running p/l:", position.running_pl)
        print("average price:", position.average_price)
        print(position.history)
        position.sell()
        print("user money:",self.user.money)
        # self.assertEqual(23, position.quantity)
        
    @unittest.skip("FAILS: TODO")
    def test_average_price_should_be_0_when_all_sold(self):
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 5
        position.sell()
        self.assertEqual(0,position.average_price)

    def test_average_price_should_reflect_sell(self):
        dnn = StockService.make_stock("DNN")
        position = BuySellActionService.make_postion(dnn,2000,"BUY",self.user)
        dnn.current_price = 5
        position.sell(1000)
        print("avg price:",position.average_price)