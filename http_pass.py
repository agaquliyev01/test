from sys import executable

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Путь к chromedriver
cdp = "/home/aga/Desktop/chromedriver_linux64/chromedriver"

# Создание экземпляра Service с путем к chromedriver
service = Service(cdp)

# Инициализация веб-драйвера с использованием Service
driver = webdriver.Chrome(service=service)
repo = "https://github.com/agaquliyev01"
# Открытие страницы после инициализации драйвера
driver.get("https://github.com/agaquliyev01")

# Ожидание загрузки страницы
#time.sleep(2)
res = driver.find_elements(By.CLASS_NAME,"repo")
time.sleep(2)
links = []
flink = []
for i in res:
    links.append(i.text)
#print(links)
for l in links:
    next_pge = f"{repo}/{l}"
    flink.append(next_pge)
print(flink)
driver.quit()