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