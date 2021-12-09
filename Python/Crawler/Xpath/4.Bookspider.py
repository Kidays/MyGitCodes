from lxml import *
from lxml import etree
import requests
import json


# def getOnePage(url):
#     try:
#         res = requests.get(url)
#         if res.status_code == 200:
#             return res.text
#         else:
#             return None
#     except Exception:
#         return None
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}


def parseOnePage(url):
    res = requests.get(url, headers=headers)  # headers=headers needed
    res0 = res.text
    selector = etree.HTML(res0)
    items = selector.xpath('//tr[@class="item"]')
    for item in items:
        book_infos = item.xpath('td/p/text()')[0]
        # //*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/p[1]
        yield{
            'name': item.xpath('td/div/a/@title')[0],
            'url': item.xpath('td/div/a/@href')[0],
            'author': book_infos.split('/')[0],
            'publisher': book_infos.split('/')[-3],
            'date': book_infos.split('/')[-2],
            'price': book_infos.split('/')[-1]
        }
# str.split(str="", num=string.count(str))

def save(content):
    with open('H:\\MyGitCodes\\Python\\Crawler\\Examples\\top250books.txt', 'at', encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def getTop250(url):
    # html = getOnePage(url)
    for item in parseOnePage(url):
        print(item)
        save(item)


urls = [
    'https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]
for url in urls:
    getTop250(url)
