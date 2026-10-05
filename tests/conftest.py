import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function') # Для точных скриншотов лучше использовать function
def browser(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('start-maximized')
    chrome_options.add_argument('--headless=new')  # настройка для GitHub Actions!
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # МАГИЯ СКРИНШОТОВ: Проверяем, упал ли тест
    # request.node.rep_call присутствует, если тест завершился ошибкой
    failed = getattr(request.node, "rep_call", None) and request.node.rep_call.failed
    if failed:
        print("[ALLURE] Тест упал! Делаю скриншот экрана...")
        # Делаем скриншот и прикрепляем его к отчету Allure
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )
    
    driver.quit()

# Вспомогательный хук для PyTest, чтобы фикстура знала о результате теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)