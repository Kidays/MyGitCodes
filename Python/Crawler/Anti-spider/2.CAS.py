import requests
import csv
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
url = 'https://www.chemsrc.com/casindex/2.html'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'}
# casindex = requests.get(url, headers=headers)
# parser = etree.HTMLParser()  # create object of lxml.etree.HTMLParser
# # etree.HTML:可以用来解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象。 作为_Element对象，可以方便的使用getparent()、remove()、xpath()等方法
# casindex = etree.HTML(casindex.text, parser=parser)
# tabhead=casindex.xpath('//*[@id="idxTbl"]/thead/tr/th')
# head_list=[]
# for head in tabhead:
#     head=head.xpath('./text()')[0]
#     head_list.append(head)
# print(head_list)
# tabcontents=casindex.xpath('//*[@class="rowDat"]')
# contents_list=[]
# for contents in tabcontents:
#     contents=contents.xpath('./td')
#     for content in contents:
#         content=content.xpath('./text()')
#         print(content)
driverpath=r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver'
service=Service(executable_path=driverpath)
browser=webdriver.Chrome(service=service)
browser.get(url)
# tab=browser.find_elements_by_id('idxTbl')
# tab=browser.find_elements(by=By.ID,value="idxTb1")
# tabhead1=browser.find_element(by=By.CLASS_NAME,value="col-md-3")
tab=browser.find_elements(by=By.XPATH,value='//*[@id="idxTbl"]/thead/tr/th')
head_list=[]
# head=tab[1].text
# for head in tab:
#     head=head.find_element(by=By.XPATH,value='./text()')[0]
for i in range(len(tab)):
    head_list.append(tab[i].text)
# head_list.append(tab[1].text)
# head_list.append(tab[2].text)
# head_list.append(tab[3].text)
# head_list.append(tab[4].text)
print(head_list)
# tabcontents=browser.find_elements(by=By.XPATH,value='//*[@id="idxTbl"]/tbody/tr')
content_list=[]
# for contents in tabcontents:
contents=browser.find_elements(by=By.XPATH,value='//*[@id="idxTbl"]/tbody/tr/td')
for i in range(len(contents)):
    content_list.append(contents[i].text)
    print(content_list)

