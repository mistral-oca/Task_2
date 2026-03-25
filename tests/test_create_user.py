import requests
import allure
from data import REGISTER_URL, LOGIN_URL, USER_WITHOUT_NAME
from helpers import generate_user


@allure.feature("User")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, delete_user):
        user = generate_user()

        with allure.step("Отправка POST запроса на создание уникального пользователя"):
            response = requests.post(REGISTER_URL, json=user)

        assert response.status_code == 200
        assert response.json()["success"] is True
        
        with allure.step("Логин для получения access_token"):
            login_response = requests.post(LOGIN_URL, json=user)

        delete_user["access_token"] = login_response.json()["accessToken"]

    @allure.title("Создание уже существующего пользователя")
    def test_create_existing_user(self, delete_user):
        user = generate_user()
        
        with allure.step("Создание пользователя"):
            requests.post(REGISTER_URL, json=user)

        
        with allure.step("Отправка POST запроса на уже существующего пользователя"):
            response = requests.post(REGISTER_URL, json=user)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

        
        with allure.step("Логин для удаления пользователя"):
            login_response = requests.post(LOGIN_URL, json=user)

        delete_user["access_token"] = login_response.json()["accessToken"]

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_required_field(self):
        
        with allure.step("Отправка POST запроса без обязательного поля name"):
            response = requests.post(REGISTER_URL, json=USER_WITHOUT_NAME)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"