from time import sleep
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.stock_service import StockService
from models.stock import Stock
from pprint import pprint


import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.buy_sell_action_repository as buy_sell_action_repository

user_repository.delete_all()
stock_repository.delete_all()
# buy_sell_action_repository.delete_all()

user = User("william100","William",32001,32001)
user_repository.save(user)

google_stock = StockService.make_stock("GOOGL")
# google_stock.fetch_price()
stock_repository.save(google_stock)



position = BuySellActionService.make_postion(google_stock,20,"BUY",user)
pprint(vars(position))
buy_sell_action_repository.save(position)
