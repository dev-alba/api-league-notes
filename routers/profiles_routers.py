from typing import List
from fastapi import APIRouter, Depends
from schemas.profile_schemas import ProfileResponse, ProfileDelete
from services import profiles_services
from core.database import get_db
from security.jwt_handler import get_current_user

profile_router=APIRouter(prefix='/profiles', tags=['Perfis'])

@profile_router.get('/', status_code=200)
def profiles_root():
    return {'message': 'Hello, Profiles'}

@profile_router.get('/{nickname}/{tagline}', status_code=200, response_model=ProfileResponse)
def get_profile_by_nickname_router(nickname: str, tagline: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    return profiles_services.get_profile_by_nickname_service(db, nickname, tagline)

@profile_router.get('/me', status_code=200, response_model=List[ProfileResponse])
def get_profile_list_by_user_id_router(current_user=Depends(get_current_user), db=Depends(get_db)):
    return profiles_services.get_profile_list_by_user_id_service(db, current_user.id)
    
@profile_router.post('/', status_code=201, response_model=ProfileResponse)
def create_profile_router(nickname: str, tagline: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    return profiles_services.create_profile_service(db, nickname, tagline, current_user.id)
    #  CRIAR LIGAÇÃO COM API LOL PARA VALIDAR PERFIL

@profile_router.patch('/', status_code=200, response_model=ProfileResponse)
def update_profile_router(nickname: str, tagline: str, new_nickname: str, new_tagline: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    return profiles_services.update_profile_service(db, current_user.id, nickname, tagline, new_nickname, new_tagline)
    
@profile_router.delete('/', status_code=204)
def delete_profile(data: ProfileDelete, current_user=Depends(get_current_user), db=Depends(get_db)):
    return profiles_services.delete_profile_service(db, current_user.id, data.nickname, data.tagline, data.password)