from pydantic import BaseModel, EmailStr, PastDatetime

#           USER SCHEMAS
class UserBase(BaseModel):
    nickname: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    class Config:
        from_attributes=True

class UserUpdate(UserBase):
    password: str
    new_password: str
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
    class Config:
        from_attributes=True

class ProfileUpdate(ProfileBase):
    new_nickname: str
    new_tagline: str     

class ProfileResponse(ProfileBase):
    id: int
    class Config:
        from_attributes=True

#           NOTES SCHEMAS
class NoteBase(BaseModel):
    id: int
    user_id: int
    content: str
    class Config:
        from_attributes=True

class NoteCreate(NoteBase):
    created_at: PastDatetime
    class Config:
        from_attributes=True

class NoteUpdate(NoteBase):
    last_update: PastDatetime
    profile_id: int
    class Config:
        from_attributes=True

class NoteResponse(NoteBase):
    created_at: PastDatetime
    profile_id: int
    class Config:
        from_attributes=True    

