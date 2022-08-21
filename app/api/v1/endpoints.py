from fastapi import APIRouter, Depends
from app.crud import crud
from fastapi.security import OAuth2PasswordBearer
import json

api_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@api_router.get("/patients", status_code=200)
def get_patients(token: str = Depends(oauth2_scheme)):
    """
    Return all patients
    """
    data = crud.get_patients()
    return data


@api_router.get("/pharmacies", status_code=200)
def get_pharmacies(token: str = Depends(oauth2_scheme)):
    """
    Return all pharmacies
    """
    data = crud.get_pharmacies()
    return data


@api_router.get("/transactions", status_code=200)
def get_transactions(token: str = Depends(oauth2_scheme)):
    """
    Return all transactions
    """
    data = crud.get_transactions()
    return data
