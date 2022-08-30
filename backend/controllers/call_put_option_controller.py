from pprint import pprint
from flask import Blueprint,request, jsonify
from models.user import User
import jsonpickle
import numpy as np
import pandas as pd

import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.buy_sell_action_repository as buy_sell_action_repository
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository
from services.buy_sell_action_service import BuySellActionService
from services.call_put_contract_service import CallPutContractService
from services.call_put_option_service import CallPutOptionService
call_put_options_blueprint = Blueprint("call_put_options_blueprint", __name__)

@call_put_options_blueprint.route("/call_put_options/search/<ticker>")
def show_buy_call_put_options(ticker):
    res = CallPutOptionService.find_calls(ticker)
    response = res.reset_index(drop=True).to_json(orient='records')
    return response


@call_put_options_blueprint.route("/call_put_options/<contract_name>")
def show_buy_call_put_option(contract_name):
    res = CallPutOptionService.find_contract(contract_name)
    price =   (res["calls"].loc[2][1] + res["calls"].loc[3][1]) / 2
    strike = res["calls"].loc[4][1]
    expires =   res["puts"].loc[0][1]
    days_range = res["puts"].loc[1][1]
    volume = res["puts"].loc[3][1]
    object = {"call_price":float(price),"strike":float(strike),"expires":str(expires),"days_range":days_range,"volume":float(volume)}
    response = jsonify(object)
    return response

@call_put_options_blueprint.route("/call_put_options", methods=['POST'])
def create_call_put_option():
    user = user_repository.select(request.json.get("data").get("user_id"))
    print(user.username)
    contract = request.json.get("data").get("contract")
    quantity = request.json.get("data").get("quantity")
    buy_sell_type = request.json.get("data").get("buy_sell_type")
    ticker = request.json.get("data").get("ticker")
    call_put_type = request.json.get("data").get("call_put_type")

    stock = stock_repository.select_by_ticker(ticker)
    stock.fetch_price()
    contract = CallPutContractService.make_contract(contract,stock,call_put_type)
    contract.fetch_c_price()
    call_put_contract_repository.save(contract)

    result = CallPutOptionService.make_position(contract,buy_sell_type,quantity,user)
    call_put_option_repository.save(result[0])
    user.money = result[1].money
    user_repository.update(result[1])

    return jsonify(request.json)
