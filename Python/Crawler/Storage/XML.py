import xmltodict
import dicttoxml
from xml.dom.minidom import parseString
from xml.etree.ElementTree import parse
import sys
import os
os.chdir(sys.path[0])
doc = parse('products.xml')
for item in doc.iterfind('products/product'):
    id = item.findtext('id')
    name = item.findtext('name')
    price = item.findtext('price')
    print('uuid', '=', item.get('uuid'))
    print('id', '=', id)
    print('name', '=', name)
    print('price', '=', price)
    print('---------------------------------------')
# d = [20, 'names', {'name': 'Bill', 'age': 30, 'salary': 2000}, {
#     'name': 'wangjun', 'age': 34, 'salary': 3000}, {'name': 'John', 'age': 25, 'salary': 2500}]
# bxml = dicttoxml.dicttoxml(d, custom_root='persons')  # bytes
# xml = bxml.decode('utf-8')
# print(xml)
# dom = parseString(xml)
# prettyxml = dom.toprettyxml(indent=' ')
# os.makedirs('files', exist_ok=True)
# f = open('files/persons.xml', 'w', encoding='utf-8')
# f.write(prettyxml)
# f.close()
# print('--------------------------------')
f = open('files/persons.xml', 'rt', encoding='utf-8')
xml = f.read()
d = xmltodict.parse(xml)
print(d)
f.close()
import pprint
print(d)
pp=pprint.PrettyPrinter(indent=4)
pp.pprint(d)