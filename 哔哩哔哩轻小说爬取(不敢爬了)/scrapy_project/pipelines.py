# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ScrapyProjectPipeline:
    def __init__(self):
        self.file = open('file.json','a',encoding='gbk')

    def process_item(self, item, spider):
        print(item)


        # json_file = json.dumps(item,ensure_ascii=False) + ',\n'
        # self.file.write('---'*10)
        # self.file.write('\n')
        # self.file.write(json_file)
        return item

    def __del__(self):
        self.file.close()