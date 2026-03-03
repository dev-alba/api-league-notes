from pydantic import BaseModel

class ProfileBase(BaseModel):
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

class ProfileDelete(ProfileBase):
    password: str
    class Config:
        from_attributes=True

class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    class Config:
        from_attributes=True