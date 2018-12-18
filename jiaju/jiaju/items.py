# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JiajuItem(scrapy.Item):
    # define the fields for your item here like:
    # 名称
    name = scrapy.Field()
    # 价格
    jg = scrapy.Field()
    # 地址
    dz = scrapy.Field()
    pass
