# from db.run_sql import run_sql
from models.user import User
import repositories.user_repository as user_repository
user = User("George100","George Smith",1000)
user2 = User("Andy1230","Andrew Smith",301231.20)

from models.stock import Stock

user_repository.save(user)
user_repository.save(user2)
print(user.id)