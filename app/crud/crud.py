from app.db.connection import DBConnection
from app.models.pharmacy import Patients, Pharmacies, Transactions

db = DBConnection()
session = db.get_session()


def get_patients():
    data = session.query(Patients).all()
    return data


def get_pharmacies():
    data = session.query(Pharmacies).all()
    return data


def get_transactions():
    data = session.query(Transactions).all()
    return data

