import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.tinder.com"
FACEBOOK_EMAIL = os.environ["FACEBOOK_EMAIL"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.maximize_window()

chrome_driver.get(URL)
time.sleep(3)

login = chrome_driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]")
login.click()

time.sleep(3)
tinder_window = chrome_driver.current_window_handle
login_facebook_button = chrome_driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button")
login_facebook_button.click()

time.sleep(3)
facebook_window = chrome_driver.window_handles[1]
chrome_driver.switch_to.window(facebook_window)
input_email = chrome_driver.find_element(By.ID, "email")
input_email.send_keys(FACEBOOK_EMAIL)
time.sleep(1)
input_password = chrome_driver.find_element(By.ID, "pass")
input_password.send_keys(FACEBOOK_PASSWORD)
time.sleep(1)
facebook_login_input = chrome_driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input")
facebook_login_input.click()

time.sleep(3)

# Unable to continue without a real Tinder account that I won't create (fakes get banned)
