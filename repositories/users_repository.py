from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, or_, func
from models.users_models import User
from security import hash_pwd, validate_pwd
from excepctions import UserNotFound, UserAlreadyExists, InvalidCredentials

def get_user_by_nickname_repo(db: Session, nickname: str) -> User:
    stmt=select(User).where(func.lower(User.nickname)==func.lower(nickname))
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    return user

def get_user_by_email_repo(db: Session, email: str) -> User:
    stmt=select(User).where(func.lower(User.email)==func.lower(email))
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    return user

def create_user_repo(db: Session, nickname: str, password: str, email: str) -> User:
    stmt=select(User).where(
        or_(func.lower(User.nickname)==func.lower(nickname),
            func.lower(User.email)==func.lower(email)))
    existing_user=db.execute(stmt).scalar_one_or_none()
    if existing_user:
        raise UserAlreadyExists
    
    hashed=hash_pwd(password)
    user=User(
        nickname=nickname,
        password=hashed,
        email=email
    )

    try:
        db.add(user)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise UserAlreadyExists
    
    db.refresh(user)

    return user

def update_user_pass_repo(db: Session, nickname: str, password: str, email: str) -> User:
    stmt=select(User).where(
        func.lower(User.nickname)==func.lower(nickname),
        func.lower(User.email)==func.lower(email)
        )
    user=db.execute(stmt).scalar_one_or_none()

    if not user:
        raise UserNotFound
    
    hashed=hash_pwd(password)
    user.password=hashed

    db.commit()
    db.refresh(user)
    return user

def delete_user_repo(db: Session, nickname: str, password: str, email: str) -> bool:
     stmt=select(User).where(
         func.lower(User.nickname)==func.lower(nickname),
         func.lower(User.email)==func.lower(email)
         )
     user=db.execute(stmt).scalar_one_or_none()

     if not user:
         raise UserNotFound
     
     validation=validate_pwd(password, user.password)

     if not validation:
         raise InvalidCredentials
     
     db.delete(user)
     db.commit()

     return True