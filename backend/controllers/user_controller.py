from pprint import pprint
from flask import Blueprint,jsonify
from models.user import User
import jsonpickle

import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.buy_sell_action_repository as buy_sell_action_repository
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/users")
def show_users():
    users = jsonpickle.encode(user_repository.select_all())
    return users

@user_blueprint.route("/users/<id>")
def show_user(id):
    found_user = user_repository.select(id)
    frozen = jsonpickle.encode(found_user)
    return frozen


@user_blueprint.route("/test")
def test():
    found_user = buy_sell_action_repository.select_all()
    frozen = jsonpickle.encode(found_user)
    return frozen

@user_blueprint.route("/test/<id>")
def test_one(id):
    user = user_repository.select(id)
    pprint(vars(user))
    user_buy_sell_actions = user_repository.buy_sell_actions(user)
    print(user_buy_sell_actions)
    frozen = jsonpickle.encode(user_buy_sell_actions)
    return frozen

# NEW
# GET '/tasks/new'

# CREATE
# POST '/tasks'

# SHOW
# GET '/tasks/<id>'

# EDIT
# GET '/tasks/<id>/edit'

# UPDATE
# PUT '/tasks/<id>'

# DELETE
# DELETE '/tasks/<id>'