import scrapy
import time
from iu.items import IuItem
class ImgSpider(scrapy.Spider):
    name = 'img'
    #allowed_domains = ['www.xxx.com']
    page=2
    start_urls=['https://www.duitang.com/blogs/tag/?name=%E3%80%82iu%E5%9B%BE%E7%89%87']+['https://www.duitang.com/blogs/tag/?name=%E3%80%82iu%E5%9B%BE%E7%89%87#!hot-p'+str(i) for i in range(2,3)]
    num=1
    def parse(self, response):
        div_list=response.xpath('//a[@class="a"]/img/@src').extract()
        item=IuItem()
        for div in div_list:
            url_img=div
            title='iu'+str(self.num)+'.jpg'
            self.num+=1
            item['title']=title
            item['url_img']=url_img
            print(title,url_img)
            yield item     
