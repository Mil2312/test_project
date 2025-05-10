import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
@pytest.fixture()
def object_id():
    create_object = CreateObject()
    payload = {
        "name": "Apple AirPods",
        "data": {
            "color": "white",
            "generation": "3rd",
            "price": 135
        }
    }
    create_object.new_object(payload)
    yield create_object.response_json['id']
    delete_object = DeleteObject()
    delete_object.delete_object(create_object.response_json['id'])
