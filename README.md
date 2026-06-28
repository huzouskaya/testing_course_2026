# testing_course_2026

PS C:\Users\AliceWolf13\testing_course_2026> python -m pytest tests/ -v
==================================================== test session starts =====================================================
platform win32 -- Python 3.13.3, pytest-7.4.0, pluggy-1.6.0 -- C:\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\AliceWolf13\testing_course_2026
plugins: allure-pytest-2.13.2
collected 10 items                                                                                                            

tests/test_of_login_page.py::TestLoginPage::test_login_page_opens PASSED                                                [ 10%]
tests/test_of_login_page.py::TestLoginPage::test_error_on_empty_login_form FAILED                                       [ 20%]
tests/test_of_main_page.py::TestMainPage::test_main_page_loads FAILED                                                   [ 30%]
tests/test_of_main_page.py::TestMainPage::test_register_button_is_displayed PASSED                                      [ 40%]
tests/test_of_main_page.py::TestMainPage::test_login_button_is_displayed PASSED                                         [ 50%]
tests/test_of_main_page.py::TestMainPage::test_go_to_templates_page FAILED                                              [ 60%]
tests/test_of_main_page.py::TestMainPage::test_footer_has_features_link FAILED                                          [ 70%]
tests/test_of_templates_page.py::TestTemplatesPage::test_templates_page_loads ERROR                                     [ 80%]
tests/test_of_templates_page.py::TestTemplatesPage::test_search_template_by_keyword ERROR                               [ 90%]
tests/test_of_templates_page.py::TestTemplatesPage::test_project_report_template_is_displayed ERROR                     [100%]

=========================================================== ERRORS ===========================================================
_______________________________ ERROR at setup of TestTemplatesPage.test_templates_page_loads ________________________________

main_page = <pages.main_page.MainPage object at 0x000001ADBD1EB130>

    @pytest.fixture(scope="function")
    def templates_page(main_page):
>       return main_page.go_to_templates()

conftest.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:20: in go_to_templates
    self.click(self.TEMPLATES_LINK)
pages\base_page.py:18: in click
    self.wait.until(EC.element_to_be_clickable(locator)).click()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="e33ad46d-1a01-4b61-a0fb-eba6804397d1")>
method = <function element_to_be_clickable.<locals>._predicate at 0x000001ADBD1A89A0>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
____________________________ ERROR at setup of TestTemplatesPage.test_search_template_by_keyword _____________________________

main_page = <pages.main_page.MainPage object at 0x000001ADBD224150>

    @pytest.fixture(scope="function")
    def templates_page(main_page):
>       return main_page.go_to_templates()

conftest.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:20: in go_to_templates
    self.click(self.TEMPLATES_LINK)
pages\base_page.py:18: in click
    self.wait.until(EC.element_to_be_clickable(locator)).click()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="39987825-7591-46cc-9860-dc788af6f4b8")>
method = <function element_to_be_clickable.<locals>._predicate at 0x000001ADBD1A82C0>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
_______________________ ERROR at setup of TestTemplatesPage.test_project_report_template_is_displayed ________________________

main_page = <pages.main_page.MainPage object at 0x000001ADBD224D50>

    @pytest.fixture(scope="function")
    def templates_page(main_page):
>       return main_page.go_to_templates()

conftest.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:20: in go_to_templates
    self.click(self.TEMPLATES_LINK)
pages\base_page.py:18: in click
    self.wait.until(EC.element_to_be_clickable(locator)).click()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="89766d81-fd71-48c9-bfb0-975ccc41d3f9")>
method = <function element_to_be_clickable.<locals>._predicate at 0x000001ADBD1A8040>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
========================================================== FAILURES ==========================================================
________________________________________ TestLoginPage.test_error_on_empty_login_form ________________________________________

self = <test_of_login_page.TestLoginPage object at 0x000001ADBCD03110>
login_page = <pages.login_page.LoginPage object at 0x000001ADBCDB11D0>

    def test_error_on_empty_login_form(self, login_page):
        """TC-10: Отображение ошибки с пустыми полями"""
        login_page.click_login_button_without_data()
