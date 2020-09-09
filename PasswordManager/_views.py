from ._globals import APP, DB
from flask import jsonify, request
from .models import PasswordEntries
from ._schemas import _ENTRY_UPDATE_SCHEMA
import jsonschema


@APP.route("/")
def webpage():
    return APP.send_static_file("index.html")


@APP.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    try:
        jsonschema.validate(data, _ENTRY_UPDATE_SCHEMA)
    except jsonschema.ValidationError:
        return "Invalid JSON payload", 400
    
    return "", 200


@APP.route("/getall")
def getall():
    pass
