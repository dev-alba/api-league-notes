from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, func, Text
from sqlalchemy.orm import relationship, mapped_column, Mapped
from core.database import Base

if TYPE_CHECKING:
    from .profiles_models import Profile

class Note(Base):
    __tablename__='tb_notes'
    id: Mapped[int]=mapped_column(primary_key=True)
    created_at: Mapped[datetime]=mapped_column(server_default=func.now())
    content: Mapped[str]=mapped_column(Text, deferred=True, nullable=False)
    last_update: Mapped[datetime]=mapped_column(server_default=func.now(), onupdate=func.now())
    profile_id: Mapped[int]=mapped_column(ForeignKey('tb_profiles.id'))
    user_id: Mapped[int]=mapped_column(ForeignKey('tb_users.id'))
    profile: Mapped['Profile']=relationship(back_populates='notes')