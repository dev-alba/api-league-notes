from fastapi import APIRouter, Depends
from core.database import get_db
from security.jwt_handler import get_current_user
from services import matchups_service

matchup_router=APIRouter(prefix='/matchups', tags=['Matchups'])

@matchup_router.get('/get/{matchup_id}', status_code=200)
def get_matchup_router(matchup_id: int, current_user=Depends(get_current_user), db=Depends(get_db)):
    return matchups_service.get_matchup_service(db, matchup_id)

@matchup_router.post('/', status_code=201)
def create_matchup_router(player_champion: str, enemy_champion: str, current_user=Depends(get_current_user), db=Depends(get_db)):
    return matchups_service.create_matchup_service(db, player_champion, enemy_champion)