from datetime import datetime
from pydantic import BaseModel, PastDatetime

class NoteBase(BaseModel):
    content: str
    class Config:
        from_attributes=True

class NoteCreate(NoteBase):
    player_champion_name: str
    enemy_champion_name: str
    class Config:
        from_attributes=True

class NoteUpdate(NoteBase):
    class Config:
        from_attributes=True

class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    last_update: datetime
    profile_id: int
    class Config:
        from_attributes=True