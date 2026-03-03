from typing import List
from sqlalchemy.exc import IntegrityError
from models.profiles_models import Profile
from repositories import profiles_repository, users_repository
from services import users_services
from core.exceptions import ProfileNotFound, ProfilesNotFound, ProfileAlreadyExists, ProfileCannotBeDeleted, UserNotFound, InvalidCredentials
from security.security import validate_pwd

def get_profile_by_nickname_service(db, nickname, tagline) -> Profile:
    profile=profiles_repository.get_profile_by_nickname_repo(db, nickname, tagline)
    if not profile:
        raise ProfileNotFound
    return profile

def get_profile_list_by_user_id_service(db, user_id) -> List[Profile]:
    profiles=profiles_repository.get_profile_list_by_user_id_repo(db, user_id)
    if not profiles:
        user=users_repository.get_user_by_user_id_repo(db, user_id)
        if not user:
            raise UserNotFound
        raise ProfilesNotFound
    return profiles

def create_profile_service(db, nickname, tagline, user_id) -> Profile:
    users_services.get_user_by_user_id_service(db, user_id)
    profile=Profile(
        user_id=user_id,
        nickname=nickname,
        tagline=tagline)        
    try:
        return profiles_repository.create_profile_repo(db, profile)
    except IntegrityError:
        raise ProfileAlreadyExists
    
def update_profile_service(db, user_id, nickname, tagline, new_nickname, new_tagline) -> Profile:
    users_services.get_user_by_user_id_service(db, user_id)
    profile=profiles_repository.auth_profile_user_id_repo(db, user_id, nickname, tagline)
    if not profile:
        raise ProfileNotFound
    profile.nickname=new_nickname
    profile.tagline=new_tagline
    try:
        return profiles_repository.update_profile_repo(db, profile)
    except IntegrityError:
        raise ProfileAlreadyExists
    
def delete_profile_service(db, user_id, nickname, tagline, password) -> bool:
    user=users_services.get_user_by_user_id_service(db, user_id)
    if not validate_pwd(password, user.password):
        raise InvalidCredentials
    profile=profiles_repository.auth_profile_user_id_repo(db, user_id, nickname, tagline)
    if not profile:
        raise ProfileNotFound
    try:
        return profiles_repository.delete_profile_repo(db, profile)
    except IntegrityError:
        raise ProfileCannotBeDeleted

def auth_profile_service(db, user_id, nickname, tagline) -> Profile:
    profile=profiles_repository.auth_profile_user_id_repo(db, user_id, nickname, tagline)
    if not profile:
        raise ProfileNotFound
    return profile