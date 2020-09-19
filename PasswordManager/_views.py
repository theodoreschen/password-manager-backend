from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from ._models import Models
import jsonschema
from ._schemas import _ENTRY_UPDATE_SCHEMA


def _webpage(app: Flask, db: SQLAlchemy, models: Models):
    return app.send_static_file("index.html")


def _update(app: Flask, db: SQLAlchemy, models: Models):
    PasswordEntries = models.PasswordEntries
    data = request.get_json()
    try:
        jsonschema.validate(data, _ENTRY_UPDATE_SCHEMA)
    except jsonschema.ValidationError:
        return "Invalid JSON payload", 400

    if "comments" not in data:
        data["comments"] = ""
    
    entry = PasswordEntries(
        sitename=data["sitename"],
        weburl=data["weburl"],
        hashalgo=data["hashalgo"],
        seed=data["seed"],
        pwlen=data["pwlen"],
        comments=data["comments"]
    )

    db.session.add(entry)
    db.session.commit()

    return "", 200


def _getall(app: Flask, db: SQLAlchemy, models: Models):
    PasswordEntries = models.PasswordEntries
    res = PasswordEntries.query.all()
    print(res)
    res = [entry.to_json() for entry in res]
    return jsonify(res), 200


def _delete(app: Flask, db: SQLAlchemy, models: Models):
    PasswordEntries = models.PasswordEntries
    data = request.get_json()
    try:
        jsonschema.validate(data, _ENTRY_UPDATE_SCHEMA)
    except jsonschema.ValidationError:
        return "Invalid JSON payload", 400

    entry = PasswordEntries(
        sitename=data["sitename"],
        weburl=data["weburl"],
        hashalgo=data["hashalgo"],
        seed=data["seed"],
        pwlen=data["pwlen"],
        comments=data["comments"]
    )

    db.session.delete(entry)
    db.session.commit()

    return "", 200


_VIEW_FUNCS = {
    "webpage": _webpage,
    "update": _update,
    "getall": _getall,
    "delete": _delete
}
