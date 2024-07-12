import time
import os
import csv
import re

import pandas as pd

from unidecode import unidecode
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

binary_path = r"C:\Users\kishan.kumar_tyreple\Desktop\chromedriver.exe"
fb_website = "https://business.facebook.com/latest/instant_forms/forms?asset_id=334167367265607&business_id=1055428358578694&nav_id=2416062922&nav_ref=bizweb_landing_fb_login_button&biz_login_source=bizweb_landing_fb_login_button"
download_folder = r"C:\Users\kishan.kumar_tyreple\Downloads"

vehicle_make_4w = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\vehicle_make_4w.csv")
vehicle_model_4w = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\vehicle_model_4w.csv")

vehicle_make_2w = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\vehicle_make_2w.csv")
vehicle_model_2w = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\vehicle_model_2w.csv")

city_name = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\city_name.csv")
pincode_city_id = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\pincode_city_id.csv")
city_id_pincode = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\city_id_pincode.csv")

vehicle_makes = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\vehicle_makes.csv")
vehicle_models = pd.read_csv("C:\\Users\\kishan.kumar_tyreple\\Downloads\\vehicle_models.csv")

vehicle_model_mapping = {
    'Hector': 'Hector 2023',
    'Hector Plus' :'Hector Plus 2023',
    'Scorpio N' : 'Scorpion',
    'Scorpio': 'Scorpion',
    'Scorpio Classic' : 'Scorpion',
    'Bolero Power Plus': 'Bolero Power Plus 2017-20',
    'Go Plus': 'Go Plus 2018-20',
    'XUV 500': 'XUV500',
    'Indica Ev2' : 'Indica eV2',
    'Grand i10 Nios' : 'Grand i10 Nios',
    'WagonR': 'Wagon R',
    'Indica Vista': 'Indica Vista 2008 13',
    'Indigo Cs': 'Indigo Cs 2008 12',
    'New Verna': 'New Verna 2017-20',
    'Vitara Brezza': 'Vitara Brezza 2020-2022',
    'RediGo': 'Redi-Go',
    'KUV 100 NXT': 'KUV 100 2016-17',
    'D Max V Cross': 'D Max V Cross 2015 2019',
    'Evalia': 'Evalia 2013',
    'CR-V': 'CR-V 2023',
    'XUV 400': 'XUV 400 Electric',
    'Qute': 'Qute (RE60)',
    'CelerioX': 'Celerio X',
    'CLA Class': 'CLA-Class',
    'Hector Plus': 'Hector',
    'AMG A35': 'AMG A 35',
    'Polo TSI': 'Polo TSI Turbo Edition',
    'SsangYong Rexton': 'Mahindra Ssangyong S101',
    'MU7': 'MU 7',
    'Sumo Gold': 'Sumo Gold 2011 13',
    'Freelande 2': 'Freelander 2',
    'D Max V': 'D Max V Cross 2015 2019',
    'A Class': 'A Class Sedan Limousine',
    'Alturas G4': 'Alturas',
    'AMG E63': 'AMG E 63',
    'RS6': 'RS6 Avant',
    'AMG C63': 'AMG C 63',
    'RSQ8': 'RS Q8',
    'Grand i10':'Grand i10 Nios'
}

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
service = Service(binary_path)
driver = webdriver.Chrome(service=service, options=opt)

def campaign_function_1():
    pass

def campaign_function_2():
    pass

