from typing import List, TYPE_CHECKING
from sqlalchemy.orm import relationship, mapped_column, Mapped
from core.database import Base

if TYPE_CHECKING:
    from .profiles_models import Profile

class User(Base):
    __tablename__='tb_users'
    id: Mapped[int]=mapped_column(primary_key=True)
    nickname: Mapped[str]=mapped_column(unique=True)
    email: Mapped[str]=mapped_column(unique=True)
    password: Mapped[str]
    profiles: Mapped[List['Profile']]=relationship(back_populates='user', cascade='all, delete-orphan')
