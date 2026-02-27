from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.profiles_models import Profile
from models.notes_models import Note

def get_notes_by_profile_repo(db: Session, profile: Profile) -> List[Note]:
    stmt=select(Note).where(Note.profile_id==profile.id)
    return db.execute(stmt).scalars().all()

def get_note_by_note_id(db: Session, note_id: int) -> Note:
    stmt=select(Note).where(Note.id==note_id)
    return db.execute(stmt).scalar_one_or_none()

def create_note_repo(db: Session, note: Note) -> Note:
    try:
        db.add(note)
        db.commit()
        db.refresh(note)
        return note
    except IntegrityError:
        db.rollback()
        raise

def update_note_repo(db: Session, note: Note, new_content: str) -> Note:
    try:
        note.content=new_content
        db.commit()
        db.refresh(note)
    except IntegrityError:
        db.rollback()
        raise
    return note

def delete_note_repo(db: Session, note: Note) -> bool:
    db.delete(note)
    db.commit()
    return True