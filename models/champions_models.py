from sqlalchemy.orm import mapped_column, Mapped
from core.database import Base

class Champion(Base):
    __tablename__='tb_champions'
    id: Mapped[int]=mapped_column(primary_key=True)
    name: Mapped[str]=mapped_column(unique=True)
    title: Mapped[str]=mapped_column(unique=True)
    image_full: Mapped[str]=mapped_column(unique=True)