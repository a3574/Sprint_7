import pytest
import allure
from objects import courier
import conftest
import helpers

class TestCourierCreating:
    @allure.title('Тест создания курьера')
    @allure.description('')
    def test_order_with_two_different_entry_order_has_been_placed(self, data):