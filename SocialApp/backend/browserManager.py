import string
import traceback
from selenium import webdriver
import chromedriver_autoinstaller


class BrowserManager:
    def __init__(self, website):
        self.website = website

    def __enter__(self):
        self.install_chrome_driver()
        self.open_browser(self.website)

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

        self.close_browser()
        return True

    def install_chrome_driver(self):
        chromedriver_autoinstaller.install()

    def open_browser(self, website: string):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=chrome_options)
        self.browser = webdriver.Chrome()
        self.browser.get(website)
        return self.browser

    def close_browser(self):
        self.browser.close()
