from bs4 import BeautifulSoup
import os
import sys
os.chdir(sys.path[0])  # enable file relative path
# with open('demo.html', 'r', encoding='utf-8') as html_file:
#     content = html_file.read()
#     soup = BeautifulSoup(content, 'lxml')
#     icon_title_tags = soup.find_all('div', class_='title')
#     for icon_tag in icon_title_tags:
#         title_name=icon_tag.text
#         print(title_name)
HTML = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>123</title>
        <a id='one' href='https://example.com/demo1'>
            <p class='test'>Test1</p>
            <p class='test'>Test2</p>
        </a>
        <a id='two' href='https://example.com/demo2'>
            <p class='test'>Test3</p>
            <p class='test'>Test4</p>
        </a>
        <a id='three' href='https://example.com/demo3'>
            <p class='test'>Test5</p>
            <p class='test'>Test6</p>
        </a>
        <a class="h">
            <p>tag1</p>
        </a>
        <a class="h hh hhh hhhh">
            <p>tag2</p>
        </a>
    </head>
    <body>
    </body>
</html>
'''
soup = BeautifulSoup(HTML, 'lxml')
print(soup.select_one('a'))
print(soup.select('a'))
print(soup.select_one('a').text)
print(soup.select_one('a').text.replace('\n', ' ', 1))  # 1:repacements
test12 = soup.select_one('a').text
print(test12[:6]+' '+test12[7:])
print(soup.select('a')[1])
print('***************************')
print(soup.select("a[href='https://example.com/demo1']"))
print(soup.select("a[href^='https://example.com']"))  # ^
print('***************************')
print(soup.select("a[href$='demo1']"))  # 'demo1':unique
print(soup.select("a[href$='demo']"))  # blank
print(soup.select("a[href*='demo']"))  # match any string that includes 'demo'
print('***************************')
print(soup.select('p.test'))  # match any tag that class is 'test'
print(soup.select('a p'))
print(soup.select_one('a p'))
print('***************************')
print(soup.select('a>p'))  # a:parent node;p:child node;has a small range
print(soup.select_one('a>p'))
print('***************************')
print(soup.select_one('p.test~p'))  # ~:sibling of p
print(soup.select('p.test~p'))
print('***************************')
print(soup.select_one('a').select('p'))
print(soup.select_one('a.h>p'))
print(soup.select_one('a.h hh hhh hhhh>p')) # None
print(soup.select_one('a.h.hh.hhh.hhhh>p'))