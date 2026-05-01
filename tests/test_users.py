def test_get_my_user(client, token_headers):
    response = client.get("/users/me", headers=token_headers)
    assert response.status_code == 200

def test_update_user(client, token_headers):
    data = {
        "password": "password",
        "new_password": "new_pass"
    }
    response = client.patch("/users/", json=data, headers=token_headers)
    assert response.status_code == 200

def test_delete_user(client, token_headers):
    data = {
        "password": "password"
    }
    response = client.post("/users/delete-confirmation", json=data, headers=token_headers)
    assert response.status_code == 204