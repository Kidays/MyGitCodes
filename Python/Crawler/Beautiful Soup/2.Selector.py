# find_all
# def find_all(self,name=None,attrs={},recursive=True,text=None,limit=None,**kwargs)
from bs4 import BeautifulSoup
import re
html = '''
<html>
<head>
    <meta charset="UTF-8">
    <title>Beautiful Soup Demo</title>
</head>
<body>
<div>
    <ul>
        <li class="item1" value1="1234" value2="hello world"><a href="https://geekori.com">geekori.com</a></li>
        <li class="item2"><a href="https://www.jd.com">JD Mall</a></li>
    </ul>
    <button id="button1">OK</button>
    <ul>
        <li class="item3"><a href="https://www.taobao.com">TaoBao</a></li>
        <li class="item4"><a href="https://www.microsoft.com">Microsoft</a></li>
        <li class="item3"><a href="https://www.google.com">Google</a></li>
    </ul>
</div>
</body>
</html>
'''
soup=BeautifulSoup(html,'lxml')
ulTags=soup.find_all(name='ul')
print(type(ulTags))
for ulTag in ulTags:
    print(ulTag)
print("*******************************************")
tags=soup.find_all(attrrs={"class":"item"})
for tag in tags:
    print(tag)
tags=soup.find_all(class_='item2')
print(tags)
tags=soup.find_all(id='button1')
print(tags)
tags=soup.find_all(text='Google')                  
print(tags)
tags=soup.find_all(text=re.compile('JD'))
print(tags)
tags=soup.find(attrs={"class":"item1"})
print(type(tags))
print(tags)
# find_parent
# find_parents
# find_next_sibling
# find_next_siblings
# find_previous_sibling
# find_previous_siblings
# find_all_next
# find_next
# find_all_previous
# find_previous