def campaign_function_3():

    files = os.listdir(download_folder)
    files = [f for f in files if os.path.isfile(os.path.join(download_folder, f))]
    latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(download_folder, f)))
    full_path = os.path.join(download_folder, latest_file)
    # print("Full path of the latest file in download folder:", full_path)

    df = pd.read_csv(full_path, encoding='utf-16', delimiter='_')

    df.to_csv('output2.xlsx')

    df = pd.read_csv('output2.xlsx', sep='\t', quoting=csv.QUOTE_NONE)

    columns_to_select = ['conditional,question,1', 'conditional,question.1,2',
    'full,name', 'phone,number', 'state', 'city', 'post,code']

    df = df[columns_to_select]

    df = df.rename(columns={'conditional,question,1': 'v_make_name',
                        'conditional,question.1,2': 'v_model_name',
                        'full,name': 'full_name',
                        'phone,number': 'mobile_phone_number',
                        'state': 'state_name',
                        'city': 'city_name',
                        'post,code': 'pincode'})

    df['mobile_phone_number'] = df['mobile_phone_number'].astype(str).str[-10:]
    df['pincode'] = df['pincode'].str.extract(r'(\d+)', expand=False)

    df.fillna(0, inplace=True)

    df['pincode'] = df['pincode'].astype('int64')

    def transliterate_to_english(name):
        return unidecode(name)

    df['full_name'] = df['full_name'].apply(transliterate_to_english)
    df['city_name'] = df['city_name'].apply(transliterate_to_english)

    def clean_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z ]', '', name).strip()
        return cleaned_name

    df['full_name'] = df['full_name'].apply(clean_name)
    df['city_name'] = df['city_name'].str.strip('"')
    df['v_make_name'] = df['v_make_name'].str.strip('""')
    df['v_model_name'] = df['v_model_name'].str.strip('""')


    df = pd.merge(df,pincode_city_id, on='pincode',how='left')
    df = df.rename(columns={'city_id':'city_id_pincode'})
    df.fillna(0, inplace=True)
    df['city_id_pincode']= df['city_id_pincode'].astype(int)

    df['city_name'] = df['city_name'].str.lower()
    city_name['city_name'] = city_name['city_name'].str.lower()

    df = pd.merge(df,city_name, on='city_name',how='left')
    df = df.rename(columns={'city_id':'city_id_city'})
    df['city_id_city'].fillna(1630, inplace=True)
    df['city_id_city']= df['city_id_city'].astype(int)

    df = pd.merge(df,city_id_pincode, on='city_id_city',how='left')
    df.fillna(0,inplace=True)
    df['pincode_id']= df['pincode_id'].astype(int)

    def merge_columns(row):
        if row['city_id_pincode'] == 0:
            return row['city_id_city'], row['pincode_id']
        else:
            return row['city_id_pincode'], row['pincode']

    df[['city_id', 'pincode']] = df.apply(merge_columns, axis=1, result_type='expand') #must be same length

    df = df.drop(columns=['city_id_pincode','city_id_city','pincode_id','state_name','city_name'])

    df = pd.merge(df, vehicle_make_4w, on='v_make_name', how='left')
    df.fillna(0,inplace=True)
    df = pd.merge(df, vehicle_model_4w, on='v_model_name', how='left')

    

    df = df.drop(columns=['v_make_name','v_model_name'])

    df['email'] = df['mobile_phone_number'] + '@tyreplex.com'
    df['v_type_id'] = '1'
    df['make_id'] = '2'
    df['source'] = 'Online Activation'
    df['sub_source'] = 'Facebook'

    new_order = [ 'email', 'full_name', 'mobile_phone_number', 'city_id','make_id','source','sub_source' ,'pincode', 'v_type_id', 'v_make_id','v_model_id',]
    df = df.reindex(columns=new_order)

    file_path = r'C:\Users\kishan.kumar_tyreple\Downloads\ceat_4w.csv'
    
    df.to_csv(file_path,index=False)

    driver.switch_to.window(driver.window_handles[-1])

    try:
        driver.find_element(By.XPATH, '//*[@id="mobile_no"]').send_keys('9879879879') #NoSuchElementException

        click_otp_button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="mobile_form"]'))).click()

        otp_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="otp_valid_input"]')))
        otp_input.send_keys('1106')

        time.sleep(2)
    except:
        pass

    click_on_upload = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH ,'/html/body/div[3]/div/div/main/div[2]/div/div[1]/ul/li/a'))).click()
    time.sleep(1)
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#upload_file > div:nth-child(1) > div > div:nth-child(6) > label')))
    element.click()
    time.sleep(1)
    file_path = r"C:\Users\kishan.kumar_tyreple\Downloads\ceat_4w.csv"
    upload_file = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="file_data"]')))
    upload_file.send_keys(file_path)

    click_on_upload_file = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="upload_file"]/div[2]/div/div[2]/button'))).click()
    time.sleep(1)
    driver.close()

