import requests
import allure


class Order:
    def __init__(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.metro_station = metro_station
        self.phone = phone
        self.rentTime = rent_time
        self.delivery_date = delivery_date
        self.comment = comment

    @allure.step('Создание заказа через post запрос.')
    def create_order(self, color=None):
        params = {'firstName': self.first_name, 'lastName': self.last_name, 'address': self.address,
                  'metroStation': self.metro_station, 'phone': self.phone, 'rentTime': self.rentTime,
                  'deliveryDate': self.delivery_date, 'comment': self.comment}
        if color is not None:
            params['color'] = color
        responce_create_order = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=params)
        return responce_create_order
    @allure.step('Принять заказ через put запрос по id заказа.')
    def accept_order(self, courier_id, order_id):
        params = {'courierId': courier_id}
        responce_accept_order = requests.put(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order_id}', data=params)
        return responce_accept_order
    @allure.step('Получить заказ через get запрос по его номеру(track).')
    def get_order_by_track(self, track):
        params = {'t': track}
        responce_get_order_by_track = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track',
                                                   data=params)
        return responce_get_order_by_track

    @classmethod
    @allure.step('Получить список заказов через get запрос.')
    def get_order_list(cls, courier_id=None, nearest_station=None, limit=None, page=None):
        params = {}
        if courier_id is not None:
            params = {'courierId': courier_id}
        if nearest_station is not None:
            params = {'nearestStation': nearest_station}
        if limit is not None:
            params = {'limit': limit}
        if page is not None:
            params = {'page': page}
        responce_get_order_list = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders', data=params)
        return responce_get_order_list
    @allure.step('Отменить заказ через put запрос.')
    def reject_order(self, track):
        params = {'t': track}
        responce_reject_order = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/cancel',
                                             data=params)
        return responce_reject_order
    @allure.step('Завершить заказ через put запрос по id заказа.')
    def finish_order(self, order_id):
        responce_finish_order = requests.put(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/finish/{order_id}')
        return responce_finish_order

