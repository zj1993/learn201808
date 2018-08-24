# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShuangseqiuItem(scrapy.Item):
    #开奖日期
    date = scrapy.Field()
    #期号
    title = scrapy.Field()
    #红球号码
    red = scrapy.Field()
    #蓝球号码
    blue = scrapy.Field()