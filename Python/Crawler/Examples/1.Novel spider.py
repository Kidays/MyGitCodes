import sys
import os
from urllib import request
import re
# uses relative path
os.chdir(sys.path[0])
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'}


def getCatelogs(url):
    # page request
    req = request.Request(url=url, headers=headers, method='GET')
    # sending requests
    response = request.urlopen(req)
    # return
    result = []
    if response.status == 200:
        # reads the contents of the page
        html = response.read().decode('utf-8')
        # get the node list
        aList = re.findall('<li class="line3">.*</li>', html)
        # <a href="/nalanwudi/33332.html" title="第一章 身死 上">第一章 身死 上</a>
        # get the attribute value of href and title
        for a in aList:
            g = re.search('href="([^>"]*)"[\s]*title="([^>"]*)"', a)
            if g != None:
                url = 'https://www.doupozw.com'+g.group(1)
                title = g.group(2)
                chapter = {'title': title, 'url': url}
                result.append(chapter)
    return result


def getChapterContent(chapters):
    for chapter in chapters:
        req = request.Request(
            url=chapter['url'], headers=headers, method='GET')
        response = request.urlopen(req)
        if response.status == 200:
            # uses absolute path
            # f = open('H:\\MyGitCodes\\Python\\Crawler\\Examples\\novel\\'+chapter['title']+'.txt', 'a+')
            # uses relative path
            f = open('novel/'+chapter['title']+'.txt', 'a+')
            # <p>“五年，成功了，我花了五年时间终于成功了。”</p>
            contents = re.findall(
                '<p>(.*?)</p>', response.read().decode('utf-8'))
            for content in contents:
                f.write(content+'\n')
            f.close()
            print(chapter['title'], chapter['url'])


getChapterContent(getCatelogs("https://www.doupozw.com/nalanwudi"))
