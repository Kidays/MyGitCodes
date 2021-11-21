import re
from urllib3 import *
import time
import json
disable_warnings()
http = PoolManager()

# get a single page html file


def getOnePage(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'}
        # request to send
        response = http.request('GET', url, headers=headers)
        data = response.data.decode('utf-8')
        if response.status == 200:
            return data
        return None
    except Exception:
        return None


def parseOnePage(html):
    # use regular expression
    # re.S: expansion "." to the entire string,enclude \n
    pattern = re.compile(
        'class="content">.*?"_blank">(.*?)</a>.*?<em>(.*?)</em>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{'name': item[0], 'score': item[1]}
        print(type(item))


def save(content):
    with open('board.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def getBoard(pagenum):
    url = 'https://www.poxiao.com/type,genre/movie,sci-fi/index_' + \
        str(pagenum)+'.html'
    html = getOnePage(url)
    for item in parseOnePage(html):
        print(item)
        save(item)


for i in range(1, 10):
    getBoard(i)
    time.sleep(1)
