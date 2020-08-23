from flask import Flask
from .data_types import SQL3
from .password_entry import PasswordEntries
import os

APP = Flask(__name__, static_url_path=os.path.abspath("./.."))


@APP.route("/")
def webpage():
    return APP.send_static_file("index.html")



