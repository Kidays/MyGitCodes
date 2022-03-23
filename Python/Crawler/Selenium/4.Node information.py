from selenium import webdriver
from selenium.webdriver import ActionChains
options=webdriver.ChromeOptions()
options.add_argument('headless')
browser=webdriver.Chrome(chrome_options=options)
browser.get('https://jd.com')
ul=browser.find_element_by_id("navitems-group1")
print(ul.text)
print('id','=',ul.id)
print('location','=',ul.location)
print('tag_name','=',ul.tag_name)
print('size','=',ul.size)
li_list=ul.find_elements_by_tag_name("li")
for li in li_list:
    print(type(li))
    print('<',li.text,'>','class=',li.get_attribute('class'))
    a=li.find_element_by_tag_name('a')
    print('href','=',a.get_attribute('href'))
browser.close()