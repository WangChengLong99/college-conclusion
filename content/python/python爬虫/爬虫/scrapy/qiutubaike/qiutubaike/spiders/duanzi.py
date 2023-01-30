#新建一个糗图百科项目
import scrapy 
from qiutubaike.items import QiutubaikeItem
# class DuanziSpider(scrapy.Spider):
#     name = 'duanzi'
#     #allowed_domains = ['www.xxx.com']
#     start_urls = ['https://www.qiushibaike.com/text/']

#     def parse(self, response):
#         #解析：作者的名称+段子内容
#         #response可以直接调用xpath方法，但和原本etree的xpath不完全相同
#         div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')#这样书写能返回所有的div
#         #print(len(div_list))
#         all_data=[]
#         for div in div_list:
#             #xpath返回的是列表，但是列表元素一定是Selector类型的对象
#             #extract可以将Selector对象中data参数存储的字符串提取出来
#             author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
#             #author=div.xpath('./div[1]/a[2]/h2/text()').extract_first()将第0个对象进行extract操作
#             #如果列表调用了extract，则表示将类表中每一个Selector对象中data对应的字符串对象提取出来，列表类型
#             duanzi=div.xpath('./a[1]/div/span/text()').extract()
#             duanzi=''.join(duanzi)
#             dic={
#                 'author':author,
#                 'duanzi':duanzi
#             }
#             all_data.append(dic)
#             #print(author,duanzi)
#         return all_data

class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #解析：作者的名称+段子内容
        #response可以直接调用xpath方法，但和原本etree的xpath不完全相同
        div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')#这样书写能返回所有的div
        all_data=[]
        for div in div_list:
            #xpath返回的是列表，但是列表元素一定是Selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            #author=div.xpath('./div[1]/a[2]/h2/text()').extract_first()将第0个对象进行extract操作
            #如果列表调用了extract，则表示将类表中每一个Selector对象中data对应的字符串对象提取出来，列表类型
            duanzi=div.xpath('./a[1]/div/span/text()').extract()
            duanzi=''.join(duanzi)
            item=QiutubaikeItem()
            item['author']=author
            item['duanzi']=duanzi
            yield item #将item提交给管道