import random
import string
import pytest


@pytest.fixture()
def get_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём коллекцию, чтобы метод мог ее вернуть
    courier_data = {}

    # генерируем логин, пароль и имя курьера
    courier_data = {'login': generate_random_string(10)}
    courier_data = {'password': generate_random_string(10)}
    courier_data = {'first_name': generate_random_string(10)}

    # возвращаем коллекцию
    return courier_data