>       assert "Email is required" in login_page.get_error_message_text()

tests\test_of_login_page.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\login_page.py:22: in get_error_message_text
    return self.get_text(self.ERROR_MESSAGE)
pages\base_page.py:28: in get_text
    return self.wait.until(EC.visibility_of_element_located(locator)).text
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="32859fd3-174f-4760-8ae2-800a909f6d08")>
method = <function visibility_of_element_located.<locals>._predicate at 0x000001ADBCDC5580>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message:

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
_____________________________________________ TestMainPage.test_main_page_loads ______________________________________________

self = <test_of_main_page.TestMainPage object at 0x000001ADBCD02AD0>
main_page = <pages.main_page.MainPage object at 0x000001ADBCDB2210>

    def test_main_page_loads(self, main_page):
        """TC-01: Загрузка главной страницы"""
        title_text = main_page.get_hero_title_text()
>       assert "Write" in title_text or "Overleaf" in title_text, f"Неверный заголовок: {title_text}"
E       AssertionError: Неверный заголовок: 
E       assert ('Write' in '' or 'Overleaf' in '')

tests\test_of_main_page.py:6: AssertionError
___________________________________________ TestMainPage.test_go_to_templates_page ___________________________________________

self = <test_of_main_page.TestMainPage object at 0x000001ADBCD19E00>
main_page = <pages.main_page.MainPage object at 0x000001ADBCD77E30>

    def test_go_to_templates_page(self, main_page):
        """TC-04: Навигация к странице шаблонов"""
>       templates_page = main_page.go_to_templates()

tests\test_of_main_page.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:20: in go_to_templates
    self.click(self.TEMPLATES_LINK)
pages\base_page.py:18: in click
    self.wait.until(EC.element_to_be_clickable(locator)).click()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="55196ec1-bf29-4734-952f-fe4d7cf42caf")>
method = <function element_to_be_clickable.<locals>._predicate at 0x000001ADBD1A8680>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
_________________________________________ TestMainPage.test_footer_has_features_link _________________________________________

self = <test_of_main_page.TestMainPage object at 0x000001ADBCD75370>
main_page = <pages.main_page.MainPage object at 0x000001ADBCD9F020>

    def test_footer_has_features_link(self, main_page):
        """TC-05: Отображение ссылки Features в футере"""
        main_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        import time
        time.sleep(1)
>       assert main_page.is_visible(main_page.FOOTER_FEATURES), "Ссылка Features не найдена в футере"
E       AssertionError: Ссылка Features не найдена в футере
E       assert False
E        +  where False = <bound method BasePage.is_visible of <pages.main_page.MainPage object at 0x000001ADBCD9F020>>(('xpath', "//footer//a[contains(text(), 'Features')]"))
E        +    where <bound method BasePage.is_visible of <pages.main_page.MainPage object at 0x000001ADBCD9F020>> = <pages.main_page.MainPage object at 0x000001ADBCD9F020>.is_visible
E        +    and   ('xpath', "//footer//a[contains(text(), 'Features')]") = <pages.main_page.MainPage object at 0x000001ADBCD9F020>.FOOTER_FEATURES

tests\test_of_main_page.py:26: AssertionError
================================================== short test summary info ===================================================
FAILED tests/test_of_login_page.py::TestLoginPage::test_error_on_empty_login_form - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_of_main_page.py::TestMainPage::test_main_page_loads - AssertionError: Неверный заголовок: 
FAILED tests/test_of_main_page.py::TestMainPage::test_go_to_templates_page - selenium.common.exceptions.TimeoutException: Message: 
FAILED tests/test_of_main_page.py::TestMainPage::test_footer_has_features_link - AssertionError: Ссылка Features не найдена в футере
ERROR tests/test_of_templates_page.py::TestTemplatesPage::test_templates_page_loads - selenium.common.exceptions.TimeoutException: Message: 
ERROR tests/test_of_templates_page.py::TestTemplatesPage::test_search_template_by_keyword - selenium.common.exceptions.TimeoutException: Message: 
ERROR tests/test_of_templates_page.py::TestTemplatesPage::test_project_report_template_is_displayed - selenium.common.exceptions.TimeoutException: Message: 
===================================== 4 failed, 3 passed, 3 errors in 302.61s (0:05:02) ======================================
PS C:\Users\AliceWolf13\testing_course_2026> python -m pytest tests/ -v
==================================================== test session starts =====================================================
platform win32 -- Python 3.13.3, pytest-7.4.0, pluggy-1.6.0 -- C:\Python313\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\AliceWolf13\testing_course_2026
plugins: allure-pytest-2.13.2
collected 10 items                                                                                                            

