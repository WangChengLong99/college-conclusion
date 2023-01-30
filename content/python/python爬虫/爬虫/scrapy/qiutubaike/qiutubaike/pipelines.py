# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# #只存到本地
# from itemadapter import ItemAdapter

# class QiutubaikePipeline:
#     fp=None
#     #重写父类的一个方法L该方法只在开始爬虫的时候被调用一次
#     def open_spider(self,spider):
#         print('开始爬虫....')
#         self.fp=open('./qiubai.txt','w',encoding='utf-8')
    
#     #该方法用来处理item类型对象
#     # 该方法可以接受爬虫文件提交过来的item对象
#     # 该方法没接收到一个item就会被调用一次
#     def process_item(self, item, spider):
#         author=item['author']
#         duanzi=item['duanzi']
#         self.fp.write(author+':'+duanzi+'\n')
#         return item
    
#     def close_spider(self,spider):
#         print('结束爬虫!')
#         self.fp.close()

#存到数据库和本地，创建两个类

## 本地
from itemadapter import ItemAdapter
import pymysql

class QiutubaikePipeline:
    fp=None
    #重写父类的一个方法L该方法只在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('开始爬虫....')
        self.fp=open('./qiubai.txt','w',encoding='utf-8')
    
    #该方法用来处理item类型对象
    # 该方法可以接受爬虫文件提交过来的item对象
    # 该方法没接收到一个item就会被调用一次
    def process_item(self, item, spider):
        author=item['author']
        duanzi=item['duanzi']
        self.fp.write(author+':'+duanzi+'\n')
        return item
    
    def close_spider(self,spider):
        print('结束爬虫!')
        self.fp.close()

## 数据库
#将数据一份存到本地一份数据库
import pymysql
class mysqlPipeline():
    conn=None
    cursor=None
    def open_spider(self,spider):
        self.conn=pymysql.Connect(host='localhost',port=3306,user='root',password='990925wcldsg',db='qiubai',charset='utf8')
    def process_item(self,item,spider):
        self.cursor=self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values("%s","%s")'%(item["author"],item["duanzi"]))
            self.conn.commit()
            
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()