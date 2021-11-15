import re
m = re.match('bird', 'bird')
if m is not None:
    print(m.group())  # bird
print(m.__class__.__name__)  # Matc
m = re.match('hello', 'world')
if m is not None:
    print(m.group())
print(m)  # None
m = re.match('hello', 'hello world')
if m is not None:
    print(m.group())  # hello
print(m)  # <re.Match object; span=(0, 5), match='hello'>
print('************************************')
m = re.search('abc', 'xabcy')
print(m.group())  # abc
m = re.match('python', 'I love python')
if m is not None:
    print(m.group())
print(m)  # None
m = re.search('python', 'I love python')
if m is not None:
    print(m.group())  # python
print(m)
print('************************************')
s = 'Bill|Mike|John'
m = re.match(s, 'Bill')
if m is not None:
    print(m.group())
m = re.match(s, 'Bill:my friend')
if m is not None:
    print(m.group())
m = re.match(s, 'My friend:Bill')
if m is not None:
    print(m.group())
print(m)  # None
m = re.search(s, 'Where is Mike?')
if m is not None:
    print(m.group())
print('************************************')
# . matches any single character
# / escape character
s = '.ind'
m = re.match(s, 'bind')
if m is not None:
    print(m.group())  # bind
m = re.match(s, 'binding')
print('<', str(m))
m = re.match(s, 'bin')
print(m)  # None
m = re.search(s, '<bind>')
print(m.group())  # bind
s1 = '3.14'
s2 = '3/.14'
m = re.match(s1, '3.14')
print(m)
m = re.match(s2, '3.14')
print(m)  # None
m = re.match(s1, '3314')
print(m, m.group())
m = re.match(s2, '3314')
print(m)  # None
print('************************************')
