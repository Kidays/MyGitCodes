import re
email = '\w+@(\w+\.)*\w+\.com'
emailList = ['abc@126.com', 'test@mail.geekori.com',
             'test-abc@grrkori.com', 'abc@geekori.com.cn']
for value in emailList:
    m = re.match(email, value)
    if m is not None:
        print(m.group())
    else:
        print('{} does not match {}'.format(value, email))
print('**************************************')
m = re.match('(\d\d\d)-(\d\d)', '123-45')
print(m.group())
m = re.match('(\d{3})-(\d{4})-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())  # 123-4567-xy
    print(m.group(1))  # 123
    print(m.group(2))  # 4567
    print(m.group(3))  # xy
    print(m.groups())  # ('123' '4567' 'xy')
print('**************************************')
m = re.match('\d{3}-\d{4}-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())  # ('xy',)
    print(m.groups()[0])  # xy
print('**************************************')
m = re.match('\d{3}-\d{4}-[a-z]{2}', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.groups())
print('**************************************')
# ^: beginning with
# $: end with
# \b: word boundary
m = re.search('^The', 'The end')
print(m)
if m is not None:
    print(m.group())  # The
m = re.search('^The', 'end. The')
print(m)  # None
if m is not None:
    print(m.group())
m = re.search('The$', 'end. The')
print(m)
if m is not None:
    print(m.group())  # The
m = re.search('The$', 'The end')
print(m)  # None
if m is not None:
    print(m.group())
m = re.search(r'\bthis', "What's this?")  # r: \b don't escape
print(m)
if m is not None:
    print(m.group())  # this
m = re.search(r'\bthis', "What'sthis?")
print(m)  # None
if m is not None:
    print(m.group())
m = re.search(r'\bthis\b', "What's this?")
print(m)
if m is not None:
    print(m.group())  # this
m = re.search(r'\bthis\b', "What's thisb")
print(m)  # None
if m is not None:
    print(m.group())
m = re.search(r'\bthis\b', "What's this2")
print(m)  # None
if m is not None:
    print(m.group())
print('**************************************')