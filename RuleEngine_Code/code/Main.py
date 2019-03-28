from flask import Flask, request
from AccountAPI import account_api
from Balance import balance_api
from jsonAPI import json_api
from json_logic import jsonLogic

app = Flask(__name__)
app.register_blueprint(account_api, url_prefix='/accounts')
app.register_blueprint(balance_api, url_prefix='/balances')
app.register_blueprint(json_api, url_prefix='/api')
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()