class TestTemplatesPage:
    
    def test_templates_page_loads(self, templates_page):
        """TC-06"""
        assert templates_page.is_visible(templates_page.SEARCH_INPUT)

    def test_search_template_by_keyword(self, templates_page):
        """TC-07"""
        templates_page.search_for_template("report")
        assert templates_page.get_search_results_count() > 0

    def test_project_report_template_is_displayed(self, templates_page):
        """TC-08"""
        assert templates_page.is_project_report_visible() is True