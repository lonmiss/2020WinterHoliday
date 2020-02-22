# 有条件的等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.taobao.com/")
wait=WebDriverWait(browser,10)
input=wait.until(EC.presence_of_all_elements_located(By.ID,'q'))
button=wait.until(EC.element_to_be_selected((By.CSS_SELECTOR,'btn-search')))
print(input,button)
browser.close()