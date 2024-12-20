# file: test_main.py

import pytest
from pages.main_page import MainPage
import allure

@pytest.mark.usefixtures("setup")
@allure.feature("Основной экран")
class TestMain:

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Авторизоваться (Войти)')
    @allure.testcase("")
    def test_login(self):
        page = MainPage()
        page.login()
        page.logout()

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Подключиться по ID (неавтор)')
    @allure.testcase("")
    def test_connect_from_id_un(self):
        page = MainPage()
        page.connect_from_id(auth='yes')

    @pytest.mark.main
    @pytest.mark.smoke
    @allure.title('Подключиться по ID (автор)')
    @allure.testcase("")
    def test_connect_from_id(self):
        page = MainPage()
        page.login()
        page.connect_from_id()

    # @pytest.mark.main
    # @pytest.mark.smoke
    # @allure.title('Подключиться по ID')
    # @allure.testcase("")
    # def test_new(self):
    #     page = MainPage()
    #     page.test_new_base_func()