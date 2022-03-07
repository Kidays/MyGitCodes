# Comma-Separated Values
import csv
with open('data.csv', 'w+')as f:
    writer = csv.writer(f)
    writer.writerow(['field1', 'field2', 'field3'])
    writer.writerow(['data11', 'data12', 'data13'])
    writer.writerow(['data21', 'data22', 'data23'])
writer=csv.writer(f,delimiter=';')
with open('data.csv','w',encoding='utf-8')as f:
    writer=csv.writer(f)
    writer.writerow(['ID','name','enterprise','price'])
    writer.writerow(['0001','iPhone9','Apple','9999'])
with open('data.csv','w')as f:
    writer=csv.writer(f)
    writer.writerow(['field1','field2'])
    writer.writerows([['data11','data12'],['data21','data22']])
with open('data.csv','w')as f:
    fieldnames=['field1','field2','field3']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'field1':'data11','field2':'data12','field3':'data13'})
    writer.writerow({'field1':'data21','field2':'data22','field3':'data23'})