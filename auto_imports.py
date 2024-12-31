from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


options = Options()
options.add_argument("--start-maximized") #maximizing the window
#options.add_experimental_option("detach", True) (if u want to detach the browser after execution to allow debugging without impacting the browser session)

def e_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
