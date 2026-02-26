from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, or_, func
from models.users_models import User
from security import hash_pwd

def get_user_by_email_repo(db: Session, email: str):
    stmt=select(User).where(
        func.lower(User.email)==func.lower(email)
        )
    return db.execute(stmt).scalar_one_or_none()

def create_user_repo(db: Session, user: User):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise

def update_user_password_repo(db: Session, user: User, new_password: str):
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