import pytest
import requests
import allure
from data import ORDERS_URL

@allure.feature("Orders")
class TestCreateOrder:
    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_auth(self, create_user, ingredients):
        _, access_token = create_user

        response = requests.post(
            ORDERS_URL,
            json={"ingredients": ingredients},
            headers={"Authorization": access_token}
        )

        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, ingredients):
        response = requests.post(
            ORDERS_URL,
            json={"ingredients": ingredients}
        )

        body = response.json()
        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = requests.post(
            ORDERS_URL,
            json={"ingredients": []}
        )

        body = response.json()
        assert response.status_code == 400
        assert body["success"] is False
        assert body["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @pytest.mark.parametrize("wrong_hash", [
        ["12345"],
        ["abcdef"],
        ["invalid_hash"]
    ])
    def test_create_order_with_wrong_hash(self, wrong_hash):

        response = requests.post(
            ORDERS_URL,
            json={"ingredients": wrong_hash}
        )
        
        assert response.status_code in (400, 500), \
            f"Unexpected status: {response.status_code}, body: {response.text}"
        
        if response.status_code == 400:
            body = response.json()
            assert body["success"] is False
            assert "incorrect" in body["message"] or "ids" in body["message"]