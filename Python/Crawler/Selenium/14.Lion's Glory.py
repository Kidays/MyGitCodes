import json
import requests
import csv
from lxml import etree
herolist_url = 'https://pvp.qq.com/web201605/js/herolist.json'
item_url = 'https://pvp.qq.com/web201605/js/item.json'
summoner_url = 'https://pvp.qq.com/web201605/js/summoner.json'
herolist = requests.get(herolist_url).text
item = requests.get(item_url).text
summoner = requests.get(summoner_url).text
herolist = json.loads(herolist)
item = json.loads(item)
summoner = json.loads(summoner)
with open('Glory_hero.csv', 'a+', newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['生存能力', '攻击伤害', '技能效果',
                    '上手难度', 'ename', 'cname', 'title',
                     'new_type', 'hero_type', 'skin_name'])
for i in herolist:
    herolist_row = []
    hero_url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(
        i['ename'])
    hero_url_html = requests.get(hero_url).text
    hero_url_html_selector = etree.HTML(hero_url_html)
    hero_url_html_list = hero_url_html_selector.xpath(
        '//ul[@class="cover-list"]/li')
    for li in hero_url_html_list:
        num = li.xpath('./span/i/@style')[0][6:]
        herolist_row.append(num)
    herolist_row.append(i['ename'])
    herolist_row.append(i['cname'])
    herolist_row.append(i['title'])
    herolist_row.append(i['new_type'])
    herolist_row.append(i['hero_type'])
    herolist_row.append(i.setdefault('skin_name', 0))
    herolist_row_select = herolist_row
    with open('Glory_hero.csv', 'a+', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(herolist_row_select)
with open('hero.csv', 'a+', newline="", encoding='utf-8')as f:
    writer = csv.writer(f)
    writer.writerow(['item_name', 'price', 'total_price', 'des1', 'des2'])
print('-------------------------------------')
with open('Glory_hero.csv', 'a+', newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['item_id', 'item_name', 'item_type',
                    'price', 'total_price', 'des1', 'des2'])
for i in item:
    item_row = []
    item_row.append(i['item_id'])
    item_row.append(i['item_name'])
    item_row.append(i['item_type'])
    item_row.append(i['price'])
    item_row.append(i['total_price'])
    i_des1 = i['des1'].replace('<p>', '', 3).replace('<br>', '', 3)
    item_row.append(i_des1.replace('</p>', '', 3))
    i_des2 = i.setdefault('des2', '0').replace(
        '<p>', '', 3).replace('<br>', '', 3)
    item_row.append(i_des2.replace('</p>', '', 3))
    item_row_select = item_row
    with open('Glory_hero.csv', 'a+', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(item_row_select)
print('-------------------------------------')
with open('Glory_hero.csv', 'a+', newline="", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['summoner_id', 'summoner_name', 'summoner_rank',
                    'summoner_description'])
for i in summoner:
    summoner_row = []
    summoner_row.append(i['summoner_id'])
    summoner_row.append(i['summoner_name'])
    summoner_row.append(i['summoner_rank'])
    summoner_row.append(i['summoner_description'])
    summoner_row_select = summoner_row
    with open('Glory_hero.csv', 'a+', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(summoner_row_select)
print('-------------------------------------')

# "dict_values([130, '宫本武藏', '剑圣', 0, 1, '剑圣|鬼剑武藏|未来纪元|万象初新|地狱之眼|霸王丸'])"
# 1155,破晓,1,2040,3400,<p>+50物理攻击<br>+35%攻击速度<br>+10%暴击率</p>
