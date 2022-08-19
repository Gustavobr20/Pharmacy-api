from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .api.v1.endpoints import api_router
import uvicorn


app = FastAPI(title="Pharmacy API")
root_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def run_server():
    uvicorn.run("app.main:app", host='127.0.0.1', port=8000, reload=True)


@root_router.get("/")
def token(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@root_router.get("/token")
def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}


app.include_router(root_router, prefix='/api', tags=['Authentication'])
app.include_router(api_router, prefix='/api/v1', tags=['Pharmacy'])

