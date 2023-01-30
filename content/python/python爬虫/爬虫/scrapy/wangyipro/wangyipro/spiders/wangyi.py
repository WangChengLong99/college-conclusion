import scrapy
from selenium import webdriver
from wangyipro.items import WangyiproItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #allowed_domains = ['www.wangyi.com']
    start_urls = ['https://news.163.com/']
    model_urls=[]#存储五个板块对应详情页的url
    #实例化一个爬虫类对象
    def __init__(self):
        self.bro = webdriver.Chrome('D://迅雷下载/chromedriver.exe')
    def parse(self, response):
        li_list=response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist=[2,3,5,6]
        for index in alist:
            model_url=li_list[index].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        #依次对每一个板块对应的页面进行请求
        for url in self.model_urls:#对每一个板块的url进行请求发送
            yield scrapy.Request(url,callback=self.parse_model)
    # 每一个板块对应的新闻标题相关内容都是动态加载出来的
    def parse_model(self,response):#解析每一个板块页面中对应新闻的标题和新闻详情页的url
        #response 
        div_list=response.xpath('/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div[@class="data_row news_article clearfix "]')
        for div in div_list:
            title=div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url=div.xpath('./div/div[1]/h3/a/@href').extract_first()
            print(new_detail_url)
            item=WangyiproItem()
            item['title']=title
            #对新闻详情页的url发起请求
            yield scrapy.Request(new_detail_url,callback=self.parse_detail,meta={'item':item})   
    def parse_detail(self,response):
        content=response.xpath('//*[@id="content"]//text()').extract()
        content=''.join(content)    
        item=response.meta['item']
        item['content']=content
        yield item
    def closed(self,spider):
        self.bro.quit()
