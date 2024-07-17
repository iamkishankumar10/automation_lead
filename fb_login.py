import requests
import json
from bs4 import BeautifulSoup

import pandas as pd
import ast
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException, TimeoutException

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from chromedriver_py import binary_path
chrome_driver_path = r"C:\Users\kishan.kumar_tyreple\Desktop\chromedriver.exe"
fb_website = "https://business.facebook.com/latest/instant_forms/forms?asset_id=334167367265607&business_id=1055428358578694&nav_id=2416062922&nav_ref=bizweb_landing_fb_login_button&biz_login_source=bizweb_landing_fb_login_button"
driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path))
driver.get(fb_website)
WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="login-panel-container"]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/span/span'))).click()
# Find the username and password fields
username_input = driver.find_element(By.ID, 'email')
password_input = driver.find_element(By.ID, 'pass')

# Enter your Facebook credentials
username_input.send_keys('9560417569')
password_input.send_keys('Kishan@10')

# Submit the form
password_input.send_keys(Keys.RETURN)

# Wait for login to process
time.sleep(10)

two_factor_input = driver.find_element(By.XPATH, '//input[@name="approvals_code"]')
# Enter the 2FA code
two_factor_input.send_keys(input())
two_factor_input.send_keys(Keys.RETURN)

# Wait for the 2FA process to complete
time.sleep(5)

WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH ,'/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/div[2]/div[1]/label/span'))).click()
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="checkpointSubmitButton"]'))).click()

