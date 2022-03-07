import fileinput
import os
import sys
os.chdir(sys.path[0])
f = open('./urls.txt', 'r+')
url = ''
while True:
    url = f.readline()
    url = url.rstrip()  # remove spaces,LF(line breaks),CR(carriage returns),tabs to the right
    if url == '':
        break
    else:
        print(url)
print('-------------------------------')
f.seek(0)
print(f.readlines())
f.write('https://jiketiku.com'+os.linesep)
f.close()
f = open('./urls.txt', 'a+')
urlList = ['https://geekori.com', os.linesep,
           'https://www.google.com'+os.linesep]
f.writelines(urlList)
f.close()
print('-------------------------------')
fileobj = fileinput.input('./urls.txt')
print(type(fileobj))
print(fileobj.readline().rstrip())
for line in fileobj:
    line = line.rstrip()
    if line != '':
        print(fileobj.lineno(), ':', line)
    else:
        print(fileobj.filename())
