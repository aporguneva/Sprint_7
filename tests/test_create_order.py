import pytest
import allure
from api_methods.orders_api import OrdersApi
from data.data import ResponseFields
from data.order_data import OrderData


class TestCreateOrder:
    @allure.title("Проверка создания заказа")
    @allure.description("Проверка, что заказ создается с различными цветами и без цветов, а также тело ответа содержит track.")
    
    @pytest.mark.parametrize("order_data", OrderData.ORDERS)
    def test_create_order_with_different_colors(self, order_data):
        
        response = OrdersApi.create_order(order_data)
        
        assert response.status_code == 201
        assert ResponseFields.TRACK in response.json()