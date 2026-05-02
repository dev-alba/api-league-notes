import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from starlette.testclient import TestClient
from main import app
from core.database import Base, get_db
from models import (
    champions_models,
    matchups_models,
    users_models,
    profiles_models,
    notes_models,
)
from models.champions_models import Champion

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture
def db_session():
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    session_maker = sessionmaker(engine)
    Base.metadata.create_all(bind=engine)
    session = session_maker()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db_session):
    app.dependency_overrides[get_db] = lambda: db_session
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.clear()


@pytest.fixture
def token_headers(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password",
    }
    client.post("/users/", json=payload)

    login_data = {"username": "John Doe", "password": "password"}

    response = client.post("/login", data=login_data)
    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def set_champions(db_session):
    champion1 = Champion(name="LeeSin", title="The Blind Monk", image_full="leesin.jpg")
    champion2 = Champion(name="Khazix", title="The Voidreaver", image_full="khazix.jpg")

    db_session.add_all([champion1, champion2])
    db_session.commit()
