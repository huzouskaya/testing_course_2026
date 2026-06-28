import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage
from pages.templates_page import TemplatesPage
from pages.login_page import LoginPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    
    service = Service("geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    
    yield driver
    
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return "https://www.overleaf.com"


@pytest.fixture(scope="function")
def main_page(driver, base_url):
    main_page = MainPage(driver)
    main_page.open(base_url)
    return main_page


@pytest.fixture(scope="function")
def templates_page(main_page):
    return main_page.go_to_templates()


@pytest.fixture(scope="function")
def login_page(main_page):
    return main_page.go_to_login()