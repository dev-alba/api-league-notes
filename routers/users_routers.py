from fastapi import APIRouter, Depends
from services import users_services
from core.database import get_db
from schemas.user_schemas import UserResponse, UserUpdatePassword, UserCreate
from security.jwt_handler import get_current_user

user_router=APIRouter(prefix='/users', tags=['Usuários'])

@user_router.get('/', status_code=200)
def users_root():
    return {'message': 'Hello, Users'}

@user_router.get('/me', status_code=200, response_model=UserResponse)
def get_me(db=Depends(get_db), current_user=Depends(get_current_user)):
    return users_services.get_user_by_user_id_service(db, current_user.id)


    
@user_router.patch('/', status_code=200, response_model=UserResponse)
def update_user_password_router(data: UserUpdatePassword, current_user: int=Depends(get_current_user), db=Depends(get_db)):
    return users_services.update_user_service(db, current_user.id, data.password, data.new_password)
    
@user_router.delete('/', status_code=204)
def delete_user_router(password: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    return users_services.delete_user_service(db, current_user.id, password)