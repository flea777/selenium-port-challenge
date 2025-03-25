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

search_box = wait.until(EC.visibility_of_element_located((By.ID, 'sb_form_q')))
search_term = 'Python Selenium'
search_box.send_keys(search_term)
search_box.submit()

wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'b_algo')))  

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

def extract_search_results(soup, n=5):
    result = []
    for item in soup.find_all('li', class_='b_algo', limit=n):
        title_tag = item.find('h2')
        if title_tag:
            link_tag = title_tag.find('a')
            title = title_tag.text.strip()
            link = link_tag['href'] if link_tag else None
            result.append({'title': title, 'link': link})

    return result

result = extract_search_results(soup)  

def print_result(result):
    for idx in enumerate(result, start=1):
        print(f"{idx}. {result['title']} - {result['link']}")

print('------------------------')
print_result(result)
print('------------------------')

driver.quit()
