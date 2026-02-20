from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from database import Base

class Champions(Base):
    __tablename__='tb_champions'
    champ_id: Mapped[int]=mapped_column(primary_key=True)
    champ_name: Mapped[str]=mapped_column(unique=True)
    champ_title: Mapped[str]=mapped_column(unique=True)