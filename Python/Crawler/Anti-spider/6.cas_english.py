from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import csv
import time
# get tab head
index = 'https://www.chemsrc.com/en/casindex/'
driverpath = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver'
service = Service(executable_path=driverpath)
browser = webdriver.Chrome(service=service)
browser.get(index)
tab = browser.find_elements(by=By.XPATH, value='//*[@id="idxTbl"]/thead/tr/th')
head_list = []
for i in range(len(tab)):
    head_list.append(tab[i].text)
with open('cas_english.csv','a+',newline='',encoding='utf-8')as f:
    writer=csv.writer(f)
    writer.writerows([head_list])
print(head_list)
# get contents
for i in range(100):
    s = i+1
    url = 'https://www.chemsrc.com/en/casindex/'+str(s)+'.html'
    driverpath = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver'
    service = Service(executable_path=driverpath)
    browser = webdriver.Chrome(service=service)
    browser.get(url)
    # get main contents
    contents = browser.find_elements(
        by=By.XPATH, value='//*[@id="idxTbl"]/tbody/tr/td')
    content_list = []
    for i in range(len(contents)):
        content_list.append(contents[i].text)
    print(len(content_list))
    # by row
    for i in range(int(len(content_list)/len(tab))):
        row_content = []
        row_content = content_list[i*len(tab):(i*len(tab)+len(tab))]
        print(row_content)
        with open('cas_english.csv','a+',newline='',encoding='utf-8')as f:
            writer=csv.writer(f)
            writer.writerows([row_content])
    # # get Chemical & Physical Properties
    # content_properties = browser.find_elements(
    #     by=By.XPATH, value='//*[@id="idxTbl"]/tbody/tr/td[3]')
    # print(len(content_properties))
    # # //*[@id="idxTbl"]/tbody/tr[2]/td[3]/text()[1]
    # properties_list = []
    # for i in range(len(content_properties)):
    #     properties_list.append(content_properties[i].text)
    # print(properties_list)

    time.sleep(0.5)