from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import yaml
import traceback
from ._views import _VIEW_FUNCS
from ._models import PasswordEntriesFactory, HashAlgorithms, Models

_db_filename = "test.db"
_password = None

try:
    config_file = "config.yml"
    with open(config_file) as fd:
        _config = yaml.load(fd, Loader=yaml.FullLoader)
    _db_filename = _config["dbfile"]
    # For now, don't know how to handle a password locked file
    # _password = _config["password"]
except FileNotFoundError:
    traceback.print_exc()
except AttributeError:
    traceback.print_exc()

# TODO: figure out how to handle passwords

APP = Flask("PasswordManager")
APP.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{_db_filename}'
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(APP)
DB = SQLAlchemy(APP)

_passwd_entries = PasswordEntriesFactory(DB)
MODELS = Models(HashAlgorithms, _passwd_entries)

print(MODELS.PasswordEntries)

@APP.route("/")
def webpage():
    return _VIEW_FUNCS["webpage"](APP, DB, MODELS)


@APP.route("/update", methods=["POST"])
def update():
    return _VIEW_FUNCS["update"](APP, DB, MODELS)


@APP.route("/getall")
def getall():
    return _VIEW_FUNCS["getall"](APP, DB, MODELS)


@APP.route("/delete", methods=["POST"])
def delete():
    return _VIEW_FUNCS["delete"](APP, DB, MODELS)
