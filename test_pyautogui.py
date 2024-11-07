import pyautogui
# import pytest
# from pages.main_page import MainPage
# from pages.base_page import *
# import allure

# pyautogui.moveTo(180, 194, duration=1)
# pyautogui.click()

# Ищем изображение на экране
location = pyautogui.locateOnScreen('img/settings_btn.png')

if location:
    # Если изображение найдено, кликаем по его центру
    pyautogui.click(pyautogui.center(location))
    print("Клик выполнен по изображению!")
else:
    print("Изображение не найдено.")

location = pyautogui.locateOnScreen('img/login_btn.png')

if location:
    # Если изображение найдено, кликаем по его центру
    pyautogui.click(pyautogui.center(location))
    print("Клик выполнен по изображению!")
else:
    print("Изображение не найдено.")


pyautogui.moveTo(229, 647, duration=1)
pyautogui.click()

pyautogui.moveTo(1245, 663, duration=1)
pyautogui.click()

# Ввод текста
pyautogui.write("rude", interval=0.25)  # Вводит текст с интервалом между символами
# pyautogui.press('enter')  # Нажимает Enter

pyautogui.moveTo(1235, 723, duration=1)
pyautogui.click()

pyautogui.write("Kief22Mo", interval=0.25)

pyautogui.moveTo(1465, 824, duration=1)
pyautogui.click()

# Ищем изображение "connect_btn.png" на экране
location = pyautogui.locateOnScreen('img/connect_btn.png')

if location:
    # Если изображение найдено, кликаем по его центру
    pyautogui.click(pyautogui.center(location))
    print("Клик выполнен по изображению!")
else:
    print("Изображение не найдено.")


# Получаем текущие координаты курсора
time.sleep(5)
x, y = pyautogui.position()
print(f"Current mouse position: ({x}, {y})")
