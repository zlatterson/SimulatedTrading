from db.run_sql import run_sql

from models.buy_sell_action import BuySellAction

import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository


def save(buy_sell_action):
    sql = "INSERT INTO buy_sell_actions (user_id, stock_id, buy_sell_type, quantity, average_price, timestamp, last_action) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [buy_sell_action.user.id, buy_sell_action.stock.id, buy_sell_action.buy_sell_type,buy_sell_action.quantity,buy_sell_action.average_price, buy_sell_action.timestamp, buy_sell_action.last_action]
    results = run_sql(sql,values)
    print("results: ",results[0]['id'])
    buy_sell_action.id = results[0]['id']
    return buy_sell_action

def select_all():
    buy_sell_actions = []
    sql = "SELECT * FROM buy_sell_actions"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row["user_id"])
        stock = stock_repository.select(row["stock_id"])
        buy_sell_action = BuySellAction(stock,row["average_price"],row["quantity"],row["buy_sell_type"],row["timestamp"],row["last_action"],user,row["id"])
        buy_sell_actions.append(buy_sell_action)
    return buy_sell_actions

def select(id):
    sql = "SELECT * FROM buy_sell_actions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = user_repository.select(result["user_id"])
        stock = stock_repository.select(result["stock_id"])
        buy_sell_action = BuySellAction(stock,result["average_price"],result["quantity"],result["buy_sell_type"],result["timestamp"],result["last_action"],user,result["id"])
    return buy_sell_action

def update(buy_sell_action):
    sql = "UPDATE buy_sell_actions SET (user_id, stock_id, buy_sell_type, quantity, average_price, timestamp, last_action) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [buy_sell_action.user.id, buy_sell_action.stock.id, buy_sell_action.buy_sell_type,buy_sell_action.quantity,buy_sell_action.average_price, buy_sell_action.timestamp, buy_sell_action.last_action,buy_sell_action.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM buy_sell_actions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM buy_sell_action WHERE id = %s"
    values = [id]
    run_sql(sql, values)