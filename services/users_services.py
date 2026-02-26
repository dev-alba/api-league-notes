from sqlalchemy.exc import IntegrityError
from repositories import users_repository
from excepctions import InvalidCredentials, UserNotFound, UserAlreadyExists, UserCannotBeDeleted
from security import validate_pwd, hash_pwd
from models.users_models import User

def create_user_service(db, nickname, email, password):
    existing_user=users_repository.get_user_by_email_repo(db, email)
    if existing_user:
        raise UserAlreadyExists
    hashed=hash_pwd(password)
    user=User(
        nickname=nickname,
        password=hashed,
        email=email)
    try:
        return users_repository.create_user_repo(db, user)
    except IntegrityError:
        raise UserAlreadyExists

def get_user_by_email_service(db, email):
    user=users_repository.get_user_by_email_repo(db, email)
    if not user:
        raise UserNotFound
    return user

def auth_user_credentials_service(db, email, password):
    user=get_user_by_email_service(db, email)
    if not validate_pwd(password, user.password):
        raise InvalidCredentials
    return user

def update_user_service(db, email, password, new_password):
    user=auth_user_credentials_service(db, email, password)
    return users_repository.update_user_password_repo(db, user, new_password)

def delete_user_service(db, email, password):
    user=auth_user_credentials_service(db, email, password)
    try:
        return users_repository.delete_user_repo(db, user)
    except IntegrityError:
        raise UserCannotBeDeleted
    