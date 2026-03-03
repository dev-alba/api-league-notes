from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.champions_models import Champion

def get_champion_repo(db: Session, champion: Champion) -> Champion:
    stmt=select(Champion).where(Champion.id==champion.id)
    return db.execute(stmt).scalar_one_or_none()

def get_all_champions_repo(db: Session) -> List[Champion]:
    stmt=select(Champion)
    return db.execute(stmt).scalars().all()

def create_champion_reto(db: Session, champion: Champion):
    db.merge(champion)
    return