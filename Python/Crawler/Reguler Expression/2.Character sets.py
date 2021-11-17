import re
m = re.match('[abcd]', 'a')  # [abcd]:a|b|c|d
print(m.group())  # a
m = re.match('a|b|c|d', 'b')
print(m.group())  # b
m = re.match('[abcd]', 'ab')
print(m.group())  # a
m = re.search('[bcd]', 'ab')
print(m.group())  # b
m = re.match('ab|cd', 'cd')
print(m.group())  # cd
m = re.match('[ab][cd]', 'ac')
print(m.group())  # ac
m = re.match('[ab][cd][ef][gh]', 'adfh')
print(m.group())  # adfh
m = re.match('[ab][cd][ef][gh]', 'abeg')
print(m)  # None
print('***********************************')
s = 'a*'  # *: 0-n
strList = ['', 'a', 'aa', 'baa']  # '' 'a' 'aa'
for value in strList:
    m = re.match(s, value)
    print(m)
# <re.Match object; span=(0, 0), match=''>
# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(0, 2), match='aa'>
# <re.Match object; span=(0, 0), match=''>
s = 'a+'
strList = ['', 'a', 'aa', 'baa']
for value in strList:
    m = re.match(s, value)
    print(m)
# None
# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(0, 2), match='aa'>
# None
s = '(abc)+'
print(re.match(s, 'abcabcabc'))
# \w: any character or number; ?: not essential; \d: any number
s = '\w?wow(\d?)+'
m = re.search(s, 'awow')
print(m)  # <re.Match object; span=(0, 4), match='awow'>
m = re.search(s, '1wow2')
print(m)  # <re.Match object; span=(0, 5), match='1wow2'>
m = re.search(s, 'bawow2433')
print(m)  # <re.Match object; span=(1, 9), match='awow2433'>
m = re.match(s, 'bawow2433')
print(m)  # None
s = '\d{3}-[a-z]{3}'
strList = ['123-abc', '432-xyz', '1234-zyx', '1-zysabc', '543-xyz^%ab']
for value in strList:
    m = re.match(s, value)
    if m is not None:
        print(m.group())
    else:
        print('{} does not match {}'.format(value, s))
# 123-abc
# 432-xyz
# 1234-zyx does not match \d{3}-[a-z]{3}        
# 1-zysabc does not match \d{3}-[a-z]{3}        
# 543-xyz
print('***********************************')
s='[a-z]?\d+'
strList=['1234','a123','ab432','b234abc']
for value in strList:
    m=re.match(s,value)
    if m is not None:
        print(m.group())
    else:
        print(m)
# 1234
# a123
# None
# b234
