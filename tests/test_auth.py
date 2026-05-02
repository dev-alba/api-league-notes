def test_create_user(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password",
    }
    response = client.post("/users/", json=payload)
    data = response.json()

    assert response.status_code == 201
    assert data["email"] == "example@email.com"
    assert "id" in data


def test_duplicated_user(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password",
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    response = client.post("/users/", json=payload)
    assert response.status_code == 409


def test_incorrect_email_format(client):
    payload = {"nickname": "John Doe", "email": "example.com", "password": "password"}

    response = client.post("/users/", json=payload)
    assert response.status_code == 422


def test_login_user(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password",
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    login_data = {"username": "John Doe", "password": "password"}

    response = client.post("/login", data=login_data)
    data = response.json()

    assert response.status_code == 200
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_incorrect_login_user(client):
    payload = {
        "nickname": "John Doe",
        "email": "example@email.com",
        "password": "password",
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 201

    login_data = {"username": "John Doe", "password": "pass"}

    response = client.post("/login", data=login_data)
    assert response.status_code == 401
