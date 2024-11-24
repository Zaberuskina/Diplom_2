import allure
from methods.user_methods import UserMethods
from data import USER_DATA, INVALID_LOGIN_DATA, LOGIN_ERROR_RESPONSE

@allure.feature("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Авторизация существующего пользователя")
    @allure.description("Тест на авторизацию существующего пользователя")
    @allure.step("Авторизация существующего пользователя")
    def test_login_existing_user(self, create_and_delete_user):
        response = UserMethods.login_user(USER_DATA)
        assert response.status_code == 200 and response.json()["success"] is True and \
               "accessToken" in response.json() and "refreshToken" in response.json() and \
               response.json()["user"]["email"] == USER_DATA["email"] and \
               response.json()["user"]["name"] == USER_DATA["name"]

    @allure.title("Авторизация с неверными данными")
    @allure.description("Тест на авторизацию с неверными данными")
    @allure.step("Авторизация с неверными данными")
    def test_login_invalid_credentials(self):
        response = UserMethods.login_user(INVALID_LOGIN_DATA)
        assert response.status_code == 401 and response.json()["success"] is False and \
               response.json()["message"] == LOGIN_ERROR_RESPONSE
