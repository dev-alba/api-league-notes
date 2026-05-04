from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.DATABASE_URL)
session_maker = sessionmaker(engine)


def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
