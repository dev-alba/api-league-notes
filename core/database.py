from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

class Base(DeclarativeBase):
    pass

load_dotenv(override=True)
engine=create_engine(f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT", "5432")}/{os.getenv("DB_NAME")}')
SessionLocal=sessionmaker(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()