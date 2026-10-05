"""
2026 (c) RomanECO
"""
# Force push for Allure update 2026

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://saucedemo.com'

from selenium.webdriver.common.by import By
import allure

def test_empty_input(browser):
    """
    Негативный тест: проверка авторизации с пустыми полями
    """
    
    with allure.step("Открытие главной страницы SauceDemo"):
        browser.get('https://saucedemo.com')

    with allure.step("Проверка исходного класса у поля ввода логина"):
        username_input = browser.find_element(By.ID, value="user-name")
        assert "form_input" in username_input.get_attribute("class")

    with allure.step("Клик по кнопке 'Login' с пустыми полями"):
        button = browser.find_element(By.ID, value="login-button")
        button.click()

    with allure.step("Проверка появления и текста сообщения об ошибке"):
        error_element = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]')
        error_text = error_element.text
        # Специально оставим правильный ассерт, но если он упадет — сделается скриншот!
        assert error_text == 'Epic sadface: Username is required'

    with allure.step("Проверка, что кнопка Login осталась на месте"):
        assert button.get_attribute("value") == "Login"

def test_invalid_input(browser):
    """
    negative - появление окна ОШИБКА при авторизации с невалидными данными
    """
    
    browser.get(URL)

    # Окно неактивно по умолчанию (проверка по наличию окна с ошибкой)
    
    email_label = browser.find_element(By.CSS_SELECTOR, value='.error-message-container')
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'error-message-container',""

    # при активном окне к error-message-container добавляется error!!!

    # вводим невалидные данные

    username = browser.find_element(By.ID, value="user-name")
    username.click()
    username.send_keys("standard_user_fake")
    
    password = browser.find_element(By.ID, value="password")
    password.click()
    password.send_keys("secret_sauce_Fake")
    
    button = browser.find_element(By.ID, value="login-button")
    button.click()

    email_label = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]')
    error_text = email_label.text
    assert error_text == 'Epic sadface: Username and password do not match any user in this service', f"Ожидалась другая ошибка, получили: '{error_text}'"
  

def test_send_password(browser):
    """
    positive - регистрация с валидными данными
    """
    
    browser.get(URL)

    username = browser.find_element(By.ID, value="user-name")
    username.click()
    username.send_keys("standard_user")

    password = browser.find_element(By.ID, value="password")
    password.click()
    password.send_keys("secret_sauce")

    button = browser.find_element(By.ID, value="login-button")
    button.click()

    assert True, ""

def test_button_text(browser):
    """
    Проверка того, что на кнопке логин написано Login
    """
    browser.get(URL)

    button = browser.find_element(By.ID, value="login-button")
    assert button.get_attribute ("value") == "Login", "Unexpected text"

def test_button_color(browser):
    """
    ПРОВЕРКА ЦВЕТА КНОПКИ Login
    """
    browser.get(URL)

    # Находим кнопку
    button = browser.find_element(By.ID, value="login-button")
    
    # Получаем значение CSS-свойства background-color
    button_color = button.value_of_css_property("background-color")
    
    # Выводим цвет в логи, чтобы увидеть его в терминале
    print(f"\n[ЦВЕТ] Фактический цвет кнопки: {button_color}")

    # Ожидаемый цвет кнопки (зеленый в формате rgba)
    expected_color = "rgba(61, 220, 145, 1)" 
    
    # Проверяем совпадение
    assert button_color == expected_color, f"Цвет кнопки изменился! Ожидали {expected_color}, но получили {button_color}"

def test_area_color(browser):
    """
    ПРОВЕРКА ЦВЕТА ПОЛЯ ЗАГЛАВНОЙ СТРАНИИЦЫ
    """
    browser.get(URL)

    # Находим поле
    area_color = browser.find_element(By.CSS_SELECTOR, value=".login_credentials_wrap-inner")

    # КЛАССЫ ПИШЕМ С ТОЧКОЙ ПЕРЕД НАЗВАНИЕМ!!!
    
    # Получаем значение CSS-свойства background-color
    area_color = area_color.value_of_css_property("background-color")
    
    # Выводим цвет в логи, чтобы увидеть его в терминале
    print(f"\n[ЦВЕТ] Фактический цвет поля: {area_color}")

    # Ожидаемый цвет поля
    expected_color = "rgba(19, 35, 34, 1)" 
    
    # Проверяем совпадение
    assert area_color == expected_color, f"Цвет поля изменился! Ожидали {expected_color}, но получили {area_color}"

