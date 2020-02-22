from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
'''
browser=webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
    input=browser.find_element_by_id("kw")
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,100)
    wait.until(EC.presence_of_all_elements_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    #print(browser.page_source)
finally:
    browser.close()


# 查找单个元素
browser=webdriver.Chrome()
browser.get("https://www.taobao.com")
input_first=browser.find_element_by_id('q')
input_second=browser.find_element_by_css_selector('#q')
input_third=browser.find_element(By.ID,'q')
print(input_first)
print(input_second)
print(input_third)
browser.close()


# 元素的交互操作

import time

browser=webdriver.Chrome()
browser.get('https://www.jd.com')
input=browser.find_element_by_id('key')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('iPad')

button=browser.find_element_by_class_name('btn-search')
button.click()
browser.close()

'''
# 将动作附加到动作链中串行执行
from selenium.webdriver import ActionChains
browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('frameResult')
source=browser.find_element_by_css_selector('#draggable')
target=browser.find_element_by_css_selector('#droppable')
actions=ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()










