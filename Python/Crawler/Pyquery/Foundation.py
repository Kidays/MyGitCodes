import requests
import pyquery
from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value="1234" value2="hello world"><a href="http://geekori.com">geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com">JD</a></li>
    </ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">taobao</a></li>
        <li class="item"><a href="https://www.microsoft.com">microsoft</a></li>
        <li class="item3"><a href="https://www.google.com">google</a></li>
    </ul>
</div>   
'''
doc = pq(html)
for a in doc('a'):
    print(a.get('href'), '---', a.text)
doc = pq(url='https://www.jd.com')
print(doc('title'))
doc=pq(requests.get('https://www.jd.com').text)
print(doc('title'))
html2 = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value="1234" value2="hello world"><a href="http://geekori.com">geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com">JD</a></li>
    </ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">taobao</a></li>
        <li class="item"><a href="https://www.microsoft.com">microsoft</a></li>
        <li class="item3"><a href="https://www.google.com">google</a></li>
    </ul>
</div>   
'''
doc=pq(html2)
result=doc('#panel .list1')
print(type(result))
print(result('.item'))
print(result('a')[1].get('href'),result('a')[1].text)
print("-------------------------------")
doc=pq(requests.get('https://jd.com').text)
group1=doc('#navitems-group1')
print(group1('a')[0].text.strip(' '),group1('a')[1].text.strip(' '),group1('a')[2].text)
group2=doc('#navitems-group2')
print(group2('a')[0].text.strip(' '),group2('a')[1].text.strip(' '))
group3=doc('#navitems-group3')
print(group3('a')[0].text.strip(' '),group3('a')[1].text.strip(' '))