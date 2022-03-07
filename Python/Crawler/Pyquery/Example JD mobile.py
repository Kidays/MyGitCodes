import pyquery
from pyquery import PyQuery as pq
import time
import xlwt
import requests
import os
import sys
os.chdir(sys.path[0])  # enable file relative path

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55',
            'cookie': '__jdu=1637678810872466352515; shshshfpa=fb724a57-88db-ffc9-88a9-9bbaf9a0fba4-1637678843; unpl=JF8EAKJnNSttWUlTDRkFHhpHTAlWWw8OTx8DZjVRV1pYGFENGgRJQhZ7XlVdXhRKFB9vYhRUVVNLUA4fBisSEXtdVV9dDE4SC2plNWRtW0tkBCsCHBAWTFtdV10JQhEAamACVllbT1QBKzIcEhl7bWReVAlMFgdqZQdRbVl7VgQaABkaFk9YU24WZkpaA2hlA1NbUUJUBBIEGBcXTF9QXVkITycCX2Q; __jdv=122270672|www.zeyouquan.com|t_1001544943_|tuiguang|03693649f6e34c75918ce261b4907ca7|1644837364879; areaId=7; ipLoc-djd=7-420-0-0; PCSYCityID=CN_410000_0_0; shshshfpb=m0yHfgvneabP3ra%2FXCSx5Kw%3D%3D; shshshfp=bef74050371e6b8aa30b6a935c4f2060; __jda=122270672.1637678810872466352515.1637678811.1644842971.1645103812.7; __jdc=122270672; __jdb=122270672.5.1637678810872466352515|7.1645103812; shshshsID=7ed5fc2def615b52934f003cb2de4c5a_5_1645104052647; 3AB9D23F7A4B3C9B=THVZDSKOQMRRR7INXCNF3SR2Y73JVVSDLY6IAHJ6DRDTH4PG7ONK5ICCQKR2RFDNASNEHI7EMJZFBATCG2OCUVU7VU'}
        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            html = result.content
            html_doc = str(html, 'utf-8')
            return html_doc
        return None
    except Exception:
        return None


def parse_one_page(html):
    doc = pq(html)
    ul = doc('.gl-warp.clearfix')
    liList = ul('.gl-item')
    for li in liList.items():
        product = li('div > div.p-name.p-name-type-2 > a > em').text()
        price = li('div > div.p-price > strong > i').text()
        seller = li('div > div.p-shop > span > a').text()
        yield{
            'product': product,
            'price': price,
            'seller': seller
        }


if __name__ == '__main__':
    urls = ['https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=c50cde07949842eaba5665a4b7804c05&page={}&s=1&click=0'.format(
        str(i)) for i in range(1, 8, 2)]
    header = ['Ranking', 'Product', 'Price', 'Seller']
    book = xlwt.Workbook(encoding='utf-8')
    sheet_all = book.add_sheet('Mobile phone sales')
    sheet_apple = book.add_sheet('iPhone sales')
    sheet_huawei = book.add_sheet('Huawei sales')
    sheet_xiaomi = book.add_sheet('Xiaomi sales')
    for h in range(len(header)):
        sheet_all.write(0, h, header[h])
        sheet_apple.write(0, h, header[h])
        sheet_huawei.write(0, h, header[h])
        sheet_xiaomi.write(0, h, header[h])
    i = 1
    apple_i = 1
    huawei_i = 1
    xiaomi_i = 1
    for url in urls:
        mobile_infos = parse_one_page(get_one_page(url))
        for mobile_info in mobile_infos:
            print(mobile_info)
            sheet_all.write(i, 0, str(i))
            sheet_all.write(i, 1, mobile_info['product'])
            sheet_all.write(i, 2, mobile_info['price'])
            sheet_all.write(i, 3, mobile_info['seller'])
            if mobile_info['product'].lower().find('apple') != -1:
                sheet_apple.write(apple_i, 0, str(apple_i))
                sheet_apple.write(apple_i, 1, mobile_info['product'])
                sheet_apple.write(apple_i, 2, mobile_info['price'])
                sheet_apple.write(apple_i, 3, mobile_info['seller'])
                apple_i += 1
            if mobile_info['product'].lower().find('华为') != -1:
                sheet_huawei.write(huawei_i, 0, str(huawei_i))
                sheet_huawei.write(huawei_i, 1, mobile_info['product'])
                sheet_huawei.write(huawei_i, 2, mobile_info['price'])
                sheet_huawei.write(huawei_i, 3, mobile_info['seller'])
                huawei_i += 1
            if mobile_info['product'].lower().find('小米') != -1:
                sheet_xiaomi.write(xiaomi_i, 0, str(xiaomi_i))
                sheet_xiaomi.write(xiaomi_i, 1, mobile_info['product'])
                sheet_xiaomi.write(xiaomi_i, 2, mobile_info['price'])
                sheet_xiaomi.write(xiaomi_i, 3, mobile_info['seller'])
                xiaomi_i += 1
            time.sleep(0.1)
            i += 1
    book.save('mobile_rank.xls')
