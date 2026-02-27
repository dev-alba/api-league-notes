from typing import List
from fastapi import APIRouter, Depends
from schemas import NoteResponse
from database import get_db
from services import notes_services

note_router=APIRouter(prefix='/notes', tags=['Notas'])

@note_router.get('/', status_code=200)
def notes_root():
    return {'message': 'Hello, Notes'}

@note_router.get('/get', status_code=200, response_model=List[NoteResponse])
def get_notes_by_profile_router(user_id: int, nickname: str, tagline: str, db=Depends(get_db)):
    return notes_services.get_notes_by_profile_service(db, user_id, nickname, tagline)

@note_router.post('/create', status_code=201, response_model=NoteResponse)
def create_note_router(user_id: int, nickname: str, tagline: str, content: str, db=Depends(get_db)):
    return notes_services.create_note_service(db, user_id, nickname, tagline, content)
    
@note_router.patch('/update', status_code=200, response_model=NoteResponse)
def update_note_router(user_id: int, nickname: str, tagline: str, note_id: int, new_content: str, db=Depends(get_db)):
    return notes_services.update_note_service(db, user_id, nickname, tagline, note_id, new_content)
    
@note_router.delete('/update/{note_id}', status_code=204)
def delete_note(user_id: int, nickname: str, tagline: str, note_id: int, db=Depends(get_db)):
    return notes_services.delete_note_service(db, user_id, nickname, tagline, note_id)