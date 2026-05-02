from sqlalchemy.orm import Session
from tests.conftest import db_session, token_headers, set_champions


def test_get_all_champions(client, db_session: Session, token_headers, set_champions):
    response = client.get("/champions/all", headers=token_headers)

    assert response.status_code == 200
    assert response.json()
