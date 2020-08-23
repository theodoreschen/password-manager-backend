from flask import Flask
from sqlalchemy import create_engine


class SqliteManager:
    DB = None
    conn = None
    _sqlite = ""
    _password = ""

    def __init__(self, sqlite_file: str, password: str):
        self._sqlite = sqlite_file
        self._password = password

        self.DB = create_engine("sqlite://{}".format(self._sqlite))
        self.conn = self.DB.connect()
    