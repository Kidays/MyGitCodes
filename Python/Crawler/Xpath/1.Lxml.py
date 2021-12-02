import os
import sys
from lxml import etree
os.chdir(sys.path[0])
parser = etree.HTMLParser()
print(type(parser))  # <class 'lxml.etree.HTMLParser'>
tree = etree.parse('test.html', parser)
root = tree.getroot()
result = etree.tostring(root, encoding='utf-8',
                        pretty_print=True, method="html")
print(str(result, 'utf-8'))
print(root.tag)  # html
print('lang=', root.get('lang'))  # lang= en
print('charset=', root[0][0].get('charset'))  # charset= UTF-8
print('charset=', root[0][1].text)  # charset= 通过Xpath过滤的HTML文档
# <!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">
#     <title>通过Xpath过滤的HTML文档</title>
# </head>

# <body></body>

# </html>
titles = tree.xpath('/html/head/title')
if len(titles) > 0:
    print(titles[0].text)
html = '''
<div>
    <ul>
        <li class="item1"><a href="https://geekori.com">geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com">京东商城</a></li>
        <li class="itme3"><a href="https://taobao.com">淘宝</a></li>
        <li class="itme4" value="1234"><a href="https://www.microsot.com">微软</a></li>
    </ul>
</div>
'''
tree = etree.HTML(html)
# use xpath to locate <li> node
aTags = tree.xpath("//li[@class='item2']")
if len(aTags) > 0:
    # <li>  <a>
    print(aTags[0][0].get('href'), aTags[0][0].text)  # https://www.jd.com 京东商城

