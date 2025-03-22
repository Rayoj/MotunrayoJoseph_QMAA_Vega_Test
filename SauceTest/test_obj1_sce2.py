import os
import time
import pytest
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


