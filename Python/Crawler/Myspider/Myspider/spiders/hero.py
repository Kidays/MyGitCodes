import scrapy


class HeroSpider(scrapy.Spider):
    name = 'hero'
    allowed_domains = ['pvp.qq.com']
    start_urls = ['https://pvp.qq.com/web201605/herolist.shtml']

    def parse(self, response):
        pass
