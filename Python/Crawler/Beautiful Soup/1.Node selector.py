from bs4 import BeautifulSoup
html = '''
<html>
    <head><title>This is a demo</title></head>
    <body>
        <a href='a.html'>First page</a>
        <p>
        <a href='b.html'>Second page</a>
    </body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
print('<'+soup.title.string+'>')
print('['+soup.a["href"]+']')
print(soup.prettify())
html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup demo</title>
</head>
<body>
<div>
    <ul>
        <li class="item1" value1="1234" value2="hello world"><a href="https://geekori.com">geekori</a></li>
        <li class="item2" ><a href="https://www.jd.com">JD</a></li>
        <li class="item3" ><a href="https://www.taobao.com">TaoBao</a></li>
        <li class="item4" ><a href="https://www.microsoft.com">Microsoft</a></li>
    </ul>
</div>
</body>
</html>
'''
soup = BeautifulSoup(html, 'lxml')
print(soup.title.name)
print(soup.li.attrs)
print(soup.li.attrs["value2"])
print(soup.li["value1"])
print(soup.a['href'])
print(soup.head)
print(type(soup.head))
head=soup.head
print(head.title.string)
print(soup.body.div.ul.li.a['href'])
print(soup.head.contents)
print(soup.head.children)
print(soup.body.div.ul.children)
print(soup.head.descendants)
for i,child in enumerate(soup.body.div.ul.contents):
    print(i,child)
print('*************************')
i=1
for child in soup.body.div.ul.children:
    print('<',i,'>',child,end=' ')
    i+=1
print(soup.a.parent)
print(soup.a.parent['class'])
print(soup.a.parents)
print('************************')
for parent in soup.a.parents:
    print('<',parent.name,'>')
secondli=soup.li.next_sibling.next_sibling
print("the first li node's next li node",secondli)
print("the second li node's previous li node",secondli.previous_sibling.previous_sibling['class'])
for sibling in secondli.next_siblings:
    print(type(sibling))
    if str.strip(sibling.string)==" ":
        print('\n')
    else:
        print(sibling)