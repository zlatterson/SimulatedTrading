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
# _______

stock = StockService.make_stock("GOOGL")
stock_repository.save(stock)
googl = stock_repository.select(1)
googl.fetch_price()
googl.current_price = 70
# _______
stock = StockService.make_stock("DNN")
stock_repository.save(stock)
dnn = stock_repository.select(2)
dnn.fetch_price()
dnn.current_price = 0.5
# ________

result = BuySellActionService.make_postion(googl,20,"BUY",user)
buy_sell_action_repository.save(result[0])
user.money = result[1].money
user_repository.update(user)

result = BuySellActionService.make_postion(dnn,1000,"BUY",user)
buy_sell_action_repository.save(result[0])
user.money = result[1].money
user_repository.update(result[1])

# MESS DATA IGNORE
# user2 = User("Danny1","Danny",100000,100000)
# user_repository.save(user2)
# danny = user_repository.select(2)

# position2 = BuySellActionService.make_postion(googl,20,"BUY",danny)
# buy_sell_action_repository.save(position2)

# 
position = buy_sell_action_repository.select(1)
position.current_price
position.sell(3)
buy_sell_action_repository.update(position)
# googl.current_price = 300
# stock_repository.update(googl)
res = user_repository.buy_sell_actions(jimmy)
# pprint(vars(res[0].stock))
# res[0].current_price
# pprint(vars(res[0].stock))
# print("running_pl: ",res[0].running_pl)
# print("percentage: ",res[0].running_pl_percentage)
r_perc = 0
total_prof = 0
total_pos_cost = 0
total_pos_value = 0
ids = []
for r in res:
    ids.append(r.id)
    total_pos_cost -= r.bought_total_price
    total_pos_value += r.current_total_price
    r_perc += r.running_pl_percentage
    total_prof += r.running_pl
total_perc = r_perc / len(res)

print(jimmy.username," is +",total_perc, "%")
print(jimmy.username," is + $",total_prof, "costing: ",total_pos_cost, "now worth: ",total_pos_value)
print("total_assets: $", jimmy.money_paid_in,jimmy.money, total_prof)

specifc_pos = buy_sell_action_repository.select(ids[0])
print(specifc_pos.quantity)
specifc_pos.current_price
specifc_pos.sell()
print(specifc_pos.quantity)


r_perc = 0
total_prof = 0
ids = []
for r in res:
    ids.append(r.id)
    r_perc += r.running_pl_percentage
    total_prof += r.running_pl
total_perc = r_perc / len(res)

print(jimmy.username," is +",total_perc, "%")
print(jimmy.username," is + $",total_prof)
print("total_assets: $", jimmy.money_paid_in,jimmy.money, total_prof)

print(result[0])
print(result[1].money)