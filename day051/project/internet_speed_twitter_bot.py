import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()

        self.TWITTER_URL = "https://www.twitter.com"
        self.SPEED_TEST_URL = "https://www.speedtest.net/"
        self.TWITTER_COOKIE_JSON = os.environ["TWITTER_COOKIE_JSON"]
        self.PROMISED_DOWN = 100
        self.PROMISED_UP = 10

    def login_twitter(self):
        self.driver.get(self.TWITTER_URL)

        # Load cookies and reload page to log in without using the login form
        with open(self.TWITTER_COOKIE_JSON) as cookie_file:
            cookies = json.load(cookie_file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

    def tweet_at_provider(self, down, up):
        post_button = self.driver.find_element(By.XPATH, """//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a""")
        post_button.click()
        time.sleep(3)

        span_text_input = self.driver.find_element(By.XPATH, """//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span""")
        post_text = f"What's up with my internet speed? I'm getting {down} Mbps out of the promised {self.PROMISED_DOWN} Mbps of download speed and {up} Mbps out of the promised {self.PROMISED_UP} Mbps of upload speed!"

        # Input one letter at a time to emulate human behavior
        for char in post_text:
            span_text_input.send_keys(char)
            time.sleep(0.2)
        time.sleep(3)
        post_it_button = self.driver.find_element(By.XPATH, """//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]""")
        post_it_button.click()

    def get_internet_speed(self):
        self.driver.get(self.SPEED_TEST_URL)
        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()

        time.sleep(10)
        while "/result/" not in self.driver.current_url:
            print("Waiting 5 more seconds...")
            time.sleep(5)

        down_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-item-download .result-data").text.strip()
        up_speed = self.driver.find_element(By.CSS_SELECTOR, ".result-item-upload .result-data").text.strip()

        return down_speed, up_speed
