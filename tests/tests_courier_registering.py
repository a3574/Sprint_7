import pytest
import allure
from objects.courier import Courier
import helpers


class TestCourierRegistering:
    @allure.title('Тест курьера можно создать.')
    @allure.description(
        'В качестве проверки факта создания используем проверку на то, что можно залогиниться и получить ID курьера.')
    def test_register_courier_will_login_success(self, get_courier_data):
        courier_data = get_courier_data
        login_id = None
        courier = courier_data['courier']
        login_id = courier.login_courier(courier.login, courier.password).json()['id']
        assert login_id is not None

    @allure.title('Тест нельзя создать двух одинаковых курьеров')
    @allure.description(
        'Выполняем регистрацию курьера, а потом пробуем его зарегистрироваться второй раз с теми же самыми данными. Проверяем, что на второй раз запрос вернет статус 409.')
    def test_register_courier_twice_failed(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        register_courier_response_2 = courier.register_courier(courier.login, courier.first_name, courier.password)
        try:
            assert register_courier_response_2.status_code == 409
        except:
            login_id = courier.login_courier(courier.login, courier.password).json()['id']
            courier.delete_courier_account(login_id)

    @allure.title('Тест чтобы создать курьера, нужно передать в ручку все обязательные поля.')
    @allure.description(
        'Пробуем по отдельности создать(зарегистрировать) без логина или пароля. Ожидаем, что ни один из запросов не вернет статус 201.')
    def test_register_courier_without_required_fields_failed(self):
        courier_data = {}
        courier_data['login'] = helpers.generate_random_string(10)
        courier_data['first_name'] = helpers.generate_random_string(10)
        courier_data['password'] = helpers.generate_random_string(10)
        courier = Courier(courier_data.get('login'), courier_data.get('first_name'), courier_data.get('password'))
        register_without_login_response = courier.register_courier(first_name=courier.first_name,
                                                                   password=courier.password)
        if register_without_login_response.status_code == 201:
            login_id = courier.login_courier(login=courier.login, password=courier.password).json()['id']
            courier.delete_courier_account(login_id)
        register_without_password_response = courier.register_courier(login=courier.login,
                                                                      first_name=courier.first_name)
        if register_without_password_response.status_code == 201:
            login_id = courier.login_courier(login=courier.login, password=courier.password).json()['id']
            courier.delete_courier_account(login_id)
        register_without_first_name_response = courier.register_courier(login=courier.login, password=courier.password)
        if register_without_first_name_response.status_code == 201:
            login_id = courier.login_courier(login=courier.login, password=courier.password).json()['id']
            courier.delete_courier_account(login_id)
        assert 201 not in [register_without_login_response.status_code, register_without_password_response.status_code,
                           register_without_first_name_response.status_code]

    @allure.title('Тест запрос возвращает правильный код ответа.')
    @allure.description('Создаем(регистрируем курьера). Проверяем что запрос вернул статус 201.')
    def test_register_courier_return_code_201_success(self, get_courier_data):
        courier_data = get_courier_data
        assert courier_data['response'].status_code == 201

    @allure.title('Тест успешный запрос возвращает {"ok":true}.')
    @allure.description('Создаем(регистрируем курьера). Проверяем что запрос вернул текст ответа {"ok":true}.')
    def test_register_courier_return_ok_true_success(self, get_courier_data):
        courier_data = get_courier_data
        assert courier_data['response'].json() == {'ok': True}

    @allure.title('Тест если одного из полей нет, запрос возвращает ошибку.')
    @allure.description(
        'Пробуем по отдельности создать(зарегистрировать) без логина, пароля или имени. Ожидаем, что каждый из случаев вернет код ответа 400.')
    def test_register_courier_without_required_fields_get_error(self):
        courier_data = {}
        courier_data['login'] = helpers.generate_random_string(10)
        courier_data['first_name'] = helpers.generate_random_string(10)
        courier_data['password'] = helpers.generate_random_string(10)
        courier = Courier(courier_data.get('login'), courier_data.get('first_name'), courier_data.get('password'))
        register_without_login_response = courier.register_courier(first_name=courier.first_name,
                                                                   password=courier.password)
        if register_without_login_response.status_code == 201:
            login_id = courier.login_courier(login=courier.login, password=courier.password).json()['id']
            courier.delete_courier_account(login_id)
        register_without_password_response = courier.register_courier(login=courier.login,
                                                                      first_name=courier.first_name)
        if register_without_password_response.status_code == 201:
            login_id = courier.login_courier(login=courier.login, password=courier.password).json()['id']
            courier.delete_courier_account(login_id)
        register_without_first_name_response = courier.register_courier(login=courier.login, password=courier.password)
        if register_without_first_name_response == 201:
            login_id = courier.login_courier(login=courier.login, password=courier.password).json()['id']
            courier.delete_courier_account(login_id)
        assert register_without_login_response.status_code == 400 and register_without_password_response.status_code == 400 and register_without_first_name_response.status_code == 400

    @allure.title('Тест если создать пользователя с логином, который уже есть, возвращается ошибка.')
    @allure.description(
        'Проверяем, что нельзя создать(зарегистрировать) пользователя с логином, который уже есть. Ожидаем, что запрос не вернет статус 201.')
    def test_register_courier_with_used_login_failed(self, get_courier_data):
        courier_data = get_courier_data
        courier = courier_data['courier']
        courier_data_2 = get_courier_data
        courier_2 = courier_data_2['courier']
        register_courier_response_2 = courier_2.register_courier(courier.login, courier_2.first_name,
                                                                 courier_2.password)
        try:
            assert register_courier_response_2.status_code != 201
        except:
            login_id = courier_2.login_courier(courier.login, courier.password).json()['id']
            courier_2.delete_courier_account(login_id)
