# from calendar import c
# # from selenium.webdriver import Chrome
# import requests
# from lxml import etree
# from selenium import webdriver
# url='https://pvp.qq.com/web201605/herolist.shtml'
# # web=Chrome()
# driver_path = r'C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get(url)
# # web.get(url)
# # url_head='https://pvp.qq.com/web201605/'
# url_list=driver.find_elements_by_xpath('//ul[@class="herolist clearfix"]/li')
# for li in url_list:
#     hero_list=li.find_element_by_xpath('./a').get_attribute('href')
#     html=requests.get(hero_list)
#     html.encoding='gbk'
#     selector=etree.HTML(html.text)
#     name=selector.xpath('//h2[@class="cover-name"]/text()')[0]
#     print(name)
#     infos=selector.xpath('//ul[@class="cover-list"]/li')
#     for para in infos:
#         scnl=para.xpath('./em/text()')[0]
#         scnl_num=para.xpath('./span/i/@style')[0][6:]
#         print(scnl,scnl_num)

import requests
import json
import csv
from lxml import etree
start_url = 'https://pvp.qq.com/web201605/herolist.shtml'
url_head = 'https://pvp.qq.com/web201605/'
start_html = requests.get(start_url)
# start_html.encoding='gbk'
start_selector = etree.HTML(start_html.text)
url_list = start_selector.xpath('//ul[@class="herolist clearfix"]/li')
# with open('hero.csv', 'w',newline="",encoding='utf-8')as f:
#     writer=csv.writer(f)
#     writer.writerow(['Hero_name','生存能力','攻击伤害','技能效果','上手难度'])
# for li in url_list:
#     hero_ls=[]
#     hero_list0=li.xpath('a/@href')[0]
#     # print(hero_list0)
#     hero_list=url_head+hero_list0
#     hero_html=requests.get(hero_list)
#     hero_html.encoding='gbk'
#     # print(hero_html)
#     hero_selector=etree.HTML(hero_html.text)
#     hero_name=hero_selector.xpath('//h2[@class="cover-name"]/text()')[0]
#     # print(type(hero_name))
#     hero_ls.append(hero_name)
#     hero_infos=hero_selector.xpath('//ul[@class="cover-list"]/li')
#     for skill_para in hero_infos:
#         # skill=skill_para.xpath('./em/text()')[0]
#         skill_value=skill_para.xpath('span/i/@style')[0][6:]
#         hero_ls.append(skill_value)
#     print(hero_ls)
#     with open('hero.csv', 'a+',newline="",encoding='utf-8')as f:
#         writer=csv.writer(f)
#         writer.writerow(hero_ls)
print('-----------------------------')
with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
    writer = csv.writer(f)
    writer.writerow(['ename', 'cname', 'title',
                    'new_type', 'hero_type', 'skin_name'])
start_url1 = 'https://pvp.qq.com/web201605/js/herolist.json'
start_html1 = requests.get(start_url1).text
start_html1 = json.loads(start_html1)
for i in start_html1:
    hero_attribute = []
    hero_attribute.append(i['ename'])
    hero_attribute.append(i['cname'])
    hero_attribute.append(i['title'])
    hero_attribute.append(i['new_type'])
    hero_attribute.append(i['hero_type'])
    hero_attribute.append(i.setdefault('skin_name', 0))
    with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(hero_attribute)
print('-----------------------------')
with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
    writer = csv.writer(f)
    writer.writerow(['item_name', 'price', 'total_price', 'des1', 'des2'])
start_url2 = 'https://pvp.qq.com/web201605/js/item.json'
start_html2 = requests.get(start_url2).text
start_html2 = json.loads(start_html2)
# print(start_html2)
for i in start_html2:
    items = []
    if i.get('des2'):
        des2 = i['des2']
    else:
        des2 = ""
    items.append(i['item_name'])
    items.append(i['price'])
    items.append(i['total_price'])
    items.append(i['des1'])
    items.append(des2)
    with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(items)
    # print(i['item_name'],i['price'],i['total_price'],i['des1'],des2)
print('-----------------------------')
with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
    writer = csv.writer(f)
    writer.writerow(['summoner_name', 'summoner_rank', 'summoner_description'])
start_url3 = 'https://pvp.qq.com/web201605/js/summoner.json'
start_html3 = requests.get(start_url3).text
start_html3 = json.loads(start_html3)
# print(start_html3)
for i in start_html3:
    summoner = []
    summoner.append(i['summoner_name'])
    summoner.append(i['summoner_rank'])
    summoner.append(i['summoner_description'])
    with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(summoner)
    # print(i['summoner_name'],i['summoner_rank'],i['summoner_description'])
