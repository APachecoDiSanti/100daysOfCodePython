from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def try_buying_most_expensive_upgrade():
    store = c_driver.find_element(By.ID, "store")
    store_items = store.find_elements(By.CSS_SELECTOR, "div")
    most_expensive_item = None
    most_expensive_cost = -1
    for item in store_items:
        item_class = item.get_attribute("class")
        if item_class == "grayed" or item_class == "amount":
            continue
        item_cost = int(item.find_element(By.CSS_SELECTOR, "b").text.strip().split(" - ")[1].replace(",", ""))
        if max(most_expensive_cost, item_cost) == item_cost:
            most_expensive_item = item
            most_expensive_cost = item_cost
    if most_expensive_item:
        most_expensive_item.click()


URL = "http://orteil.dashnet.org/experiments/cookie/"
THRESHOLD_SECONDS = 1
STOP_AFTER_SECONDS = 5*60

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

c_driver = webdriver.Chrome(chrome_options)
c_driver.maximize_window()
c_driver.get(URL)

cookie = c_driver.find_element(By.ID, "cookie")

start_time_check = time.time()
previous_time_check = start_time_check
while previous_time_check - start_time_check < STOP_AFTER_SECONDS:
    cookie.click()
    current_time_check = time.time()
    if current_time_check - previous_time_check >= THRESHOLD_SECONDS:
        try_buying_most_expensive_upgrade()
        previous_time_check = current_time_check

cps = c_driver.find_element(By.ID, "cps").text
print(cps)
