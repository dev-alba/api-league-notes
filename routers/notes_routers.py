from fastapi import APIRouter

note_router=APIRouter(prefix='/notes', tags=['Notas'])

@note_router.get('/', status_code=200)
def notes_root():
    return {'message': 'Hello, Notes'}