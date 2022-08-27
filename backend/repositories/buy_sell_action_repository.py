from db.run_sql import run_sql

from models.buy_sell_action import BuySellAction

def save(buy_sell_action):
    sql = "INSERT INTO buy_sell_actions (user_id, stock_id, buy_sell_type, quantity, average_price, timestamp, last_action) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [buy_sell_action.user.id, buy_sell_action.stock.id, buy_sell_action.buy_sell_type,buy_sell_action.quantity,buy_sell_action.average_price, buy_sell_action.timestamp, buy_sell_action.last_action]
    results = run_sql(sql,values)
    print("results: ",results[0]['id'])
    buy_sell_action.id = results[0]['id']
    return buy_sell_action

# def select_all():
#     transactions = []
#     sql = "SELECT * FROM transactions"
#     results = run_sql(sql)
#     for row in results:
#         merchant = merchant_repository.select(row["merchant_id"])
#         item = item_repository.select(row["item_id"])
#         user = user_repository.select(row["user_id"])
#         transaction = Transaction(merchant,user,item,row["cost"],row["time"])
#         transactions.append(transaction)
#     return transactions

# def select(id):
#     sql = "SELECT * FROM transactions WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         merchant = merchant_repository.select(result["merchant_id"])
#         item = item_repository.select(result["item_id"])
#         user = user_repository.select(result["user_id"])
#         transaction = Transaction(merchant,user,item,result["cost"],result["time"])
#     return transaction

# def update(transaction):
#     sql = "UPDATE transactions SET (merchant_id, user_id, item_id, cost, time) = (%s,%s,%s,%s,%s) WHERE id = %s"
#     values = [transaction.merchant.id,transaction.user.id,transaction.item.id,transaction.cost,transaction.time,transaction.id]
#     run_sql(sql, values)

# def delete_all():
#     sql = "DELETE FROM transactions"
#     run_sql(sql)

# def delete(id):
#     sql = "DELETE FROM transactions WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)
