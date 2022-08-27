from db.run_sql import run_sql

from models.call_put_contract import CallPutContract

import repositories.stock_repository as stock_repository


def save(call_put_contract):
    sql = "INSERT INTO call_put_contracts (stock_id, contract_name, call_put_type, k, expires) VALUES (%s,%s,%s,%s,%s) RETURNING id"
    values = [call_put_contract.stock.id, call_put_contract.contract_name, call_put_contract.call_put_type,call_put_contract.k,call_put_contract.expires]
    results = run_sql(sql,values)
    call_put_contract.id = results[0]['id']
    return call_put_contract

def select_all():
    call_put_contracts = []
    sql = "SELECT * FROM call_put_contracts"
    results = run_sql(sql)
    for row in results:
        stock = stock_repository.select(row["stock_id"])
        buy_sell_action = CallPutContract(row["contract_name"],stock,row["call_put_type"],row["k"],row["expires"],row["id"])
        call_put_contracts.append(buy_sell_action)
    return call_put_contracts

def select(id):
    sql = "SELECT * FROM call_put_contracts WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        stock = stock_repository.select(result["stock_id"])
        call_put_contract = CallPutContract(result["contract_name"],stock,result["call_put_type"],result["k"],result["expires"],result["id"])
    return call_put_contract

def update(call_put_contract):
    sql = "UPDATE call_put_contracts SET (stock_id, contract_name, call_put_type, k, expires) = (%s,%s,%s,%s,%s) WHERE id = %s"
    values = [call_put_contract.stock.id, call_put_contract.contract_name, call_put_contract.call_put_type,call_put_contract.k,call_put_contract.expires,call_put_contract.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM call_put_contracts"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM call_put_contracts WHERE id = %s"
    values = [id]
    run_sql(sql, values)
