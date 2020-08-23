from .flask_app import APP
from .data_types import SQL3
from .sqlite_manager import SqliteManager


class PasswordManager:
    def __init__(self, sqlite_file: str, password: str):
        global SQL3
        SQL3 = SqliteManager(sqlite_file, password)

    