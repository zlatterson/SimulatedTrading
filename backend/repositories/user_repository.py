from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (username,name,currency,money) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [user.username, user.name, user.currency, user.money]
    results = run_sql(sql,values)
    user.id = results[0]['id']
    return user