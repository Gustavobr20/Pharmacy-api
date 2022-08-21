from fastapi import FastAPI, Depends, HTTPException, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.crud import crud
from .api.v1.endpoints import api_router


app = FastAPI(title="Pharmacy API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@app.get("/")
def get_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.post("/token")
def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):

    user = crud.get_user(form_data.username)

    if user:
        if user.PASSWORD == form_data.password:
            return {"access_token": user.USERNAME, "token_type": "bearer"}

    raise HTTPException(
        status_code=400, detail="Incorrect username or password")


@app.post("/user/create", status_code=200)
def create_user(username: str = Form(), password: str = Form()):

    user_created = crud.create_user(username, password)

    if user_created:
        return {"message": "user created successfully"}
    else:
        return {"message": "user is already in use, please change"}


app.include_router(api_router, prefix='/api/v1', tags=['Pharmacy'])
