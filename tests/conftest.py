"""
2026 (c) RomanECO
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless=new')  #фоновый режим для сервера
    
    # Оставляем браузер открытым
    # chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver  
    
    # driver.quit()  # Закомментировано по вашему запросу