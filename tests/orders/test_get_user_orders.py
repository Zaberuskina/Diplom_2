import allure
from methods.order_methods import OrderMethods
from data import NOT_AUTHORIZED_RESPONSE

@allure.feature("Получение заказов пользователя")
class TestGetUserOrders:
    @allure.title("Получение заказов пользователя с авторизацией")
    @allure.description("Тест на получение заказов пользователя с авторизацией")
    @allure.step("Получение заказов пользователя с авторизацией")
    def test_get_user_orders_authorized(self, create_and_delete_user):
        access_token = create_and_delete_user.json()["accessToken"]
        orders_response = OrderMethods.get_user_orders(access_token)
        assert orders_response.status_code == 200 and orders_response.json()["success"] is True

    @allure.title("Получение заказов пользователя без авторизации")
    @allure.description("Тест на получение заказов пользователя без авторизации")
    @allure.step("Получение заказов пользователя без авторизации")
    def test_get_user_orders_unauthorized(self):
        response = OrderMethods.get_user_orders(None)
        assert response.status_code == 401 and response.json()["success"] is False and \
               response.json()["message"] == NOT_AUTHORIZED_RESPONSE
