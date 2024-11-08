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
        self.hide_element(MainLocators.WARNING_PASS)

    def logout(self):
        time.sleep(3)
        self.click(MainLocators.SETTINGS_BTN)
        self.click(MainLocators.LOGIN_BTN)

    def connect_from_id(self):
        time.sleep(3)
        self.click(MainLocators.ID_FIELD)
        pag.hotkey('ctrl', 'a')
        pag.keyDown('delete')
        self.set_text('000111333')
        self.click(MainLocators.CONNECT_BTN)
        # self.click(MainLocators.X_BTN)

    def full_screen_cs(self):
        time.sleep(3)
        self.click(MainLocators.FULL_SCREEN_CS_BTN)
