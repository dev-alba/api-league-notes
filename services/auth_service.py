from services.users_services import user_auth_credentials_service
from security.jwt_handler import create_access_token

def authenticate_user(db, identifier, password):
    user=user_auth_credentials_service(db, identifier, password)
    token=create_access_token(data={"sub": str(user.id)})
    return token