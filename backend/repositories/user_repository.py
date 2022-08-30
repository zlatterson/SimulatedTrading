from db.run_sql import run_sql
from models.buy_sell_action import BuySellAction
from models.call_put_option import CallPutOption

from models.user import User
from services.stock_service import StockService
import repositories.stock_repository as stock_repository
import repositories.call_put_contract_repository as call_put_contract_repository

def save(user):
    sql = "INSERT INTO users (username,name,money_paid_in,money) VALUES (%s,%s,%s,%s) RETURNING id"
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

def buy_sell_actions(user):
    buy_sell_actions = []

    sql = "SELECT * FROM buy_sell_actions WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)
    for row in results:
        stock = stock_repository.select(row["stock_id"])
        buy_sell_action = BuySellAction(stock,row["average_price"],row["quantity"],row["buy_sell_type"],row["timestamp"],row["last_action"],user,row["id"])
        buy_sell_actions.append(buy_sell_action)
    return buy_sell_actions

def buy_sell_action(user, stock):
    buy_sell_action = None
    sql = "SELECT * FROM buy_sell_actions WHERE user_id = %s AND stock_id= %s"
    values = [user.id, stock.id]
    result = run_sql(sql,values)[0]
    if result:
        buy_sell_action = BuySellAction(stock,result["average_price"],result["quantity"],result["buy_sell_type"],result["timestamp"],result["last_action"],user,result["id"])
    return buy_sell_action


def call_put_options(user):
    call_put_options = []

    sql = "SELECT * FROM call_put_options WHERE user_id = %s"
    values = [user.id]
    results = run_sql(sql, values)
    for row in results:
        call_put_contract = call_put_contract_repository.select(row["call_put_contract_id"])
        call_put_option = CallPutOption(call_put_contract,row["buy_sell_type"],row["n_contracts"],row["bought_c_price"],row["bought_contracts_value"],row["timestamp"],user,row["id"])
        call_put_options.append(call_put_option)
    return call_put_options


    call_put_options = []
    sql = "SELECT * FROM call_put_options"
    results = run_sql(sql)
    print(results)
    for row in results:
        user = user_repository.select(row["user_id"])
        call_put_contract = call_put_contract_repository.select(row["call_put_contract_id"])
        call_put_option = CallPutOption(call_put_contract,row["buy_sell_type"],row["n_contracts"],row["bought_c_price"],row["bought_contracts_value"],row["timestamp"],user,row["id"])
        call_put_options.append(call_put_option)
    return call_put_options