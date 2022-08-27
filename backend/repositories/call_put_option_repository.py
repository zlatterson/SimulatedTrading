from db.run_sql import run_sql

from models.call_put_contract import CallPutContract

import repositories.stock_repository as stock_repository


def save(call_put_option):
    sql = "INSERT INTO call_put_contracts (stock_id, contract_name, call_put_type, k, expires) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [call_put_contract.stock.id, call_put_contract.contract_name, call_put_contract.call_put_type,call_put_contract.k,call_put_contract.expires]
    results = run_sql(sql,values)
    call_put_contract.id = results[0]['id']
    return call_put_contract

# def select_all():
#     call_put_contracts = []
#     sql = "SELECT * FROM call_put_contracts"
#     results = run_sql(sql)
#     for row in results:
#         stock = stock_repository.select(row["stock_id"])
#         buy_sell_action = CallPutContract(row["contract_name"],stock,row["call_put_type"],row["k"],row["expires"],row["id"])
#         call_put_contracts.append(buy_sell_action)
#     return call_put_contracts

# def select(id):
#     sql = "SELECT * FROM call_put_contracts WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         stock = stock_repository.select(result["stock_id"])
#         call_put_contract = CallPutContract(result["contract_name"],stock,result["call_put_type"],result["k"],result["expires"],result["id"])
#     return call_put_contract

# def update(buy_sell_action):
#     sql = "UPDATE buy_sell_actions SET (user_id, stock_id, buy_sell_type, quantity, average_price, timestamp, last_action) = (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
#     values = [buy_sell_action.user.id, buy_sell_action.stock.id, buy_sell_action.buy_sell_type,buy_sell_action.quantity,buy_sell_action.average_price, buy_sell_action.timestamp, buy_sell_action.last_action,buy_sell_action.id]
#     run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM call_put_options"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM call_put_options WHERE id = %s"
    values = [id]
    run_sql(sql, values)
