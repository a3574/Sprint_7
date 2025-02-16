import requests
import allure


class Courier:
    def __init__(self, login, first_name, password):
        self.login = login
        self.first_name = first_name
        self.password = password

    @allure.step('Регистрация курьера через post запрос.')
    def register_courier(self, login=None, first_name=None, password=None):
        params = {}
        if login is not None:
            params['login'] = login
        if first_name is not None:
            params['firstName'] = first_name
        if password is not None:
            params['password'] = password
        responce_register_courier = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier',data=params)
        return responce_register_courier

    @allure.step('Логин курьера через post запрос')
    def login_courier(self, login=None, password=None):
        params = {}
        if login is not None:
            params['login'] = login
        if password is not None:
            params['password'] = password
        responce_login_courier = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
                                               data=params)
        return responce_login_courier

    @allure.step('Удаление курьера через delete запрос по id курьера.')
    def delete_courier_account(self, courier_id):
        response_delete_courier_account = requests.delete(
            f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}")
        return response_delete_courier_account

    @allure.step('Получение кол-ва заказов клиента через get запрос по id курьера.')
    def get_courier_orders_count(self, courier_id):
        response_get_courier_orders_count = requests.get(
            f"https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}/ordersCount")
        return response_get_courier_orders_count
