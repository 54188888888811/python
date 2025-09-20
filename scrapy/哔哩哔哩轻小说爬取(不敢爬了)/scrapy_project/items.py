# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    detail = scrapy.Field()
    pass
# if __name__ == '__main__':
#     all_item = ScrapyProjectItem()
#     all_item['name'] = 'sb'
#     all_item['detail'] = 'sadadadd'
#     print(all_item)
