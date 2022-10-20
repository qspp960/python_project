from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


chrome_driver_path = '/Applications/development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# tinder login
driver.get("https://tinder.com/")
sleep(10)
cookie_unexcept = driver.find_element(By.XPATH,'//*[@id="t1452431810"]/div/div[2]/div/div/div[1]/div[2]/button')
cookie_unexcept.click()
sleep(30)

tinder_login = driver.find_element(By.XPATH,'//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
tinder_login.click()
sleep(10)


fb_login = driver.find_element(By.XPATH,'//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(10)

base_window = driver.window_handles[0]
fb_popup_window = driver.window_handles[1]

driver.switch_to.window(fb_popup_window)

fb_login_email = driver.find_element(By.XPATH,'//*[@id="email"]')
fb_login_email.send_keys("01040156267")
fb_login_pw = driver.find_element(By.XPATH,'//*[@id="pass"]')
fb_login_pw.send_keys("@@@@@@@")

fb_login_btn = driver.find_element(By.XPATH,'//*[@id="loginbutton"]')
fb_login_btn.click()

sleep(5)
driver.switch_to.window(base_window)
sleep(20)


tinder_location_check = driver.find_element(By.XPATH,'//*[@id="t-275949266"]/main/div/div/div/div[3]/button[1]')
tinder_location_check.click()

#google_login = driver.find_element(By.XPATH,'//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[1]/div/button')
# google_login.click()
# sleep(10)
#
#
# base_window = driver.window_handles[0]
# google_popup_window = driver.window_handles[1]
#
# driver.switch_to.window(google_popup_window)

# Google login popup
# driver.find_element(By.XPATH,'//*[@id="identifierId"]').send_keys("euihyun960@gmail.com")
# sleep(10)
# driver.find_element(By.XPATH,'//*[@id="identifierNext"]').click()
