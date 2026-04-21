import requests
from urls import Url
import allure

class OrdersApi:
    @staticmethod
    @allure.step("Запрс на Получение списка заказов")

    def get_orders():
        return requests.get(f"{Url.BASE_URL}{Url.LIST_ORDERS}")
    

    @staticmethod
    @allure.step("Запрс на Создание заказа")
    def create_order(order_data):
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", json=order_data)