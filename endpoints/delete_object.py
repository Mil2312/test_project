import requests
from endpoints.base_endpoint import Endpoint

response = None
response_json = None

class DeleteObject(Endpoint):
    def delete_object(self,object_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
        self.response_json = self.response.json()

    def check_status_code_404(self):
        assert self.response.status_code == 404
