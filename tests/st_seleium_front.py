"""
2026 (c) RomanECO
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import time


def run_smoke_test():
    print("\n[СТАРТ ТЕСТА] Инициализация настроек Chrome...")
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    # УБРАЛИ строку "detach": True, так как теперь мы хотим закрывать браузер

    # Блокируем окна об утечке данных от Google Chrome
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    print("[ДРАЙВЕР] Скачивание/подготовка ChromeDriver...")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = "https://saucedemo.com"
        print(f"[НАВИГАЦИЯ] Открываю страницу: {url}")
        browser.get(url)
        
        print("[ПОИСК] Ищу поле ввода логина...")
        username_field = browser.find_element(By.ID, value="user-name")
        print("✅ Поле логина найдено. Ввожу данные...")
        username_field.send_keys("standard_user")

        print("[ПОИСК] Ищу поле ввода пароля...")
        password_field = browser.find_element(By.ID, value="password")
        print("✅ Поле пароля найдено. Ввожу данные...")
        password_field.send_keys("secret_sauce")

        print("[ПОИСК] Ищу кнопку входа...")
        login_button = browser.find_element(By.ID, value="login-button")
        print("✅ Кнопка найдена. Выполняю клик...")
        login_button.click()

        print("[ОЖИДАНИЕ] Жду 2 секунды...")
        time.sleep(2)

        print("[ПРОВЕРКА] Ищу заголовок каталога товаров...")
        page_title_element = browser.find_element(By.CLASS_NAME, value="title")
        page_title_text = page_title_element.text
        
        if page_title_text == "Products":
            print(f"🎉 ТЕСТ УСПЕШНО ПРОЙДЕН! Найден заголовок: '{page_title_text}'")
        else:
            print(f"❌ ТЕСТ ПРОВАЛЕН! Найдено: '{page_title_text}'")

    except Exception as error:
        print("\n💥 КРИТИЧЕСКАЯ ОШИБКА В ХОДЕ ВЫПОЛНЕНИЯ ТЕСТА!")
        print(f"Тип ошибки: {type(error).__name__}")
        print(f"Описание: {error}")

    finally:
        # ДОБАВЛЕНО: Этот блок выполнится ВСЕГДА, закрывая браузер в конце
        print("[ЗАВЕРШЕНИЕ] Закрываю браузер...")
        browser.quit()


# Запускаем функцию
run_smoke_test()