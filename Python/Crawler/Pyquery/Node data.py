from lxml import etree
from pyquery import PyQuery as pq
html = '''
<div id="panel">
    <ul class="list1">
        <li class="item1" value1="1234" value2="hello world">
            hello
            123
            <a href="http://geekori.com">geekori.com</a>
        </li>
        <li class="item"><a href="https://www.jd.com">JD</a></li>
        <li class="item2"></li>
    </ul>
    <ul class="list2">
        <li class="item1"><a href="https://www.taobao.com">taobao</a></li>
        <li class="item"><a href="https://www.microsoft.com">microsoft</a></li>
        <li class="item3"><a href="https://www.google.com">google</a></li>
    </ul>
</div>   
'''
doc = pq(html)
result = doc('.item1')
print(result[0].tag)  # li
print('value1:', result[0].get('value1'))  # 1234
print('value2:', result.attr('value2'))  # hello world
print('value2:', result.attr.value2)  # hello world
print(result.text())  # geekori.com taobao
for node in result:
    print(node.text)
print(str(etree.tostring(result[0], pretty_print=True), 'utf-8'))
print(result.html())  # inner code
print('-----------------------------')
for node in result:
    print(str(etree.tostring(node, pretty_print=True), 'utf-8'))
print('-----------------------------')
html = '''
<div id='panel'>
    <ul class='list1'>
        <li class='item1 item2 item3'>google</li>
        <li class='item1 item2'>microsoft</li>
    </ul>
</div>
'''
doc = pq(html)
li = doc('.item1.item2')
print(li)
li.addClass('myitem')
print(li)
li.removeClass('item1')
print(li)
li.removeClass('item2 item3')
print(li)
print('-----------------------------')
html = '''
<div id='panel'>
    <ul class='list1'>
        <li class='item1 item2 item3'>google</li>
        <li class='item1 item2'>microsoft</li>
    </ul>
</div>
'''
doc = pq(html)
li = doc('.item1.item2')
print(li)
print(li.text())  # google microsoft
print(li.html())  # google
li.attr('id', 'list')  # add
li.attr('class', 'myitem1,myitem2')  # modify
print(li)
li.removeAttr('id')
print(li)
li.text('list')
print(li)
li.text("\n<a href='https://www.google.com'/>\n")
print(li)
print(li.text())
print('-----------------------------')
li.html("\n<a href='https://www.google.com'/>\n")
print(li)
print(li.text())
print(li.html())
print('-----------------------------')
html = '''
<div id='panel'>
    <ul class='list1'>
        <li class='item1 item2 item3'>google<p>microsoft</p>Facebook</li>
    </ul>
</div>
'''
doc=pq(html)
li=doc('.item1.item2')
print(li.text())
li.remove('p')
print(li.text())
li=doc('.item1.item2')
print(li.find('p').remove())
print(li.text())