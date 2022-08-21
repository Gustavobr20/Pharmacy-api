from fastapi import APIRouter, Form
from app.crud import crud


api_router = APIRouter()


@api_router.get("/patients", status_code=200)
def get_patients():

    data = crud.get_patients()
    return data


@api_router.get("/pharmacies", status_code=200)
def get_pharmacies():

    data = crud.get_pharmacies()
    return data


@api_router.get("/transactions", status_code=200)
def get_transactions():

    data = crud.get_transactions()
    return data
