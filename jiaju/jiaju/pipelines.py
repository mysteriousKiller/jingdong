# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class JiajuPipeline(object):
    def __init__(self): # 写入文件
        self.f = open('itcast.json','w')
        # 可选实现，做参数初始化等
        # doing something

    def process_item(self, item, spider): # 返回的数据到item 这里
        content = json.dumps(dict(item),ensure_ascii = False)
        # 这表示我们在处理item数据的时候，中文会按u 处理
        self.f.write(content)
        return item

    # item (Item 对象) - 被爬取的 item
    # spider (spider 对象) - 爬取该item的spider
    # 这个方法必须实现，每个 item pipeline 组件都需要调用该方法
    # 这个方法必须返回一个item 对象，被丢弃的item将不会被之后的 pipeline 组件所处理

    def close_spider(self,spider): # 爬虫结束的时候执行，现在用于关闭文件
        self.f.close()
        # spider (spider 对象) - 被关闭的spider
        #可选实现，当spider被关闭是，这个方法被调用

    def open_spider(self,spider):
        # spider (spider 对象) - 被开启的spider
        #可选实现，当spider 被开启是，这个方法被调用
        pass


# 可以写写进数据库的管道
