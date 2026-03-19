from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from core.database import get_db
from services import auth_service, users_services
from schemas.user_schemas import UserResponse, UserCreate


auth_router=APIRouter(tags=['Authentication'])

@auth_router.post('/login')
def login_user_router(form_data: OAuth2PasswordRequestForm=Depends(), db=Depends(get_db)):
    token=auth_service.authenticate_user(db, form_data.username, form_data.password)
    return {"access_token": token, "token_type": "bearer"}

@auth_router.post('/register', status_code=201, response_model=UserResponse)
def create_user_router(data: UserCreate, db=Depends(get_db)):
    return users_services.create_user_service(db, data.nickname, data.email, data.password)