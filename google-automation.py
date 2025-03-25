from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

url = 'https://www.bing.com/'
driver.get(url)
driver.maximize_window()
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')


