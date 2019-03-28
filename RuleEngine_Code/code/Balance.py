from flask import Blueprint
import json

balance_api = Blueprint('balance_api', __name__)

@balance_api.route("/balance")
def getBalance():
    return "list of balance"