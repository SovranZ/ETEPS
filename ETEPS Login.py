from time import sleep

from auto_imports import *
from helpers import login

username = os.getenv("ETDEV1")
password = os.getenv("ETDEV1P")
driver = e_driver()
login(driver,username, password)


WebDriverWait(driver, 10).until(EC.title_contains("overview"))
assert "overview" in driver.title, "Page title is incorrect"
#driver.get("https://dev.eteps.co/main-module/teams?limit=10")
sleep(10)


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Wait for the username field to be visible
# username_field = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.ID, "username"))
# ) ---> better waiting enhancement



#try


#except Exception as e:
#    print("An error occurred:", e)

#finally:
#    pass
    #driver.quit() (comment pass and uncomment this line if u want the driver to quit after execution, otherwise you will allow impacting the browser through coding after execution)


