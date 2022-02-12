import os
import time

from dotenv import load_dotenv
from browserManager import BrowserManager

load_dotenv()


class getDataFromInstagramComments:
    def __init__(self):
        with BrowserManager(os.getenv("SCRAP_URL")) as browser_manager:
            self.browser = browser_manager
            self.login()
            time.sleep(2)

    def login(self):
        username_input = self.browser.find_element_by_css_selector(
            "input[name='username']")

        password_input = self.browser.find_element_by_css_selector(
            "input[name='password']")

        username_input.send_keys(os.getenv("USER"))
        password_input.send_keys(os.getenv("PASS"))

        login_button = self.browser.find_element_by_xpath(
            "//button[@type='submit']")
        login_button.click()
