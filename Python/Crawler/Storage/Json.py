# [
#     {"item1":"value1","item2":30,"item3":10},
#     {"item1":"value2","item2":30,"item3":20}
# ]
import dicttoxml
import json
import os
import sys
from this import d
os.chdir(sys.path[0])
data = {'name': 'Bill',
        'company': 'Microsoft',
        'age': 34}  # dict
jsonStr = json.dumps(data)  # dict to json
print(type(jsonStr))  # str
print(jsonStr)
data = json.loads(jsonStr)  # json to dict
print(type(data))  # dict
print(data)
s = '''{'name':'Bill','company':'Microsoft',
'age':34}'''
data = eval(s)  # json to dict
print(type(data))
print(data)
print(data['company'])
f = open('files/products.json', 'r', encoding='utf-8')
jsonStr = f.read()
json1 = eval(jsonStr)
json2 = json.loads(jsonStr)
print(json1)
print(json2)
print(json2[0]['name'])
f.close()


class Product:
    def __init__(self, d):
        self.__dict__ = d


f = open('files/products copy.json', 'r')
jsonStr = f.read()
myl = json.loads(jsonStr, object_hook=Product)
print('name', '=', myl.name)
print('price', '=', myl.price)
print('count', '=', myl.count)
print('-------------------------------------')


def json2Product(d):
    return Product(d)


my2 = json.loads(jsonStr, object_hook=json2Product)
print('name', '=', my2.name)
print('price', '=', my2.price)
print('count', '=', my2.count)
f.close()


class Product1:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


def Product2Dict(obj):
    return{
        'name': obj.name,
        'price': obj.price,
        'count': obj.count
    }


product = Product1('Tesla', 100000, 20)
jsonStr = json.dumps(product, default=Product2Dict, ensure_ascii=False)
print(jsonStr)
f = open('files/products.json', 'r', encoding='utf-8')
jsonStr = f.read()
d = json.loads(jsonStr)
xmlStr = dicttoxml.dicttoxml(d).decode('utf-8')
print(xmlStr)
f.close()
