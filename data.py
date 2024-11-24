# Базовый URL
BASE_URL = "https://stellarburgers.nomoreparties.site/api"

# Данные для создания пользователя
USER_DATA = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
}

# Данные для обновления пользователя
UPDATE_USER_DATA = {
    "email": "new-email@yandex.ru",
    "name": "NewUsername"
}

# Данные для создания заказа
ORDER_DATA = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa7a"]
}

# Неверные данные для логина
INVALID_LOGIN_DATA = {
    "email": "invalid@yandex.ru",
    "password": "invalid"
}

# Данные для создания заказа без ингредиентов
ORDER_DATA_WITHOUT_INGREDIENTS = {
    "ingredients": []
}

# Данные для создания заказа с неверным хешем ингредиентов
ORDER_DATA_INVALID_HASH = {
    "ingredients": ["invalid_hash"]
}
#Ответ при неверных ингредиентах
INVALID_INGREDIENTS_RESPONSE = "One or more ids provided are incorrect"

#Ответ при пустых ингредиентах
WITHOUT_INGREDIENTS_RESPONSE = "Ingredient ids must be provided"

#Не авторизован ответ
NOT_AUTHORIZED_RESPONSE = "You should be authorised"

#Отсутствующие поля ответ
MISSING_FIELDS_RESPONSE = "Email, password and name are required fields"

#пользователь существует ответ
USER_EXISTS_RESPONSE = "User already exists"

#Авторизация с неверными данными ответ
LOGIN_ERROR_RESPONSE = "email or password are incorrect"