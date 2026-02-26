from typing import List
from fastapi import APIRouter, Depends, HTTPException
from schemas import NoteResponse, NoteCreate, NoteUpdate
from database import get_db
from repositories import notes_repository
from excepctions import ProfileNotFound, NoteNotFound, UserNotFound, NotesNotFound

note_router=APIRouter(prefix='/notes', tags=['Notas'])

@note_router.get('/', status_code=200)
def notes_root():
    return {'message': 'Hello, Notes'}

@note_router.get('/get', status_code=200, response_model=List[NoteResponse])
def get_note_by_profile(user_id: int, nickname: str, tagline: str, db=Depends(get_db)):
    try:
        notes=notes_repository.get_notes_by_profile_repo(db, user_id, nickname, tagline)
        return notes
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail='Perfil não encontrado no sistema. Por favor verifique os dados e tente novamente.')
    except NotesNotFound:
        raise HTTPException(status_code=404, detail='Nenhuma nota encontrada para o perfil. Por favor verifique se o perfil informado possui alguma nota e tente novamente.')

@note_router.post('/create', status_code=201, response_model=NoteCreate)
def create_note(user_id: int, nickname: str, tagline: str, content: str, db=Depends(get_db)):
    try:
        note=notes_repository.create_note_repo(db, user_id, nickname, tagline, content)
        return note
    except ProfileNotFound:
        raise HTTPException(status_code=404, detail='Perfil não encontrado no sistema. Por favor verifique os dados e tente novamente.')
    
@note_router.patch('/update', status_code=200, response_model=NoteUpdate)
def update_note(user_id: int, note_id: int, new_content: str, db=Depends(get_db)):
    try:
        note=notes_repository.update_note_repo(db, user_id, note_id, new_content)
        return note
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except NoteNotFound:
        raise HTTPException(status_code=404, detail='Nenhuma nota com esse ID encontrada no sistema. Por favor verifique se o perfil informado possui essa nota e tente novamente.')
    
@note_router.delete('/update/{note_id}', status_code=204)
def delete_note(user_id: int, note_id: int, db=Depends(get_db)):
    try:
        notes_repository.delete_note_repo(db, user_id, note_id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail='Usuário não encontrado no sistema. Por favor, verifique os dados e tente novamente.')
    except NoteNotFound:
        raise HTTPException(status_code=404, detail='Nenhuma nota com esse ID encontrada no sistema. Por favor verifique se o perfil informado possui essa nota e tente novamente.')