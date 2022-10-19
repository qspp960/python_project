from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

APPLY_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3044053929&geoId=105149562&keywords=Python%20Developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD&refresh=true"


chrome_driver_path = '/Applications/development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(APPLY_URL)

driver.find_element(By.CSS_SELECTOR,'.btn-secondary-emphasis').click()
sleep(10)

driver.find_element(By.ID,'username').send_keys("euihyun960@gmail.com")
driver.find_element(By.ID,'password').send_keys("*****")
driver.find_element(By.CSS_SELECTOR,'.login__form_action_container button').click()

sleep(10)

love_apply_page = driver.find_elements(By.CSS_SELECTOR,'.full-width.artdeco-entity-lockup__title.ember-view a')


for page in love_apply_page:
    print(page.text)
    page.click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR,'.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary').click()
    sleep(10)

# driver.find_element(By.CSS_SELECTOR,'.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary').click()
# driver.find_element(By.CSS_SELECTOR,'.jobs-unified-top-card__primary-description span span a').click()
#
# sleep(10)
#
# driver.find_element(By.CSS_SELECTOR,'.follow.org-company-follow-button.org-top-card-primary-actions__action.artdeco-button.artdeco-button--primary').click()
#
# sleep(20)
#
# driver.find_element(By.CSS_SELECTOR,'.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view').click()

