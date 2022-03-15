# Asynchronous Javascript and XML:AJAx
import requests
import json
import random
import string
import os
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}
word = input('Please input your keywords:')
print(word)
dir_name = ''.join(random.sample(string.ascii_letters+string.digits, 8))
print('img save in', dir_name)
os.mkdir(dir_name)
max_value = 100
current_value = 0
image_index = 1
while current_value < max_value:
    result = requests.get('https://image.baidu.com/search/acjson?tn=resultjson_com&logid=11134655420435027584&ipn=rj&ct=201326592&is=&fp=result&fr=&word={}&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={}&rn=30&gsm=1e&1647178131032='.format(word, word, current_value), headers=headers)
    json_str = result.content
    json_doc = str(json_str, 'utf-8')
    imageResult = json.loads(json_doc)
    data = imageResult['data']
    for record in data:
        url = record.get('middleURL')
        if url != None:
            print('downloading:', url)
            r = requests.get(url)
            filename = dir_name+'/'+str(image_index).zfill(10)+'.png'
            # zfill: returns a string of the specified length
            with open(filename, 'wb')as f:
                f.write(r.content)
                image_index += 1
    current_value += 30
print('download complete!')
