from fastapi import APIRouter, Depends
from services import users_services
from database import get_db
from schemas import UserResponse, UserUpdatePassword, UserDelete, UserCreate

user_router=APIRouter(prefix='/users', tags=['Usuários'])

@user_router.get('/', status_code=200)
def users_root():
    return {'message': 'Hello, Users'}

@user_router.get('/{email}', status_code=200, response_model=UserResponse)
def get_user_router(email: str, db=Depends(get_db)):
    return users_services.get_user_by_email_service(db, email)

@user_router.post('/', status_code=201, response_model=UserResponse)
def create_user_router(data: UserCreate, db=Depends(get_db)):
    return users_services.create_user_service(db, data.nickname, data.email, data.password)
    
@user_router.patch('/', status_code=200, response_model=UserResponse)
def update_user_password_router(data: UserUpdatePassword, db=Depends(get_db)):
    return users_services.update_user_service(db, data.email, data.password, data.new_password)
    
@user_router.delete('/', status_code=204)
def delete_user_router(data: UserDelete, db=Depends(get_db)):
    return users_services.delete_user_service(db, data.email, data.password)