from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_driver_path = '/Applications/development/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(10)
        go_test = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_test.click()
        sleep(50)
        self.down = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        sleep(15)
        login_twitter = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/span[1]')
        login_twitter.click()
        sleep(10)

        base_window = self.driver.window_handles[0]
        google_popup_window = self.driver.window_handles[1]

        self.driver.switch_to.window(google_popup_window)

        login_google = self.driver.find_element(By.XPATH,'//*[@id="credentials-picker"]/div[1]/div[1]')
        login_google.click()
        sleep(10)

