import requests
from faker import Faker
from endpoints.base_endpoint import Endpoint

class UpdateObject(Endpoint):
    response = None
    response_json = None

    def update_object(self, object_id, payload=None):
        fake = Faker()  # Инициализация Faker

        payload = {
                "name": fake.catch_phrase(),  # Случайное название (например, "Innovative wireless earbuds")
                "data": {
                    "color": fake.color_name(),  # Случайный цвет ("white", "black", "red" и т.д.)
                    "generation": f"{fake.random_int(min=1, max=5)}th",  # "1st", "2nd", ... "5th"
                    "price": fake.random_int(min=50, max=200)  # Случайная цена от 50 до 200
                }
            }

        requestUrl = f"https://api.restful-api.dev/objects/{object_id}"
        self.response = requests.put(requestUrl, json=payload)
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name
