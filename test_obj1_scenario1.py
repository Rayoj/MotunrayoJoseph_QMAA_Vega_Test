import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# These class config are Constants which is why I made them a class
class Config:
    BASE_URL = "https://www.saucedemo.com/v1/index.html"
    USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
    PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    WAIT_TIME = 5  # Wait time in seconds

#These are the Locators. I created them here for manageability purposes and to avoid Hardcoded Strings.
class Locators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

# Page Object Model (POM)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*Locators.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        time.sleep(Config.WAIT_TIME)  # Wait for page transition

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_by_lowest_price(self):
        sort_dropdown = self.driver.find_element(*Locators.SORT_DROPDOWN)
        Select(sort_dropdown).select_by_value("lohi")
        time.sleep(Config.WAIT_TIME)  # Allow sorting to take effect

    def verify_sorted_prices(self):
        item_prices = self.driver.find_elements(*Locators.ITEM_PRICES)
        prices = [float(price.text.replace("$", "")) for price in item_prices]
        assert prices == sorted(prices), "Sorting failed: Prices are not in ascending order"
        print("Test Passed: Sorting verified successfully!")

# Test Execution Function
def test_sort_products(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # Specify ChromeDriver path explicitly
    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get("https://www.saucedemo.com/v1/index.html")
    driver.maximize_window()

    # (Continue with login and test steps...)
     # Perform login
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    # Sort products and verify
    products_page = ProductsPage(driver)
    products_page.sort_by_lowest_price()
    products_page.verify_sorted_prices()
    driver.quit()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Selenium Test in Headed or Headless Mode")
    parser.add_argument("--headless", action="store_true", help="Run tests in headless mode")
    args = parser.parse_args()
    test_sort_products(headless=args.headless)




    # Headless mode instructions

    # To run this Selenium test in headless mode through the console, follow these steps:

    # Prerequisites
    # Install Python (if not installed)

    # Ensure you have Python installed. You can check by running:
    # python --version

    # If python is not installed, download it from python.org.

    # Install Required Dependencies.

    # Install Selenium and any required packages using pip:

    # pip install selenium
    # Ensure Chrome and ChromeDriver are Installed.

    # Steps to run the test in headless mode.

    # 1. Open the console
    # On Windows: Open Command Prompt (cmd)
    # On macOS/Linux: Open Terminal

    # 2. Navigate to the script's directory
    # Use cd to go to the folder where your script is located.

    # 3. Run the test in headless mode
    # Execute the following command:

    # e.g., python obj1_scenario1.py --headless (you should replace with the actual file name.)

    # If the test passes, you will see:
    # Test Passed: Sorting verified successfully!

    # If it fails, an AssertionError will be displayed, indicating the issue.


