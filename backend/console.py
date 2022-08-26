from time import sleep
from models.user import User
import repositories.user_repository as user_repository
from services.buy_sell_action_service import BuySellActionService
from services.stock_service import StockService
from models.stock import Stock
user_repository.delete_all()

user = User("Jimmya","Jimmy",1000)
user_repository.save(user)

all_users = user_repository.select_all()
for user in all_users:
    print(user.username, 
        user.name, 
        user.currency,
        user.money_paid_in,
        user.money,
        user.id)
user.name = "Diane"

user_repository.update(user)

all_users = user_repository.select_all()
for user in all_users:
    print(user.username, 
        user.name, 
        user.currency,
        user.money_paid_in,
        user.money,
        user.id)