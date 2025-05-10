import requests
from endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):
    def __init__(self):
        self.response = None
        self.response_json = None

    def get_object(self, id):  # Используем параметр id
        self.response = requests.get(f'https://api.restful-api.dev/objects/{id}')
        self.response_json = self.response.json()

    def check_status_code_200(self):
        assert self.response.status_code == 200

    def check_status_code_404(self):
        assert self.response.status_code == 404

    def check_response_id(self, object_id):
        assert self.response_json['id'] == object_id
get_object.py
