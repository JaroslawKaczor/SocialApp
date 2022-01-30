import time
from browserManager import BrowserManager

with BrowserManager("http://www.instagram.com") as browser:
    time.sleep(5)
