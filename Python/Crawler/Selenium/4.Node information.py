from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

options=webdriver.ChromeOptions()
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
options.add_argument('headless')
browser=webdriver.Chrome(chrome_options=options)
browser.get('https://jd.com')
ul=browser.find_element(by=By.ID,value="navitems-group1")
print(ul.text)
print('id','=',ul.id)
print('location','=',ul.location)
print('tag_name','=',ul.tag_name)
print('size','=',ul.size)
li_list=ul.find_elements(by=By.TAG_NAME,value="li")
for li in li_list:
    print(type(li))
    print('<',li.text,'>','class=',li.get_attribute('class'))
    a=li.find_element(by=By.TAG_NAME,value='a')
    print('href','=',a.get_attribute('href'))
browser.close()