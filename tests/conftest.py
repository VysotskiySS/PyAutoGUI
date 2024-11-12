# file: conftest.py

import pytest
import time
import subprocess

from pages.base_page import BasePage

# Хранит процесс приложения
app_process = None

@pytest.fixture(scope="function")
def setup():
    global app_process
    run_app()
    yield
    teardown()

def run_app():
    global app_process
    program_name = 'rudesktop'  # Убедитесь, что это верное имя исполняемого файла
    app_process = subprocess.Popen(program_name)  # Запускаем приложение
    full_screen()

def full_screen():
    time.sleep(2)
    subprocess.Popen(['xdotool', 'key', 'alt+F10'])

def teardown():
    BasePage().get_screen()
    close_app()

def close_app():
    global app_process
    if app_process:
        kill_process('rudesktop')
        # app_process.terminate()  # Прекращаем выполнение процесса приложения
        # app_process = None  # Сбрасываем переменную

# Закрытие программы по её имени
def kill_process(name):
    try:
        subprocess.run(["pkill", "-f", name], check=True)
        print(f"Процесс {name} был успешно завершён.")
    except subprocess.CalledProcessError:
        print(f"Не удалось завершить процесс {name}.")

# def get_screen(self):
#     # Снимаем текущий экран и сохраняем его как файл
#     screenshot = pag.screenshot()
#     screen = "screen.png"
#     screenshot.save(screen)
#     # Передаем скриншот в Allure
#     allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)