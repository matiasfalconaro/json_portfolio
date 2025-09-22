from .db import db


def get_basics():
    """Devuelve los datos de 'basics' como dict."""
    basics = db.basics.find_one({}, {"_id": 0})
    return basics or {}


def get_work():
    """Devuelve la lista de trabajos."""
    return list(db.work.find({}, {"_id": 0}))


def get_education():
    return list(db.education.find({}, {"_id": 0}))


def get_certificates():
    return list(db.certificates.find({}, {"_id": 0}))


def get_projects():
    return list(db.projects.find({}, {"_id": 0}))
