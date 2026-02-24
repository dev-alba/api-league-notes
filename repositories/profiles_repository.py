from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, or_, func
from sqlalchemy.exc import IntegrityError
from models.profiles_models import Profile
from models.users_models import User
from excepctions import ProfileNotFound, ProfileAlreadyExists, InvalidCredentials, UserNotFound, ProfilesNotFound
from security import validate_pwd

def get_profile_by_nickname_repo(db: Session, nickname: str, tagline: str) -> Profile:
    stmt=select(Profile).where(
        func.lower(Profile.nickname)==func.lower(nickname),
        func.lower(Profile.tagline)==func.lower(tagline))
    profile=db.execute(stmt).scalar_one_or_none()
    if not profile:
        raise ProfileNotFound
    return profile

def get_profiles_by_user_id_repo(db: Session, user_id: int) -> List[Profile]:
    stmt=select(Profile).where(Profile.user_id==user_id)
    profiles=db.execute(stmt).scalars().all()
    if not profiles:
        stmt=select(User).where(User.id==user_id)
        user=db.execute(stmt).scalar_one_or_none()
        if not user:
            raise UserNotFound
        raise ProfilesNotFound
    return profiles

def create_profile_repo(db: Session, user_id: int, nickname: str, tagline: str) -> Profile:
    stmt=select(User).where(User.id==user_id)
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    stmt=select(Profile).where(Profile.nickname==nickname, Profile.tagline==tagline)
    profile=db.execute(stmt).scalar_one_or_none()
    if profile:
        raise ProfileAlreadyExists
    profile=Profile(
        user_id=user_id,
        nickname=nickname,
        tagline=tagline
    )
    try:
        db.add(profile)
        db.commit()
        db.refresh(profile)
    except IntegrityError:
        raise ProfileAlreadyExists
    return profile

def update_profile_repo(db: Session, user_id: int, nickname: str, tagline: str, new_nickname: str, new_tagline: str) -> Profile:
    stmt=select(User).where(User.id==user_id)
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    stmt=select(Profile).where(
        func.lower(Profile.nickname)==func.lower(nickname),
        func.lower(Profile.tagline)==func.lower(tagline),
        Profile.user_id==user_id
    )
    profile=db.execute(stmt).scalar_one_or_none()
    if not profile:
        raise ProfileNotFound 
    profile.nickname=new_nickname
    profile.tagline=new_tagline
    try:
        db.commit()
        db.refresh(profile)
        return profile
    except IntegrityError:
        db.rollback()
        raise ProfileAlreadyExists
    
def delete_profile_repo(db: Session, user_id: int, password: str, nickname: str, tagline: str) -> bool:
    stmt=select(User).where(User.id==user_id)
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    validation=validate_pwd(password, user.password)
    if not validation:
        raise InvalidCredentials
    stmt=select(Profile).where(
        func.lower(Profile.nickname)==func.lower(nickname), 
        func.lower(Profile.tagline)==func.lower(tagline),
        Profile.user_id==user_id
    )
    profile=db.execute(stmt).scalar_one_or_none()
    if not profile:
        raise ProfileNotFound
    db.delete(profile)
    db.commit()
    return True    
