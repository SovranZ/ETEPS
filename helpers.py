from auto_imports import *


def login(driver, username, password):
    """
    Logs into the ETEPS Dev Website.
    :param driver: Selenium WebDriver instance
    :param username: Username for dev login
    :param password: Password for dev login
    """

    driver.get("https://dev.eteps.co")
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "/html/body/app-root/div/div/app-login/div/div[1]/div[1]/form/mat-form-field[1]/div[1]/div/div[2]/input").send_keys(
        username)  # Replace 'username' with the actual ID or locator
    driver.find_element(By.XPATH,
                        "/html/body/app-root/div/div/app-login/div/div[1]/div[1]/form/mat-form-field[2]/div[1]/div/div[2]/input").send_keys(
        password)  # Replace 'password' with the actual ID or locator

    driver.find_element(By.XPATH, "/html/body/app-root/div/div/app-login/div/div[1]/div[1]/div[2]/button").click()
    WebDriverWait(driver, 10).until(EC.url_changes("https://dev.eteps.co"))

    print("Successfully logged in to", driver.title, "develop")
