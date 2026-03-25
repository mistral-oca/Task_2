import pytest
import requests

from helpers import generate_user
from data import REGISTER_URL, LOGIN_URL, DELETE_USER_URL, INGREDIENTS_URL


@pytest.fixture
def create_user():
    user = generate_user()

    requests.post(REGISTER_URL, json=user)

    login_response = requests.post(LOGIN_URL, json={
        "email": user["email"],
        "password": user["password"]
    })

    access_token = login_response.json()["accessToken"]

    yield user, access_token

    requests.delete(
        DELETE_USER_URL,
        headers={"Authorization": access_token}
    )

@pytest.fixture
def delete_user():
    tokens = {}

    yield tokens

    if "access_token" in tokens:
        requests.delete(
            DELETE_USER_URL,
            headers={"Authorization": tokens["access_token"]}
        )

@pytest.fixture
def ingredients():
    response = requests.get(INGREDIENTS_URL)
    data = response.json()["data"]

    return [data[0]["_id"], data[1]["_id"]]