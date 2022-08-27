from flask import Blueprint,jsonify
from models.user import User
import jsonpickle

import repositories.user_repository as user_repository
import repositories.stock_repository as stock_repository
import repositories.call_put_contract_repository as call_put_contract_repository
import repositories.call_put_option_repository as call_put_option_repository

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/users")
def show_users():
    users = jsonpickle.encode(user_repository.select_all())
    return users

@user_blueprint.route("/users/new")
def show_user(id):
    found_user = call_put_option_repository.select(id)
    frozen = jsonpickle.encode(found_user)
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