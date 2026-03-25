import requests
import allure
from data import UPDATE_USER_URL
from helpers import generate_user

@allure.feature("User")
class TestUpdateUser:

    @allure.title("Изменение email пользователя с авторизацией")
    def test_update_email_with_auth(self, create_user):
        user, access_token = create_user
        new_data = generate_user()
        payload = {"email": new_data["email"]}

        with allure.step("Отправка PATCH запроса для изменения email"):
            response = requests.patch(
                UPDATE_USER_URL,
                json=payload,
                headers={"Authorization": access_token}
            )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["email"] == payload["email"]

    @allure.title("Изменение name пользователя с авторизацией")
    def test_update_name_with_auth(self, create_user):
        user, access_token = create_user
        new_data = generate_user()
        payload = {"name": new_data["name"]}

        with allure.step("Отправка PATCH запроса для изменения name"):
            response = requests.patch(
                UPDATE_USER_URL,
                json=payload,
                headers={"Authorization": access_token}
            )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert body["user"]["name"] == payload["name"]

    @allure.title("Изменение password пользователя с авторизацией")
    def test_update_password_with_auth(self, create_user):
        user, access_token = create_user
        new_data = generate_user()
        payload = {"password": new_data["password"]}

        with allure.step("Отправка PATCH запроса для изменения password"):
            response = requests.patch(
                UPDATE_USER_URL,
                json=payload,
                headers={"Authorization": access_token}
            )
        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        

    @allure.title("Изменение email пользователя без авторизации")
    def test_update_email_without_auth(self):
        new_data = generate_user()
        payload = {"email": new_data["email"]}

        with allure.step("Отправка PATCH запроса без авторизации"):
            response = requests.patch(UPDATE_USER_URL, json=payload)
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

    @allure.title("Изменение name пользователя без авторизации")
    def test_update_name_without_auth(self):
        new_data = generate_user()
        payload = {"name": new_data["name"]}

        with allure.step("Отправка PATCH запроса без авторизации"):
            response = requests.patch(UPDATE_USER_URL, json=payload)
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"

    @allure.title("Изменение password пользователя без авторизации")
    def test_update_password_without_auth(self):
        new_data = generate_user()
        payload = {"password": new_data["password"]}

        with allure.step("Отправка PATCH запроса без авторизации"):
            response = requests.patch(UPDATE_USER_URL, json=payload)
        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"