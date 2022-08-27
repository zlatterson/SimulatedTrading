from flask import Blueprint,jsonify
from models.user import User

import repositories.user_repository as user_repository

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route("/user/<id>")
def show_users(id):
    found_user = user_repository.select(id)
    found_user.toJSON()
    return jsonify(found_user)