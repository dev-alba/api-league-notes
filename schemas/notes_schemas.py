from pydantic import BaseModel, PastDatetime

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
    profile_id: int
    class Config:
        from_attributes=True

class NoteResponse(NoteBase):
    created_at: PastDatetime
    last_update: PastDatetime
    profile_id: int
    class Config:
        from_attributes=True  