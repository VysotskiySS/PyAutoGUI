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
        page.connect_from_id()
        page.logout()