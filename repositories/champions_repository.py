from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from models.champions_models import Champion

def get_champion_by_id_repo(db: Session, champion: Champion) -> Champion:
    stmt=select(Champion).where(Champion.id==champion.id)
    return db.execute(stmt).scalar_one_or_none()

def get_champion_by_name_repo(db: Session, champion_name: str) -> Champion:
    stmt=select(Champion).where(func.lower(Champion.name)==func.lower(champion_name))
    return db.execute(stmt).scalar_one_or_none()

def get_all_champions_repo(db: Session) -> List[Champion]:
    stmt=select(Champion)
    return db.execute(stmt).scalars().all()

def create_champion_repo(db: Session, champion: Champion):
    db.merge(champion)
    return