from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = '/Applications/development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")



cookie = driver.find_element(By.ID,"cookie")

time_upgrade = time.time() + 5
five_min = time.time() + 100

while True:
    driver.find_element(By.ID,"cookie").click()

    if time.time() > time_upgrade:
        current_money = driver.find_element(By.ID,"money").text
        if ',' in current_money:
            current_money = current_money.replace(',','')
        current_money = int(current_money)

        items_id = driver.find_elements(By.CSS_SELECTOR,"#store>div")
        items_money = driver.find_elements(By.CSS_SELECTOR, "#store>div>b")
        items = []

        for i in range(len(items_id)):
            money = items_money[i].text.split(' ')[-1]
            if ',' in money:
                money = money.replace(',','')
            if items_id[i].get_attribute('id') != 'buyElder Pledge':
                item = {
                    'id': items_id[i].get_attribute('id'),
                    'money': money,
                }
                items.append(item)

        items = reversed(items)

        for item in items:
            if int(item['money']) <= current_money:
                driver.find_element(By.ID,item['id']).click()
                break

        time_upgrade = time.time() + 5

    if time.time() >= five_min:
        print(driver.find_element(By.ID,'cps').text)
        break











