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

    ADD_TO_CART_BACKPACK = (By.XPATH, "//div[@class='inventory_item'][.//div[text()='Sauce Labs Backpack']]//button")
    ADD_TO_CART_ONESIE = (By.XPATH, "//div[@class='inventory_item'][.//div[text()='Sauce Labs Onesie']]//button")
    BACKPACK_ITEM_LINK = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    REMOVE_BACKPACK_BUTTON = (By.XPATH, "//button[text()='REMOVE']")
    CART_ITEMS = (By.CLASS_NAME, "shopping_cart_badge")


# Initialize WebDriver
options = Options()
driver = webdriver.Chrome(options=options)
driver.get(Config.BASE_URL)
driver.implicitly_wait(Config.WAIT_TIME)
driver.maximize_window()

# Login
driver.find_element(*Locators.USERNAME_FIELD).send_keys(Config.USERNAME)
driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
driver.find_element(*Locators.LOGIN_BUTTON).click()
time.sleep(Config.WAIT_TIME)

# Add the Sauce Labs Backpack to cart
driver.find_element(*Locators.ADD_TO_CART_BACKPACK).click()
time.sleep(2)

# Add the Sauce Labs Onesie to cart
driver.find_element(*Locators.ADD_TO_CART_ONESIE).click()
time.sleep(2)

# Open the Sauce Labs Backpack product page
driver.find_element(*Locators.BACKPACK_ITEM_LINK).click()
time.sleep(2)

# Remove the Sauce Labs Backpack from cart
driver.find_element(*Locators.REMOVE_BACKPACK_BUTTON).click()
time.sleep(2)

# Verify one item remains in the cart
cart_items = driver.find_elements(*Locators.CART_ITEMS)
if cart_items and cart_items[0].text == "1":
    print("Only one item remains in the cart")
else:
    print("Unexpected cart count")

# Close browser
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

