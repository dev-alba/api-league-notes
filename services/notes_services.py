from repositories import profiles_repository, notes_repository
from services import profiles_services, matchups_service
from core.exceptions import ProfileNotFound, NotesNotFound, NoteNotFound, MatchupNotFound, Unauthorized
from models.notes_models import Note

def get_notes_by_profile_service(db, user_id, nickname, tagline):
    profile=profiles_repository.auth_profile_user_id_repo(db, user_id, nickname, tagline)
    if not profile: 
        raise ProfileNotFound
    notes=notes_repository.get_notes_by_profile_repo(db, profile)
    if not notes:
        raise NotesNotFound
    return notes
    
def create_note_service(db, user_id, nickname, tagline, player_champion_name, enemy_champion_name, content):
    profile=profiles_services.auth_profile_service(db, user_id, nickname, tagline)
    matchup=matchups_service.get_matchup_by_names(db, player_champion_name, enemy_champion_name)
    if not matchup:
        raise MatchupNotFound
    note=Note(
        matchup_id=matchup.id,
        profile_id=profile.id,
        content=content)
    return notes_repository.create_note_repo(db, note)

def update_note_service(db, user_id, nickname, tagline, note_id, new_content):
    profile=profiles_services.auth_profile_service(db, user_id, nickname, tagline)
    note=notes_repository.get_note_by_note_id(db, note_id)
    if not note:
        raise NoteNotFound
    if note.profile_id == profile.id:
        return notes_repository.update_note_repo(db, note, new_content)
    raise Unauthorized

def delete_note_service(db, user_id, nickname, tagline, note_id):
    profile=profiles_services.auth_profile_service(db, user_id, nickname, tagline)
    note=notes_repository.get_note_by_note_id(db, note_id)
    if not note:
        raise NoteNotFound
    if note.profile_id == profile.id:
        return notes_repository.delete_note_repo(db, note)
    raise Unauthorized