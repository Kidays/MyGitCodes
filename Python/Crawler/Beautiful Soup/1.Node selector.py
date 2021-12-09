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