tests/test_of_login_page.py::TestLoginPage::test_login_page_opens PASSED                                                [ 10%]
tests/test_of_login_page.py::TestLoginPage::test_error_on_empty_login_form FAILED                                       [ 20%]
tests/test_of_main_page.py::TestMainPage::test_main_page_loads FAILED                                                   [ 30%]
tests/test_of_main_page.py::TestMainPage::test_register_button_is_displayed PASSED                                      [ 40%]
tests/test_of_main_page.py::TestMainPage::test_login_button_is_displayed PASSED                                         [ 50%]
tests/test_of_main_page.py::TestMainPage::test_go_to_templates_page FAILED                                              [ 60%]
tests/test_of_main_page.py::TestMainPage::test_footer_has_features_link PASSED                                          [ 70%]
tests/test_of_templates_page.py::TestTemplatesPage::test_templates_page_loads ERROR                                     [ 80%]
tests/test_of_templates_page.py::TestTemplatesPage::test_search_template_by_keyword ERROR                               [ 90%]
tests/test_of_templates_page.py::TestTemplatesPage::test_project_report_template_is_displayed ERROR                     [100%]

=========================================================== ERRORS ===========================================================
_______________________________ ERROR at setup of TestTemplatesPage.test_templates_page_loads ________________________________

main_page = <pages.main_page.MainPage object at 0x000001A6FDDA2030>

    @pytest.fixture(scope="function")
    def templates_page(main_page):
>       return main_page.go_to_templates()

conftest.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:18: in go_to_templates
    self.click(self.TEMPLATES_LINK)
pages\base_page.py:18: in click
    self.wait.until(EC.element_to_be_clickable(locator)).click()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="059186fd-47a3-4fde-9958-065fac91656c")>
method = <function element_to_be_clickable.<locals>._predicate at 0x000001A6FDD94900>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
____________________________ ERROR at setup of TestTemplatesPage.test_search_template_by_keyword _____________________________

request = <SubRequest 'driver' for <Function test_search_template_by_keyword>>

    @pytest.fixture(scope="function")
    def driver(request):
        options = Options()
        options.add_argument("--window-size=1920,1080")
    
>       service = Service(GeckoDriverManager().install())

