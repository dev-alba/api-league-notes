from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, func, Text
from models.profiles_models import Profile
from models.notes_models import Note
from models.users_models import User
from excepctions import ProfileNotFound, NoteNotFound, UserNotFound, NotesNotFound


def get_notes_by_profile_repo(db: Session, user_id: int, nickname: str, tagline: str) -> List[Note]:
    stmt=select(Profile).where(
        Profile.user_id==user_id,
        func.lower(Profile.nickname)==func.lower(nickname),
        func.lower(Profile.tagline)==func.lower(tagline)
        )
    profile=db.execute(stmt).scalar_one_or_none()
    if not profile:
        raise ProfileNotFound
    stmt=select(Note).where(Note.profile_id==profile.id)
    notes=db.execute(stmt).scalars().all()
    if not notes:
        raise NotesNotFound
    return notes

def create_note_repo(db: Session, user_id: int, nickname: str, tagline: str, content: Text) -> Note:
    stmt=select(Profile).where(
        Profile.user_id==user_id,
        func.lower(Profile.nickname)==func.lower(nickname),
        func.lower(Profile.tagline)==func.lower(tagline)        
    )
    profile=db.execute(stmt).scalar_one_or_none()
    if not profile:
        raise ProfileNotFound
    note=Note(
        user_id=user_id,
        content=content,
        profile_id=profile.id
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def update_note_repo(db: Session, user_id: int, note_id: int, new_content: str) -> Note:
    stmt=select(User).where(User.id==user_id)
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    stmt=select(Note).where(Note.id==note_id)
    note=db.execute(stmt).scalar_one_or_none()
    if not note:
        raise NoteNotFound
    note.content=new_content
    db.commit()
    db.refresh(note)
    return note

def delete_note_repo(db: Session, user_id: int, note_id: int) -> bool:
    stmt=select(User).where(User.id==user_id)
    user=db.execute(stmt).scalar_one_or_none()
    if not user:
        raise UserNotFound
    stmt=select(Note).where(Note.id==note_id)
    note=db.execute(stmt).scalar_one_or_none()
    if not note:
        raise NoteNotFound
    db.delete(note)
    db.commit()
    return True