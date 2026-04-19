import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
from helper import register_new_courier_and_return_login_password
from api_methods.courier_api import CourierApi


import pytest
from helper import register_new_courier_and_return_login_password
from api_methods.courier_api import CourierApi


@pytest.fixture
def new_courier():
    login, password, _ = register_new_courier_and_return_login_password()

    yield login, password

    
    response = CourierApi.login_courier(login, password)
    courier_id = response.json().get("id")

    if courier_id:
        CourierApi.delete_courier(courier_id)