conftest.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\firefox.py:39: in install
    driver_path = self._get_driver_binary_path(self.driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\manager.py:35: in _get_driver_binary_path
    binary_path = self._cache_manager.find_driver(driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver_cache.py:108: in find_driver
    key = self.__get_metadata_key(driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver_cache.py:142: in __get_metadata_key
    driver_version = self.get_cache_key_driver_version(driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver_cache.py:152: in get_cache_key_driver_version
    return driver.get_driver_version_to_download()
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver.py:48: in get_driver_version_to_download
    return self.get_latest_release_version()
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\drivers\firefox.py:29: in get_latest_release_version
    resp = self._http_client.get(
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\http.py:36: in get
    self.validate_response(resp)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

resp = <Response [403]>

    @staticmethod
    def validate_response(resp: requests.Response):
        status_code = resp.status_code
        if status_code == 404:
            raise ValueError(f"There is no such driver by url {resp.url}")
        elif status_code == 401:
            raise ValueError(f"API Rate limit exceeded. You have to add GH_TOKEN!!!")
        elif resp.status_code != 200:
>           raise ValueError(
                f"response body:\n{resp.text}\n"
                f"request url:\n{resp.request.url}\n"
                f"response headers:\n{dict(resp.headers)}\n"
            )
E           ValueError: response body:
E           {"message":"API rate limit exceeded for 91.149.113.120. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)","documentation_url":"https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"}
E           
E           request url:
E           https://api.github.com/repos/mozilla/geckodriver/releases/latest
E           response headers:
E           {'Date': 'Sun, 28 Jun 2026 11:09:03 GMT', 'Server': 'Varnish', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'deny', 'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'", 'Access-Control-Allow-Origin': '*', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-RateLimit-Used, X-RateLimit-Resource, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset', 'Content-Type': 'application/json; charset=utf-8', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'X-GitHub-Media-Type': 'github.v3; format=json', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Used': '60', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Reset': '1782645762', 'Content-Length': '280', 'X-GitHub-Request-Id': '3D4D:1A183A:1227E308:115B51F4:6A4100CF'}

..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\http.py:19: ValueError
_______________________ ERROR at setup of TestTemplatesPage.test_project_report_template_is_displayed ________________________

request = <SubRequest 'driver' for <Function test_project_report_template_is_displayed>>

    @pytest.fixture(scope="function")
    def driver(request):
        options = Options()
        options.add_argument("--window-size=1920,1080")
    
>       service = Service(GeckoDriverManager().install())

conftest.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\firefox.py:39: in install
    driver_path = self._get_driver_binary_path(self.driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\manager.py:35: in _get_driver_binary_path
    binary_path = self._cache_manager.find_driver(driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver_cache.py:105: in find_driver
    driver_version = self.get_cache_key_driver_version(driver)
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver_cache.py:152: in get_cache_key_driver_version
    return driver.get_driver_version_to_download()
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\driver.py:48: in get_driver_version_to_download
    return self.get_latest_release_version()
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\drivers\firefox.py:29: in get_latest_release_version
    resp = self._http_client.get(
..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\http.py:36: in get
    self.validate_response(resp)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

resp = <Response [403]>

    @staticmethod
    def validate_response(resp: requests.Response):
        status_code = resp.status_code
        if status_code == 404:
            raise ValueError(f"There is no such driver by url {resp.url}")
        elif status_code == 401:
            raise ValueError(f"API Rate limit exceeded. You have to add GH_TOKEN!!!")
        elif resp.status_code != 200:
>           raise ValueError(
                f"response body:\n{resp.text}\n"
                f"request url:\n{resp.request.url}\n"
                f"response headers:\n{dict(resp.headers)}\n"
            )
E           ValueError: response body:
E           {"message":"API rate limit exceeded for 91.149.113.120. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)","documentation_url":"https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"}
E           
E           request url:
E           https://api.github.com/repos/mozilla/geckodriver/releases/latest
E           response headers:
E           {'Date': 'Sun, 28 Jun 2026 11:09:05 GMT', 'Server': 'Varnish', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'deny', 'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'", 'Access-Control-Allow-Origin': '*', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-RateLimit-Used, X-RateLimit-Resource, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset', 'Content-Type': 'application/json; charset=utf-8', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'X-GitHub-Media-Type': 'github.v3; format=json', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '0', 'X-RateLimit-Used': '60', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Reset': '1782645762', 'Content-Length': '280', 'X-GitHub-Request-Id': '3D76:3DA19B:10CCF896:1006ABF2:6A4100D1'}

..\AppData\Roaming\Python\Python313\site-packages\webdriver_manager\core\http.py:19: ValueError
========================================================== FAILURES ==========================================================
________________________________________ TestLoginPage.test_error_on_empty_login_form ________________________________________

self = <test_of_login_page.TestLoginPage object at 0x000001A6FD8A3250>
login_page = <pages.login_page.LoginPage object at 0x000001A6FD959090>

    def test_error_on_empty_login_form(self, login_page):
        """TC-10: Отображение ошибки с пустыми полями"""
        login_page.click_login_button_without_data()
>       error_text = login_page.get_error_message_text()

tests\test_of_login_page.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\login_page.py:22: in get_error_message_text
    return self.get_text(self.ERROR_MESSAGE)
pages\base_page.py:28: in get_text
    return self.wait.until(EC.visibility_of_element_located(locator)).text
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="aa34439f-72ff-4f95-853d-89f7207b1b7b")>
method = <function visibility_of_element_located.<locals>._predicate at 0x000001A6FD9654E0>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message:

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
_____________________________________________ TestMainPage.test_main_page_loads ______________________________________________

self = <test_of_main_page.TestMainPage object at 0x000001A6FD8A3390>
main_page = <pages.main_page.MainPage object at 0x000001A6FD95AAD0>

    def test_main_page_loads(self, main_page):
        """TC-01: Загрузка главной страницы"""
>       title_text = main_page.get_hero_title_text()

tests\test_of_main_page.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:15: in get_hero_title_text
    return self.get_text(self.HERO_TITLE)
pages\base_page.py:28: in get_text
    return self.wait.until(EC.visibility_of_element_located(locator)).text
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="ca10d036-23fc-4e95-8d6c-a143eafe8507")>
method = <function visibility_of_element_located.<locals>._predicate at 0x000001A6FDD5F9C0>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
___________________________________________ TestMainPage.test_go_to_templates_page ___________________________________________

self = <test_of_main_page.TestMainPage object at 0x000001A6FD8B9CD0>
main_page = <pages.main_page.MainPage object at 0x000001A6FD91F890>

    def test_go_to_templates_page(self, main_page):
        """TC-04: Навигация к странице шаблонов"""
>       templates_page = main_page.go_to_templates()

tests\test_of_main_page.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pages\main_page.py:18: in go_to_templates
    self.click(self.TEMPLATES_LINK)
pages\base_page.py:18: in click
    self.wait.until(EC.element_to_be_clickable(locator)).click()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <selenium.webdriver.support.wait.WebDriverWait (session="e033f618-b6a6-4e07-813c-04d561a6709e")>
method = <function element_to_be_clickable.<locals>._predicate at 0x000001A6FDD94360>, message = ''

    def until(self, method: Callable[[WebDriver], Union[Literal[False], T]], message: str = "") -> T:
        """Calls the method provided with the driver as an argument until the \
        return value does not evaluate to ``False``.
    
        :param method: callable(WebDriver)
        :param message: optional message for :exc:`TimeoutException`
        :returns: the result of the last call to `method`
        :raises: :exc:`selenium.common.exceptions.TimeoutException` if timeout occurs
        """
        screen = None
        stacktrace = None
    
        end_time = time.monotonic() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, "screen", None)
                stacktrace = getattr(exc, "stacktrace", None)
            time.sleep(self._poll)
            if time.monotonic() > end_time:
                break
>       raise TimeoutException(message, screen, stacktrace)
E       selenium.common.exceptions.TimeoutException: Message: 
E       Stacktrace:
E       RemoteError@chrome://remote/content/shared/RemoteError.sys.mjs:8:8
E       WebDriverError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:169:5
E       NoSuchElementError@chrome://remote/content/shared/webdriver/Errors.sys.mjs:538:5
E       dom.find/</<@chrome://remote/content/shared/DOM.sys.mjs:137:16

..\AppData\Roaming\Python\Python313\site-packages\selenium\webdriver\support\wait.py:101: TimeoutException
================================================== short test summary info ===================================================
FAILED tests/test_of_login_page.py::TestLoginPage::test_error_on_empty_login_form - selenium.common.exceptions.TimeoutException: Message:
FAILED tests/test_of_main_page.py::TestMainPage::test_main_page_loads - selenium.common.exceptions.TimeoutException: Message: 
FAILED tests/test_of_main_page.py::TestMainPage::test_go_to_templates_page - selenium.common.exceptions.TimeoutException: Message: 
ERROR tests/test_of_templates_page.py::TestTemplatesPage::test_templates_page_loads - selenium.common.exceptions.TimeoutException: Message: 
ERROR tests/test_of_templates_page.py::TestTemplatesPage::test_search_template_by_keyword - ValueError: response body:
ERROR tests/test_of_templates_page.py::TestTemplatesPage::test_project_report_template_is_displayed - ValueError: response body:
===================================== 3 failed, 4 passed, 3 errors in 214.31s (0:03:34)