from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from models.matchups_models import Matchup

def get_matchup_repo(db: Session, matchup_id: int) -> Matchup:
    stmt=select(Matchup).where(Matchup.id==matchup_id)
    return db.execute(stmt).scalar_one_or_none()

def get_matchup_by_champions(db: Session, player_champ: int, enemy_champ: int) -> Matchup:
    stmt=select(Matchup).where(Matchup.player_champion==player_champ, Matchup.enemy_champion==enemy_champ)
    return db.execute(stmt).scalar_one_or_none()

def create_matchup_repo(db: Session, matchup: Matchup) -> Matchup:
    try:
        db.add(matchup)
        db.commit()
        db.refresh(matchup)
        return matchup
    except IntegrityError:
        db.rollback()
        raise