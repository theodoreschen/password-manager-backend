from enum import Enum, auto
from flask_sqlalchemy import SQLAlchemy


class Models:
    HashAlgorithms = None
    PasswordEntries = None

    def __init__(self, HashAlgorithms, PasswordEntries):
        self.PasswordEntries = PasswordEntries
        self.HashAlgorithms = HashAlgorithms


class HashAlgorithms(Enum):
    MD5 = auto()
    SHA1 = auto()
    SHA256 = auto()

    def __str__(self):
        return f"{self.name}"


def PasswordEntriesFactory(db: SQLAlchemy):
    class PasswordEntries(db.Model):
        sitename = db.Column(db.String, unique=True, primary_key=True)
        weburl = db.Column(db.String)
        hashalgo = db.Column(db.Enum(HashAlgorithms))
        seed = db.Column(db.String)
        pwlen = db.Column(db.Integer, default=16)
        comments = db.Column(db.String)

        def __repr__(self) -> str:
            return f"<{self.sitename}: {self.hashalgo}({self.seed})[{self.pwlen}]>"

        def to_json(self) -> dict:
            return {
                "sitename": self.sitename,
                "weburl": self.weburl,
                "hashalgo": str(self.hashalgo),
                "seed": self.seed,
                "pwlen": self.pwlen,
                "comments": self.comments
            }

    return PasswordEntries
