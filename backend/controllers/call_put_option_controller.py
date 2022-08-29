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
from services.call_put_option_service import CallPutOptionService
call_put_options_blueprint = Blueprint("call_put_options_blueprint", __name__)

# @call_put_options_blueprint.route("/buy_sell_actions/search/<ticker>")
# def show_buy_call_put_options(ticker):
#     res = CallPutOptionService.find_calls(ticker)
#     call_put_options = jsonpickle.encode(res)
#     return call_put_options