import pytest
import requests
import allure

from data import Url, DataForOrder, Flags


class TestCreationOrder:

    @allure.title('Successful order creation with all color variations. Handle:/api/v1/orders')
    @pytest.mark.parametrize('scooter_color', DataForOrder.scooter_color)
    def test_creation_order_choice_color_true(self, scooter_color):
        order_data = DataForOrder.order_data
        order_data['color'] = scooter_color
        order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        assert order.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order.json()
        requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{order.json()['track']}')



