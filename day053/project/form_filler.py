import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FormFiller:

    def __init__(self, data):
        self.FORM_URL = os.environ["FORM_URL"]
        self.data = data

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()

    def input_data(self):

        for details in self.data:
            self.driver.get(self.FORM_URL)
            time.sleep(3)
            form_elements = self.driver.find_elements(By.XPATH, """//div[@role="listitem"]""")
            input_address = form_elements[0].find_element(By.CSS_SELECTOR, "input")
            input_address.send_keys(details["address"])
            time.sleep(0.3)
            input_price = form_elements[1].find_element(By.CSS_SELECTOR, "input")
            input_price.send_keys(details["price"])
            time.sleep(0.3)
            input_link = form_elements[2].find_element(By.CSS_SELECTOR, "input")
            input_link.send_keys(details["link"])
            time.sleep(0.3)
            button_submit = self.driver.find_element(By.XPATH, """//div[@role="button"]""")
            button_submit.click()
            while "formResponse" not in self.driver.current_url:
                time.sleep(3)
