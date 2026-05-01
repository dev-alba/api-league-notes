def test_create_user(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password"
    }
    response = client.post("/users/", json = payload)
    data = response.json()

    assert response.status_code == 201
    assert data["email"] == "example@email.com"
    assert "id" in data

def test_duplicated_user(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password"
    }
    response = client.post("/users/", json = payload)
    assert response.status_code == 201

    response = client.post("/users/", json=payload)
    assert response.status_code == 409