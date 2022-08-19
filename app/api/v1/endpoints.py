from fastapi import APIRouter
from app.crud import *


api_router = APIRouter()


@api_router.get("/patients", status_code=200)
def search_patients():

    data = get_patients()
    return data


@api_router.get("/pharmacies", status_code=200)
def search_pharmacies():

    data = get_pharmacies()
    return data


@api_router.get("/transactions", status_code=200)
def search_transactions():

    data = get_transactions()
    return data
