from db.run_sql import run_sql

from models.user import User

def save(user):
    sql = "INSERT INTO users (name,username,money_paid_in,money) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [user.username, user.name, user.money_paid_in,user.money]
    results = run_sql(sql,values)
    user.id = results[0]['id']
    return user

def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row["username"],row["name"],row["money_paid_in"],row["money"],row["id"])
        users.append(user)
    return users

def select(id):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    user = User(result["username"],result["name"],result["money_paid_in"],result["money"],result["id"])
    return user


def update(user):
    sql = "UPDATE users SET (username, name, money_paid_in, money) = (%s,%s,%s,%s) WHERE id = %s"
    values = [user.username,user.name,user.money_paid_in,user.money,user.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)