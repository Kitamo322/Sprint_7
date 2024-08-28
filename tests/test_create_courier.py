import requests
import pytest
import allure
from data import ResponseBody, Url, DataForRegistration


class TestsCreateNewCourier:

    @allure.title('Test Successful new courier creation. Handle:/api/v1/courier')
    def test_creation_courier_success(self, create_courier):
        response_status_code = create_courier[1]
        response_body_text = create_courier[2]
        assert response_status_code == 201 and (response_body_text == ResponseBody.COURIER_CREATION_SUCCESS)

    @allure.title('Test Registration of two Identical Couriers Error. Handle:/api/v1/courier')
    def test_creation_courier_clone_error(self, create_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier[0])
        assert response.status_code == 409 and (response.json() == ResponseBody.COURIER_NAME_ALREADY_EXIST)

    @allure.title('Test Courier Registration Deficit Data Error, Not enough: Login or Password. Handle:/api/v1/courier')
    @pytest.mark.parametrize('data_setup', DataForRegistration.reg_data)
    def test_creation_courier_deficit_data_error(self, data_setup):
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_COURIER}', data_setup)
        assert response.status_code == 400 and (response.json() == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA)