def campaign_function_4():
    files = os.listdir(download_folder)
    files = [f for f in files if os.path.isfile(os.path.join(download_folder, f))]
    latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(download_folder, f)))
    full_path = os.path.join(download_folder, latest_file)

    df = pd.read_csv(full_path, encoding='utf-16', delimiter='_')

    df.to_csv('output2.xlsx')

    df = pd.read_csv('output2.xlsx', sep='\t', quoting=csv.QUOTE_NONE)

    columns_to_select = ['conditional,question,1', 'conditional,question.1,2',
    'full,name', 'phone,number', 'state', 'city', 'post,code']

    df = df[columns_to_select]

    df = df.rename(columns={'conditional,question,1': 'v_make_name',
                        'conditional,question.1,2': 'v_model_name',
                        'full,name': 'full_name',
                        'phone,number': 'mobile_phone_number',
                        'state': 'state_name',
                        'city': 'city_name',
                        'post,code': 'pincode'})

    df['mobile_phone_number'] = df['mobile_phone_number'].astype(str).str[-10:]
    df['pincode'] = df['pincode'].str.extract(r'(\d+)', expand=False)

    df.fillna(0, inplace=True)

    df['pincode'] = df['pincode'].astype('int64')

    def transliterate_to_english(name):
        return unidecode(name)

    df['full_name'] = df['full_name'].apply(transliterate_to_english)
    df['city_name'] = df['city_name'].apply(transliterate_to_english)

    def clean_name(name):
        cleaned_name = re.sub(r'[^a-zA-Z ]', '', name).strip()
        return cleaned_name

    df['full_name'] = df['full_name'].apply(clean_name)
    df['city_name'] = df['city_name'].str.strip('"')
    df['v_make_name'] = df['v_make_name'].str.strip('""')
    df['v_model_name'] = df['v_model_name'].str.strip('""')

    # Function to correct vehicle model names using regular expressions
    def correct_vehicle_model_name(model_name):
        for incorrect_name, correct_name in vehicle_model_mapping.items():
            model_name = re.sub(r'\b{}\b'.format(incorrect_name), correct_name, model_name)
        return model_name
    
    df['v_model_name'] = df['v_model_name'].apply(correct_vehicle_model_name)

    df = pd.merge(df,pincode_city_id, on='pincode',how='left')
    df = df.rename(columns={'city_id':'city_id_pincode'})
    df.fillna(0, inplace=True)
    df['city_id_pincode']= df['city_id_pincode'].astype(int)

    df['city_name'] = df['city_name'].str.lower()
    city_name['city_name'] = city_name['city_name'].str.lower()

    df = pd.merge(df,city_name, on='city_name',how='left')
    df = df.rename(columns={'city_id':'city_id_city'})
    df['city_id_city'].fillna(1630, inplace=True)
    df['city_id_city']= df['city_id_city'].astype(int)

    df = pd.merge(df,city_id_pincode, on='city_id_city',how='left')
    df.fillna(0,inplace=True)
    df['pincode_id']= df['pincode_id'].astype(int)

    def merge_columns(row):
        if row['city_id_pincode'] == 0:
            return row['city_id_city'], row['pincode_id']
        else:
            return row['city_id_pincode'], row['pincode']

    df[['city_id', 'pincode']] = df.apply(merge_columns, axis=1, result_type='expand') #must be same length

    df = df.drop(columns=['city_id_pincode','city_id_city','pincode_id','state_name','city_name'])

    df = pd.merge(df, vehicle_makes, on='v_make_name', how='left')
    df.fillna(0, inplace=True)
    df = pd.merge(df, vehicle_models, on='v_model_name', how='left')

    df = df.drop(columns=['v_make_name','v_model_name'])

    df['email'] = df['mobile_phone_number'] + '@tyreplex.com'
    df['v_type_id'] = '1'
    df['make_id'] = '2'
    df['source'] = 'Online Activation'
    df['sub_source'] = 'Facebook'

    new_order = [ 'email', 'full_name', 'mobile_phone_number', 'city_id','make_id','source','sub_source' ,'pincode', 'v_type_id', 'v_make_id','v_model_id',]
    df = df.reindex(columns=new_order)

    file_path = r'C:\Users\kishan.kumar_tyreple\Downloads\ceat_4w.csv'

    df.to_csv(file_path,index=False)

    driver.switch_to.window(driver.window_handles[-1])

    try:
        driver.find_element(By.XPATH, '//*[@id="mobile_no"]').send_keys('9879879879') #NoSuchElementException

        click_otp_button = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="mobile_form"]'))).click()

        otp_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="otp_valid_input"]')))
        otp_input.send_keys('1106')

        time.sleep(2)
    except:
        pass

    click_on_upload = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH ,'/html/body/div[3]/div/div/main/div[2]/div/div[1]/ul/li/a'))).click()
    time.sleep(1)
    element = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#upload_file > div:nth-child(1) > div > div:nth-child(6) > label')))
    element.click()
    time.sleep(1)
    file_path = r"C:\Users\kishan.kumar_tyreple\Downloads\ceat_4w.csv"
    upload_file = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="file_data"]')))
    upload_file.send_keys(file_path)

    click_on_upload_file = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH ,'//*[@id="upload_file"]/div[2]/div/div[2]/button'))).click()
    time.sleep(1)

    driver.close()





