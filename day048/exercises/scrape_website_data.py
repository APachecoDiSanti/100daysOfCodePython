from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.python.org"

# Keep browser open after finishing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget .menu li")

events_dict = {}
index = 0
for event in events:
    time_tag = event.find_element(By.CSS_SELECTOR, value="time")
    anchor_tag = event.find_element(By.CSS_SELECTOR, value="a")
    events_dict[index] = {
        "time": time_tag.get_attribute("datetime"),
        "name": anchor_tag.text
    }
    index += 1

print(events_dict)

# driver.close()  # Closes active tab
driver.quit()  # Quits the entire browser
