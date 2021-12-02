# //a[@lcass="item1"]
from lxml import etree
import os
import sys
os.chdir(sys.path[0])
parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)
nodes = html.xpath('//a[@href="https://geekori.com"]')
print('total', len(nodes), 'nodes')
for i in range(0, len(nodes)):
    print(nodes[i].text)
# all the href attribute of the selected node that contains "www"
nodes = html.xpath('//a[contains(@href,"www")]')
print('total', len(nodes), 'nodes')
for i in range(0, len(nodes)):
    print(nodes[i].text)
# get all <a> nodes attributes that contains "www"
urls = html.xpath('//a[contains(@href,"www")]/@href')
for i in range(0, len(nodes)):
    print(urls[i])
print('******************************************')
# multi-attribute matches
# or and
aList = html.xpath(
    '//a[@href="https://www.jd.com" or @href="https://geekori.com"]')
for a in aList:
    print(a.text, a.get('href'))
aList = html.xpath('//a[contains(@href,"www") and ../@value="1234"]')
for a in aList:
    print(a.text, a.get('href'))
print('******************************************')
# | + - * div = != < <= > >= or and mod
# '\\li[positon()=3]' '\\li[3]'
text = '''
<div>
    <a href="https://geekori.com">geekori.com</a>
    <a href="https://www.jd.com">JingDong</a>
    <a href="https://www.google.com">Google</a>
    <a href="https://www.microsoft.com">Microsoft</a>
</div>
'''
html = etree.HTML(text)
a1 = html.xpath('//a[1]/text()')
a2 = html.xpath('//a[2]/text()')
print(a1, a2)
lasta = html.xpath('//a[last()]/text()')
print(lasta)
aList = html.xpath('//a[position() > 2]/text()')
print(aList)
aList = html.xpath('//a[position()=2 or position()=last()-1]/text()')
print(aList)
print('******************************************')
# select the joint axis
text = '''
<html>
<head>
    <meta charset='UTF-8'>
    <title>XPath Demo</title>
</head>
<body class='item'>
<div>
    <ul class='item'>
        <li class='item1'><a href='https://geekori.com'>geekori.com</a></li>
        <li class='item2'><a href='https://www.jd.com'>JD</a><value url='https://geekori.com'/><value url='https://www.google.com'/></li>
        <li class='item3'><a href='https://www.taobao.com'>taobao</a><a href='https://www.tmall.com/'>tianmao</a></li>
        <li class='item4' value='1234'><a href='https://www.microsoft.com'>Microsoft</a></li>
        <li class='item5'><a href='https://www.google.com'>Google</a></li>
    </ul>
</div>
</body>
</html>
'''
html = etree.HTML(text)
# get all the ancestor nodes: html body div ul
result = html.xpath('//li[1]/ancestor::*')
for value in result:
    print(value.tag, end=' ')
print()
# body ul
result = html.xpath('//li[1]/ancestor::*[@class="item"]')
for value in result:
    print(value.tag, end=' ')
print()
result = html.xpath('//li[4]/attribute::*')
# item4 1234
print(result)
result = html.xpath('//li[3]/child::*')
for value in result:
    # https://www.taobao.com taobao https://www.tmall.com/ tianmao
    print(value.get('href'), value.text, end=' ')
print()
result = html.xpath('//li[2]/descendant::value')
for value in result:
    # https://geekori.com https://www.google.com 
    print(value.get('url'), end=' ')
print()
result = html.xpath('//li[1]/following::*')
for value in result:
    # li a value value li a a li a li a
    print(value.tag, end=' ')
print()
result = html.xpath('//li[1]/following::*[position() >4]')
for value in result:
    # li a a li a li a
    print(value.tag, end=' ')
print()
result = html.xpath('//li[1]/following-sibling::*')
for value in result:
    # the same level node
    print(value.tag, end=' ')
print()
