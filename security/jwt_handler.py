from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timezone, timedelta
from services import users_services
from dotenv import load_dotenv
from core.exceptions import InvalidToken, ExpiredInvalidToken
from core.database import get_db
import jwt
import os

oauth2_scheme=OAuth2PasswordBearer(tokenUrl='/login') 
load_dotenv(override=True)

ACCESS_TOKEN_EXPIRE_MINUTES=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")

def create_access_token(data: dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt=jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id=payload.get("sub")
        if not user_id:
            raise InvalidToken
        return user_id
    except jwt.PyJWTError:
        raise ExpiredInvalidToken
    
def get_current_user(token: str=Depends(oauth2_scheme), db=Depends(get_db)):
    user_id=verify_token(token)
    return users_services.get_user_by_user_id_service(db, int(user_id))