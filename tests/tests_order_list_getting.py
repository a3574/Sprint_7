import pytest
import allure
from objects.order import Order


class TestOrderListGetting:
    @allure.title('Тест на то, что в тело ответа возвращается список заказов.')
    @allure.description('Проверяю, что при обращении на ручку с заказами возвращается список с заказами')
    def test_order_list_getting_all_orders_get_success(self):
        order_list = None
        get_order_list_response = Order.get_order_list()
        if get_order_list_response.status_code == 200:
            order_list = get_order_list_response.json()['orders']
