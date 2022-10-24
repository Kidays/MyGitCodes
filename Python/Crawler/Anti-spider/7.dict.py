import math
import time
import requests
import random
import hashlib


class Crawl():
    def __init__(self):
        self.headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=912089102@10.108.162.133; ___rl__test__cookies={}; OUTFOX_SEARCH_USER_ID_NCOO=703153964.911955'.format(math.ceil(time.time()*1000)),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
            'Referer': 'https://fanyi.youdao.com/'
        }
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

# define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
#     var n = e("./jquery-1.7");
#     e("./utils");
#     e("./md5");
#     var r = function(e) {
#         var t = n.md5(navigator.appVersion)
#           , r = "" + (new Date).getTime()
#           , i = r + parseInt(10 * Math.random(), 10);
#         return {
#             ts: r,
#             bv: t,
#             salt: i,
#             sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
#         }
#     };
###########################################
# i: 你好
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 16658410108256
# sign: 2dded38efaa6c6fd4882749eb3c66eac
# lts: 1665841010825
# bv: 476414572dc9132c2e6562015cc36254
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME
    def spider(self, key):
        times = str(math.ceil(time.time()*1000)+random.randint(0, 9))
        sign = self.Md5("fanyideskweb"+key+str(times)+"Ygy_4c=r#e#4EX^NUGUc5")
        bv = self.Md5(self.headers['User-Agent'])
        data = {
            "i": key,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": times,
            "sign": sign,
            "lts": times[:-1],
            "bv": bv,
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
        res = requests.post(self.url, data=data, headers=self.headers).json()
        if res.get('errorCode') == 0:
            print('Tanslate result:'+res.get('translateResult')[0][0]['tgt'])
# translateResult: [[{tgt: "hello", src: "你好"}]]
#     0: [{tgt: "hello", src: "你好"}]
#         0: {tgt: "hello", src: "你好"}
#             src: "你好"
#             tgt: "hello"
#     type: "zh-CHS2en"

    def Md5(self, value):
        md = hashlib.md5()
        md.update(value.encode('utf-8'))  # 接收字节类型，以16进制表示
        return md.hexdigest()


if __name__ == '__main__':
    while True:
        s = input('Please input:')
        Crawl().spider(s)
        if s == 'y':
            break
