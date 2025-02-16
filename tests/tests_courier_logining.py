import pytest
import allure
from objects.courier import Courier
import helpers


class TestCourierLogining:
    @allure.title('Тест курьер может авторизоваться.')
    @allure.description('Проверяем, что запрос на логин вернул статус 200.')
    def test_logining_courier_return_status_201_success(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        assert courier.login_courier(courier.login, courier.password).status_code == 200

    @allure.title('Тест успешный запрос возвращает id.')
    @allure.description('Проверяем, что запрос на логин вернул ID курьера.')
    def test_logining_courier_return_id_success(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        login_id = courier.login_courier(courier.login, courier.password).json()['id']
        assert login_id is not None

    @allure.title('Тест для авторизации нужно передать все обязательные поля.')
    @allure.description(
        'Почередно пробуем авторизоваться без логина и без пароля. Ожидаем, что ни один запрос не вернет статус 200.')
    def test_logining_courier_without_required_fields_return_id_false(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        response_login_without_login = courier.login_courier(login=courier.login)
        response_without_password = courier.login_courier(password=courier.password)
        assert 200 not in [response_login_without_login.status_code, response_without_password.status_code]

    @allure.title('Тест если какого-то поля нет, запрос возвращает ошибку.')
    @allure.description(
        'Почередно пробуем авторизоваться без логина и без пароля. Ожидаем, что каждый запрос вернет статус 400.')
    def test_logining_courier_without_required_fields_return_error_success(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        response_login_without_login = courier.login_courier(login=courier.login)
        response_without_password = courier.login_courier(password=courier.password)
        assert response_login_without_login.status_code == 400 and response_without_password.status_code == 400

    @allure.title('Тест система вернёт ошибку, если неправильно указать логин или пароль.')
    @allure.description(
        'Пробуем вместо авторизаваться используя логин вместо пароля и наоборот. Ожидаем, что ни один запрос не вернет статус 200.')
    def test_logining_courier_without_required_fields_return_error_success(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        response_login = courier.login_courier(password=courier.login, login=courier.password)
        assert response_login.status_code != 200

    @allure.title('Тест если авторизоваться под несуществующим пользователем, запрос возвращает ошибку.')
    @allure.description(
        'Пробуем авторизаваться под незарегистрированным курьером. Ожидаем, что ни один запрос вернет статус 404.')
    def test_logining_courier_unregistered_get_error_404_success(self, get_courier_data):
        courier_data = {}
        courier_data['login'] = helpers.generate_random_string(10)
        courier_data['first_name'] = helpers.generate_random_string(10)
        courier_data['password'] = helpers.generate_random_string(10)
        courier = Courier(courier_data.get('login'), courier_data.get('first_name'), courier_data.get('password'))
        response_login = courier.login_courier(password=courier.login, login=courier.password)
        assert response_login.status_code == 404

