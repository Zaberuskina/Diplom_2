import requests
from data import BASE_URL

class UserMethods:
    @staticmethod
    def create_user(user_data):
        return requests.post(f"{BASE_URL}/auth/register", json=user_data)

    @staticmethod
    def login_user(user_data):
        return requests.post(f"{BASE_URL}/auth/login", json=user_data)

    @staticmethod
    def get_user_info(access_token):
        headers = {"Authorization": access_token} if access_token else {}
        return requests.get(f"{BASE_URL}/auth/user", headers=headers)

    @staticmethod
    def update_user(access_token, update_data):
        headers = {"Authorization": access_token} if access_token else {}
        return requests.patch(f"{BASE_URL}/auth/user", json=update_data, headers=headers)

    @staticmethod
    def delete_user(access_token):
        headers = {"Authorization": access_token} if access_token else {}
        return requests.delete(f"{BASE_URL}/auth/user", headers=headers)
