from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
import traceback

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
DB = SQLAlchemy(APP)