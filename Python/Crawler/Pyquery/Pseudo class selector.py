import pyquery
from pyquery import PyQuery as pq
html='''
<div id="panel">
    <ul>
        <li class="item1"><a href="http://geekori.com">geekori.com</a></li>
        <li class="item"><a href="https://www.jd.com">JD</a></li>
        <li class="item3"><a href="https://www.taobao.com">taobao</a></li>
        <li class="item"><a href="https://www.microsoft.com">microsoft</a></li>
        <li class="item3"><a href="https://www.google.com">google</a></li>
    </ul>
</div>   
'''
doc=pq(html)
li=doc('li:first-child')
print(li)
li=doc('li:last-child')
print(li)
li=doc('li:nth-child(3)')
print(li)
print('---------------------------------------')
li=doc('li:lt(2)')
print(li)
li=doc('li:gt(3)')
print(li)
li=doc('li:nth-child(2n+1)')
print(li)
li=doc('li:contains(com)')
print(li)
al1=doc(':contains(com)')
print(len(al1))
for t in al1:
    print(t.tag,end=' ')