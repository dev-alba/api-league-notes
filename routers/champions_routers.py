from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from security.jwt_handler import get_current_user

champion_router=APIRouter(prefix='/champions', tags=['Campeões'])

@champion_router.get('/', status_code=200)
def champions_root(current_user=Depends(get_current_user)):
    return {'message': 'Hello, Champions'}

@champion_router.post('/create', status_code=201)
def creating_champion(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return {'message': 'Champion created succefully.'}