import unittest
from handler import *


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.web_browser = get_web_browser()
        self.url_main_page = "https://www.exness.com/"
        self.title_main_page = "Exness"
        self.good_email = "test_task_123@rambler.ru"
        self.good_password = "12345Qwert"

    def tearDown(self):
        self.web_browser.quit()

    def test_site_is_avaliable(self):
        """
            Main page open correctly
        """
        open_page(self.web_browser, self.url_main_page)
        self.assertIn(self.title_main_page, self.web_browser.title)

    def test_login_succesfull(self):
        """
            Verify if a user will be able to login with
            a valid email and valid password
        """
        open_page(self.web_browser, self.url_main_page)
        focus_on_header_signin(self)
        put_email(self.web_browser, self.good_email)
        put_password(self.web_browser, self.good_password)
        push_login_button(self.web_browser)

        header_signin = self.web_browser.find_elements_by_id("header-signin")
        self.assertTrue(len(header_signin) == 0)   # new page opened
        possible_urls_sp = ["https://www.exness.com/member/",
                            "https://www.exness.com/intl/ru/member/"]
        self.assertIn(self.web_browser.current_url, possible_urls_sp)

    def test_login_wrong_password_wrong_email(self):
        """
            Verify if a user cannot login with
            an invalid email and an invalid password.
        """
        open_page(self.web_browser, self.url_main_page)
        focus_on_header_signin(self)
        put_email(self.web_browser, self.good_email*2)
        put_password(self.web_browser, self.good_password * 2)
        push_login_button(self.web_browser)

        header_signin = self.web_browser.find_elements_by_id("header-signin")
        self.assertTrue(len(header_signin) == 1)  # the same page

    def test_login_wrong_password_good_email(self):
        """
            Verify if a user cannot login with
            a valid username and an invalid password.
        """
        open_page(self.web_browser, self.url_main_page)
        focus_on_header_signin(self)
        put_email(self.web_browser, self.good_email)
        put_password(self.web_browser, self.good_password*2)
        push_login_button(self.web_browser)

        error_xpath = "//p[@class='txt-p txt-p__danger auth-error']"
        error_msg = self.web_browser.find_element_by_xpath(error_xpath)
        possible_error_message = ["Некорректный логин или пароль. Проверьте данные и попробуйте снова.",
                                  "No such login or password. Please check correctness and try again"]
        self.assertIn(error_msg.text.strip(), possible_error_message)

    def test_login_good_password_wrong_email(self):
        """
            Verify if a user cannot login with
             an invalid email and an valid password.
        """
        open_page(self.web_browser, self.url_main_page)
        focus_on_header_signin(self)
        put_email(self.web_browser, self.good_email)
        put_password(self.web_browser, self.good_password * 2)
        push_login_button(self.web_browser)

        header_signin = self.web_browser.find_elements_by_id("header-signin")
        self.assertTrue(len(header_signin) == 1)  # the same page


if __name__ == '__main__':
    unittest.main()
