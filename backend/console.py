# from db.run_sql import run_sql
from models.user import User
import repositories.user_repository as user_repository
user = User("George100","George Smith",102103)

from models.stock import Stock

user_repository.save(user)
print(user.id)