import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@pytest.fixture(scope="module")
def browser():
    # Setup Chrome options
    logger.info("Step 1: Open the browser")
    print("Step 1: Open the browser")
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
    
    
def test_successful_login(browser: WebDriver):
    """Authentication: Valid Login Test"""
    print("Authentication: Valid Login Test called")
    # Test data
    username = "standard_user"
    password = "secret_sauce"

    logger.info("Step 2: navigate to login page")
    # Navigate to login page
    browser.get("https://www.saucedemo.com/")

    # Example: wait up to 10 seconds for an element to be visible
    wait = WebDriverWait(browser, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    logger.info("Step 3: Input username")

    # Enter credentials and login
    usernamefield = browser.find_element(By.ID,"user-name")
    usernamefield.send_keys(username)

    time.sleep(2)
    logger.info("Step 4: Input password")

    passwordfield = browser.find_element(By.XPATH, "//input[@id='password']")
    passwordfield.send_keys(password)

    logger.info("Step 5: Click login button")

    time.sleep(2)
    loginButton = browser.find_element(By.ID, "login-button")
    loginButton.click()

    time.sleep(2)

    # Verify successful login
    assert "inventory" in browser.current_url


def test_add_to_cart(browser: WebDriver):
    """Add to Cart Test"""
    
    browser.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)
    logger.info("Step 6: Add to cart")
    items_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket"
    ]
    for item in items_to_add:
        add_to_cart_button = browser.find_element(By.ID, f"add-to-cart-{item}")
        add_to_cart_button.click()
    time.sleep(2)
    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    if cart_icon:
        counter = cart_icon.text
        assert counter == "4"
        print("Items successfully added to the cart.")


def test_checkout(browser: WebDriver):
    """Checkout Test"""
    browser.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)
    logger.info("Step 7: Proceed to checkout")
    checkout_button = browser.find_element(By.ID, "checkout").click()
    time.sleep(2)
    first_name = browser.find_element(By.ID, "first-name").send_keys("Najifa")
    last_name = browser.find_element(By.ID, "last-name").send_keys("Esha")
    postal_code = browser.find_element(By.ID, "postal-code").send_keys("12345")
    continue_button = browser.find_element(By.ID, "continue").click()
    time.sleep(2)
    finish_button = browser.find_element(By.ID, "finish").click()
    time.sleep(2)
    back_home_button = browser.find_element(By.ID, "back-to-products").click()
    time.sleep(2)
    #assert "inventory" in browser.current_url
    
    
def test_remove_from_cart(browser: WebDriver):
    """Remove from Cart Test"""
    browser.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)
    logger.info("Step 8: Remove items from cart")
    # List of items to add
    items_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "test.allthethings()-t-shirt-(red)"
    ]
    # Add items to cart
    for item in items_to_add:
        add_to_cart_button = browser.find_element(By.ID, f"add-to-cart-{item}")
        add_to_cart_button.click()
    time.sleep(2)
    # List of items to remove
    items_to_remove = [
        "sauce-labs-backpack"
    ]
    for item in items_to_remove:
        remove_button = browser.find_element(By.ID, f"remove-{item}")
        remove_button.click()
    time.sleep(2)
    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    if cart_icon:
        counter = cart_icon.text
        assert counter == str(len(items_to_add) - len(items_to_remove))
        print("Item(s) successfully removed from the cart.")
    
    
def test_remove_from_checkout(browser: WebDriver):
    """Remove from Cart Test"""
    
    browser.get("https://www.saucedemo.com/inventory.html")
    time.sleep(2)
    logger.info("Step 6: Add to cart")
    items_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket"
    ]
    for item in items_to_add:
        add_to_cart_button = browser.find_element(By.ID, f"add-to-cart-{item}")
        add_to_cart_button.click()
    time.sleep(2)

    browser.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)
    # List of items to remove
    items_to_remove = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light"
    ]
    for item in items_to_remove:
        remove_button = browser.find_element(By.ID, f"remove-{item}")
        remove_button.click()
    time.sleep(2)
    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    if cart_icon:
        counter = cart_icon.text
        assert counter == str(len(items_to_add) - len(items_to_remove))
        print("Item(s) successfully removed from the cart.")