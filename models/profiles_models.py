from typing import List, TYPE_CHECKING
from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped
from database import Base

if TYPE_CHECKING:
    from .users_models import User
    from .notes_models import Note

class Profile(Base):
    __tablename__='tb_profiles'
    id: Mapped[int]=mapped_column(primary_key=True)
    nickname: Mapped[str]=mapped_column()
    tagline: Mapped[str]=mapped_column()
    user_id: Mapped[int]=mapped_column(ForeignKey('tb_users.id'))
    notes: Mapped[List['Note']]=relationship(back_populates='profile', cascade='all, delete-orphan')
    user: Mapped['User']=relationship(back_populates='profiles')

    __table_args__ = (
        UniqueConstraint('nickname', 'tagline', name='_UC_nickname_tagline'),
    )