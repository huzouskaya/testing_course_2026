import time

class TestMainPage:
    
    def test_main_page_loads(self, main_page):
        """TC-01"""
        title_text = main_page.get_hero_title_text()
        assert "Write" in title_text or "Overleaf" in title_text, f"Неверный заголовок: {title_text}"
    
    def test_register_button_is_displayed(self, main_page):
        """TC-02"""
        assert main_page.is_visible(main_page.REGISTER_BUTTON), "Кнопка Register не найдена"
    
    def test_login_button_is_displayed(self, main_page):
        """TC-03"""
        assert main_page.is_visible(main_page.LOGIN_BUTTON), "Кнопка Log In не найдена"
    
    def test_go_to_templates_page(self, main_page):
        """TC-04"""
        templates_page = main_page.go_to_templates()
        assert "/templates" in templates_page.get_current_url(), "Не удалось перейти на страницу шаблонов"
    
    def test_footer_has_features_link(self, main_page):
        """TC-05"""
        main_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        assert main_page.is_visible(main_page.FOOTER_FEATURES), "Ссылка Features не найдена в футере"