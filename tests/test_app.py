from urllib import response
from app import __version__
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_version():
    assert __version__ == '0.1.0'

def test_create_user():
    
    response = client.post("/user/create", 
                    data={'username': 'pytest1', 'password': 'pytest1'})

    response.status_code == 201
    assert response.json() == {"message": "user created successfully"}


def test_get_patients():
    response = client.get("/api/v1/patients",
                          headers={"Authorization": "Bearer GUSTAVOBR20"})

    assert response.status_code == 200


def test_get_patient_by_query_param():
    response = client.get("/api/v1/patients/?uuid=PATIENT0001",
                          headers={"Authorization": "Bearer GUSTAVOBR20"})

    data = [{
        "DATE_OF_BIRTH": "1996-10-25T00:00:00",
        "UUID": "PATIENT0001",
        "FIRST_NAME": "JOANA",
        "LAST_NAME": "SILVA"
    }]

    assert response.status_code == 200
    assert response.json() == data
    

def test_get_patients_not_authenticated():
    response = client.get("/api/v1/patients")
    
    data = {"detail": "Not authenticated"}

    assert response.status_code == 401
    assert response.json() == data


def test_get_pharmacies():
    response = client.get("/api/v1/pharmacies",
                          headers={"Authorization": "Bearer GUSTAVOBR20"})
    assert response.status_code == 200


def test_get_pharmacies_by_query_param():
    response = client.get("/api/v1/pharmacies/?name=DROGA MAIS",
                          headers={"Authorization": "Bearer GUSTAVOBR20"})
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_get_pharmacies_not_authenticated():
    response = client.get("/api/v1/pharmacies")

    data = {"detail": "Not authenticated"}

    assert response.status_code == 401
    assert response.json() == data


def test_get_transactions():
    response = client.get("/api/v1/transactions",
                          headers={"Authorization": "Bearer GUSTAVOBR20"})
    assert response.status_code == 200


def test_get_transactions_by_query_param():
    response = client.get("/api/v1/transactions/?uuid_patient=PATIENT0001",
                          headers={"Authorization": "Bearer GUSTAVOBR20"})
    assert response.status_code == 200


def test_get_transactions_not_authenticated():
    response = client.get("/api/v1/transactions")
    
    data = {"detail": "Not authenticated"}

    assert response.status_code == 401
    assert response.json() == data
