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