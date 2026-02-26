from typing import List
from fastapi import APIRouter, Depends, HTTPException
from schemas import ProfileCreate, ProfileResponse, ProfileUpdate
from repositories import profiles_repository
from database import get_db
from excepctions import ProfileNotFound, ProfileAlreadyExists, InvalidCredentials, UserNotFound, ProfilesNotFound

profile_router=APIRouter(prefix='/profiles', tags=['Perfis'])

@profile_router.get('/', status_code=200)
def profiles_root():
    return {'message': 'Hello, Profiles'}

@profile_router.get('/get/{nickname}/{tagline}', status_code=200, response_model=ProfileResponse)
def get_profile_by_nick(nickname: str, tagline: str, db=Depends(get_db)):
    try:
        profile=profiles_repository.get_profile_by_nickname_repo(db, nickname, tagline)
        return profile
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail='Perfil não encontrado no sistema. Por favor verifique os dados e tente novamente.')

@profile_router.get('/profiles/{user_id}', status_code=200, response_model=List[ProfileResponse])
def get_profiles_by_user_id(user_id: int, db=Depends(get_db)):
    try:
        profiles=profiles_repository.get_profiles_by_user_id_repo(db, user_id)
        return profiles
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except ProfilesNotFound:
        raise HTTPException(status_code=404, detail='Nenhum perfil encontrado no sistema. Por favor verifique os dados e tente novamente.')
    
@profile_router.post('/create', status_code=201, response_model=ProfileCreate)
def create_profile(data: ProfileCreate, db=Depends(get_db)):
    try:
        profile=profiles_repository.create_profile_repo(db, data.user_id, data.nickname, data.tagline)
        return profile
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    #  CRIAR LIGAÇÃO COM API LOL PARA VALIDAR PERFIL

@profile_router.patch('/update', status_code=200, response_model=ProfileResponse)
def update_profile(data: ProfileUpdate, db=Depends(get_db)):
    try:
        profile=profiles_repository.update_profile_repo(db, data.user_id, data.nickname, data.tagline, data.new_nickname, data.new_tagline)
        return profile
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail='Nenhum perfil encontrado no sistema. Por favor verifique os dados e tente novamente.')
    except ProfileAlreadyExists:
        raise HTTPException(status_code=409, detail='O nome de usuário/tagline digitado já existe no sistema. Por favor tente novamente com outra combinação.')
    
@profile_router.delete('/delete/{nickname}/{tagline}', status_code=204)
def delete_profile(user_id: int, password: str, nickname: str, tagline: str, db=Depends(get_db)):
    try:
        profiles_repository.delete_profile_repo(db, user_id, password, nickname, tagline)
        return
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail='Nenhum perfil encontrado no sistema. Por favor verifique os dados e tente novamente.')
    except InvalidCredentials:
        raise HTTPException(status_code=403, detail='Credenciais inválidas. Por favor, verifique os dados e tente novamente.')     