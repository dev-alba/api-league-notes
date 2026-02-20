from pydantic import BaseModel, EmailStr, PastDatetime

#           USER SCHEMAS
class UserBase(BaseModel):
    nickname: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    class Config:
        from_attributes=True

class UserDelete(UserBase):
    password: str
    class Config:
        from_attributes=True

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes=True


#           PROFILE SCHEMAS
class ProfileBase(BaseModel):
    user_id: int
    nickname: str
    tagline: str
    class Config:
        from_attributes=True

class ProfileCreate(ProfileBase):
    id: int
    class Config:
        from_attributes=True

class ProfileDelete(BaseModel):
    class Config:
        from_attributes=True        

class ProfileResponse(ProfileBase):
    id: int
    class Config:
        from_attributes=True

#           NOTES SCHEMAS
class NoteBase(BaseModel):
    id: str
    created_at: PastDatetime
    user_id: int
    profile_id: int
    content: str
    class Config:
        from_attributes=True
