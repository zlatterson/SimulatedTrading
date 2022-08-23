# from db.run_sql import run_sql
# from models.user import User

# user = User("George100","George Smith",10000)
# def save(user):
#     sql = "INSERT INTO users (username,name,money) VALUES (%s,%s,%s) RETURNING id"
#     values = [user.username, user.name, user.money]
#     results = run_sql(sql,values)
#     user.id = results[0]['id']
#     return user
# save(user)

from models.stock import Stock


# print(Stock(si.get_premarket_price(ticker))