import allure
from faker import Faker
from api_methods.courier_api import CourierApi
from data.data import ResponseMessages

fake = Faker()


class TestCreateCourier:

    @allure.title("Создание курьера успешно")
    @allure.description("Проверка, что курьер создаётся при корректных данных. Ожидается статус 201 и ответ {'ok': True}")

    def test_create_courier_success(self):
        payload = {
            "login": fake.user_name() + str(fake.random_int()),
            "password": fake.password(),
            "firstName": fake.first_name()
        }

        response = CourierApi.create_courier(payload)

        assert response.status_code == 201
        assert response.json()["ok"] == True


    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Проверка, что система не позволяет создать курьера с уже существующим логином. Ожидается ошибка 409")

    def test_create_duplicate_courier(self):
        login = fake.user_name() + str(fake.random_int())

        payload = {
            "login": login,
            "password": fake.password(),
            "firstName": fake.first_name()
        }

    
        response1 = CourierApi.create_courier(payload)
        assert response1.status_code == 201

       
        response2 = CourierApi.create_courier(payload)

        assert response2.status_code == 409
        assert response2.json()["message"] == ResponseMessages.ERROR_LOGIN_EXISTS


    @allure.title("Ошибка при отсутствии логина")
    @allure.description("Проверка, что при отсутствии обязательного поля login система возвращает ошибку 400")

    def test_create_missing_login(self):
        payload = {
            "password": fake.password(),
            "firstName": fake.first_name()
        }

        response = CourierApi.create_courier(payload)

        assert response.status_code == 400
        assert ResponseMessages.ERROR_NOT_ENOUGH_DATA in response.json()["message"]


    @allure.title("Ошибка при отсутствии пароля")
    @allure.description("Проверка, что при отсутствии обязательного поля password система возвращает ошибку 400")

    def test_create_missing_password(self):
        payload = {
            "login": fake.user_name(),
            "firstName": fake.first_name()
        }

        response = CourierApi.create_courier(payload)

        assert response.status_code == 400
        assert ResponseMessages.ERROR_NOT_ENOUGH_DATA in response.json()["message"]
