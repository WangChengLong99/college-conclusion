import scrapy

class FirstSpider(scrapy.Spider):#
    #爬虫文件的名称：就是爬虫源文件的一个唯一标识
    name='test'
    #允许的域名，可以用来限定start_urls列表中哪些url可以进行请求发送
    #allowed_domains = ['www.baidu.com']一般不用，因为网站中还有图片，链接等网址
    #起始的url列表：该列表中存放的url会被scrapy自动进行请求的发送
    start_urls=['https://www.baidu.com/','https://www.sogou.com']
    #用作于数据解析：response参数表示的请求成功后对应的相应对象
    
    def parse(self,response):
        print(response)
