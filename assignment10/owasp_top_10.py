import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get('https://owasp.org/Top10/2025/')
list1 = driver.find_elements(By.CSS_SELECTOR,'ol > li')

top10 = []
for lis in list1:
    name = lis.find_element(By.CSS_SELECTOR, "a").text
    link = lis.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
    dict1 = {
        'Title': name,
        'Link':link
    }
    top10.append(dict1)
print(top10)
driver.quit()

with open('owasp_top_10.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=top10[0].keys())
    writer.writeheader()
    writer.writerows(top10)