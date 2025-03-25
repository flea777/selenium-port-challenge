from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from time import sleep

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

url = 'https://www.mercadolivre.com.br/'
driver.get(url)
driver.maximize_window()

search_box = wait.until(EC.visibility_of_element_located((By.ID, 'cb1-edit')))
search_term = 'Macbook'
search_box.send_keys(search_term)
search_box.submit()

sleep(3)

# for item in soup.find_all('h3', class_='poly-component__title-wrapper', limit=n):