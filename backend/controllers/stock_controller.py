from pprint import pprint
from flask import Blueprint,request, jsonify
from models.user import User
import jsonpickle
import numpy as np

import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.buy_sell_action_repository as buy_sell_action_repository
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository
from services.stock_service import StockService

stocks_blueprint = Blueprint("stocks", __name__)


@stocks_blueprint.route("/stocks")
def show_stocks():
    res = stock_repository.select_all()
    for r in res:
        r.fetch_price()
    stocks = jsonpickle.encode(res)
    return stocks


@stocks_blueprint.route("/stocks/<id>")
def show_stock(id):
    res = stock_repository.select(id)
    res.fetch_price()
    stock = jsonpickle.encode(res)
    return stock

@stocks_blueprint.route("/stocks/search/<ticker>")
def show_stock_by_ticker(ticker):
    try:
        res = stock_repository.select_by_ticker(ticker)
    except IndexError:
        try:
            new_stock = StockService.make_stock(ticker)
            stock_repository.save(new_stock)
            res = stock_repository.select_by_ticker(ticker)
        except:
            return
    res.fetch_price()
    stock = jsonpickle.encode(res)
    return stock

# @stocks_blueprint.route("/stocks/new/<ticker>")
# def show_stock(ticker):
#     res = stock_repository.select(id)
#     res.fetch_price()
#     stock = jsonpickle.encode(res)
#     return stock