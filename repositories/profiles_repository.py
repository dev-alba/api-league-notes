from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from models.profiles_models import Profile

def get_profile_by_nickname_repo(db: Session, nickname: str, tagline: str) -> Profile:
    stmt=select(Profile).where(
        func.lower(Profile.nickname)==func.lower(nickname),
        func.lower(Profile.tagline)==func.lower(tagline))
    return db.execute(stmt).scalar_one_or_none()

def get_profile_list_by_user_id_repo(db: Session, user_id: int) -> List[Profile]:
    stmt=select(Profile).where(Profile.user_id==user_id)
    return db.execute(stmt).scalars().all()

def create_profile_repo(db: Session, profile: Profile) -> Profile:
    try:
        db.add(profile)
        db.commit()
        db.refresh(profile)
        return profile
    except IntegrityError:
        db.rollback()
        raise

def auth_profile_user_id_repo(db: Session, user_id: int, nickname: str, tagline: str) -> Profile:
    stmt=select(Profile).where(
        func.lower(Profile.nickname)==func.lower(nickname),
        func.lower(Profile.tagline)==func.lower(tagline),
        Profile.user_id==user_id)
    return db.execute(stmt).scalar_one_or_none()

def update_profile_repo(db: Session, profile: Profile) -> Profile:
    try:
        db.commit()
        db.refresh(profile)
        return profile
    except IntegrityError:
        db.rollback()
        raise
    
def delete_profile_repo(db: Session, profile: Profile) -> bool:
    try:
        db.delete(profile)
        db.commit()
        return True
    except IntegrityError:
        raise