import allure
from methods.user_methods import UserMethods
from data import USER_DATA, MISSING_FIELDS_RESPONSE, USER_EXISTS_RESPONSE

@allure.feature("Регистрация пользователя")
class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    @allure.description("Тест на создание уникального пользователя")
    @allure.step("Создание уникального пользователя")
    def test_create_unique_user(self, create_and_delete_user):
        response = create_and_delete_user
        assert response.status_code == 200 and response.json()["success"] is True and \
               "accessToken" in response.json() and "refreshToken" in response.json() and \
               response.json()["user"]["email"] == USER_DATA["email"] and \
               response.json()["user"]["name"] == USER_DATA["name"]

    @allure.title("Создание существующего пользователя")
    @allure.description("Тест на создание уже существующего пользователя")
    @allure.step("Создание существующего пользователя")
    def test_create_existing_user(self):
        # Создание пользователя
        UserMethods.create_user(USER_DATA)
        # Попытка создать пользователя снова
        response = UserMethods.create_user(USER_DATA)
        assert response.status_code == 403 and response.json()["success"] is False and \
               response.json()["message"] == USER_EXISTS_RESPONSE
        # Удаление пользователя после теста
        access_token = UserMethods.login_user(USER_DATA).json()["accessToken"]
        UserMethods.delete_user(access_token)

    @allure.title("Создание пользователя с отсутствующими полями")
    @allure.description("Тест на создание пользователя с отсутствующими полями")
    @allure.step("Создание пользователя с отсутствующими полями")
    def test_create_user_missing_field(self):
        user_data = {
            "email": USER_DATA["email"],
            "password": USER_DATA["password"]
        }
        response = UserMethods.create_user(user_data)
        assert response.status_code == 403 and response.json()["success"] is False and \
               response.json()["message"] == MISSING_FIELDS_RESPONSE
