"""
2026 (c) RomanECO
"""
from selenium.webdriver.common.by import By 

URL = 'https://saucedemo.com'


def test_empty_input(browser):
    """
    negative - выскакивает окно ОШИБКИ при авторизации с незаполненными полями
    """
    
    browser.get(URL)

    # Окно неактивно по умолчанию (проверка по полю ввода имени пользователя)

    email_label = browser.find_element(By.ID, value='user-name')
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'input_error form_input',""

    # при активном окне к input_error form_input добавляется error!!!

    button = browser.find_element(By.ID, value="login-button")
    button.click()

    email_label = browser.find_element(By.CSS_SELECTOR, value='[data-test="error"]')
    error_text = email_label.text
    assert error_text == 'Epic sadface: Username is required', f"Ожидалась другая ошибка, получили: '{error_text}'"

def test_invalid_input(browser):
    """
    negative - выскакивает окно ОШИБКИ при авторизации с невалидными данными
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
    Hа кнопке логин написано Login
    """
    browser.get(URL)

    button = browser.find_element(By.ID, value="login-button")
    assert button.get_attribute ("value") == "Login", "Unexpected text"

def test_button_color(browser):
    """
    ПРОВЕРКА ЦВЕТА КНОПКИ
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
    ПРОВЕРКА ЦВЕТА ПОЛЯ
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