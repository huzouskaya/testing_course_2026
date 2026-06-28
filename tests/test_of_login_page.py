class TestLoginPage:
    
    def test_login_page_opens(self, login_page):
        """TC-09"""
        assert "/login" in login_page.get_current_url()        

    def test_error_on_empty_login_form(self, login_page):
        """TC-10"""
        login_page.click_login_button_without_data()
        assert login_page.is_error_message_visible()