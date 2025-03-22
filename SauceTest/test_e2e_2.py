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
    WAIT_TIME = 3 # Wait time in seconds

# These are the Locators. I created them here for manageability purposes and to avoid hardcoded strings.
class Locators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    MENU_BUTTON = (By.XPATH, "//button[contains(text(), 'Open Menu')]")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

# Page Object Model (POM)
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*Locators.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        time.sleep(Config.WAIT_TIME)

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.find_element(*Locators.MENU_BUTTON).click()
        time.sleep(1)  # Allow menu to open
        self.driver.find_element(*Locators.LOGOUT_LINK).click()
        time.sleep(Config.WAIT_TIME)

    def is_on_login_page(self):
        return self.driver.current_url == Config.BASE_URL

# Main Test Execution
if __name__ == "__main__":
    # Set up WebDriver
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)
    driver.maximize_window()

    # Login
    login_page = LoginPage(driver)
    login_page.login(Config.USERNAME, Config.PASSWORD)

    # Logout
    logout_page = LogoutPage(driver)
    logout_page.logout()

    # Verify Redirection to Login Page
    assert logout_page.is_on_login_page(), "Logout failed! User is not redirected to the login page."

    print("Test Passed: Successfully logged in and logged out.")

    # Close Browser
    driver.quit()





   