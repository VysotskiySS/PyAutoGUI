# file: main_page.py
import time
from os import times
import pyautogui as pag

from config import *
from locators import *
from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self):
        super().__init__()


    def login(self, login=valid_login, password=valid_password):
        time.sleep(3)
        self.click(MainLocators.SETTINGS_BTN)
        self.click(MainLocators.LOGIN_BTN)
        self.click(MainLocators.LOGIN_FIELD)
        self.set_text(login)
        self.click(MainLocators.PASSWORD_FIELD)
        self.set_text(password)
        self.click(MainLocators.OK_BTN)
        time.sleep(3)
        self.hide_text('Неверный E-Mail или пароль',(1148, 791, 1328, 839))

    def logout(self):
        time.sleep(3)
        self.click(MainLocators.SETTINGS_BTN)
        self.click(MainLocators.LOGIN_BTN)
        self.click(MainLocators.SETTINGS_BTN)
        self.find_text('Войти', (180, 635, 370, 655))

    def connect_from_id(self, auth='no'):
        time.sleep(3)
        self.click(MainLocators.ID_FIELD)
        self.clear_text()
        self.set_text(valid_remote_device_id)
        self.click(MainLocators.CONNECT_BTN)
        if auth == 'yes':
            self.set_pass()
        time.sleep(3)
        self.find_element(CSLocators.CS_PANEL)

    def set_pass(self):
        # self.find_element(MainLocators.PASSWORD_WINDOW)
        self.set_text(valid_password)
        self.click(MainLocators.OK_BTN)

    def full_screen_cs(self):
        time.sleep(3)
        self.click(MainLocators.FULL_SCREEN_CS_BTN)

    # def test_new_base_func(self):
    #     self.click(self.get_element(MainLocators.SETTINGS_BTN))
