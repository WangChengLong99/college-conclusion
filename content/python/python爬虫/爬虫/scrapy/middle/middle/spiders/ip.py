import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = ['www.ip.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        page_text=response.text
        with open('ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
