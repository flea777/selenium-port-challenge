from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

url = 'https://www.mercadolivre.com.br/'
driver.get(url)
driver.maximize_window()

search_box = wait.until(EC.visibility_of_element_located((By.ID, 'cb1-edit')))
search_term = 'Notebook'
search_box.send_keys(search_term)
search_box.submit()

element_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'poly-card__content')))

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

def extract_search_results(soup, n=3):
  result = []
  for item in soup.find_all('div', class_='poly-card__content', limit=n):
    product_title = item.find('h3').text.strip()
    product_price = item.find('span', class_='andes-money-amount__fraction').text.strip()
    result.append({'title': product_title, 'price': product_price})
  
  return result

result = extract_search_results(soup)

def print_result(result):
  for idx, item in enumerate(result, start=1):
    print(f"{idx}. {item['title']} - R${item['price']}")

print('------------------------')
print_result(result)
print('------------------------')