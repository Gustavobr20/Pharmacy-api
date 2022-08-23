from uuid import UUID
from app.db.connection import DBConnection
from app.models import *

db = DBConnection()
session = db.get_session()


def get_patients() -> object:
    """
    Retorna do banco de dados todos os dados dos pacientes
    """

    data = session.query(Patients).all()
    return data


def get_patient_by_uuid(uuid: str):
    """
    Retorna os dados do paciente pelo seu uuid
    """
    data = session.query(Patients).filter(Patients.UUID == uuid).all()
    return data


def get_pharmacies() -> object:
    """
    Retorna do banco de dados todos os dados das farmacias
    """

    data = session.query(Pharmacies).all()
    return data


def get_pharmacie_by_name(name: str):
    """
    Retorna todas as localidades da farmacia especificada pelo nome
    """
    data = session.query(Pharmacies).filter(
        Pharmacies.NAME == name.upper()).all()
    return data


def get_transactions() -> object:
    """
    Retorna do banco de dados todas as transações em farmacias
    """

    data = session.query(Transactions).all()
    return data


def get_transaction_by_uuid_patient(uuid_patient: str):
    """
    Retorna todas as transações que o paciente fez
    """
    data = session.query(Transactions).filter(
        Transactions.PATIENT_UUID == uuid_patient.upper()).all()
    return data


def get_user(username: str):
    """
    Busca e retorna do banco de dados um usúario filtrado pelo username
    """

    data = session.query(Users).filter(Users.USERNAME == username).all()

    if len(data) > 0:
        return data[0]
    else:
        return False


def create_user(username: str, password: str) -> bool:
    """
    Insere um novo usuário no banco de dados
    """

    # Busca no banco de dados se existe um usuario filtrando pelo username
    data = session.query(Users).filter(
        Users.USERNAME == username).all()

    # Verifica se retornou algum dado do banco
    if len(data) == 0:

        # Pega o ultimo dado do banco para criar o próximo uuid do novo usuario
        last_uuid = session.query(Users).order_by(Users.UUID.desc()).first()

        new_idx = str(int(last_uuid.UUID[4::]) + 1)

        new_numbers_uuid = new_idx.replace(new_idx, f'{new_idx:0>4}')

        # Insere o novo usuario
        new_user = Users(UUID="USER" + new_numbers_uuid,
                         USERNAME=username, PASSWORD=password)

        session.add(new_user)
        session.commit()
        session.close()

        return True
    else:
        return False
