from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    REGISTER_BUTTON = (By.CSS_SELECTOR, "a[href='/register']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='/login']")
    TEMPLATES_LINK = (By.XPATH, "//a[contains(@href, '/templates')]")
    HERO_TITLE = (By.XPATH, "//h1[contains(@class, 'home-top-text')]")
    FOOTER_FEATURES = (By.XPATH, "//footer//a[contains(text(), 'Careers')]")
    
    def get_hero_title_text(self):
        self.wait.until(EC.visibility_of_element_located(self.HERO_TITLE))
        return self.get_text(self.HERO_TITLE)
    
    def go_to_templates(self):
        self.click(self.TEMPLATES_LINK)
        from pages.templates_page import TemplatesPage
        templates_page = TemplatesPage(self.driver)
        templates_page.wait.until(EC.visibility_of_element_located(templates_page.SEARCH_INPUT))
        return templates_page
    
    def go_to_login(self):
        self.click(self.LOGIN_BUTTON)
        from pages.login_page import LoginPage
        return LoginPage(self.driver)