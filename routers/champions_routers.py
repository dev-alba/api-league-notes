from fastapi import APIRouter, Depends
from core.database import get_db
from security.jwt_handler import get_current_user
from services import champions_service

champion_router=APIRouter(prefix='/champions', tags=['Campeões'])

@champion_router.get('/', status_code=200)
def champions_root(current_user=Depends(get_current_user)):
    return {'message': 'Hello, Champions'}

@champion_router.get('/all', status_code=200)
def get_all_champions_router(db=Depends(get_db), current_user=Depends(get_current_user)):
    return champions_service.get_all_champions_service(db)