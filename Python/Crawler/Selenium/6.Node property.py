from selenium import webdriver
import time
driver=webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver')
driver.get('https://www.jd.com')
ul=driver.find_element_by_id('navitems-lk')
li_list=ul.find_elements_by_tag_name('li')
a1=li_list[0].find_elements_by_tag_name('a')
a2=li_list[1].find_elements_by_tag_name('a')
js='''
arguments[0].text="python"
arguments[0].href="https://item/jd.com/12417245.html"
arguments[1].text="JK"
arguments[1].href="https://geekori.com"
'''
driver.execute_script(js,a1,a2)