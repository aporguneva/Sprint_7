import allure
from api_methods.courier_api import CourierApi
from data.data import ResponseMessages, ResponseFields

class TestLogin:
    @allure.title("Проверка успешной авторизации")
    @allure.description("Проверка, что при успешной авторизации верный статус код и запрос возвращает id")
    def test_login_courier_success(self, new_courier):
        login, password = new_courier

        response = CourierApi.login_courier(login, password)

        # проверки
        assert response.status_code == 200
        assert ResponseFields.COURIER_ID in response.json()


    @allure.title("Авторизация без пароля")
    @allure.description("Проверка, что при попытке авторизации без пароля возвращается ошибка 400 с сообщением 'Недостаточно данных для входа'")
    def test_login_missing_password(self, new_courier):
        login, _ = new_courier

        response = CourierApi.login_courier(login, "")

        assert response.status_code == 400
        assert response.json().get("message") == ResponseMessages.ERROR_LOGIN_NOT_ENOUGH_DATA


    @allure.title("Авторизация без логина")
    @allure.description("Проверка, что при попытке авторизации без логина возвращается ошибка 400 с сообщением 'Недостаточно данных для входа'")
    def test_login_missing_login(self, new_courier):   
        _, password = new_courier

        response = CourierApi.login_courier("", password)

        assert response.status_code == 400
        assert response.json().get("message") == ResponseMessages.ERROR_LOGIN_NOT_ENOUGH_DATA

    
    @allure.title("Авторизация с неверным паролем")
    @allure.description("Проверка, что при попытке авторизации с неправильным паролем возвращается ошибка 404 с сообщением 'Учетная запись не найдена'")
    def test_login_wrong_password(self, new_courier):
        login, _ = new_courier

        response = CourierApi.login_courier(login, "wrong_password")

        assert response.status_code == 404
        assert response.json().get("message") == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND
    


    @allure.title("Авторизация с неверным логином")
    @allure.description("Проверка, что при попытке авторизации с неправильным логином возвращается ошибка 404 с сообщением 'Учетная запись не найдена'")
    def test_login_wrong_login(self, new_courier):
        _, password = new_courier

        response = CourierApi.login_courier("wrong_login", password)

        assert response.status_code == 404
        assert response.json().get("message") == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND



    @allure.title("Авторизация несуществующего пользователя")
    @allure.description("Проверка, что при попытке авторизации с данными несуществующего пользователя возвращается ошибка 404 с сообщением 'Учетная запись не найдена'")
    def test_login_nonexistent_user(self):
        response = CourierApi.login_courier("fake_login_123", "fake_password_123")

        assert response.status_code == 404
        assert response.json().get("message") == ResponseMessages.ERROR_ACCOUNT_NOT_FOUND

    


    




