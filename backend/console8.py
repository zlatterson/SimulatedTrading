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

user_repository.save(User("Martin500","Martin M",103.2,103.2))
user_repository.save(User("James400","James M",99.2,99.2))


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
print(result[1].money)
user.money = result[1].money
user_repository.update(user)

result2 = BuySellActionService.make_postion(dnn,123000,"BUY",user)
buy_sell_action_repository.save(result2[0])
user.money = result2[1].money
user_repository.update(result2[1])
print(result2[1].money)

mrman = user_repository.select(1)
pprint(vars(mrman))

ps = user_repository.buy_sell_actions(mrman)

total_profit = 0
for p in ps:
    pprint(vars(p))
    p.current_price
    total_profit += p.running_pl
print("total prift:", total_profit)
print("total spent: ", mrman.money - mrman.money_paid_in)

tick = "AMZN"
try:
    stock = stock_repository.select_by_ticker(tick)
except IndexError:
    new_stock = StockService.make_stock(tick)
    stock_repository.save(new_stock)

# if stock == None:
#     print("hi")

# StockService.make_stock(tick)
# try:
#     StockService.make_stock(tick)
# except:
#     pass
# else:
#     stock_repository.select_by_ticker(tick)