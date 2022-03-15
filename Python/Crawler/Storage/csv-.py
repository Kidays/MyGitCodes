# Comma-Separated Values
import csv
with open('data.csv', 'w',encoding='utf-8')as f:
    writer=csv.writer(f)
    writer.writerow(['ID','Product Name','Enterprise','Price'])
    writer.writerow(['0001','iPhone13','Apple',9999])
    writer.writerow(['0002','Tesla','Tesla',12345])
    writer.writerow(['0003','Xphone','Huawei',2345])
with open('data1.csv','w',encoding='utf-8')as f:
    writer=csv.writer(f,delimiter=';')
    writer.writerow(['ID','Product Name','Enterprise','Price'])
    writer.writerow(['0001','iPhone13','Apple',9999])
    writer.writerow(['0002','Tesla','Tesla',12345])
    writer.writerow(['0003','Xphone','Huawei',2345])
with open('data2.csv','w',encoding='utf-8')as f:
    writer=csv.writer(f)
    writer.writerow(['ID','Product Name','Enterprise','Price'])
    writer.writerows([['0001','iPhone13','Apple',9999],['0002','Tesla','Tesla',12345],['0003','Xphone','Huawei',2345]])
with open('data3.csv','w',encoding='utf-8')as f:
    fieldnames=['ID','Product Name','Enterprise','Price']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'ID':'0001','Product Name':'iPhone13','Enterprise':'Apple','Price':9999})
    writer.writerow({'ID':'0002','Product Name':'Tesla','Enterprise':'Tesla','Price':12345})
    writer.writerow({'ID':'0003','Product Name':'Xphone','Enterprise':'Huawei','Price':2345})
with open('data.csv','a',encoding='utf-8')as f:
    fieldnames=['ID','Product Name','Enterprise','Price']
    writer=csv.DictWriter(f,fieldnames=fieldnames)
    writer.writerow({'ID':'0004','Product Name':'iPad','Enterprise':'Apple','Price':2345})
with open('data.csv','r',encoding='utf-8')as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
import pandas as pd
df=pd.read_csv('data.csv')
print(df)