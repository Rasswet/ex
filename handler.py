import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver_path():
    current_dir = os.path.abspath(os.curdir)
    driver_name = 'chromedriver.exe'
    driver_path = os.path.join(current_dir, driver_name)
    return driver_path


def get_web_browser():
    executable_path = get_driver_path()
    web_browser = webdriver.Chrome(executable_path=executable_path)
    web_browser.implicitly_wait(8)  # seconds
    web_browser.maximize_window()
    return web_browser


def open_page(web_browser, url_to_open):
    web_browser.get(url_to_open)


def get_into_frame(self):
    iframe = self.web_browser.find_element_by_name("iframe-sidebar-signup")
    self.web_browser.switch_to.frame(iframe)


def focus_on_header_signin(self):
    header_signin = WebDriverWait(self.web_browser,
                                  5).until(EC.presence_of_element_located((By.ID, 'header-signin')))
    header_signin.click()


def put_email(web_browser, email):
    email_field = ('signinlogin')
    email_field = WebDriverWait(web_browser,
                                5).until(EC.presence_of_element_located((By.ID, email_field)))
    email_field.clear()
    email_field.send_keys(email)


def put_password(web_browser, password):
    password_element = web_browser.find_element_by_id("signinPassword")
    password_element.clear()
    password_element.send_keys(password)


def push_login_button(web_browser):
    button_login = web_browser.find_element_by_id("signin-form-button")
    button_login.click()
