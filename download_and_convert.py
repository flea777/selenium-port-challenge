from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from fpdf import FPDF

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

url = 'https://demo.automationtesting.in/FileDownload.html'
driver.get(url)
driver.maximize_window()

text = 'A vida é feita de desafios, mas cada passo dado com determinação nos aproxima de nossos objetivos.'

text_box = wait.until(EC.visibility_of_element_located((By.ID, 'textbox')))
text_box.send_keys(text)

generate_file_button = wait.until(EC.visibility_of_element_located((By.ID, 'createTxt')))
generate_file_button.click()

download_button = wait.until(EC.visibility_of_element_located((By.ID, 'link-to-download')))
download_button.click()

sleep(5)
driver.quit()

def text_to_pdf(txt_file_path, pdf_file_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15) 
    pdf.add_page()
    pdf.set_font('Arial', size=14)

    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        for line in txt_file:
            pdf.multi_cell(0, 10, line.strip()) 
    
    pdf.output(pdf_file_path)

txt_file_path = '/home/crocodile/Downloads/info.txt'
pdf_file_path = 'output.pdf' 

text_to_pdf(txt_file_path, pdf_file_path)