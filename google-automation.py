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

tag_text_area_input = wait.until(EC.visibility_of_element_located((By.ID, 'sb_form_q')))

text_to_search = 'Python Selenium'
tag_text_area_input.send_keys(text_to_search)
tag_text_area_input.submit()

wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'b_algo')))  

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

def get_h2_from_first_n_lis(soup, li_class, n=5):
    first_n_lis = soup.find_all('li', class_=li_class, limit=n)
    tag_h2_search_title = [li.find('h2') for li in first_n_lis if li.find('h2')]
    return [h2.text.strip() for h2 in tag_h2_search_title]

first_titles = get_h2_from_first_n_lis(soup, 'b_algo')  
print(first_titles)

sleep(5)
driver.quit()
