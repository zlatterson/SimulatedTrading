from db.run_sql import run_sql

from models.call_put_contract import CallPutContract
from models.call_put_option import CallPutOption

import repositories.user_repository as user_repository
import repositories.call_put_contract_repository as call_put_contract_repository

def save(call_put_option):
    sql = "INSERT INTO call_put_options (user_id, call_put_contract_id, n_contracts, bought_c_price, bought_contracts_value, timestamp) VALUES (%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [call_put_option.user.id,call_put_option.call_put_contract.id, call_put_option.n_contracts, call_put_option.bought_c_price,call_put_option.bought_contracts_value,call_put_option.timestamp]
    results = run_sql(sql,values)
    call_put_option.id = results[0]['id']
    return call_put_option

def select_all():
    call_put_options = []
    sql = "SELECT * FROM call_put_options"
    results = run_sql(sql)
    print(results)
    for row in results:
        user = user_repository.select(row["user_id"])
        call_put_contract = call_put_contract_repository.select(row["call_put_contract_id"])
        call_put_option = CallPutOption(call_put_contract,row["n_contracts"],row["bought_c_price"],row["bought_contracts_value"],row["timestamp"],user,row["id"])
        call_put_options.append(call_put_option)
    return call_put_options


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
