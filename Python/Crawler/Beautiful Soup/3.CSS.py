import requests
from bs4 import BeautifulSoup
html = '''
<div>
    <ul>
        <li class="item1" value="1234" value2="hello world">
            <a href="http://geekori.com">geekori.com</a>
        </li>
        <li class="item">
            <a href="https://www.jd.com">JD</a>
            <a href="https://www.baidu.com">Baidu</a>
        </li>
    </ul>
    <button id="button1">OK</button>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">Taobao</a></li>
        <li class="item4"><a href="https://www.microsoft.com">Microsoft</a></li>
        <li class="item"><a href="https://www.google.com">Google</a></li>
    </ul>
</div>
'''
soup = BeautifulSoup(html, 'lxml')
tags = soup.select('.item')
for tag in tags:
    print(tag)
tags = soup.select('#button1')
print(tags)
print('********************************')
tags = soup.select('a')[2:]
for tag in tags:
    print(tag)
print('********************************')
# Nest select
tags = soup.select('.item')  # select
for tag in tags:
    aTags = tag.select('a')
    for aTag in aTags:
        print(aTag)
        print(aTag['href'], aTag.get_text())  # get_text
print('********************************')
for tag in tags:
    aTags = tag.find_all(name='a')  # find_all
    for aTag in aTags:
        print(aTag)
        print(aTag.attrs['href'], aTag.string)


#################################################

result = requests.get('https://www.jd.com')
soup = BeautifulSoup(result.text, 'lxml')
aTag = soup.select('#navitems-group1 > li.fore1 > a')
print(aTag)
print(aTag[0].string, aTag[0]['href'])
print('----------------------------')
group1 = soup.select('#navitems-group1')
group2 = soup.select('#navitems-group2')
group3 = soup.select('#navitems-group3')
for value in group1:
    aTags = value.find_all(name="a")
    for aTag in aTags:
        print(aTag.string)
for value in group2:
    aTags = value.find_all(name="a")
    for aTag in aTags:
        print(aTag.string)
for value in group3:
    aTags = value.find_all(name="a")
    for aTag in aTags:
        print(aTag.string)
