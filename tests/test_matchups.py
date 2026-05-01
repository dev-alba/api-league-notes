from sqlalchemy.orm import Session

def test_create_matchup(client, db_session: Session, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    response = client.post("/matchups/", params=payload, headers=token_headers)
    assert response.status_code == 201

def test_get_matchup(client, db_session: Session, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    response = client.post("/matchups/", params=payload, headers=token_headers)
    data = response.json()
    matchup_id = data["id"]

    response = client.get(f"/matchups/get/{matchup_id}", headers=token_headers)
    assert response.status_code == 200