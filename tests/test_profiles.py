def test_create_profile(client, token_headers):
    data = {
        "nickname": "User",
        "tagline": "TEST"
    }
    response = client.post("/profiles/", params=data, headers=token_headers)
    assert response.status_code == 201

def test_get_profile(client, token_headers):
    data = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=data, headers=token_headers)

    nickname = data["nickname"]
    tagline = data["tagline"]

    response = client.get(f"/profiles/{nickname}/{tagline}", headers=token_headers)
    assert response.status_code == 200

def test_get_my_profile(client, token_headers):
    data = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=data, headers=token_headers)

    response = client.get("/profiles/me", headers=token_headers)
    assert response.status_code == 200
    assert response.json()[0]["nickname"] == "User"

def test_update_profile(client, token_headers):
    data = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=data, headers=token_headers)

    new_data = {
        "new_nickname": "John",
        "new_tagline": "Doe"
    }
    response = client.patch("/profiles/", params=data, json=new_data, headers=token_headers)

    assert response.status_code == 200

def test_delete_profile(client, token_headers):
    data = {
        "nickname": "User",
        "tagline": "TEST"
    }
    client.post("/profiles/", params=data, headers=token_headers)

    profile_data = {
        "nickname": "User",
        "tagline": "TEST"
    }
    password = {
        "password": "password"
    }
    nickname = profile_data["nickname"]
    tagline = profile_data["tagline"]

    response = client.post(f"/profiles/{nickname}/{tagline}/delete-confirmation", params=profile_data, json=password, headers=token_headers)
    assert response.status_code == 204