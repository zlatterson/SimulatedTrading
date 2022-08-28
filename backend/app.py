from flask import Flask
from controllers.user_controller import users_blueprint
from controllers.buy_sell_actions_controller import buy_sell_actions_blueprint

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_blueprint)
app.register_blueprint(buy_sell_actions_blueprint)

if __name__ == '__main__':
    app.run(debug=True)