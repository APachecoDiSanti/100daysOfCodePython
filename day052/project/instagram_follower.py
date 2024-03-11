import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Using approximate XPATH since Instagram has implemented bot protection
# Unable to test this
class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()

        self.INSTAGRAM_URL = "https://www.instagram.com"
        self.INSTAGRAM_COOKIE_JSON = os.environ["INSTAGRAM_COOKIE_JSON"]
        self.follow_buttons = []

    def login(self):
        self.driver.get(self.INSTAGRAM_URL)

        # Load cookies and reload page to log in without using the login form
        with open(self.INSTAGRAM_COOKIE_JSON) as cookie_file:
            cookies = json.load(cookie_file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

    def find_followers(self, account):
        self.driver.get(f"{self.INSTAGRAM_URL}/{account}")
        time.sleep(3)
        followers_page = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button")
        followers_page.click()
        time.sleep(3)

        followers_list = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div")
        start_scroll_height = -1
        last_scroll_height = followers_list.get_attribute("scrollHeight")
        while last_scroll_height != start_scroll_height:
            start_scroll_height = last_scroll_height
            followers_list.send_keys(Keys.PAGE_DOWN)
            last_scroll_height = followers_list.get_attribute("scrollHeight")
            time.sleep(2)

        self.follow_buttons = followers_list.find_elements(By.CSS_SELECTOR, "button")

    def follow(self):
        for button in self.follow_buttons:
            button.click()
            time.sleep(2)
