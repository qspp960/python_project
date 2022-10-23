from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class InstagramFollowBot():

    def __init__(self):
        chrome_driver_path = '/Applications/development/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(5)
        self.driver.find_element(By.NAME,'username').send_keys("euihyun960@gmail.com")
        self.driver.find_element(By.NAME,'password').send_keys("qs!!806701")

        sleep(10)
        self.driver.find_element(By.CSS_SELECTOR,'button._acan._acap._acas').click()
        sleep(20)
        self.driver.find_element(By.CSS_SELECTOR,'button._acan._acao._acas').click()
        sleep(20)
        self.driver.find_element(By.CSS_SELECTOR,'button._a9--._a9_1').click()
        sleep(10)

    def find_ariana(self):
        self.driver.find_element(By.CSS_SELECTOR,'div._aawf._aawg._aexm input').send_keys("ariana grande")
        sleep(10)

        self.driver.find_element(By.CSS_SELECTOR,'div._abm4 a').click()
        sleep(20)

    def follow_ariana(self):
        self.driver.find_element(By.CSS_SELECTOR,'button._acan._acap._acas').click()
        sleep(10)

        self.driver.find_elements(By.CSS_SELECTOR,'ul.x78zum5.x1q0g3np.xieb3on li a')[1].click()
        sleep(10)

    def ariana_follower_following(self):
        self.follower = self.driver.find_elements(By.CSS_SELECTOR,'div._aano div div div div button')
        count = 0
        for f in self.follower:
            count += 1
            if count == 5:
                break
            else:
                f.click()
