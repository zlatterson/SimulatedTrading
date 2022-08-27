from db.run_sql import run_sql

from models.stock import Stock

def save(stock):
    sql = "INSERT INTO stocks (ticker,summary) VALUES (%s,%s) RETURNING id"
    values = [stock.ticker, stock.summary]
    results = run_sql(sql,values)
    stock.id = results[0]['id']
    return stock

def select_all():
    stocks = []
    sql = "SELECT * FROM stocks"
    results = run_sql(sql)
    for row in results:
        stock = Stock(row["ticker"],row["summary"],row["id"])
        stocks.append(stock)
    return stocks

def select(id):
    stock = None
    sql = "SELECT * FROM stocks where id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        stock = Stock(row["ticker"],row["summary"],row["id"])
    return stock

def update(stock):
    sql = "UPDATE stocks SET (ticker, summary) = (%s,%s,%s) WHERE id = %s"
    values = [stock.ticker,stock.summary,stock.id]
    run_sql(sql,values)

def delete_all():
    sql = "DELETE FROM stocks"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM stocks WHERE id = %s"
    values = [id]
    run_sql(sql, values)