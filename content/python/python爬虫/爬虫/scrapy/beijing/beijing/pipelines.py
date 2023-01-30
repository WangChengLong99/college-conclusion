# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class BeijingPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imgsPileLine(ImagesPipeline):
    title=1
    def get_media_requests(self,item,info):
        self.title=item['title']
        yield scrapy.Request(item['url_img'])
    def file_path(self,request,response=None,info=None):
        imgName=self.title
        return imgName
    def item_completed(self,results,item,info):
        return item#返回给下一个管道
