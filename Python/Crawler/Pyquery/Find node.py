from pyquery import PyQuery as pq
from lxml import etree
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value="1234" value2="hello world"><a href="http://geekori.com">geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com">JD</a></li>
    </ul>
    <ul class="list2">
        <li class="item3"><a href="https://www.taobao.com">taobao</a></li>
        <li class="item"><a href="https://www.microsoft.com">microsoft</a></li>
        <li class="item3"><a href="https://www.google.com">google</a></li>
    </ul>
</div>   
'''
doc = pq(html)  # doc=pq(filename='test.html')
result=doc('.list1')
aList=result.find('a')
print(type(aList))
for a in aList:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))
print('------------------------------------')
result=doc('.item')
aList=result.children('a')
for a in aList:
    print(str(etree.tostring(a,pretty_print=True,encoding='utf-8'),'utf-8'))
print('------------------------------------')
print(result.parent())
print(len(result.parents()))
print(len(result.parents('#panel')),result.parents('#panel')[0].tag)
print('------------------------------------')
print(result.siblings())
print(result.siblings('.item1'))