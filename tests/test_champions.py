from sqlalchemy.orm import Session
from models.champions_models import Champion
from tests.conftest import db_session


def test_get_all_champions(client, db_session: Session):
    payload= {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password"
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    login_data = {
        "username": "John Doe",
        "password": "password"
    }

    response = client.post("/login", data=login_data)
    data = response.json()

    token = data["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    new_champion = Champion(id = 1, name = "LeeSin", title = "The Blind Monk", image_full = "leesin.jpg")
    db_session.add(new_champion)
    db_session.commit()

    response = client.get("/champions/all", headers = headers)

    assert response.status_code == 200
    assert response.json()