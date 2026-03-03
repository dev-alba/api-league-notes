from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from core.database import get_db
from services import auth_service

auth_router=APIRouter(prefix='/login', tags=['Login'])

@auth_router.post('/')
def login(form_data: OAuth2PasswordRequestForm=Depends(), db=Depends(get_db)):
    token=auth_service.authenticate_user(db, form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}