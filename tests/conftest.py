import pytest
from objects.courier import Courier
from objects.order import Order
import helpers

@pytest.fixture()
def get_courier_data():
    courier_data = {}
    courier_data['login'] = helpers.generate_random_string(10)
    courier_data['first_name'] = helpers.generate_random_string(10)
    courier_data['password'] = helpers.generate_random_string(10)
    courier = Courier(courier_data['login'], courier_data['first_name'], courier_data['password'])
    courier_data['courier'] = courier
    courier_data['response'] = courier.register_courier(courier_data['login'], courier_data['first_name'], courier_data['password'])
    yield courier_data
    login_id = courier.login_courier(courier.login, courier.password).json()['id']
    courier.delete_courier_account(login_id)

@pytest.fixture(params=[['BLACK'],['GREY'],['BLACK','GREY'],None])
def get_order_data(request):
    order_data = {}
    order_data['first_name'] = helpers.generate_random_string(10)
    order_data['last_name'] = helpers.generate_random_string(10)
    order_data['address'] = helpers.generate_random_string(10)
    order_data['metro_station'] = helpers.generate_random_number(2)
    order_data['phone'] = helpers.generate_random_phone_number()
    order_data['rent_time'] = helpers.generate_random_number(6)
    order_data['delivery_date'] = helpers.generate_random_date()
    order_data['comment'] = helpers.generate_random_string(10)
    order = Order(order_data['first_name'], order_data['last_name'], order_data['address'],
                  order_data['metro_station'], order_data['phone'], order_data['rent_time'],
                  order_data['delivery_date'], order_data['comment'])
    order_data['order'] = order
    order_data['response'] = order.create_order(request.param)
    yield order_data
    order.reject_order(order_data['response'].json()['track'])
