from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
INVALID_PASSWORD = "wrong_password"

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    return driver

def test_valid_login():
    driver = setup_driver()
    wait = WebDriverWait(driver, 10)




