import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Координаты: ({x}, {y})", end='\r')
        time.sleep(0.5)  # Обновляем каждые 0.5 секунд
except KeyboardInterrupt:
    print("\nЗавершено.")
