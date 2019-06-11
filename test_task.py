import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):

    @staticmethod
    def get_driver_path():
        current_dir = os.path.abspath(os.curdir)
        driver_name = 'chromedriver.exe'
        driver_path = os.path.join(current_dir, driver_name)
        return driver_path

    def get_into_frame(self):

        iframe = self.web_browser.find_element_by_name("iframe-sidebar-signup")
        self.web_browser.switch_to.frame(iframe)

    def setUp(self):
        executable_path = self.get_driver_path()
        self.web_browser = webdriver.Chrome(executable_path=executable_path)
        self.web_browser.implicitly_wait(8)  # seconds
        self.web_browser.maximize_window()
        self.good_email = "test_task_123@rambler.ru"
        self.good_password = "12345Qwert"

    def tearDown(self):
        self.web_browser.quit()

    def test_site_is_avaliable(self):
        self.web_browser.get("https://www.exness.com/")
        self.assertIn("Exness", self.web_browser.title)

    def test_login_succesfull(self):
        """
            Correct password and wrond e-mail
        """
        self.web_browser.get("https://www.exness.com/")

        header_signin = WebDriverWait(self.web_browser,
                                      5).until(EC.presence_of_element_located((By.ID, 'header-signin')))
        header_signin.click()

        email_field = ('signinlogin')
        email_field = WebDriverWait(self.web_browser,
                                    5).until(EC.presence_of_element_located((By.ID, email_field)))
        email_field.clear()
        email_field.send_keys(self.good_email)

        password = self.web_browser.find_element_by_id("signinPassword")
        password.clear()
        password.send_keys(self.good_password)

        button_login = self.web_browser.find_element_by_id("signin-form-button")
        button_login.click()

        header_signin = self.web_browser.find_elements_by_id("header-signin")
        self.assertTrue(len(header_signin) == 0)   # new page opened
        possible_urls_sp = ["https://www.exness.com/member/",
                            "https://www.exness.com/intl/ru/member/"]
        self.assertIn(self.web_browser.current_url, possible_urls_sp)

    def test_login_wrong_password_good_email(self):
        """
            Wrong password but good e-mail. Opened new page
        """
        self.web_browser.get("https://www.exness.com/")

        header_signin = WebDriverWait(self.web_browser,
                                      5).until(EC.presence_of_element_located((By.ID, 'header-signin')))
        header_signin.click()

        email_field = ('signinlogin')
        email_field = WebDriverWait(self.web_browser,
                                    5).until(EC.presence_of_element_located((By.ID, email_field)))
        email_field.clear()
        email_field.send_keys(self.good_email)

        password = self.web_browser.find_element_by_id("signinPassword")
        password.clear()
        password.send_keys(self.good_password*2)

        button_login = self.web_browser.find_element_by_id("signin-form-button")
        button_login.click()

        error_xpath = "//p[@class='txt-p txt-p__danger auth-error']"
        error_msg = self.web_browser.find_element_by_xpath(error_xpath)
        possible_error_message = ["Некорректный логин или пароль. Проверьте данные и попробуйте снова.",
                                  "No such login or password. Please check correctness and try again"]
        self.assertIn(error_msg.text.strip(), possible_error_message)

    def test_login_wrong_password_wrong_email(self):
        """
            Wrong password and wrond e-mail
        """
        self.web_browser.get("https://www.exness.com/")

        header_signin = WebDriverWait(self.web_browser,
                                      5).until(EC.presence_of_element_located((By.ID, 'header-signin')))
        header_signin.click()

        email_field = ('signinlogin')
        email_field = WebDriverWait(self.web_browser,
                                    5).until(EC.presence_of_element_located((By.ID, email_field)))
        email_field.clear()
        email_field.send_keys(self.good_email*2)

        password = self.web_browser.find_element_by_id("signinPassword")
        password.clear()
        password.send_keys(self.good_password*2)

        button_login = self.web_browser.find_element_by_id("signin-form-button")
        button_login.click()

        header_signin = self.web_browser.find_elements_by_id("header-signin")
        self.assertTrue(len(header_signin) == 1)  # the same page

    def test_login_good_password_wrong_email(self):
        """
            Good password but wrond e-mail
        """
        self.web_browser.get("https://www.exness.com/")

        header_signin = WebDriverWait(self.web_browser,
                                      5).until(EC.presence_of_element_located((By.ID, 'header-signin')))
        header_signin.click()

        email_field = ('signinlogin')
        email_field = WebDriverWait(self.web_browser,
                                    5).until(EC.presence_of_element_located((By.ID, email_field)))
        email_field.clear()
        email_field.send_keys(self.good_email * 2)

        password = self.web_browser.find_element_by_id("signinPassword")
        password.clear()
        password.send_keys(self.good_password)

        button_login = self.web_browser.find_element_by_id("signin-form-button")
        button_login.click()

        header_signin = self.web_browser.find_elements_by_id("header-signin")
        self.assertTrue(len(header_signin) == 1)  # the same page


if __name__ == '__main__':
    unittest.main()
