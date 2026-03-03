from sqlalchemy.exc import IntegrityError
from repositories import users_repository
from core.exceptions import InvalidCredentials, UserNotFound, UserAlreadyExists, UserCannotBeDeleted
from security.security import validate_pwd, hash_pwd
from models.users_models import User

def create_user_service(db, nickname, email, password) -> User:
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

def get_user_by_user_id_service(db, user_id) -> User:
    user=users_repository.get_user_by_user_id_repo(db, user_id)
    if not user:
        raise UserNotFound
    return user

def get_user_by_email_service(db, email) -> User:
    user=users_repository.get_user_by_email_repo(db, email)
    if not user:
        raise InvalidCredentials
    return user

def user_auth_credentials_service(db, identifier, password) -> User:
    user=users_repository.get_user_by_nick_or_email_repo(db, identifier)
    if not validate_pwd(password, user.password):
        raise InvalidCredentials
    return user

def user_auth_user_id(db, user_id, password) -> User:
    user=users_repository.get_user_by_user_id_repo(db, user_id)
    if not user:
        validate_pwd(password, password)
        raise UserNotFound
    if not validate_pwd(password, user.password):
        raise InvalidCredentials
    return user

def update_user_service(db, user_id, password, new_password) -> User:
    user=user_auth_user_id(db, user_id, password)
    user.password=hash_pwd(new_password)
    return users_repository.update_user_password_repo(db, user, new_password)

def delete_user_service(db, user_id, password) -> bool:
    user=user_auth_user_id(db, user_id, password)
    try:
        return users_repository.delete_user_repo(db, user)
    except IntegrityError:
        raise UserCannotBeDeleted