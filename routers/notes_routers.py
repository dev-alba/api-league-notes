from typing import List
from fastapi import APIRouter, Depends
from schemas.notes_schemas import NoteResponse, NoteCreate, NoteUpdate
from core.database import get_db
from services import notes_services
from security.jwt_handler import get_current_user

note_router=APIRouter(prefix='/notes', tags=['Notas'])

@note_router.get('/', status_code=200)
def notes_root(current_user=Depends(get_current_user)):
    return {'message': 'Hello, Notes'}

@note_router.get('/get', status_code=200, response_model=List[NoteResponse])
def get_notes_by_profile_router(nickname: str, tagline: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    return notes_services.get_notes_by_profile_service(db, current_user.id, nickname, tagline)

@note_router.post('/create', status_code=201, response_model=NoteResponse)
def create_note_router(nickname: str, tagline: str, data: NoteCreate, current_user=Depends(get_current_user), db=Depends(get_db)):
    return notes_services.create_note_service(db, current_user.id, nickname, tagline, data.player_champion_name, data.enemy_champion_name, data.content)
    
@note_router.patch('/update', status_code=200, response_model=NoteResponse)
def update_note_router(nickname: str, tagline: str, note_id: int, data: NoteUpdate, current_user=Depends(get_current_user), db=Depends(get_db)):
    return notes_services.update_note_service(db, current_user.id, nickname, tagline, note_id, data.content)
    
@note_router.delete('/delete/{note_id}', status_code=204)
def delete_note(nickname: str, tagline: str, note_id: int, current_user=Depends(get_current_user), db=Depends(get_db)):
    return notes_services.delete_note_service(db, current_user.id, nickname, tagline, note_id)