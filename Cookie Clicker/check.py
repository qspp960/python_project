from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = '/Applications/development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

items_money = driver.find_elements(By.CSS_SELECTOR, "#store>div>b")
money = items_money[7].text.split(' ')[-1]
money = money.replace(',','')

items_id = driver.find_elements(By.CSS_SELECTOR,"#store>div")
items_money = driver.find_elements(By.CSS_SELECTOR, "#store>div>b")
items = []
current_money = int(driver.find_element(By.ID,"money").text)
for i in range(len(items_id)):
    money = items_money[i].text.split(' ')[-1]
    if ',' in money:
        money = money.replace(',','')
    item = {
            'id': items_id[i].get_attribute('id'),
            'money': money,
        }
    items.append(item)

# for i in range(len(items)):
#     if int(items[i]['money']) > current_money:
#         print('big')
# money = money.replace(',','')
print(items)