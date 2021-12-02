from lxml import etree
import sys
import os
os.chdir(sys.path[0])
# //: select all the nodes that meet the requirements
# //*: select all nodes
# //li: select all <li> nodes
parser = etree.HTMLParser()
html = etree.parse('demo.html', parser)
nodes = html.xpath('//*')
print('共', len(nodes), '个节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].tag, end=' ')


def printNodeTree(node, indent):
    print(indent+node.tag)
    indent += ' '
    children = node.getchildren()
    if len(children) > 0:
        for i in range(0, len(children)):
            printNodeTree(children[i], indent)


print()
printNodeTree(nodes[0], "")
nodes = html.xpath('//a')
print()
print('共', len(nodes), '个<a>节点')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')
print('\n')
print('************************************')
nodes = html.xpath('//li/a')
print('total ', len(nodes), ' nodes')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')
print()
nodes = html.xpath('//ul//a')
print(nodes)
for i in range(0, len(nodes)):
    print(nodes[i].text, end=' ')
print()
nodes = html.xpath('//ul/a')
print('total ', len(nodes), ' nodes')
print(nodes)
print('************************************')
# ..: '//a[@class="class"]/..'       '//a[@class="class"]/parent::*'
#
result = html.xpath('//a[@href="https://www.jd.com"]/../@class')
print('attribute of class=', result)
result = html.xpath('//a[@href="https://www.jd.com"]/parent::*/@class')
print('attritbute of class=', result)
