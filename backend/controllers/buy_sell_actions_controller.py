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

buy_sell_actions_blueprint = Blueprint("buy_sell_actions", __name__)

@buy_sell_actions_blueprint.route("/buy_sell_actions/<id>")
def show_buy_sell_action(id):
    buy_sell_action = jsonpickle.encode(buy_sell_action_repository.select(id))
    return buy_sell_action
