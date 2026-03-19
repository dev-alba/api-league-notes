from repositories import matchups_repository, champions_repository
from models.matchups_models import Matchup
from core.exceptions import MatchupAlreadyExists, MatchupNotFound

def get_matchup_service(db, matchup_id):
    matchup=matchups_repository.get_matchup_repo(db, matchup_id)
    if not matchup:
        raise MatchupNotFound
    return matchups_repository.get_matchup_repo(db, matchup_id)

def create_matchup_service(db, player_champ_name, enemy_champ_name):
    player_champ=champions_repository.get_champion_by_name_repo(db, player_champ_name)
    enemy_champ=champions_repository.get_champion_by_name_repo(db, enemy_champ_name)
    matchup=matchups_repository.get_matchup_by_champions(db, player_champ.id, enemy_champ.id)
    if not matchup:
        matchup=Matchup(
            player_champion_id=player_champ,
            enemy_champion_id=enemy_champ
        )
        try:
            return matchups_repository.create_matchup_repo(db, matchup)
        except:
            raise MatchupAlreadyExists            
    