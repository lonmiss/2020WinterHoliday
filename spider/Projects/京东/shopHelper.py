from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 用chrome浏览器
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

def get_first_page(commodity):
    try:
        url="https://www.jd.com"
        browser.get(url)
        input=browser.find_element_by_id("key")
        input.send_keys(commodity)
        cnt=browser.find_element_by_css_selector("#search > div > div.form > button")
        cnt.click()
        #获取页数
        browser.implicitly_wait(3)
        pages=browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b')
        print(pages)
        #pages=browser.find_element_by_css_selector('#J_bottomPage > span.p-skip > em:nth-child(1) > b')
        return int(pages.text)
    except TimeoutError:
        return get_first_page(commodity)

def deal_with_html():
    return None

def change_page(nums):
    time.sleep(3)
    input_page_num=browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/input')
    input_page_num.send_keys(u'\ue003')
    input_page_num.send_keys(nums)
    cnt_click=browser.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/a')
    cnt_click.click()

def main():
    total=get_first_page('iphone6')
    print(total)
    # 实现页面的跳转
    total=3
    for i in range(total):
        change_page(i+2)



if __name__ == '__main__':
    main()
