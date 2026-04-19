import allure
from api_methods.orders_api import OrdersApi
from data.data import ResponseFields

class TestOrderList:
    @allure.title("Проверка получения списка заказов")
    @allure.description("Проверка, что при запросе списка заказов в теле ответа возвращается список заказов в поле 'orders'")
    def test_get_list_of_orders(self):
        response = OrdersApi.get_orders()

        assert response.status_code == 200

        response_body = response.json()
        
        assert ResponseFields.ORDERS in response_body
        assert isinstance(response_body[ResponseFields.ORDERS], list)

