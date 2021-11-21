import re
# findall: return a list
result = re.findall('bike', 'bike')
print(result)  # ['bike']
result = re.findall('bike', 'This is my bike,where is your bike?')
print(result)  # ['bike', 'bike']
s = '12-a-abc43-a-xyz---78-A-ytr'
result = re.findall(r'\d\d-a-[a-z]{3}', s)
print(result)  # ['12-a-abc', '43-a-xyz']
result = re.findall(r'(\d\d)-a-([a-z]{3})', s)
print(result)  # [('12', 'abc'), ('43', 'xyz')]
result = re.match(r'(\d\d)-a-([a-z]{3})', s)
print(result.groups())  # ('12', 'abc')
result = re.match(r'(\d\d)-a-([a-z]{3})', s)
print(result.group())  # 12-a-abc
result = re.match(r'(\d\d)-a-([a-z]{3})', s)
print(result.group(2))  # abc
print('**************************************')
result = re.findall(r'\d\d-a-[a-z]{3}', s, re.I)  # re.I: ignorecase
print(result)  # ['12-a-abc', '43-a-xyz', '78-A-ytr']
result = re.findall(r'(\d\d)-a-([a-z]{3})', s, re.I)
print(result)  # [('12', 'abc'), ('43', 'xyz'), ('78', 'ytr')]
result = re.findall(r'(\d\d)-a-([a-z]){3}', s, re.I)
print(result)  # [('12', 'c'), ('43', 'z'), ('78', 'r')]
result = re.finditer(r'(\d){2}-a-([a-z]){3}', s, re.I)
print(result)  # <callable_iterator object at 0x0000018BE68F3FA0>
for x in result:
    print(x.group(), end='<')
    groups = x.groups()
    for i in groups:
        print(i, end='')
    print('>')
# 12-a-abc<2c>
# 43-a-xyz<3z>
# 78-A-ytr<8r>
print('**************************************')
# sub
# subn： return a tuple
result = re.sub('Bill', 'Mike', 'Bill is my son')  # first search ,then replace
print(result)  # Mike is my son
result = re.subn('Bill', 'Mike', 'Bill is my son, I love Bill')
print(result)  # ('Mike is my son, I love Mike', 2)
print(result[0])  # Mike is my son, I love Mike
result = re.subn('([0-9])([a-z]+)', r'NO.(\1-\2)', '01-1abc,02-2xyz,03-9hgf')
print(result)  # ('01-NO.(1-abc),02-NO.(2-xyz),03-NO.(9-hgf)', 3)
print('**************************************')
# split： return a list of segmentation results
result = re.split(';', 'Bill;Mike;John')
print(result)  # ['Bill','Mike','John']
result = re.split('[,;.\s]+', 'a,b,,d,d;x    c;d.   e')  # \s: space character
print(result)
result = re.split('[a-z]{3}-[0-9]{2}', 'testabc-4321productxyz-43abill')
print(result)
result = re.split('[a-z]{3}-[0-9]{2}',
                  'testabc-4321productxyz-43abill', maxsplit=1)
print(result)
print('**************************************')
# most commonly used regular expressions
# Email: '[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[a-zA-Z](2,3)'
# IP Address: '\d(1,3)\.\d{1,3}\.\d{1,3})\.\d{1,3}'
# Web Address: 'https?:/{2}\w.+'
