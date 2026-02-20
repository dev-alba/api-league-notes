from passlib.context import CryptContext

pwd_context=CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)

def hash_pwd(password: str) -> str:
    return pwd_context.hash(password)

def validate_pwd(pwd: str, hashed_pwd: str) -> bool:
    return pwd_context.verify(pwd, hashed_pwd)

