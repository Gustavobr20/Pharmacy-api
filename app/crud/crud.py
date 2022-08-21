from app.db.connection import DBConnection
from app.models import *

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


def get_user(username: str):

    data = session.query(Users).filter(Users.USERNAME == username).all()

    if len(data) > 0:
        return data[0]
    else:
        return False


def create_user(username: str, password: str):

    data = session.query(Users).filter(
        Users.USERNAME == username.upper()).all()

    if len(data) == 0:

        last_uuid = session.query(Users).order_by(Users.UUID.desc()).first()

        new_idx = str(int(last_uuid.UUID[4::]) + 1)

        new_numbers_uuid = new_idx.replace(new_idx, f'{new_idx:0>4}')

        new_user = Users(UUID="USER" + new_numbers_uuid,
                         USERNAME=username, PASSWORD=password)

        session.add(new_user)
        session.commit()
        session.close()

        return True
    else:
        return False
