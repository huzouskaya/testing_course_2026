import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class TemplatesPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "#algolia-search")
    PROJECT_REPORT_CARD = (By.XPATH, "//a[contains(@href, 'report')]")
    SEARCH_RESULTS = (By.XPATH, "//div[contains(@class, 'card')]")
    
    def search_for_template(self, query):
        self.input_text(self.SEARCH_INPUT, query)
        time.sleep(1)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.RETURN)
        time.sleep(2)
        return self
    
    def is_project_report_visible(self):
        return self.is_visible(self.PROJECT_REPORT_CARD)
    
    def get_search_results_count(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS))