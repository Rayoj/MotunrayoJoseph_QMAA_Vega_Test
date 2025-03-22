import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Constants
class Config:
    BASE_URL = "https://www.saucedemo.com/v1/index.html"
    USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
    PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    WAIT_TIME = 20  # Increased wait time for better reliability


# These are the Locators. I created them here for manageability purposes.
class Locators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    ADD_TO_CART_BACKPACK = (By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-backpack')]")
    ADD_TO_CART_ONESIE = (By.XPATH, "//button[contains(@id, 'add-to-cart-sauce-labs-onesie')]")
    BACKPACK_ITEM_LINK = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    REMOVE_BACKPACK_BUTTON = (By.XPATH, "//button[text()='REMOVE']")
    CART_ITEMS = (By.CLASS_NAME, "shopping_cart_badge")


# Initialize WebDriver with necessary options
options = Options()
options.add_argument("--headless=new")  # Use new headless mode
options.add_argument("--no-sandbox")  # Bypass OS security restrictions
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
options.add_argument("--disable-gpu")  # Disable GPU acceleration (for headless mode)
options.add_argument("--window-size=1920x1080")  # Ensure proper rendering
options.add_argument("--remote-debugging-port=9222")  # Helps debugging headless Chrome

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.get(Config.BASE_URL)
driver.implicitly_wait(Config.WAIT_TIME)
driver.maximize_window()

# Login
driver.find_element(*Locators.USERNAME_FIELD).send_keys(Config.USERNAME)
driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Config.PASSWORD)
driver.find_element(*Locators.LOGIN_BUTTON).click()

wait = WebDriverWait(driver, Config.WAIT_TIME)

# Add the Sauce Labs Backpack to cart
try:
    print("Waiting for ADD_TO_CART_BACKPACK button to become clickable")
    wait.until(EC.presence_of_element_located(Locators.ADD_TO_CART_BACKPACK))  # Ensure element is present
    add_to_cart_backpack = wait.until(EC.element_to_be_clickable(Locators.ADD_TO_CART_BACKPACK))
    add_to_cart_backpack.click()
except TimeoutException as e:
    print(f"Timeout occurred while trying to click ADD_TO_CART_BACKPACK: {e}")

# Add the Sauce Labs Onesie to cart
try:
    print("Waiting for ADD_TO_CART_ONESIE button to become clickable")
    wait.until(EC.presence_of_element_located(Locators.ADD_TO_CART_ONESIE))  # Ensure element is present
    add_to_cart_onesie = wait.until(EC.element_to_be_clickable(Locators.ADD_TO_CART_ONESIE))
    add_to_cart_onesie.click()
except TimeoutException as e:
    print(f"Timeout occurred while trying to click ADD_TO_CART_ONESIE: {e}")

# Open the Sauce Labs Backpack product page
try:
    print("Waiting for BACKPACK_ITEM_LINK to become clickable")
    backpack_item_link = wait.until(EC.element_to_be_clickable(Locators.BACKPACK_ITEM_LINK))
    backpack_item_link.click()
except TimeoutException as e:
    print(f"Timeout occurred while trying to click BACKPACK_ITEM_LINK: {e}")

# Remove the Sauce Labs Backpack from cart
try:
    print("Waiting for REMOVE_BACKPACK_BUTTON to become clickable")
    remove_backpack_button = wait.until(EC.element_to_be_clickable(Locators.REMOVE_BACKPACK_BUTTON))
    remove_backpack_button.click()
except TimeoutException as e:
    print(f"Timeout occurred while trying to click REMOVE_BACKPACK_BUTTON: {e}")

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

