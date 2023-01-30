import scrapy
from beijing.items import BeijingItem
import time
class FengjingSpider(scrapy.Spider):
    name = 'fengjing'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kbeijing/']
    def parse(self, response):
        li_list=response.xpath('//*[@id="main"]/div[3]/ul[@class="clearfix"]/li')
        root='https://pic.netbian.com/'
        for li in li_list:
            time.sleep(3)
            title=li.xpath('./a/b/text()').extract()[0]
            url_img=li.xpath('./a/img/@src').extract()[0]
            item=BeijingItem()
            item['title']=title+'.jpg'
            item['url_img']=root+url_img
            print(title)
            print(url_img)
            yield item
            
            
            
