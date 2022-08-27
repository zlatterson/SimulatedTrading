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
buy_sell_action_repository.delete_all()

user = User("william100","William",32001,32001)
user_repository.save(user)

google_stock = StockService.make_stock("GOOGL")
stock_repository.save(google_stock)



found = stock_repository.select(1)
found.current_price = 114
stock_repository.update(found)
position = BuySellActionService.make_postion(found,20,"BUY",user)
buy_sell_action_repository.save(position)

found.current_price = 200
stock_repository.update(found)

specifc_bsa = buy_sell_action_repository.select(1)
pprint(vars(specifc_bsa))
pprint(vars(position))
specifc_bsa.stock.current_price = 3000
specifc_bsa.buy(2)
# specifc_bsa.sell(19)

user_repository.update(specifc_bsa.user)
print(specifc_bsa.average_price)
print(specifc_bsa.current_price)
print(specifc_bsa.quantity)
buy_sell_action_repository.update(specifc_bsa)
slect = buy_sell_action_repository.select(1)
# pprint(vars(slect))
pprint(vars(specifc_bsa))
print(specifc_bsa.running_pl_percentage)

# user1 = user_repository.select(1)
# print(user1.money, user1.money_paid_in)