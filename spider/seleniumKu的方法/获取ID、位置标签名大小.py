from selenium import webdriver

browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)
input=browser.find_element_by_class_name('Zi Zi--LabelRoundtable')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()