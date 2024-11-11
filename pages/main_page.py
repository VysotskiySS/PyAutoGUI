# file: main_page.py
import time
from os import times
import pyautogui as pag
from locators import *
from pages.base_page import BasePage

class MainPage(BasePage):

    def __init__(self):
        super().__init__()


    def login(self):
        time.sleep(3)
        self.click(MainLocators.SETTINGS_BTN)
        self.click(MainLocators.LOGIN_BTN)
        self.click(MainLocators.LOGIN_FIELD)
        self.set_text('rude')
        self.click(MainLocators.PASSWORD_FIELD)
        self.set_text('Kief22Mo')
        self.click(MainLocators.OK_BTN)
        time.sleep(3)
        self.hide_text('Неверный E-Mail или пароль',(1148, 791, 1328, 839))

    def logout(self):
        time.sleep(3)
        self.click(MainLocators.SETTINGS_BTN)
        self.click(MainLocators.LOGIN_BTN)
        self.click(MainLocators.SETTINGS_BTN)
        self.find_text('Войти', (180, 635, 370, 655))

    def connect_from_id(self):
        time.sleep(3)
        self.click(MainLocators.ID_FIELD)
        self.clear_text()
        self.set_text('000111333')
        self.click(MainLocators.CONNECT_BTN)
        time.sleep(3)
        self.find_element(CSLocators.CS_PANEL)


    def full_screen_cs(self):
        time.sleep(3)
        self.click(MainLocators.FULL_SCREEN_CS_BTN)
