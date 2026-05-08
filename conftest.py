import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
from helpers.helper import generate_courier_data
from api_methods.courier_api import CourierApi

@pytest.fixture
def new_courier():
    data = generate_courier_data()
    CourierApi.create_courier(data)

    login = data["login"]
    password = data["password"]

    login_response = CourierApi.login_courier(login, password)
    courier_id = None

    if login_response.status_code == 200:
        courier_id = login_response.json().get("id")

    yield login, password 
    if courier_id:
        CourierApi.delete_courier(courier_id)
