import requests
from endpoints.base_endpoint import Endpoint
class UpdateObject(Endpoint):
    response = None
    response_json = None

    def update_object(self, object_id, payload):
        payload = {
            "name": "Apple AirPods",
            "data":
                {
                    "color": "white",
                    "generation": "3rd",
                    "price": 135
                }
        }
        requestUrl = f"https://api.restful-api.dev/objects/{object_id}"
        self.response = requests.put(requestUrl, json=payload)
        self.response_json = self.response.json()


    def check_response_name(self, name):
        assert self.response_json['name'] == name
