from repositories import matchups_repository, champions_repository
from models.matchups_models import Matchup
from core.exceptions import MatchupAlreadyExists, MatchupNotFound, ChampNotFound

def get_matchup_service(db, matchup_id):
    matchup=matchups_repository.get_matchup_repo(db, matchup_id)
    if not matchup:
        raise MatchupNotFound
    return matchups_repository.get_matchup_repo(db, matchup_id)

def get_matchup_by_names(db, player_champion_name, enemy_champion_name):
    player_champion=champions_repository.get_champion_by_name_repo(db, player_champion_name)
    enemy_champion=champions_repository.get_champion_by_name_repo(db, enemy_champion_name)
    if not player_champion or not enemy_champion:
        raise ChampNotFound
    matchup=matchups_repository.get_matchup_by_champions_ids(db, player_champion.id, enemy_champion.id)
    if not matchup:
        matchup=create_matchup_service(db, player_champion.id, enemy_champion.id)
        return matchup
    return matchup

def create_matchup_service(db, player_champion_id, enemy_champion_id):
    matchup=Matchup(
        player_champion_id=player_champion_id,
        enemy_champion_id=enemy_champion_id
    )
    try:
        return matchups_repository.create_matchup_repo(db, matchup)
    except:
        raise MatchupAlreadyExists