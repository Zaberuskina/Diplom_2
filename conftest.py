import pytest
from methods.user_methods import UserMethods
from data import USER_DATA

@pytest.fixture
def create_and_delete_user():
    response = UserMethods.create_user(USER_DATA)
    yield response
    UserMethods.delete_user(response.json()["accessToken"])
