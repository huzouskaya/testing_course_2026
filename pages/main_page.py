import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a[href='/register']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    TEMPLATES_LINK = (By.XPATH, "//a[contains(@href, '/templates')]")
    HERO_TITLE = (By.XPATH, "//h1[contains(@class, 'home-top-text')]")
    FOOTER_FEATURES = (By.XPATH, "//footer//a[contains(text(), 'Careers')]")
    
    def get_hero_title_text(self):
        return self.get_text(self.HERO_TITLE)
    
    def go_to_templates(self):
        self.click(self.TEMPLATES_LINK)
        time.sleep(2)
        from pages.templates_page import TemplatesPage
        return TemplatesPage(self.driver)
    
    def go_to_login(self):
        self.click(self.LOGIN_BUTTON)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)