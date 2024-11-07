# file: conftest.py

import subprocess
import pytest
import allure
import pyautogui as pag
import time
# import keyboard
import subprocess

# Хранит процесс приложения
app_process = None

@pytest.fixture(scope="function")
def setup():
    global app_process
    run_app()
    full_screen()
    yield
    close_app()

def run_app():
    global app_process
    program_name = 'rudesktop'  # Убедитесь, что это верное имя исполняемого файла
    app_process = subprocess.Popen(program_name)  # Запускаем приложение

# def full_screen():
#     pag.hotkey('alt', 'f10')


# def full_screen():
    # time.sleep(3)
    # keyboard.press_and_release('alt+f10')


def full_screen():
    time.sleep(2)
    subprocess.Popen(['xdotool', 'key', 'alt+F10'])

def close_app():
    global app_process
    if app_process:
        app_process.terminate()  # Прекращаем выполнение процесса приложения
        app_process = None  # Сбрасываем переменную