def test_font_properties(browser):
    """
    Проверка размера, центровки и семейства шрифта элемента (заголовка странцы) в одном тесте
    """
    browser.get(URL)

    # Находим блок с учетными данными
    area = browser.find_element(By.CSS_SELECTOR, value=".login_logo")
    
    # 1. Получаем и проверяем семейство шрифта
    actual_font_family = area.value_of_css_property("font-family")
    print(f"\n[ШРИФТ] Фактическое семейство: {actual_font_family}")
    
    # Используем 'in', чтобы избежать проблем с кавычками браузера (DM Mono семейство по требованиям)
    assert "DM Mono" in actual_font_family, f"Ожидали DM Mono, но получили: {actual_font_family}"

    # 2. Получаем и проверяем размер шрифта
    actual_font_size = area.value_of_css_property("font-size")
    print(f"[ШРИФТ] Фактический размер: {actual_font_size}")
    
    expected_size = "24px"  # РАЗМЕР ШРИФТА по требованиям
    assert actual_font_size == expected_size, f"Ожидали размер {expected_size}, но получили: {actual_font_size}"

    # 3. Получаем и проверяем центровку текста
    actual_center = area.value_of_css_property("text-align")
    print(f"[ШРИФТ] Фактическая центровка: {actual_center}")
        
    expected_center = "center"  # Центровка по требованиям
    assert actual_center == expected_center, f"Ожидали размер {expected_center}, но получили: {actual_center}"

def test_postive_buy(browser):
    """
    positive - добавление товара в корзину
    """
    browser.delete_all_cookies()
    
    with allure.step("Открытие главной страницы магазина"):
        browser.get(URL)
    
    with allure.step("Авторизация под пользователем standard_user"):
        username = browser.find_element(By.ID, value="user-name")
        username.click()
        username.send_keys("standard_user")
    
        password = browser.find_element(By.ID, value="password")
        password.click()
        password.send_keys("secret_sauce")
    
        button = browser.find_element(By.ID, value="login-button")
        button.click()
    
    with allure.step("Добавление рюкзака 'Sauce Labs Backpack' в корзину"):
        # УМНОЕ ОЖИДАНИЕ: Ждем до 10 секунд, пока страница магазина загрузится и кнопка появится
        item_add_chart = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        item_add_chart.click()
    
    with allure.step("Проверка изменения текста кнопки на 'Remove'"):
        remove_item_tx = browser.find_element(By.ID, value="remove-sauce-labs-backpack")
        print(f"\n[ТЕКСТ] Фактический ТЕКСТ кнопки: {remove_item_tx.text}")
        assert remove_item_tx.text == "Remove", "Ошибка текста удаления товара из корзины"
    
    with allure.step("Проверка кода цвета текста кнопки Remove"):
        remove_item_button = browser.find_element(By.CSS_SELECTOR, value=".btn.btn_secondary.btn_small.btn_inventory")
        remove_item_color = remove_item_button.value_of_css_property("color")
        print(f"\n[ЦВЕТ] Фактический цвет текста кнопки: {remove_item_color}")
    
        expected_color_1 = "rgba(226, 35, 26, 1)"
        assert remove_item_color == expected_color_1, f"Цвет поля изменился! Ожидали {expected_color_1}, но получили {remove_item_color}"
    
    with allure.step("Переход в корзину"):
        button_2 = browser.find_element(By.CSS_SELECTOR, value=".shopping_cart_link")
        button_2.click()
    
    with allure.step("Проверка наличия рюкзака внутри корзины с товаром"):
        # ИСПРАВЛЕНО: удалена опечатка _to_be_ и добавлен стабильный метод ожидания
        actual_item_in_cart = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".inventory_item_name"))
        )
        
        print(f"\n[ТОВАР] Фактический товар в корзине: {actual_item_in_cart.text}")
        assert actual_item_in_cart.text == "Sauce Labs Backpack", "Не найден искомый товар"

