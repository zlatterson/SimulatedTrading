from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# app.register_blueprint()

if __name__ == '__main__':
    app.run(debug=True)