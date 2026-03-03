from pydantic import BaseModel, EmailStr

class LoginBase(BaseModel):
    pass

class LoginSchema(LoginBase):
    email: EmailStr
    password: str
    class Config:
        from_attributes=True   