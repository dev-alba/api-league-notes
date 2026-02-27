from typing import List
from fastapi import APIRouter, Depends
from schemas import ProfileCreate, ProfileResponse, ProfileUpdate, ProfileDelete
from services import profiles_services
from database import get_db

profile_router=APIRouter(prefix='/profiles', tags=['Perfis'])

@profile_router.get('/', status_code=200)
def profiles_root():
    return {'message': 'Hello, Profiles'}

@profile_router.get('/{nickname}/{tagline}', status_code=200, response_model=ProfileResponse)
def get_profile_by_nickname_router(nickname: str, tagline: str, db=Depends(get_db)):
    return profiles_services.get_profile_by_nickname_service(db, nickname, tagline)

@profile_router.get('/{user_id}', status_code=200, response_model=List[ProfileResponse])
def get_profile_list_by_user_id_router(user_id: int, db=Depends(get_db)):
    return profiles_services.get_profile_list_by_user_id_service(db, user_id)
    
@profile_router.post('/', status_code=201, response_model=ProfileResponse)
def create_profile_router(data: ProfileCreate, db=Depends(get_db)):
    return profiles_services.create_profile_service(db, data.nickname, data.tagline, data.user_id)
    #  CRIAR LIGAÇÃO COM API LOL PARA VALIDAR PERFIL

@profile_router.patch('/', status_code=200, response_model=ProfileResponse)
def update_profile_router(data: ProfileUpdate, db=Depends(get_db)):
    return profiles_services.update_profile_service(db, data.user_id, data.nickname, data.tagline, data.new_nickname, data.new_tagline)
    
@profile_router.delete('/', status_code=204)
def delete_profile(data: ProfileDelete, db=Depends(get_db)):
    return profiles_services.delete_profile_service(db, data.user_id, data.nickname, data.tagline, data.password)