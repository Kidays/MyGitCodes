# import requests
# from lxml import etree
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37'}
# url = 'https://www.pearvideo.com/category_1'
# page_text = requests.get(url=url, headers=headers).text
# tree = etree.HTML(page_text)
# li_list=tree.xpath('//*[@id="listvideoListUl"]/li')
# for li in li_list:
#     detail_url='https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
#     name=li.xpath('./div/a/div[2]/text()')[0]
#     # print(detail_url,name)
#     page_text1=requests.get(url=detail_url,headers=headers).text
#     print(page_text1)

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
 
# 处理SSL证书错误问题
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# 忽略无用的日志
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)
try:
    driver.get('https://www.pearvideo.com/category_1')
    detail_url=driver.find_element(by=By.XPATH,value='//*[@id="listvideoListUl"]/li')
    print(detail_url)
except Exception as e:
    print(e)
    driver.close()
 

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# s = Service("C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver")
# driver = webdriver.Chrome(service=s)
# browser=webdriver.Chrome('C:/Users/Administrator/Downloads/chromedriver_win32/chromedriver')