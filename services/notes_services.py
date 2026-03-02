from repositories import profiles_repository, notes_repository
from services import profiles_services
from excepctions import ProfileNotFound, NotesNotFound, NoteNotFound
from models.notes_models import Note

def get_notes_by_profile_service(db, user_id, nickname, tagline):
    profile=profiles_repository.auth_profile_user_id_repo(db, user_id, nickname, tagline)
    if not profile: 
        raise ProfileNotFound
    notes=notes_repository.get_notes_by_profile_repo(db, profile)
    if not notes:
        raise NotesNotFound
    return notes
    
def create_note_service(db, user_id, nickname, tagline, content):
    profile=profiles_services.auth_profile_service(db, user_id, nickname, tagline)
    note=Note(
        user_id=user_id,
        content=content,
        profile_id=profile.id)
    return notes_repository.create_note_repo(db, note)

def update_note_service(db, user_id, nickname, tagline, note_id, new_content):
    profiles_services.auth_profile_service(db, user_id, nickname, tagline)
    note=notes_repository.get_note_by_note_id(db, note_id)
    if not note:
        raise NoteNotFound
    return notes_repository.update_note_repo(db, note, new_content)

def delete_note_service(db, user_id, nickname, tagline, note_id):
    profiles_services.auth_profile_service(db, user_id, nickname, tagline)
    note=notes_repository.get_note_by_note_id(db, note_id)
    if not note:
        raise NoteNotFound
    return notes_repository.delete_note_repo(db, note)