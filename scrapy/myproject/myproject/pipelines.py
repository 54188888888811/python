# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter


class MyprojectPipeline:
    def __init__(self):
        self.detail_list = []
    def process_item(self, item, spider):   #item为name，uil 的字典,对应值为列表
        print(item)
        # with open('h.json','w')as f:
        #     json.dump(item, f)
        return item
