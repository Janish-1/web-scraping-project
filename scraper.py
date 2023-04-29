#Website scraped: https://www.acnc.gov.au/charity/charities?search=24663972307

import time
from selenium.webdriver.common.by import By
import pandas as pd
import undetected_chromedriver as uc
from re import search

all_ids = []
ids = pd.read_csv("1000_ABN.csv")
for i in range(1000):
    j = ids['ABN'][i]
    all_ids.append(j) 
all_names =[]
for i in all_ids:
    try:
        for j in ids:
            url = "https://www.acnc.gov.au/charity/charities?search="+ str(i)
            driver = uc.Chrome()
            driver.get(url)
            time.sleep(0.5)
            m = driver.find_elements(by=By.TAG_NAME, value="a")
            all_links = []
            for lnk in m:
                all_links.append(lnk.get_attribute("href"))

            valid_links = []
            for i in all_links:
                try:
                    if search("profile",i) and i != '':
                        valid_links.append(i)
                except Exception as e:
                    continue

            for i in valid_links:
                url1 = i
                driver.get(url1)
                time.sleep(0.5)
                l = driver.find_element(by= By.XPATH,value="/html/body/div[1]/div/div/div[2]/header/div[4]/div[3]/div/div/nav/ul/li[3]/a/span")
                l.click()
                time.sleep(0.5)
                n = driver.find_elements(by=By.CLASS_NAME,value="h5.card-title.text-primary")
                for i in n:
                    all_names.append(i.get_attribute("innerHTML"))

            driver.close()
    except Exception as e:
        continue

file = open('names.txt','w')
file.writelines(all_names)
file.close()