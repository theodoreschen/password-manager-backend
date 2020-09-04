from ._globals import DB
from enum import Enum, auto


class HashAlgorithms(Enum):
    MD5 = auto()
    SHA1 = auto()
    SHA256 = auto()


class PasswordEntries(DB.Model):
    sitename = DB.Column(DB.String, unique=True, primary_key=True)
    weburl = DB.Column(DB.String)
    hashalgo = DB.Column(DB.Enum(HashAlgorithms))
    seed = DB.Column(DB.String)
    pwlen = DB.Column(DB.Integer, default=16)
    comments = DB.Column(DB.String)

    def __repr__(self) -> str:
        return f"<{self.sitename}: {self.hashalgo}({self.seed})[{self.pwlen}]"
