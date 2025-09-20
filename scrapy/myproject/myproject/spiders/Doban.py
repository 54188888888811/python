from typing import Iterable, Any
import re
import scrapy
import os
os.system ('cls')
from myproject.items import MyprojectItem
#------------------------豆瓣爬虫排行榜名称，uil地址detail内容简介


class DobanSpider(scrapy.Spider):
    name = "Doban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/chart"]
    item = MyprojectItem()
    times = 0
    uil_list = []
    # a = 0
    # b = 0   #用于判断deep_parse 执行次数
    finally_detail_list = []
    def start_requests(self) -> Iterable[Any]:
        yield scrapy.Request(self.start_urls[0], headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'}
                             , callback=self.parse)

    def parse(self, response):
        if self.times == 0:
            parsed_response = response.xpath("//table//*[(@class='pl2')]/a/text()").getall()
            #print(parsed_response)
            extracted_texts = []
            name_list = []  #电影名称的列表
            for s in parsed_response:
                stripped = s.strip()  # 去除前后空白
                if stripped:  # 如果字符串非空
                    # 去除末尾可能存在的斜杠和空格
                    cleaned = stripped.rstrip(' /')
                    extracted_texts.append(cleaned)
                    # 输出提取的文本
            for i in extracted_texts:  #进一步去除 \n
                name = i.replace('\n', '')
                name_list.append(name)

            self.item['name'] = name_list   #封装item【name】
            temporary = response.xpath('//table//tr//a/@href').getall()
            for i in temporary:
                if i not in self.uil_list:
                    self.uil_list.append(i)
            self.item['uil'] = self.uil_list    #封装item【uil】

            #print(self.uil_list)
        if self.uil_list:
            #print(self.uil_list)
            yield scrapy.Request(self.uil_list[0],  # 请求的URL
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'},  # 自定义请求头
                callback=self.deep_parse,cb_kwargs={'remaining_urls': self.uil_list[1:]})  # 指定响应处理函数)



    def deep_parse(self,response,remaining_urls):
        #print(remaining_urls)
        self.times += 1
        parse_response = response.xpath("//span[@property='v:summary']/text()").getall()
        cleaned_text = ' '.join(
            part.strip().replace('\u3000', ' ')  # 处理全角空格
            for part in parse_response
        ).replace('\n', '')  # 移除所有换行符
        # 压缩多余空格
        final_text = ' '.join(cleaned_text.split())
        self.finally_detail_list.append(final_text)
        if remaining_urls:
            next_uil = remaining_urls[0]
            #print(next_uil)
            yield scrapy.Request(next_uil,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'},  # 自定义请求头
                callback=self.deep_parse,cb_kwargs={'remaining_urls': remaining_urls[1:]})
        else:   # 最终的detail信息表（存有顺序）
            self.item['detail'] = self.finally_detail_list
            yield self.item

