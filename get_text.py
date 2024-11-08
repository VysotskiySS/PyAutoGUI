import pytesseract
import cv2
import numpy as np
from PIL import Image
import pyautogui
import Levenshtein

def get_text(coordinates):
    # Заданные координаты (x1, y1, x2, y2)
    # coordinates = (1148, 791, 1328, 839)  # Пример координат

    # Сделать скриншот
    screenshot = pyautogui.screenshot()

    # Преобразовать изображение в формат OpenCV
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Вырезать область по заданным координатам
    x1, y1, x2, y2 = coordinates
    roi = screenshot[y1:y2, x1:x2]  # Region of Interest (ROI)

    # Преобразовать в серый цвет (рекомендуется для OCR)
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Уменьшение шума
    blurred_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)

    # # Бинаризация
    # binary_roi = cv2.adaptiveThreshold(blurred_roi, 255,
    #                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                    cv2.THRESH_BINARY, 11, 2)

    config = '--oem 3 --psm 6'

    # Использовать pytesseract для извлечения текста
    text = pytesseract.image_to_string(blurred_roi , lang='rus+eng', config=config)

    # Печать извлеченного текста
    print("Извлеченный текст:", text)
    return text


def similarity_percentage(str1, str2):
    # Вычисляем расстояние Левенштейна
    distance = Levenshtein.distance(str1, str2)

    # Максимальная длина строки
    max_len = max(len(str1), len(str2))

    # Вычисляем процент совпадения
    similarity = ((max_len - distance) / max_len) * 100

    return similarity


# Пример использования функции
# string1 = get_text()
# string2 = "Неверный E-Mail или пароль"
# similarity = similarity_percentage(string1, string2)
# print(f"Процент совпадения: {similarity:.0f}")

def find_text(string, coordinates):
    string1 = get_text(coordinates)
    similarity = similarity_percentage(string1, string)
    assert similarity > 80, f'Текст {string} по следующим координатам {coordinates} не найден'

find_text('Неверный E-Mail или пароль',(1148, 791, 1328, 839))
