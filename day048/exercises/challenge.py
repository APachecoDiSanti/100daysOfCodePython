from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()
driver.get(URL)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("TestFirstName")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("TestLastName")

email = driver.find_element(By.NAME, "email")
email.send_keys("test@email.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up_button.click()

driver.quit()
