# file: base_page.py
import allure
import pyautogui as pag
import pytesseract
import numpy as np
from PIL import Image
import cv2
import os
import time
from locators import *

class BasePage:
    def __init__(self):
        pass

    def get_size(self):
        pag.size()

    def get_os_name(self):
        return os.name

    def click_img(self, locator):
        # Ищем изображение на экране
        location = pag.locateOnScreen(locator)
        if location:
            # Кликаем по его центру
            pag.click(pag.center(location))
        else:
            raise ValueError(f"Элемент{locator} не найден")

    def click_coordinate(self, x, y, duration=1):
        pag.moveTo(x, y, duration)
        pag.click()

    def set_text(self, text):
        pag.write(text, interval=0.25)  # Вводит текст с интервалом между символами

    def click(self, locator, element_name=None):
        if element_name is not None:
            with allure.step(f"Клик по элементу '{element_name}'"):
                if isinstance(locator, str):
                    self.click_img(locator)
                else:
                    self.click_coordinate(*locator)
        else:
            if isinstance(locator, str):
                self.click_img(locator)
            else:
                self.click_coordinate(*locator)

    def get_screen(self):
        # Снимаем текущий экран и сохраняем его как файл
        screenshot = pag.screenshot()
        screenshot.save("screenshot.png")

    def get_text_from_img(self):
        # Загрузка изображения
        img = cv2.imread('screenshot.png')
        # Преобразование изображения в оттенки серого
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Улучшение изображения
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        # Применение OCR
        text = pytesseract.image_to_string(gray, lang='eng')
        return text

    def find_element(self, locator):
        # Ищем изображение на экране
        location = pag.locateOnScreen(locator)
        if location:
            # Кликаем по его центру
            pass
        else:
            raise ValueError(f"Элемент{locator} не найден")

    def hide_element(self, locator):
        # Ищем изображение на экране
        try:
            location = pag.locateOnScreen(locator)
            if location:
                raise ValueError(f"Элемент{locator} найден")
            else:
                pass
        except Exception:
            pass

    def get_text_from_coordinates(self, coordinates):
        # Сделать скриншот
        screenshot = pag.screenshot()
        # Преобразовать изображение в формат OpenCV
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        # Вырезать область по заданным координатам
        x1, y1, x2, y2 = coordinates
        roi = screenshot[y1:y2, x1:x2]  # Region of Interest (ROI)
        # Преобразовать в серый цвет (рекомендуется для OCR)
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # Уменьшение шума
        blurred_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)
        config = '--oem 3 --psm 6' # Настройка Tesseract
        # Использовать pytesseract для извлечения текста
        text = pytesseract.image_to_string(blurred_roi, lang='rus+eng', config=config)
        return text
