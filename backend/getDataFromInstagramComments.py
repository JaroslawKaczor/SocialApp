import time
from browserManager import BrowserManager

MAIN_URL = "http://www.instagram.com"


class getDataFromInstagramComments:
    def __init__(self):
        with BrowserManager(MAIN_URL) as browser_manager:
            self.browser = browser_manager
            self.login()
            time.sleep(2)

    def login(self):
        username_input = self.browser.find_element_by_css_selector(
            "input[name='username']")

        password_input = self.browser.find_element_by_css_selector(
            "input[name='password']")

        username_input.send_keys("LOGIN")
        password_input.send_keys("PASSWORD")

        login_button = self.browser.find_element_by_xpath(
            "//button[@type='submit']")
        login_button.click()
