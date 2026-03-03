from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    nickname: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    class Config:
        from_attributes=True

class UserUpdatePassword(BaseModel):
    email: EmailStr
    password: str
    new_password: str
    class Config:
        from_attributes=True

class UserDelete(BaseModel):
    email: EmailStr
    password: str
    class Config:
        from_attributes=True

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes=True