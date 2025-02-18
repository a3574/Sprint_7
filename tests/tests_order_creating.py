import pytest
import allure


class TestCourierCreating:
    @allure.title('Тест для проверки выбора цвета в заказе.')
    @allure.description(
        'Проверяем, по очереди, что можно указать один из цветов, выбрать оба или вовсе не указывать цвета. Ожидаем, что в теле ответа будет track.')
    def test_order_creating_return_status_201_and_track_success(self, get_order_data):
        order_data = get_order_data
        track_id = None
        assert order_data['response'].status_code == 201 and 'track' in order_data['response'].json()

