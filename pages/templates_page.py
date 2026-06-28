import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class TemplatesPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "#algolia-search")
    PROJECT_REPORT_CARD = (By.XPATH, "//a[contains(@href, 'report')]")
    SEARCH_RESULTS = (By.XPATH, "//div[contains(@class, 'card')]")
    
    def search_for_template(self, query):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        self.input_text(self.SEARCH_INPUT, query)
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT)).send_keys(Keys.RETURN)
        self.wait.until(EC.visibility_of_any_elements_located(self.SEARCH_RESULTS))
        return self
    
    def is_project_report_visible(self):
        return self.is_visible(self.PROJECT_REPORT_CARD)
    
    def get_search_results_count(self):
        return len(self.driver.find_elements(*self.SEARCH_RESULTS))