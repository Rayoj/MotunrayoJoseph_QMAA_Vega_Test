### Selenium Test Automation for SauceDemo

## Overview
This project contains a series of automated tests using Selenium WebDriver to interact with the SauceDemo application. The scripts cover the following scenarios:

1. **Login and Sort Products**: This script performs login and sorts products by price.
2. **Add to Cart and Remove Items**: This script tests adding products to the cart and removing items.
3. **End-to-End Test (Login, Add to Cart, Shipping, and Checkout)**: This script tests the entire user journey from login to checkout.
4. **End-to-End Test (Login and Logout)**: This script verifies logging in and logging out functionality.

## Documentation and Reports

[Manual Test cases/Bug Reports](https://docs.google.com/spreadsheets/d/1BBfHc9QDRFo4FEbQ5YbqyA8LUGy4udS0DXHnpLA0sFg/edit?gid=1629745064#gid=1629745064)


- [Automation Test Cases/Bug Reports] (https://docs.google.com/spreadsheets/d/1IKDhQWKng5LtuXNTvAxaXQNKsYYi9WTOmlwAxm4CRpk/edit?gid=1629745064#gid=1629745064)

- [Test Report] (https://docs.google.com/document/d/1ZJFGSeQVNEcTtbmf7CP6O0I-25I6zcNyUPIH4V2q8Xs/edit?tab=t.0)

## Test Coverage
The test suite covers the following functionalities of the SauceDemo website:

1. **Login**
- Verify login functionality with valid credentials.
- Verify login with invalid credentials.
- Verify redirection to the products page after successful login.
- Verify that the user cannot log in with empty fields.

2. **Product Sorting**
- Verify sorting products by price (low to high).
- Verify sorting products by price (high to low).
- Verify sorting products by name (A-Z).
- Verify sorting products by name (Z-A).

3. **Add to Cart and Remove Items**
- Verify adding products to the cart.
- Verify removing items from the cart.
- Verify cart reflects the correct count of items.
- Verify the total price is updated correctly when an item is added or removed.

4. **Checkout Process**
- Verify entering shipping information.
- Verify order confirmation after successful checkout.
- Verify the cart is empty after checkout.

5. **Logout**
- Verify that the user can log out successfully.
- Verify that the user is redirected to the login page after logout.
- Verify that session data is cleared after logout.

**Requirements**
- Python 3.x
- Selenium WebDriver
- ChromeDriver
- Google Chrome (for WebDriver)
- Installation
- Install Python and Selenium via pip:

```bash
pip install selenium
```
<Note>
Download ChromeDriver and ensure it is accessible in your PATH or specify the path directly in the scripts.
</Note>

## Test Scripts

1. Login and Sort Products
This test script automates the login process for the SauceDemo website and verifies that the products are sorted by price in ascending order.

**How to run:**

```bash
python login_sort_products.py --headless  # Run in headless mode
```

2. Add to Cart and Remove Items
This script tests the addition of products to the cart and their removal. It ensures that after removing an item, only one product remains in the cart.

**How to run:**

```bash
python add_to_cart_remove.py
```

3. End-to-End Test (Login, Add to Cart, Shipping, and Checkout)
This script automates the end-to-end process from logging in to the checkout page, entering shipping details, and confirming the order.

**How to run:**

```bash
python end_to_end_checkout.py
```

4. End-to-End Test (Login and Logout)
This script automates the login and logout process for the SauceDemo website and verifies that the user is redirected to the login page after logout.

**How to run:**

```bash
python login_logout.py
```

## Headless Mode Configuration

To run the tests in headless mode, you need to add an argument for running the tests in the background without the GUI of the browser. In all the scripts, you can include the --headless flag to run the tests in headless mode, which is useful for continuous integration environments or when you don't need the browser's graphical interface.


Author

**Motunrayo Joseph**


