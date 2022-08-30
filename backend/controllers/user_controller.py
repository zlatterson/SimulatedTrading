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

users_blueprint = Blueprint("user", __name__)

@users_blueprint.route("/users")
def show_users():
    """return the information of all users, showing profit/loss"""
    users = jsonpickle.encode(user_repository.select_all())
    return users

@users_blueprint.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def show_user(user_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        user = jsonpickle.encode(user_repository.select(user_id))
        return user
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        data = request.form # a multidict containing POST data

    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
    else:
        # POST Error 405 Method Not Allowed
        pass

@users_blueprint.route("/users/<user_id>/buy_sell_actions")
def show_user_buy_sell_actions(user_id):
    user = user_repository.select(user_id)
    response = user_repository.buy_sell_actions(user)
    for res in response:
        pprint(vars(res))
        res.score = float(res.running_pl_percentage)
        res.stock._current_price = float(res.stock._current_price)
    user_buy_sell_actions = jsonpickle.encode(response)
    return user_buy_sell_actions

@users_blueprint.route("/users/<user_id>/call_put_options")
def show_user_call_put_options(user_id):
    user = user_repository.select(user_id)
    response = user_repository.call_put_options(user)
    for res in response:
        res.call_put_contract.fetch_c_price()
        res.call_put_contract.current_c_price = float(res.call_put_contract.current_c_price)
    user_call_put_options = jsonpickle.encode(response)
    return user_call_put_options