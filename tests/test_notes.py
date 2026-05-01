def test_create_note(client, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    client.post("/matchups/", params=payload, headers=token_headers)

    profile = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=profile, headers=token_headers)

    data = {
        "content": "Test",
        "player_champion_name": "LeeSin",
        "enemy_champion_name": "Khazix"
    }

    response = client.post("/notes/", json=data, params=profile, headers=token_headers)
    assert response.status_code == 201
    assert response.json()["content"] == "Test"

def test_get_note(client, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    client.post("/matchups/", params=payload, headers=token_headers)

    profile = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=profile, headers=token_headers)

    data = {
        "content": "Test",
        "player_champion_name": "LeeSin",
        "enemy_champion_name": "Khazix"
    }
    client.post("/notes/", json=data, params=profile, headers=token_headers)

    response = client.get("/notes/get", params=profile, headers=token_headers)
    assert response.status_code == 200

def test_get_notes_by_matchup(client, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    client.post("/matchups/", params=payload, headers=token_headers)

    profile = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=profile, headers=token_headers)

    data = {
        "content": "Test",
        "player_champion_name": "LeeSin",
        "enemy_champion_name": "Khazix"
    }
    client.post("/notes/", json=data, params=profile, headers=token_headers)

    payload = {
        "nickname": "User",
        "tagline": "TEST",
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }

    response = client.get("/notes/get-by-matchup", params=payload, headers=token_headers)
    assert response.status_code == 200
    assert response.json()[0]["content"] == "Test"

def test_update_note(client, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    client.post("/matchups/", params=payload, headers=token_headers)

    profile = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=profile, headers=token_headers)

    data = {
        "content": "Test",
        "player_champion_name": "LeeSin",
        "enemy_champion_name": "Khazix"
    }
    response = client.post("/notes/", json=data, params=profile, headers=token_headers)
    note_id = response.json()["id"]

    old_note = {
        "note_id": note_id,
        "nickname": profile["nickname"],
        "tagline": profile["tagline"]
    }

    new_note = {
        "content": "New content"
    }
    response = client.patch(f"/notes/update/{note_id}", params=old_note, json=new_note, headers=token_headers)
    assert response.status_code == 200
    assert response.json()["content"] == "New content"

def test_delete_note(client, token_headers, set_champions):
    payload = {
        "player_champion": "LeeSin",
        "enemy_champion": "Khazix"
    }
    client.post("/matchups/", params=payload, headers=token_headers)

    profile = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=profile, headers=token_headers)

    data = {
        "content": "Test",
        "player_champion_name": "LeeSin",
        "enemy_champion_name": "Khazix"
    }
    response = client.post("/notes/", json=data, params=profile, headers=token_headers)
    note_id = response.json()["id"]

    note = {
        "note_id": note_id,
        "nickname": profile["nickname"],
        "tagline": profile["tagline"]
    }

    response = client.delete(f"/notes/delete/{note_id}", params=note, headers=token_headers)
    assert response.status_code == 204