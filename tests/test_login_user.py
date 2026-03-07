import requests
import allure
from data import LOGIN_URL
from helpers import generate_user

@allure.feature("User")
class TestLoginUser:

    @allure.title("Логин существующего пользователя")
    def test_login_existing_user(self, create_user):
        user, _ = create_user

        response = requests.post(LOGIN_URL, json={
            "email": user["email"],
            "password": user["password"]
        })

        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "accessToken" in body
        assert "refreshToken" in body
        assert body["user"]["email"] == user["email"]

    @allure.title("Логин с неверным паролем")
    def test_login_with_wrong_credentials(self):
        user = generate_user()

        response = requests.post(LOGIN_URL, json={
            "email": user["email"],
            "password": "wrong_password"
        })

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "email or password are incorrect"