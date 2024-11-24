import allure
from methods.user_methods import UserMethods
from data import UPDATE_USER_DATA, NOT_AUTHORIZED_RESPONSE

@allure.feature("Обновление данных пользователя")
class TestUpdateUser:
    @allure.title("Обновление данных пользователя с авторизацией")
    @allure.description("Тест на обновление данных пользователя с авторизацией")
    @allure.step("Обновление данных пользователя с авторизацией")
    def test_update_user_authorized(self, create_and_delete_user):
        access_token = create_and_delete_user.json()["accessToken"]
        update_response = UserMethods.update_user(access_token, UPDATE_USER_DATA)
        assert update_response.status_code == 200 and update_response.json()["success"] is True and \
               update_response.json()["user"]["email"] == UPDATE_USER_DATA["email"] and \
               update_response.json()["user"]["name"] == UPDATE_USER_DATA["name"]

    @allure.title("Обновление данных пользователя без авторизации")
    @allure.description("Тест на обновление данных пользователя без авторизации")
    @allure.step("Обновление данных пользователя без авторизации")
    def test_update_user_unauthorized(self):
        response = UserMethods.update_user(None, UPDATE_USER_DATA)
        assert response.status_code == 401 and response.json()["success"] is False and \
               response.json()["message"] == NOT_AUTHORIZED_RESPONSE
