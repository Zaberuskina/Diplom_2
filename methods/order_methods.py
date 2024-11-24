import requests
from data import BASE_URL

class OrderMethods:
    @staticmethod
    def get_ingredients():
        return requests.get(f"{BASE_URL}/ingredients")

    @staticmethod
    def create_order(access_token, order_data):
        headers = {"Authorization": access_token} if access_token else {}
        return requests.post(f"{BASE_URL}/orders", json=order_data, headers=headers)

    @staticmethod
    def get_user_orders(access_token):
        headers = {"Authorization": access_token} if access_token else {}
        return requests.get(f"{BASE_URL}/orders", headers=headers)
