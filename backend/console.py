from time import sleep
from models.user import User
from services.buy_sell_action_service import BuySellActionService
from services.stock_service import StockService
from models.stock import Stock
from pprint import pprint


import repositories.user_repository as user_repository

user_repository.delete_all()

user = User("J11mmya","Jimmy",1100.123,1100.123)
user_repository.save(user)
user2 = User("Anator123","Paul",231.123,231.123)
user_repository.save(user2)

print(user2.username)

all_users = user_repository.select_all()
for us in all_users:
    print("username:",us.username, 
        "name:",us.name, 
        us.currency,
        us.money_paid_in,
        us.money,
        us.id)

user.name = "Andrew"
user2.money = 9999
user_repository.update(user)
user_repository.update(user2)

all_users = user_repository.select_all()
for us in all_users:
    pprint(vars(us))
