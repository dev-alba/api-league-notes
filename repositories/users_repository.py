from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, func, or_
from models.users_models import User
from security.security import hash_pwd

def get_user_by_user_id_repo(db: Session, user_id: int) -> User:
    stmt=select(User).where(User.id==user_id)
    return db.execute(stmt).scalar_one_or_none()

def get_user_by_email_repo(db: Session, email: str) -> User:
    stmt=select(User).where(
        func.lower(User.email)==func.lower(email))
    return db.execute(stmt).scalar_one_or_none()

def get_user_by_nick_or_email_repo(db: Session, identifier: str) -> User:
    stmt=select(User).where(
        or_(func.lower(User.email)==func.lower(identifier), 
            func.lower(User.nickname)==func.lower(identifier))
        )
    return db.execute(stmt).scalar_one_or_none()

def create_user_repo(db: Session, user: User) -> User:
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise

def update_user_password_repo(db: Session, user: User, new_password: str) -> User:
    user.password=hash_pwd(new_password)
    try:
        db.commit()
        db.refresh(user)
        return user
    except Exception:
        db.rollback()
        raise

def delete_user_repo(db: Session, user: User) -> bool:
    try:
         db.delete(user)
         db.commit()
    except IntegrityError:
        db.rollback()
        raise
    return True