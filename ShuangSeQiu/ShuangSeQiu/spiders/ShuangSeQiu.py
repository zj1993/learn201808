# -*- coding: utf-8 -*-
import time
import datetime

import scrapy

from ..items import ShuangseqiuItem

class ShuangSeQiu(scrapy.Spider):
    # 用于区别Spider
    name = 'ShuangSeQiu'
    # 允许访问的域
    allowed_domains = ['datachart.500.com']
    # 爬取的网址
    start_urls = ["http://datachart.500.com/ssq/history/newinc/history.php?start=00001"]

    # 爬取的方法
    def parse(self, response):
        # 实例一个容器保存爬取的信息
        item = ShuangseqiuItem()

        #当前时间
        now = datetime.datetime.now()
        #获取两年前的今天
        last_year = int(now.year) - 2
        last = str(last_year) + '-' + str(now.month) + '-' + str(now.day)
        #获取两年前的今天的时间戳
        ts = int(time.mktime(time.strptime(last, "%Y-%m-%d")))

        for box in response.xpath('//tr[@class="t_tr1"]'):
            #获取双色球时间，并转为时间戳
            date = int(time.mktime(time.strptime(box.xpath('td/text()').extract()[15], "%Y-%m-%d")))
            if ts < date:
                #中奖日期
                item['date'] = box.xpath('td/text()').extract()[15]
                #期号
                item['title'] = box.xpath('td/text()').extract()[0]
                #红球号码
                item['red'] = box.xpath('td/text()').extract()[1:7]
                #蓝球号码
                item['blue'] = box.xpath('td/text()').extract()[7]
                # 返回信息
                print(item)
                yield item
