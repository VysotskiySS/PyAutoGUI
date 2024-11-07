import os
import subprocess
import pygetwindow as gw
import pyautogui
import time

# Замените 'your_program' на имя вашей программы или полный путь к ней
program_name = 'rudesktop'

# Запускаем программу
subprocess.Popen(program_name)

# Даем время программе для загрузки
time.sleep(2)

# Получаем список всех окон
windows = gw.getWindowsWithTitle('RuDesktop')  # Замените на заголовок окна программы

if windows:
    window = windows[0]

    # Получаем размеры и положение второго монитора (если он есть)
    monitor_2 = pyautogui.getWindows()  # Замените на параметры вашего монитора
    if monitor_2:
        # Перемещаем окно на второй монитор
        window.moveTo(monitor_2[0].left, monitor_2[0].top)  # Замените индексы, если нужно

        # Устанавливаем окно в полноэкранный режим, если это возможно
        window.maximize()
else:
    print("Окно не найдено")