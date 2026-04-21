import requests
from urls import Url
import allure

class CourierApi:
    @staticmethod
    @allure.step("Запрс на Создание курьера")
    def create_courier(payload):
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER}", json=payload)

    @staticmethod
    @allure.step("Запрс на Логин курьера")
    def login_courier(login, password):
        payload = {
        "login": login,
        "password": password
    }

        return requests.post(
            f"{Url.BASE_URL}{Url.LOGIN_COURIER}",
            json=payload
    )

    @staticmethod
    @allure.step("Запрс на Удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(
            f"{Url.BASE_URL}{Url.CREATE_COURIER}/{courier_id}"
        )

