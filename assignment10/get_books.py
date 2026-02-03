# TASK 3
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
search_res = driver.find_elements(By.CSS_SELECTOR,'li.row.cp-search-result-item') 

results = []
for res in search_res:
    title = res.find_element(By.CSS_SELECTOR, "h3.cp-title span.title-content").text
    authors = res.find_elements(By.CSS_SELECTOR, "a.author-link")
    authors = [x.text for x in authors]
    author = '; '.join(authors)
    form_year = res.find_element(By.CSS_SELECTOR, "div.cp-format-info span.display-info-primary" ).text
    dict_res = {
        'Title':title,
        'Author':author,
        'Format-Year':form_year
    }
    results.append(dict_res)
driver.quit()

df = pd.DataFrame(results)
print(df)

# TASK 4
df.to_csv('get_books.csv', index= False)
with open("get_books.json", "w") as file:
    json.dump(results,file,indent=4)