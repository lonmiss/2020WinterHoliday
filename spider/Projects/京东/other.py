from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def deal_with_html(page):
    html=BeautifulSoup(page,"html5lib")
    productsList=html.find_all(class_="gl-item")
    prodect={}
    text=BeautifulSoup(productsList[0],"html5lib")
    id=text.find()








browser.get('https://search.jd.com/Search?keyword=iphone6&enc=utf-8&pvid=9290dd7d391b42c18a17962aecd05f3e')
page=browser.page_source
deal_with_html(page)
browser.close()


"""
https://img14.360buyimg.com/n1/s450x450_jfs/t1/99211/32/6397/71054/5df2fe8eE081f3582/b8df1898cec4e1eb.jpg
"""