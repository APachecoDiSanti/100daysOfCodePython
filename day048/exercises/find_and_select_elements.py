from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.python.org"

# Keep browser open after finishing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

search_box = driver.find_element(By.NAME, value="q")
print(search_box.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
anchor = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(anchor.text)
bug_link = driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
print(bug_link.text)

# driver.close()  # Closes active tab
driver.quit()  # Quits the entire browser
