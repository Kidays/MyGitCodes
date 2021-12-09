import xlwt
import requests
from lxml import etree
import time


def GetOnePage(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//*[@id="book-img-text"]/ul/li')
    for info in infos:
        style_1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        yield{
            'Title': info.xpath('div[2]/h2/a/text()')[0],
            'Author': info.xpath('div[2]/p[1]/a[1]/text()')[0],
            'Style': style_1+style_2,
            'Complete': info.xpath('div[2]/p[1]/span/text()')[0],
            'Introduction': info.xpath('div[2]/p[2]/text()')
        }


header = ['Title', 'Author', 'Style', 'Complete', 'Introduction']
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Novels')
for h in range(len(header)):
    sheet.write(0, h, header[h])
urls = [
    'https://www.qidian.com/all/page{}'.format(str(i)) for i in range(1, 3)]
i = 1
for url in urls:
    novels = GetOnePage(url)
    for novel in novels:
        print(novel)
        time.sleep(0.1)
        sheet.write(i, 0, novel['Title'])
        sheet.write(i, 1, novel['Author'])
        sheet.write(i, 2, novel['Style'])
        sheet.write(i, 3, novel['Complete'])
        sheet.write(i, 4, novel['Introduction'])
        i += 1
book.save('H:\\MyGitCodes\\Python\\Crawler\\Xpath\\novels.xls')
