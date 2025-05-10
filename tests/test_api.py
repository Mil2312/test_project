import allure
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
        "name": "Apple AirPods",
        "data": {
            "color": "white",
            "generation": "3rd",
            "price": 135
        }
    }

def test_create_object():
    with allure.step('Сreate object'):
        new_object_endpoint = CreateObject()
        new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_status_code_200()
    with allure.step('Сheck name'):
        new_object_endpoint.check_name(payload['name'])

def test_get_object(object_id):
    with allure.step('Get object'):
        get_object_endpoint = GetObject()
        get_object_endpoint.get_object(object_id)
    get_object_endpoint.check_status_code_200()
    with allure.step('Сheck response id'):
        get_object_endpoint.check_response_id(object_id)

@allure.feature('New test update object')
def test_put_object(object_id):
    with allure.step('Update object'):
        update_object_endpoint = UpdateObject()
        update_object_endpoint.update_object(object_id, payload)
    update_object_endpoint.check_status_code_200()
    with allure.step('Сheck name'):
        update_object_endpoint.check_response_name(payload['name'])

@allure.feature('New test delete object')
def test_delete_object(object_id):
    with allure.step('Update object'):
        delete_object_endpoint = DeleteObject()
        delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_status_code_200()
