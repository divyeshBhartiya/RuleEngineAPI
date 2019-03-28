from flask import Blueprint
from flask import request
from json_logic import jsonLogic
import pdb
import json

json_api = Blueprint('json_api', __name__)

@json_api.route("/jsonValue",methods=['POST'])
def accountList():
    expressn = json.loads(request.form['expression'])
    dataValue = json.loads(request.form['dataValue'])
    # expressn = {"if" : [
    # {"<=": [{"var":"temp"}, 0]}, "freezing",
    # {"<=": [{"var":"temp"}, 100]}, "liquid",
    # {">": [{"var":"temp"}, 100]}, "gas"
    # ]}
    # dataValue = {"temp":10}
    apiResponse = jsonLogic(expressn, dataValue )
    print(apiResponse)
    return json.dumps(apiResponse)
    
@json_api.route("/result")
def namesList():
    my_json_string = json.dumps({'key1': 'Expression', 'key2': 'Value'})
    return my_json_string