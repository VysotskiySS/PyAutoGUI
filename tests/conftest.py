# file: conftest.py

import pytest
import time
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

def full_screen():
    time.sleep(2)
    subprocess.Popen(['xdotool', 'key', 'alt+F10'])

def close_app():
    global app_process
    if app_process:
        app_process.terminate()  # Прекращаем выполнение процесса приложения
        app_process = None  # Сбрасываем переменную