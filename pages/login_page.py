from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'error') or contains(@role, 'alert')]")
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'OK')]")
    
    def accept_cookies(self):
        if self.is_visible(self.COOKIE_ACCEPT_BUTTON):
            self.click(self.COOKIE_ACCEPT_BUTTON)
        return self
    
    def click_login_button_without_data(self):
        self.accept_cookies()
        self.click(self.LOGIN_FORM_BUTTON)
        return self
    
    def get_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE)