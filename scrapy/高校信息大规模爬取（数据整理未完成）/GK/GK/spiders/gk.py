import requests
import scrapy
import os  #---清屏
import re
import pdb

os.system('cls')


#scrapy crawl gk --nolog

class GK(scrapy.Spider):
    name = "gk"
    allowed_domains = ["www.creditsailing.com"]
    start_urls = ["http://www.creditsailing.com/school/31/0/1/1/0/1.html"]
    var_uils = []
    var_name = []
    name_time = 0
    def start_requests(self):  #yield 约等于 return  不同在于执行yield后会继续执行而return会停止
        for n in range(31, 32):  # 31到44（含）
            url = f"http://www.creditsailing.com/school/{n}/0/1/1/0/1.html"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):

        gaokao_name = response.xpath('//li/div[1]/a/@alt')  # 高校名字
        gaokao_uil = response.xpath('//li/div[1]/div/p[1]/a/@href')

        for i in gaokao_name:
            temp = {}
            temp['uil'] = i.get()  #虽然键是‘uil’但内容却是名字
            self.var_name.append(temp['uil'])
        for o in gaokao_uil:
            new_temp = {}
            new_temp['name'] = 'http://www.creditsailing.com' + o.get()  # uil
            self.var_uils.append(new_temp['name'])
        for h in self.var_uils:  #高校主页uil地址
            yield scrapy.Request(h,
                                 callback=self.new_parse)
        #pdb.set_trace() #断点
        # print(self.var_name)
        # print(type(self.var_name[0][0]))


    #//a/@href
    def new_parse(self, response, **kwargs):

        yx = response.xpath('//a[contains(text(), "院校分数线")]/@href').get()  #院校分数线
        #print(response)
        zy = response.xpath('//a[contains(text(), "专业分数线")]/@href').getall()  #专业录取分
        #print(yx)
        new_yx = 'http://www.creditsailing.com' + yx
        new_zy = 'http://www.creditsailing.com' + zy[0]
        yield scrapy.Request(new_yx,callback=self.yx)
        yield scrapy.Request(new_zy, callback=self.zy)


    def yx(self,response):
        print(response)
        last_yx = response.xpath('//table/tbody/tr').getall()
        obj_a = re.compile('<td>(?P<ject>.*?)</td>')
        #<td>北京</td>
        q = []

        for i in last_yx:
            result_1 = re.findall(obj_a,i)
            q.append(result_1)
        #print(q)

        #object_yx = re.compile('<td>(?P<ject>.*?)</td>')
        #result_1 = re.findall(object_yx,last_yx)

        with open('x.txt', 'a', encoding='utf-8') as f:
            f.write(self.var_name[self.name_time])
            f.write('  ')
            old_time = self.name_time
            self.name_time+=1
        #pdb.set_trace()
        for w in q:  #院校录取分
            #print(w)

            #’w‘ 为 ['北京', '综合', '2023', '本科', '不限', '575', '15169'],

            with open('x.txt', 'a', encoding='utf-8') as f:
                f.write(old_time)
                f.write("   ")
            for e in w:
                print(e)

                with open('x.txt','a',encoding='utf-8')as f:
                    f.write(e)
                    f.write("      ")
            f.write('\n')


    def zy(self,response):
        result = response.xpath('//table/tbody/tr').getall()
        obj = re.compile('<td>(?P<ject>.*?)</td>')

        for n in result:
            p = obj.finditer(n)
            for pl in p:
                with open('u.txt','a',encoding='utf-8')as f:
                    f.write(pl.group('ject'))
                    f.write('       ')
                # print(pl.group('ject'))
                # print('---'*15)
                #print()
            with open('u.txt', 'a', encoding='utf-8') as f:
                f.write('\n')

        # #print(type(response))
        #
        #
        # last_zy = response.xpath('//tbody/tr').getall() #数据为每一个高校专业的列表
        # print(last_zy)
        # # for r in last_zy:
        # #     print(response)
        # #     print('-----'*10)
        # #     print(r)
        # # m = 10
        # #
        # # print(last_zy[m])
        # #for m in :
        #
        # object_zy = re.compile('<td>(?P<ject>.*?)</td>')
        # result_2 = re.findall(object_zy,last_zy)
        # y = []
        # y.append(result_2)
        # # for w in y:
        # #     for e in w:
        # #         with open('x.txt','a',encoding='utf-8')as f:
        # #             f.write(e)
        # #             f.write("       ")
        # #     with open('x.txt', 'a', encoding='utf-8') as f:
        # #         f.write('\n')
        # #print(last_zy)
