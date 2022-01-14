from bs4 import BeautifulSoup
import requests
import time
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}


def save_pic(url, name):
    r = requests.get(url)
    name =
def get_links(url):
    result=requests.get(url,headers=headers)
    soup=BeautifulSoup(result.text,'lxml')
    # Names like class or def name cannot be used as variables in python. In this case,you can attach an underscore to resolve naming conflicts
    links=soup.find_all(class_='li-index-handset')
    for link in links:
        href=link["href"]
        result1=requests.get(href,headers=headers)
        soup=BeautifulSoup(result1.text,'lxml')
        links1=soup.find_all(class_='li10-1-3_big')
        for link1 in links1:
            href1=link1["href"]
            result2=requests.get(href1,headers=headers)
            soup=BeautifulSoup(result2.text,'lxml')
            links2=soup.find_all(class_='zhuanti_STYLE19')
            links2[-1].a.string
            

# http://www.kole8.com/zhuanti/index_2.html\
# body > div.class_div_css10 > ul > li:nth-child(5)
# body > div.class_div_css10 > ul > li:nth-child(6)
# body > div.class_div_css10 > ul > li:nth-child(28)

# http://www.kole8.com/zhuanti/html/20215/view_zhuanti_388.html
# body > div:nth-child(8) > ul.class_div_css10 > li:nth-child(1)
# body > div:nth-child(8) > ul.class_div_css10 > li:nth-child(1) > a:nth-child(1)
# body > div:nth-child(8) > ul.class_div_css10 > li:nth-child(15)
# body > div:nth-child(8) > ul.class_div_css10 > li:nth-child(15) > a:nth-child(1)
# http://www.kole8.com/zhuanti/html/20215/view_zhuanti_list_225523.html
# body > div.class_div_css09 > ul > li.li09-1-3 > p:nth-child(2) > a > img
# body > div.class_div_css09 > ul > li.li09-1-6 > span: nth-child(23)
# body > div.class_div_css09 > ul > li.li09-1-6 > span:nth-child(11)

# http://www.kole8.com/zhuanti/html/20215/view_zhuanti_list_225603.html
# body > div.class_div_css09 > ul > li.li09-1-3 > p:nth-child(2) > a > img

# http://www.kole8.com/zhuanti/index_3.html\
# body > div.class_div_css10 > ul > li:nth-child(5)
# body > div.class_div_css10 > ul > li:nth-child(5) > a:nth-child(1)
# http://www.kole8.com/zhuanti/html/20212/view_zhuanti_364.html
# body > div:nth-child(8) > ul.class_div_css10 > li:nth-child(1)
# body > div:nth-child(8) > ul.class_div_css10 > li:nth-child(1) > a:nth-child(1)
# http://www.kole8.com/zhuanti/html/20212/view_zhuanti_list_203379.html
# body > div.class_div_css09 > ul > li.li09-1-3 > p:nth-child(2) > a > img
# body > div.class_div_css09 > ul > li.li09-1-6 > span.zhuanti_STYLE18
# body > div.class_div_css09 > ul > li.li09-1-6 > span.zhuanti_STYLE18
# body > div.class_div_css09 > ul > li.li09-1-6 > span:nth-child(3)

# body > div.class_div_css10 > ul > li:nth-child(28)

