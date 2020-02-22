from selenium import webdriver

browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get("https://www.zhihu.com/explore")
input=browser.find_element_by_id('root')
print(input)
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()