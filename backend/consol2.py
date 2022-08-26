from time import sleep
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.stock_service import StockService
from models.stock import Stock
from pprint import pprint


import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository

user_repository.delete_all()
stock_repository.delete_all()

user = User("thinkingobject1","Jimmy",1100.123,1100.123)
user_repository.save(user)


google_stock = StockService.make_stock("GOOGL")
pprint(vars(google_stock))
stock_repository.save(google_stock)


all_stocks = stock_repository.select_all()
for st in all_stocks:
    st.fetch_price()
    pprint(vars(st))
    print(st.id, st.current_price)

stocky = stock_repository.select(39)
stocky.fetch_price()
print(stocky.current_price)
# user = user_repository.select(1)
# print(stonk.current_price)
