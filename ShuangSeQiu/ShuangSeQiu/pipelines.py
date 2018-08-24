# -*- coding: utf-8 -*-
import json

# from openpyxl import Workbook

class ShuangseqiuPipeline(object):
    def __init__(self):
        self.file = open('data.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入文件
        self.file.write(line)


