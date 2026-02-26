from fastapi import APIRouter, Depends, HTTPException
from repositories import users_repository
from database import get_db
from schemas import UserResponse, UserUpdate, UserCreate
from excepctions import UserAlreadyExists, UserNotFound, InvalidCredentials

user_router=APIRouter(prefix='/users', tags=['Usuários'])

@user_router.get('/', status_code=200)
def users_root():
    return {'message': 'Hello, Users'}

@user_router.get('/get', status_code=200, response_model=UserResponse)
def get_user(
    nickname: str | None = None,
    email: str | None = None,
    db=Depends(get_db)
    ):
    if nickname:
        try:
            user=users_repository.get_user_by_nickname_repo(db, nickname)
            return user
        except UserNotFound:
            raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    if email:
        try:
            user=users_repository.get_user_by_email_repo(db, email)
            return user
        except UserNotFound:
            raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    raise HTTPException(status_code=400, detail='Informe nickname ou email para executar a busca.')

@user_router.post('/create', status_code=201, response_model=UserResponse)
def create_user(data: UserCreate, db=Depends(get_db)):
    try:
        user=users_repository.create_user_repo(db, data.nickname, data.password, data.email)
        return user
    except UserAlreadyExists:
        raise HTTPException(status_code=409, detail='Usuário já existente no sistema. Por favor, digite outro nickname/email e tente novamente.')
    
@user_router.patch('/update', status_code=200, response_model=UserResponse)
def update_user_password(data: UserUpdate, db=Depends(get_db)):
    try:
        user=users_repository.update_user_pass_repo(db, data.nickname, data.password, data.email, data.new_password)
        return user
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except InvalidCredentials:
        raise HTTPException(status_code=403, detail='Credenciais inválidas. Por favor, verifique os dados e tente novamente.') 
    
@user_router.delete('/delete/{nickname}', status_code=204)
def delete_user(nickname: str, password: str, email: str, db=Depends(get_db)):
    try:
        users_repository.delete_user_repo(db, nickname, password, email)
        return
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except InvalidCredentials:
        raise HTTPException(status_code=403, detail='Credenciais inválidas. Por favor, verifique os dados e tente novamente.')