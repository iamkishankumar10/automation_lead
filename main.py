from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import re

import pandas as pd

from unidecode import unidecode
binary_path = r"chromedriver.exe"
fb_website = "https://business.facebook.com/latest/instant_forms/forms?asset_id=334167367265607&business_id=1055428358578694&nav_id=2416062922&nav_ref=bizweb_landing_fb_login_button&biz_login_source=bizweb_landing_fb_login_button"
download_folder = r"Downloads"

vehicle_make_4w = pd.read_csv("vehicle_make_4w.csv")
vehicle_model_4w = pd.read_csv("vehicle_model_4w.csv")

vehicle_make_2w = pd.read_csv("vehicle_make_2w.csv")
vehicle_model_2w = pd.read_csv("vehicle_model_2w.csv")

city_name = pd.read_csv("city_name.csv")
pincode_city_id = pd.read_csv("pincode_city_id.csv")
city_id_pincode = pd.read_csv("city_id_pincode.csv")

vehicle_makes = pd.read_csv("vehicle_makes.csv")
vehicle_models = pd.read_csv("vehicle_models.csv")


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import schedule
from selenium import webdriver
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
service = Service(binary_path)
driver = webdriver.Chrome(service=service, options=opt)

from all_lead_campaign_function import campaign_function_1
from all_lead_campaign_function import campaign_function_2
from all_lead_campaign_function import campaign_function_3
from all_lead_campaign_function import campaign_function_4



fb_campaigns = [
    {
        'campaign_form_id': '1097911688065321',
        'campaign_form_name': "Feb'24 Two Wheeler Leads-1",
        'status': 0,
        # 'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[1]/td[7]/div/div/div/span/div/div/div",
        'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/span/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[1]/td[7]/div/div/div/span/div/div/div",
        'campaign_function': campaign_function_1
    },
    {
        'campaign_form_id': '359375497058054',
        'campaign_form_name': "Feb'24 Two Wheeler Leads",
        'status': 0,
        # 'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[7]/div/div/div/span/div/div/div",
        'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/span/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[2]/td[7]/div/div/div/span/div/div/div",
        'campaign_function': campaign_function_2
    },
    {
        'campaign_form_id': '2706608299492753',
        'campaign_form_name': "15-17 Inch Tyres-Jan'24-Lead-From",
        'status': 1,
        # 'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[3]/td[7]/div/div/div/span/div/div/div",
        # 'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/span/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[6]/td[7]/div/div/div/span/div/div/div",
        'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/span/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[3]/td[7]/div/div/div/span/div/div/div",
        'campaign_function': campaign_function_3
    },
    {
        'campaign_form_id': '383639434140484',
        'campaign_form_name': "Jan'24-Lead Form",
        'status': 0,
        # 'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[4]/td[7]/div/div/div/span/div/div/div",
        'campaigns_download_button_xpath' : "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/span/div/div/div[1]/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/table/tbody[1]/tr[4]/td[7]/div/div/div/span/div/div/div",
        'campaign_function': campaign_function_4
    },
]

opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
service = Service(binary_path)
driver = webdriver.Chrome(service=service, options=opt)

driver.get(fb_website)
driver.switch_to.window(driver.window_handles[-1])
original_window = driver.current_window_handle

time.sleep(10)


for campaigns in fb_campaigns:
    if campaigns['status'] == 1:
        download_button_xpath = campaigns['campaigns_download_button_xpath']
        campaign_form_name = campaigns['campaign_form_name']
        campaign_function = campaigns['campaign_function']
        campaign_status = campaigns['status']
        max_retries = 3
        for _ in range(max_retries):
            try:
                WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,download_button_xpath))).click()
                break
            except ElementNotInteractableException:
                print("Element not interactable, retrying...")
                
        time.sleep(2)
        driver.page_source
        time.sleep(2)
        element = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/div[2]/div[2]/span')
        text = element.text
        match = re.search(r'\d+', text)
        no_of_leads = 0  # Default value if no match is found
        if match:
            no_of_leads = int(match.group())
        if no_of_leads > 0:
            if campaign_function:
                download_new_leads_button = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,'/html/body/div[5]/div[2]/div/div/div/div/div[2]/div/div[4]/div[1]/div[2]/div[1]'))).click()
                download_leads = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div[2]/div/table/tbody/tr/td[3]/a'))).click()
                time.sleep(1)
                driver.execute_script("window.open('https://www.tyreplex.com/tp-admin/?mod=upload_file');")
                campaign_function()
                print(f"{no_of_leads} New Leads have been Uploaded for the campaign of {campaign_form_name}")
            else:
                print(f"No function found for campaign : {campaign_form_name}")
        else:
            print(f"No leads for campaign : {campaign_form_name}")

        time.sleep(2)
        
        try:
            driver.switch_to.window(original_window)
        except:
            pass

        WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div/div[1]/div/div[2]/div/button'))).click()
    else:
        pass
driver.quit()


