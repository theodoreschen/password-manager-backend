from ._globals import APP
from flask import jsonify, requests
from .models import PasswordEntries


@APP.route("/")
def webpage():
    return APP.send_static_file("index.html")


@APP.route("/update", methods=["POST"])
def update():
    pass


@APP.route("/getall")
def getall():
    pass
