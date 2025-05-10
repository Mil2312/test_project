import allure
class Endpoint:
    response = None
    response_json = None

    def check_status_code_200(self):
        with allure.step('Сheck status code is 200'):
            assert self.response.status_code == 200
