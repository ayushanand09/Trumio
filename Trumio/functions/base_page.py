from selenium.webdriver.support.ui import WebDriverWait
import time

class BasePage:
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.wait = WebDriverWait(driver, 10)