import requests
from lxml import etree
import time
import xlwt


def getOnePage(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    contents = selector.xpath(
        '/html/body/div[2]/div[1]/div[4]/div[1]/div/div/div/table/tbody/tr')
    for content in contents:
        try:  # NULL is aborted
            yield{
                '排名': content.xpath('td[1]/text()')[0],
                '国家/地区': content.xpath('td[2]/text()')[0],
                '所在洲': content.xpath('td[3]/text()')[0],
                '人口': content.xpath('td[4]/text()')[0],
                '占世界%': content.xpath('td[5]/text()')[0]
            }
        except IndexError:
            pass
# url = 'https://www.kylc.com/stats/global/yearly/g_population_total/{}.html'.format(
#         str(2021))
# print(getOnePage(url))
book = xlwt.Workbook(encoding='utf-8')
for year in range(1960, 2022):
    header = ['排名', '国家/地区', '所在洲', '人口', '占世界%']
    sheet = book.add_sheet(str(year))
    for h in range(len(header)):
        sheet.write(0, h, header[h])
    url = 'https://www.kylc.com/stats/global/yearly/g_population_total/{}.html'.format(
        str(year))
    i = 1
    datas = getOnePage(url)
    for data in datas:
        # print(data)
        time.sleep(0.05)
        sheet.write(i, 0, data['排名'])
        sheet.write(i, 1, data['国家/地区'])
        sheet.write(i, 2, data['所在洲'])
        sheet.write(i, 3, data['人口'])
        sheet.write(i, 4, data['占世界%'])
        i += 1
book.save('H:\\MyGitCodes\\Python\\Crawler\\Xpath\\populations.xls')
