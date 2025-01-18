from time import sleep
from auto_imports import *
from helpers import login
from locators import DEPARTMENTS_BUTTON



username = os.getenv("ETDEV1")
password = os.getenv("ETDEV1P")
if not username or not password:
    raise ValueError("Username or Password environment variable is not set.")
driver = e_driver()
login(driver, username, password)

print("Current URL after login:", driver.current_url)
print("Current Page Title:", driver.title)

# Ensure the page is fully loaded
WebDriverWait(driver, 10).until(EC.title_contains("ETEPS"))
assert "ETEPS" in driver.title, "Page title is incorrect"

# Print cookies to ensure session is established
print("Cookies after login:")
for cookie in driver.get_cookies():
    print(cookie)

sleep(10)
# Navigate to the "teams" page

try:
    driver.find_element(*DEPARTMENTS_BUTTON).click()
except Exception as e:
    print (f"Error while navigating to 'teams': {e}")
#print("URL after navigation:", driver.current_url)




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