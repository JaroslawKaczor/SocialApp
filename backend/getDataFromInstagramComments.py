import os
import time
import pdb

from dotenv import load_dotenv
from browserManager import BrowserManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


class getDataFromInstagramComments:
    def __init__(self):
        with BrowserManager(os.getenv("SCRAP_URL")) as browser_manager:
            self.browser = browser_manager
            self.close_modal_accept_cookie()
            self.login()
            self.close_modal_save_login()

    def close_modal_accept_cookie(self):
        self.browser.find_element_by_xpath(
            "//*[contains(text(), 'Allow Essential')]").click()

        wait(self.browser, 10).until_not(
            EC.visibility_of_element_located((By.XPATH, '//div[@role="presentation"]')))

    def login(self):
        username_input = self.browser.find_element_by_css_selector(
            "input[name='username']")

        password_input = self.browser.find_element_by_css_selector(
            "input[name='password']")

        username_input.send_keys(os.getenv("USERNAME"))
        password_input.send_keys(os.getenv("PASSWORD"))

        login_button = self.browser.find_element_by_xpath(
            "//button[@type='submit']")
        login_button.click()

    def close_modal_save_login(self):
        wait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Save your login information?')]")))
        self.browser.find_element_by_xpath(
            "//button[contains(text(), 'Not now')]").click()
