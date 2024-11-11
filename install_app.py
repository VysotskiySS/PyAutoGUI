import requests
import subprocess

# URL вашего скрипта
url = 'https://192.168.10.74/peers/install/rudesktop-2.7.740-amd64.deb.sh'

# Скачиваем скрипт
response = requests.get(url)
script_content = response.text

# Сохраняем скрипт во временный файл
with open('temp_script.sh', 'w') as file:
    file.write(script_content)

try:
    # Делаем файл исполняемым
    subprocess.run(['chmod', '+x', 'temp_script.sh'], check=True)

    # Запускаем скрипт
    subprocess.run(['./temp_script.sh'], check=True)
finally:
    # Удаляем временный файл после выполнения
    import os

    os.remove('temp_script.sh')