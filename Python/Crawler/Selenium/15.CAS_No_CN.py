import requests
import csv
from lxml import etree
url = 'https://www.chemsrc.com/casindex/2.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'}
casindex = requests.get(url, headers=headers)
parser = etree.HTMLParser()
# print(casindex)
casindex = etree.HTML(casindex.text)
# tabcontent = casindex.xpath('//*[@id="idxTbl"]')
tabhead = casindex.xpath('//*[@id="idxTbl"]/thead/tr/th')
head_list = []
for head in tabhead:
    head = head.xpath('./text()')[0]
    head_list.append(head)
print(head_list)
subs_content = casindex.xpath('//*[@id="idxTbl"]/tr')
for subs in subs_content:
    sub_content = []
    sub_name = subs.xpath('./td[1]/a/text()')[0]
    sub_content.append(sub_name)
    sub_english_name = subs.xpath('./td[2]/text()')[0]
    sub_content.append(sub_english_name)
    sub_attributes = subs.xpath('./td[3]/text()')[0]
    sub_content.append(sub_attributes)
    sub_CAS_No = subs.xpath('./td[4]/a/text()')[0]
    sub_content.append(sub_CAS_No)
    sub_formula_text = subs.xpath('./td[5]/text()')
    sub_formula_number = subs.xpath('./td[5]/sub/text()')
    sub_formula = []
    # if no range: TypeError: 'int' object is not iterable
    for i in range(len(sub_formula_text)-1):
        sub_formula.append(sub_formula_text[i]+sub_formula_number[i])
    print(sub_formula)
    sub_formula_text = ''
    for i in range(len(sub_formula)):
        sub_formula_text += sub_formula[i]
    sub_content.append(sub_formula_text)
    print(sub_content)
    # //*[@id="idxTbl"]/tbody/tr[1]/td[1]/a
