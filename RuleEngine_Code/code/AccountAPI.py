from flask import Blueprint
import json

account_api = Blueprint('account_api', __name__)

@account_api.route("/account")
def accountList():
    return "list of accounts"

@account_api.route("/names")
def namesList():
    my_json_string = json.dumps({'key1': 'Ram', 'key2': 'val2'})
    return my_json_string