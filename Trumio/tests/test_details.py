from selenium import webdriver
import pytest
import logging
from functions.login_page import LoginPage
from functions.products_page import ProductsPage
from functions.checkout_page import CheckoutPage
from utils.helpers import Utils

config = Utils.load_config()
username_password = config['credentials']
link = config['host_name']['host']

@pytest.mark.suite7
class TestDetails:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.log = Utils.custom_logger(logLevel=logging.INFO, log_file_name=f"{self.__class__.__name__}.log")
        self.login_page = LoginPage(self.driver, self.log)
        self.products_page = ProductsPage(self.driver, self.log)
        self.checkout_page = CheckoutPage(self.driver, self.log)
        # self.driver.maximize_window()  

    def test_details(self):
        self.log.info("Starting the test_details test.")

        for username in username_password.keys():
            password = username_password[username]
            self.log.info(f"Testing username: {username}")

            try:
                self.driver.get(link)
                self.login_page.login(username, password)

                # Added an assertion to check if login was successful or failed
                if self.login_page.is_login_successful():
                    self.products_page.open_cart()
                    self.checkout_page.enter_personal_details('Ayush', 'Anand', '201301')
                else:
                    self.log.error(f"Login failed for user: {username}. Invalid credentials or locked user")

            except Exception as e:
                self.log.error(f"An error occurred: {str(e)}")

            finally:
                # Close the current browser instance
                self.driver.quit()

                # Reinitialize the WebDriver and pages for the next iteration
                self.driver = webdriver.Chrome()  # Reinitialize WebDriver
                self.login_page = LoginPage(self.driver, self.log)
                self.products_page = ProductsPage(self.driver, self.log)

                self.log.info("Finished the test_details test.")
