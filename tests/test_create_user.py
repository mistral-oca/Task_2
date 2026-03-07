import requests
import allure
from data import REGISTER_URL
from helpers import generate_user

@allure.feature("User")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user = generate_user()

        response = requests.post(REGISTER_URL, json=user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self, create_user):
        user, _ = create_user

        response = requests.post(REGISTER_URL, json=user)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_required_field(self):

        user = {
            "email": "test@yandex.ru",
            "password": "password"
        }

        response = requests.post(REGISTER_URL, json=user)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"