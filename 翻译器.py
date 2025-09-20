import requests
import re
from fake_useragent import UserAgent
# 脚本维护-2025-8-10--1 ——百度翻译需要cookies，已解决 添加元素 session ，session.post()用法|但问题依旧存在
# 目前推测为ip问题，理由修改完cookies后成功返回了一次正常结果,辅证 http://www.lryc.cn/news/416335.html?action=onClick
# 百度翻译目前仅作为参考，并不稳定
class Short_word:   #百度翻译
    def __init__(self):
        self.uil = self
        self.ky_name = ky_name


    def short_word_more_mean(self,ky_name):
        session = requests.session()    #保持会话，添加cookies
        random_headers = UserAgent()
        date = {"kw": ky_name}
        headers = {"user-agent":random_headers.random,"referer":"https://fanyi.baidu.com/mtpe-individual/transText","origin": "https://fanyi.baidu.com"}
        respon = session.post(bd_translate_uil,data=date,headers=headers)
        #print(respon.json())
        #print(type(respon.text))
        try:
            if respon.json()['data']:   # 检验是否为空集
                json_dictionary = respon.json()['data'][0]["v"]
                obj_n = re.compile(r'n\. (.*?) vt')
                obj_vt = re.compile(r'vt\. (.*)')
                test_n = re.findall(obj_n,json_dictionary)
                test_vt = re.findall(obj_vt,json_dictionary)
                #print(test_vt)
                if test_n and len(test_n)>= 1:  # 检验是否为空集
                    result_n = re.findall(obj_n,json_dictionary)[0]
                    print('百度翻译 n :', result_n)
                if test_vt and len(test_vt)>= 1:  # 检验是否为空集
                    result_vt = re.findall(obj_vt,json_dictionary)[0]
                    print('百度翻译 vt :', result_vt)
                else:
                    if len(json_dictionary)>= 1:
                        print('百度翻译 {}的翻译是：'.format(ky_name),json_dictionary)
        except Exception:
            print("\n百度:触发对方反爬,链接失败")


def english(text_name):  # 英翻中
    uil = 'https://cn.bing.com/translator'
    heander = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bing.com/translator',
        'Content-Type': 'application/x-www-form-urlencoded'
        ,
    }
    reop = requests.get(uil, headers=heander)
    obj1 = re.compile(r'params_AbusePreventionHelper = (.*?);')
    a = obj1.findall(reop.text)  # 查找token
    b = eval(a[0])
    key = b[0]
    param = b[1]
    obj2 = re.compile(r'IG:"(.*?)",')  # 查找IG
    obj2_a = obj2.findall(reop.text)
    IG = obj2_a[0]
    new_param = {"IG":IG,
                 "IID":"translator.5022.4"}
    url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=FFEB3453664B412382446351E8F72096&IID=translator.5028.63'
    date = {'fromLang': 'en',
            'to': 'zh-Hans',
            'text': '{}'.format(text_name),
            'tryFetchingGenderDebiasedTranslations': 'true',
            'token': '{}'.format(param),
            'key': '{}'.format(key)}
    resp = requests.post(url, headers=heander,params=new_param ,data=date)
    obj = re.compile('"text":"(?P<text>.*?)",')#re匹配结果
    result = obj.findall(resp.text)[0]
    print("微软翻译是", result)


def chinese_long(text_name):  # 中翻英
    uil = 'https://cn.bing.com/translator'
    heander = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.bing.com/translator',
        'Content-Type': 'application/x-www-form-urlencoded'}
    reop = requests.get(uil, headers=heander)
    obj1 = re.compile(r'params_AbusePreventionHelper = (.*?);')
    a = obj1.findall(reop.text)  # 查找token
    b = eval(a[0])
    key = b[0]
    param = b[1]
    url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=FFEB3453664B412382446351E8F72096&IID=translator.5028.63'
    date = {'fromLang': 'zh-Hans',
            'to': 'en',
            'text': '{}'.format(text_name),
            'tryFetchingGenderDebiasedTranslations': 'true',
            'token': '{}'.format(param),
            'key': '{}'.format(key)}#传递参数
    resp = requests.post(url, headers=heander, data=date)
    obj = re.compile('"text":"(?P<text>.*?)",')
    result = obj.findall(resp.text)[0]
    print("微软翻译是", result)


bd_translate_uil = 'https://fanyi.baidu.com/sug'


while 1:
    text_name = input('请输入：')
    a = Short_word
    
    #print(type(text_name))
    Inspection = re.compile(r"[\u4e00-\u9fff]+", re.I)  #检验是否为中文
    try:
        if Inspection.search(text_name):
            chinese_long(text_name)
        else:
            english(text_name)
        a.short_word_more_mean(bd_translate_uil, text_name)
    except ValueError:
        print('百度翻译崩溃了')

           


