from fastapi import APIRouter, Depends
from app.crud import crud
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

api_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@api_router.get("/patients", status_code=200)
def get_patients(uuid: str | None = None, token: str = Depends(oauth2_scheme)):
    """
    Return all patients
    """
    if uuid:
        data = crud.get_patient_by_uuid(uuid)
    else:
        data = crud.get_patients()

    json_data = JSONResponse(content=jsonable_encoder(data))

    return json_data


@api_router.get("/pharmacies", status_code=200)
def get_pharmacies(name: str | None = None, token: str = Depends(oauth2_scheme)):
    """
    Return all pharmacies
    """
    if name:
        data = crud.get_pharmacie_by_name(name)
    else:
        data = crud.get_pharmacies()

    json_data = JSONResponse(content=jsonable_encoder(data))

    return json_data


@api_router.get("/transactions", status_code=200)
def get_transactions(uuid_patient: str | None = None, token: str = Depends(oauth2_scheme)):
    """
    Return all transactions
    """
    if uuid_patient:
        data = crud.get_transaction_by_uuid_patient(uuid_patient)
    else:
        data = crud.get_transactions()

    json_data = JSONResponse(content=jsonable_encoder(data))

    return json_data
