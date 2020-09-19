import json
# import os

# print(os.path.abspath("."))

_ENTRY_UPDATE_SCHEMA = {}
try:
    with open("schemas/entry_update.json") as fd:
        _ENTRY_UPDATE_SCHEMA = json.load(fd)
except FileNotFoundError:
    # Apple is stupid in how it handles this
    with open("PasswordManager/schemas/entry_update.json") as fd:
        _ENTRY_UPDATE_SCHEMA = json.load(fd)