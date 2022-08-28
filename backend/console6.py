from time import sleep
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.call_put_contract_service import CallPutContractService
from services.call_put_option_service import CallPutOptionService
from services.stock_service import StockService
from models.stock import Stock
from pprint import pprint
 
import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.buy_sell_action_repository as buy_sell_action_repository
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository

user_repository.delete_all()
stock_repository.delete_all()
call_put_contract_repository.delete_all()
buy_sell_action_repository.delete_all()
call_put_option_repository.delete_all()

user = User("Jimmy120","Jimmy",200100.123,200100.123)
user_repository.save(user)
jimmy = user_repository.select(1)

stock = StockService.make_stock("GOOGL")
stock_repository.save(stock)
googl = stock_repository.select(1)
googl.fetch_price()

position = BuySellActionService.make_postion(googl,20,"BUY",user)
buy_sell_action_repository.save(position)


# MESS DATA IGNORE
user2 = User("Danny1","Danny",100000,100000)
user_repository.save(user2)
danny = user_repository.select(2)

position2 = BuySellActionService.make_postion(googl,20,"BUY",danny)
buy_sell_action_repository.save(position2)

# 
position = buy_sell_action_repository.select(1)
position.current_price
position.sell(3)
buy_sell_action_repository.update(position)

googl.current_price = 300
stock_repository.update(googl)

res = user_repository.buy_sell_actions(jimmy)
pprint(vars(res[0].stock))
res[0].stock.fetch_price()
res[0].stock.current_price = 0
pprint(vars(res[0].stock))
print("running_pl: ",res[0].running_pl)
print("percentage: ",res[0].running_pl_percentage)
# print(res[0].stock)
