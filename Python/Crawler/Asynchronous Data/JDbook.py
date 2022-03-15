import requests
import re
import json
import csv
import os
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}
fetch_comment_count=15
index=0
page_index=10
flag=True
while flag:
    url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=11993134&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(page_index)
    page_index+=1
    html=requests.get(url,headers=headers)
    text=str(html.content,encoding='iso-8859-1')
    # print(text)
    leftIndex=text.find('{')
    rightIndex=text.rfind('}')
    json_str=text.replace('fetchJSON_comment98(','')
    json_str=json_str.replace("(",'')
    json_str=json_str.replace("true",'"true"')
    json_str=json_str.replace("false",'"false"')
    json_str=json_str.replace("null",'"null"')
    json_str=json_str.replace(";",'')
    json_obj=json.loads(json_str)
    for i in range(0,len(json_obj['comments'])):
        try:
            comment=json_obj['comments'][i]['content'].encode(encoding='iso-8859-1').decode('GB18030')
            if comment!='此用户未填写评价内容':
                print('<',index+1,'>',comment)
                creationTime=json_obj['comments'][i]['creationTime']
                nickname=json_obj['comments'][i]['nickname'].encode(encoding='iso-8859-1').decode('GB18030')
                print(creationTime)
                print(nickname)
                print('---------------------------')
                index+=1
        except:
            pass
        if index==fetch_comment_count:
            flag=False
            break