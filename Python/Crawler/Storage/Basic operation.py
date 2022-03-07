import sys
import os
os.chdir(sys.path[0])  # enable file relative path
f = open('./test.txt', 'w')
# second parameter:
# r:default read
# w:write
# a:add to
# b:binary mode
# t:text mode
# +:read&write  r+,w+,a+;
# r+: if file does not exist,report exceptions
# w+:if file does not exist,create new file,else overwrite
# a+:if file does not exist,create new file,else add new contents
print(f.write('I love '))  # 7
print(f.write('python'))  # 6
f.close()
f = open('./test.txt', 'r')
print(f.read(7))  # I love
print(f.read(6))  # python
f.close()
try:
    f = open('./test2.txt', 'r+')
except Exception as e:
    print(e)
f = open('./test2.txt', 'a+')
print(f.write('Hello'))  # How are you?Hello
f.close()
f = open('./test2.txt', 'a+')
print(f.read())
f.seek(0)
print(f.read())
f.close()
try:
    f = open('./test2.txt', 'w+')
    print(f.read())  # nothing
    f.write('How are you?')
    f.seek(0)
    print(f.read())  # How are you?
finally:
    f.close()
