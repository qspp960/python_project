from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from rental_data_manager import RentalDataManager


SURVEY_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfeYPjkmUr1SC99O7dtfjL18g61MhZkzzA9wzvOiDbzBrouKA/viewform?usp=sf_link'

class DataInputSheet():

    def __init__(self):
        chrome_driver_path = '/Applications/development/chromedriver'
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(url=SURVEY_URL)
        sleep(10)


    def input_data(self,rental_data):
        input_form = self.driver.find_elements(By.CSS_SELECTOR,'input.whsOnd.zHQkBf')
        sleep(10)
        for form in input_form:
            form.send_keys(rental_data.rental_price[0])
            sleep(5)

        self.driver.find_element(By.CSS_SELECTOR,'div.uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd').click()

