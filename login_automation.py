import os
from dotenv import load_dotenv

load_dotenv()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

url = 'https://www.saucedemo.com/'
driver.get(url)
driver.maximize_window()

username_input = wait.until(EC.visibility_of_element_located((By.ID, 'user-name')))
password_input = wait.until(EC.visibility_of_element_located((By.ID, 'password')))

username_input.send_keys(os.environ['USERNAME'])
password_input.send_keys(os.environ['PASSWORD'])
password_input.submit()

add_to_cart_button = wait.until(EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-backpack')))
add_to_cart_button.click()