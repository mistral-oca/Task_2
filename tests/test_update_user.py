import requests
import pytest
import allure
from data import UPDATE_USER_URL
from helpers import generate_user

@allure.feature("User")
class TestUpdateUser:

    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_update_user_with_auth(self, create_user, field):

        user, access_token = create_user

        new_data = generate_user()

        payload = {field: new_data[field]}

        response = requests.patch(
            UPDATE_USER_URL,
            json=payload,
            headers={"Authorization": access_token}
        )

        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True

        if field != "password":
            assert body["user"][field] == payload[field]


    @allure.title("Изменение данных пользователя без авторизации")
    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_update_user_without_auth(self, field):

        new_data = generate_user()

        payload = {field: new_data[field]}

        response = requests.patch(
            UPDATE_USER_URL,
            json=payload
        )

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"