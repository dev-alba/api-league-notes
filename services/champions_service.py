from repositories import champions_repository
from core import exceptions

def get_champion_service(db, champion):
    champion=champions_repository.get_champion_repo(db, champion)
    if not champion:
        raise exceptions.ChampNotFound
    return champion

def get_all_champions_service(db):
    champions=champions_repository.get_all_champions_repo(db)
    if not champions:
        raise exceptions.ChampionsNotFound
    return champions

def create_champion_service(db, champion):
    champion_existent=champions_repository.get_champion_repo(db, champion)
    if not champion_existent:
        return champions_repository.create_champion_reto(db, champion)
    raise exceptions.ChampAlreadyExists()