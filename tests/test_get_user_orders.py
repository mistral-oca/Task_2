import requests
import pytest
import allure
from data import ORDERS_URL

@allure.feature("Orders")
class TestGetUserOrders:

    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_orders_authorized_user(self, create_user, ingredients):
        
        _, access_token = create_user

        requests.post(
            ORDERS_URL,
            json={"ingredients": ingredients},
            headers={"Authorization": access_token}
        )

        response = requests.get(
            ORDERS_URL,
            headers={"Authorization": access_token}
        )

        body = response.json()

        assert response.status_code == 200
        assert body["success"] is True
        assert "orders" in body
        assert len(body["orders"]) > 0  

    @allure.title("Получение заказов без авторизации")
    def test_get_orders_unauthorized_user(self):
        
        response = requests.get(ORDERS_URL)

        body = response.json()

        assert response.status_code == 401
        assert body["success"] is False
        assert body["message"] == "You should be authorised"