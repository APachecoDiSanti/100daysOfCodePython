import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def check_for_captcha():
    if "/checkpoint/challenge/" in chrome_driver.current_url:
        input("Press enter once the captcha has been solved.")


def login():
    chrome_driver.get(LOGIN_URL)
    input_email = chrome_driver.find_element(By.ID, "session_key")
    input_email.send_keys(LINKEDIN_EMAIL)
    input_password = chrome_driver.find_element(By.ID, "session_password")
    input_password.send_keys(LINKEDIN_PASSWORD)
    button_sign_in = chrome_driver.find_element(By.CLASS_NAME, "sign-in-form__submit-btn--full-width")
    button_sign_in.click()
    check_for_captcha()


LINKEDIN_EMAIL = os.environ["LINKEDIN_EMAIL"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3833819852&f_AL=true&f_WT=2&geoId=90000084&keywords=python%20developer&location=San%20Francisco%20Bay%20Area&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"
LOGIN_URL = "https://www.linkedin.com/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.maximize_window()

login()

# Saving jobs instead of applying to them
chrome_driver.get(URL)
time.sleep(2)  # Wait for <ul> to load
job_list = chrome_driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
jobs = job_list.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
for job in jobs:
    job.click()
    time.sleep(3)  # wait for job details to load
    save_button = chrome_driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
