import requests
from bs4 import BeautifulSoup
import time

# Функция для получения курса валюты
def get_currency_rate():
    # Адрес сайта, с которого мы будем получать данные
    url = "https://www.google.com/search?q=курс+доллара+к+рублю"
    
    # Получаем содержимое страницы
    response = requests.get(url)
    
    # Создаем объект BeautifulSoup для парсинга HTML-разметки
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Получаем элемент с курсом валюты
    result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
    
    # Возвращаем курс валюты как число
    return float(result.replace(",", "."))

# Основной код программы
if __name__ == "__main__":
    # Получаем текущий курс валюты
    current_rate = get_currency_rate()
    print(f"Текущий курс валюты: {current_rate}")
    
    # Запускаем бесконечный цикл
    while True:
        # Ждем 5 секунд
        time.sleep(5)
        
        # Получаем новый курс валюты
        new_rate = get_currency_rate()
        
        # Если произошло сильное изменение курса валюты, отправляем уведомление
        if abs(new_rate - current_rate) > 2:
            print(f"Сильное изменение курса валюты! Старое значение: {current_rate}, новое значение: {new_rate}")
            current_rate = new_rate