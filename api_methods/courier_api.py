import requests
from urls import Url

class CourierApi:
    @staticmethod 
    def create_courier():
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER}")
    
    @staticmethod
    def create_courier(payload):
        return requests.post(f"{Url.BASE_URL}{Url.CREATE_COURIER}", json=payload)


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
    def delete_courier(courier_id):
        return requests.delete(
            f"{Url.BASE_URL}{Url.CREATE_COURIER}/{courier_id}"
        )

