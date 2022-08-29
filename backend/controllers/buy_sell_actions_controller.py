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
from services.buy_sell_action_service import BuySellActionService

buy_sell_actions_blueprint = Blueprint("buy_sell_actions", __name__)

@buy_sell_actions_blueprint.route("/buy_sell_actions/<id>")
def show_buy_sell_action(id):
    res = buy_sell_action_repository.select(id)
    res.stock.current_price
    buy_sell_action = jsonpickle.encode(res)
    return buy_sell_action

@buy_sell_actions_blueprint.route("/buy_sell_actions", methods=['POST'])
def get_buy_sell_action():
    """Search if stock exists for a user
    """
    user = user_repository.select(request.json.get("data").get("user_id"))
    stock = stock_repository.select(request.json.get("data").get("stock_id"))
    stock.fetch_price()
    quantity = request.json.get("data").get("quantity")
    buy_sell_type = request.json.get("data").get("buy_sell_type")
    existing_position = None
    try:
        existing_position = user_repository.buy_sell_action(user, stock)
    except:
        result = BuySellActionService.make_postion(stock,quantity,buy_sell_type,user)
        buy_sell_action_repository.save(result[0])
        user.money = result[1].money
        user_repository.update(user)

    if existing_position != None:
        existing_position.stock.fetch_price()
        existing_position.buy(quantity)
        buy_sell_action_repository.update(existing_position)
        user_repository.update(existing_position.user)



    # BuySellActionService.make_postion()
    return jsonify(request.json)
    res = buy_sell_action_repository.select(id)
    res.stock.current_price
    buy_sell_action = jsonpickle.encode(res)
    return buy_sell_action

