import json

_ENTRY_UPDATE_SCHEMA = {}
with open("schemas/entry_update.json") as fd:
    _ENTRY_UPDATE_SCHEMA = json.load(fd)