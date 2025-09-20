import re
import sys
from typing import Iterable, Any
from scrapy_project.items import ScrapyProjectItem
import os
os.system('cls')
import scrapy
import time
#scrapy crawl first_spider --nolog
class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["www.linovelib.com"]
    start_urls = ["https://www.linovelib.com"]
    temp = {}
    def start_requests(self):   #yield 约等于 return  不同在于执行yield后会继续执行而return会停止
        yield scrapy.Request(
            self.start_urls[0],  # 请求的URL
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'},  # 自定义请求头
            callback=self.parse  # 指定响应处理函数
        )

    def parse(self, response, **kwargs):    # response 为 源文件，需要提取uil
        #print(response)
        n_list = response.xpath("//div[@class='mind-book']/div[contains(@class,'imgbox img-book fl')]/a")
        #print(n_list)
        for n in n_list:

            self.temp['uil'] = 'https://www.linovelib.com'+n.xpath("@href").get()
            self.temp['name'] = n.xpath("./img/@alt").get()
            #print(self.temp['name'])
            yield scrapy.Request(self.temp['uil'],  # 请求的URL
                callback=self.detailed_spot,meta={'name' : self.temp['name']})  # 指定响应处理函数)
            # sys.exit() #结束进程


#cd C:\pythonProject\scrapy_project
    def detailed_spot(self,response):

        print(response)
        result = response.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/div[3]/p').get()#还差一个正则表达式
        # print(result)

        obj = re.compile('[\u4e00-\u9fa5]')
        true_result = obj.findall(result)
        content = ''.join(true_result)
        temp_detail = {}
        temp_detail['detail'] = content
        #print(temp_detail['detail'])
        #print(temp_detail)
        all_item = ScrapyProjectItem()
        all_item['name'] = response.meta['name']
        all_item['detail'] = temp_detail['detail']
        yield all_item['name']
        yield all_item['detail']

        # for i in result:
        #     print(i)



            #//div[3]/p/text()
            # print(temp['name'])
            # print('https://www.linovelib.com'+temp['uil'])
            # with open('text.txt','a',encoding='utf-8')as f:
            #     f.write(temp['name'])
            #     f.write('\n')
            #     f.write('https://www.linovelib.com'+temp['uil'])
            #     f.write('\n')