

import pytest

def test_get_users_returns_200_and_non_empty_list(api):
    response = api.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    for user in data:
        assert {"id", "name", "username", "email"} <= user.keys()


@pytest.mark.parametrize("user_id", ["9999", "-1", "abc"])
def test_invalid_user_ids_return_404(api, user_id):
    response = api.get(f"/users/{user_id}")
    assert response.status_code == 404


def test_get_users_with_trailing_slash_returns_200(api):
    response = api.get("/users/")

    assert response.status_code == 200


def test_create_user_returns_201_and_generated_id(api):
    payload = {
        "name": "Gulcan Test",
        "username": "gulcan_qa",
        "email": "gulcan@example.com",
    }

    response = api.post("/users", payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert isinstance(data["id"], int)


def test_update_user_returns_200(api):
    payload = {
        "name": "Gulcan Updated",
        "username": "gulcan_updated",
        "email": "gulcan.updated@example.com",
    }

    response = api.put("/users/1", payload)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]


def test_delete_user_returns_200(api):
    response = api.delete("/users/1")

    assert response.status_code == 200
    assert response.json() == {}