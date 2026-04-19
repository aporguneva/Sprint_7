import requests
from urls import Url

class OrdersApi:
    @staticmethod #получение списка заказов
    def get_orders():
        return requests.get(f"{Url.BASE_URL}{Url.LIST_ORDERS}")
    
    @staticmethod #создание заказа
    def create_order(order_data):
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_ORDER}", json=order_data)