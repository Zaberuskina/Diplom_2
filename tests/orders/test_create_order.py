import allure
from methods.order_methods import OrderMethods
from data import ORDER_DATA, ORDER_DATA_WITHOUT_INGREDIENTS, ORDER_DATA_INVALID_HASH, WITHOUT_INGREDIENTS_RESPONSE, INVALID_INGREDIENTS_RESPONSE

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    @allure.description("Тест на создание заказа с авторизацией и ингредиентами")
    @allure.step("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_authorized(self, create_and_delete_user):
        access_token = create_and_delete_user.json()["accessToken"]
        order_response = OrderMethods.create_order(access_token, ORDER_DATA)
        assert order_response.status_code == 200 and order_response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    @allure.description("Тест на создание заказа без авторизации")
    @allure.step("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        response = OrderMethods.create_order(None, ORDER_DATA)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Тест на создание заказа без ингредиентов")
    @allure.step("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, create_and_delete_user):
        access_token = create_and_delete_user.json()["accessToken"]
        order_response = OrderMethods.create_order(access_token, ORDER_DATA_WITHOUT_INGREDIENTS)
        assert order_response.status_code == 400 and order_response.json()["message"] == WITHOUT_INGREDIENTS_RESPONSE

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    @allure.description("Тест на создание заказа с неверным хешем ингредиентов")
    @allure.step("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, create_and_delete_user):
        access_token = create_and_delete_user.json()["accessToken"]
        order_response = OrderMethods.create_order(access_token, ORDER_DATA_INVALID_HASH)
        assert order_response.status_code == 400 and order_response.json()["message"] == INVALID_INGREDIENTS_RESPONSE
