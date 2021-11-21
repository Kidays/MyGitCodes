from sre_constants import JUMP
import requests
import re
import chardet
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29'}
jokeLists = []



def verifySex(class_name):
    if class_name == 'womenIcon':
        return 'Woman'
    else:
        return 'Man'


def getJoke(url):
    res = requests.get(url)
    # chardet.detect(res)
    # res.content.decode('gbk')
    # get id
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    # /D: matching Unicode not a number
    levels = re.findall(
        '<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    # get sex
    sexs = re.findall('<div class="articleGender(.*?)">', res.text, re.S)
    # get content
    contents = re.findall(
        '<div class="article.*?<span>(.*?)</span>', res.text, re.S)
    # get index
    laughs = re.findall(
        '<span.*?<i class="number">(\d+)</i>.*?</span>', res.text, re.S)
    # get number of comments
    comments = re.findall(
        '<span.*?<a.*?<i class="number">(\d+)</i>.*?</a>', res.text, re.S)

    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {'id': id, 'level': level, 'sex': verifySex(
            sex), 'content': content, 'laugh': laugh, 'comment': comment}
        jokeLists.append(info)


urls = [
    'https://www.qiushibaike.com/text/page/{}/'.format(str(i) for i in range(1, 10))]
for url in urls:
    getJoke(url)
for joke in jokeLists:
    f = open('H:\\MyGitCodes\\Python\\Crawler\\Examples\\jokes.txt', 'a+',encoding='utf-8')
    try:
        f.write(joke['id']+'\n')
        f.write(joke['level']+'\n')
        f.write(joke['sex']+'\n')
        f.write(joke['content']+'\n')
        f.write(joke['laugh']+'\n')
        f.write(joke['comment']+'\n')
        f.close()
    except UnicodeEncodeError:
        pass
