import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Constants
class Config:
    BASE_URL = "https://www.saucedemo.com/v1/index.html"
    USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
    PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    WAIT_TIME = 3  # Wait time in seconds

# These are the Locators. I created them here for manageability purposes.
class Locators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn_primary') and contains(@class, 'btn_inventory')]")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout_button")
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CLASS_NAME, "cart_button")
    FINISH_BUTTON = (By.CLASS_NAME, "btn_action.cart_button")
    ORDER_CONFIRMATION = (By.CLASS_NAME, "complete-header")


# Page Object Model
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*Locators.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        time.sleep(Config.WAIT_TIME)

# Checkout Process
class CheckoutProcess:
    def __init__(self, driver):
        self.driver = driver

# Add an item to cart.

    def add_to_cart(self):
        self.driver.find_element(*Locators.ADD_TO_CART_BUTTON).click()
        time.sleep(Config.WAIT_TIME)

# Proceed to checkout by clicking the cart icon.
    def proceed_to_checkout(self):
        self.driver.find_element(*Locators.CART_BUTTON).click()
        time.sleep(Config.WAIT_TIME)
        self.driver.find_element(*Locators.CHECKOUT_BUTTON).click()
        time.sleep(Config.WAIT_TIME)

# Enter your shipping details.
    def enter_shipping_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*Locators.FIRST_NAME_FIELD).send_keys(first_name)
        self.driver.find_element(*Locators.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(*Locators.POSTAL_CODE_FIELD).send_keys(postal_code)
        self.driver.find_element(*Locators.CONTINUE_BUTTON).click()
        time.sleep(Config.WAIT_TIME)

# Click the FINISH button to checkout.
    def finish_checkout(self):
        self.driver.find_element(*Locators.FINISH_BUTTON).click()
        time.sleep(Config.WAIT_TIME)

# Verify order confirmation by getting the "thank you for your order" message.
    def verify_order_confirmation(self):
        confirmation_text = self.driver.find_element(*Locators.ORDER_CONFIRMATION).text
        return confirmation_text == "THANK YOU FOR YOUR ORDER"


# Test Execution
options = Options()
driver = webdriver.Chrome(options=options)
driver.get(Config.BASE_URL)
driver.maximize_window()

test_login = LoginPage(driver)
test_login.login(Config.USERNAME, Config.PASSWORD)

test_checkout = CheckoutProcess(driver)
test_checkout.add_to_cart()
test_checkout.proceed_to_checkout()
test_checkout.enter_shipping_info("Ray", "Janet", "800001")
test_checkout.finish_checkout()

assert test_checkout.verify_order_confirmation(), "Order confirmation message not found!"
print("Test Passed: ✅Order confirmation message found!")

driver.quit()


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

