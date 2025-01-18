from auto_imports import *
from locators import LOGIN_USERNAME, LOGIN_PASSWORD, LOGIN_BUTTON

def login(driver, username, password):
    """
    Logs into the ETEPS Dev Website.
    :param driver: Selenium WebDriver instance
    :param username: Username for dev login
    :param password: Password for dev login
    """

    driver.get("https://dev.eteps.co")
    time.sleep(2)
    driver.find_element(*LOGIN_USERNAME).send_keys(username)
    driver.find_element(*LOGIN_PASSWORD).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_changes("https://dev.eteps.co"))

    print("Successfully logged in to", driver.title, "develop")