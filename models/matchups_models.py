from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped
from core.database import Base
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .notes_models import Note
    from .champions_models import Champion

class Matchup(Base):
    __tablename__='tb_matchups'
    id: Mapped[int]=mapped_column(primary_key=True)
    player_champion_id: Mapped[int]=mapped_column(ForeignKey('tb_champions.id'))
    enemy_champion_id: Mapped[int]=mapped_column(ForeignKey('tb_champions.id'))

    notes: Mapped[List['Note']]=relationship(back_populates='matchup')
    player_champion: Mapped['Champion']=relationship('Champion', foreign_keys=[player_champion_id])
    enemy_champion: Mapped['Champion']=relationship('Champion', foreign_keys=[enemy_champion_id])

    __table_args__ = (
        UniqueConstraint('player_champion_id', 'enemy_champion_id', name='_UC_champ_id_enemy_id'),
    )