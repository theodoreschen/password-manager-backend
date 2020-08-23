from sqlalchemy import MetaData, Table, String, Column
from sqlalchemy.sql import select
from .sqlite_manager import SqliteManager
from typing import List, Dict


class PasswordEntries(Table):
    _db = None

    def __init__(self, db: SqliteManager):
        super(PasswordEntries, self).__init__(
            "PasswordEntries", MetaData(),
            Column("name", String, primary_key=True),
            Column("web_url", String),
            Column("hash_algo", String),
            Column("seed", String),
            Column("comments", String)
        )

        self._db = db

    def add(
        self, name: str, seed: str, *,
        web_url:str="", hash_algo:str="md5", comments:str=""
    ):
        ins = self.insert().values(
            name=name, seed=seed, web_url=web_url, hash_algo=hash_algo,
            comments=comments
        )
        self._db.conn.execute(ins)

    @staticmethod
    def get_all(self, pe: PasswordEntries) -> List[dict]:
        s = select([pe])
        result = self._db.conn.execute(s)
        output = []
        for row in result:
            output.append({
                "name": row["name"],
                "web_url": row["web_url"],
                "hash_algo": row["hash_algo"],
                "seed": row["seed"],
                "comments": row["comments"]
            })
        return output

    @staticmethod
    def get_one(self, pe: PasswordEntries, site_name: str) -> dict:
        s = select([pe]).where(pe.c.name == site_name)
        result = self._db.conn.execute(s)
        if len(result) == 1:
            row = result[0]
            return {
                "name": row["name"],
                "web_url": row["web_url"],
                "hash_algo": row["hash_algo"],
                "seed": row["seed"],
                "comments": row["comments"]
            }
        return {}
