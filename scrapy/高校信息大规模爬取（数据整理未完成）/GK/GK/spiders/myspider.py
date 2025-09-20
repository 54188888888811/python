import scrapy
import re


#scrapy crawl myspider --nolog

class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["www.creditsailing.com"]
    start_urls = ["http://www.creditsailing.com/school/major_score/all/2023/3018341.html",'http://www.creditsailing.com/school/major_score/all/2023/3018304.html']

    def start_requests(self):  #yield 约等于 return  不同在于执行yield后会继续执行而return会停止
        for i in range(0,1):
            yield scrapy.Request(
                self.start_urls[i],  # 请求的URL
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0'},
                # 自定义请求头
                callback=self.parse  # 指定响应处理函数
            )

    def parse(self, response, **kwargs):
        result = response.xpath('//table/tbody/tr').getall()
        obj = re.compile('<td>(?P<ject>.*?)</td>')
        for n in result:
            p = obj.finditer(n)
            with open('t.txt','a',encoding='utf-8')as f:
                f.write('北京大学')
                f.write('  ')
            for pl in p:
                with open('t.txt','a',encoding='utf-8')as f:
                    f.write(pl.group('ject'))
                    f.write('    ')
                print(pl.group('ject'))
                print('---'*15)
                #print()
            with open('t.txt', 'a', encoding='utf-8') as f:
                f.write('\n')
