import requests
import re

print("""李狗蛋(汤js)出品

套用bing翻译的接口，
现在句子和词组都能翻译啦！""")


def english(text_name):  # 英翻中
    uil = 'https://cn.bing.com/translator'
    heander = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
        ,
    }
    reop = requests.get(uil, headers=heander)
    obj1 = re.compile(r'params_AbusePreventionHelper = (.*?);')
    a = obj1.findall(reop.text)  # 查找token
    b = eval(a[0])
    key = b[0]
    param = b[1]
    url = 'https://cn.bing.com/ttranslatev3?isVertical=1&&IG=FFEB3453664B412382446351E8F72096&IID=translator.5028.63'
    date = {'fromLang': 'en',
            'to': 'zh-Hans',
            'text': '{}'.format(text_name),
            'tryFetchingGenderDebiasedTranslations': 'true',
            'token': '{}'.format(param),
            'key': '{}'.format(key)}
    resp = requests.post(url, headers=heander, data=date)
    obj = re.compile('"text":"(?P<text>.*?)",')
    result = obj.findall(resp.text)[0]
    print("翻译是", result)


def chinese_long(text_name):  # 中翻英
    uil = 'https://cn.bing.com/translator'
    heander = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
        ,
    }
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
            'key': '{}'.format(key)}
    resp = requests.post(url, headers=heander, data=date)
    obj = re.compile('"text":"(?P<text>.*?)",')
    result = obj.findall(resp.text)[0]
    print("翻译是", result)


while 1:
    text_name = input('请输入：')
    #print(type(text_name))
    Inspection = re.compile(r"[\u4e00-\u9fff]+", re.I)  #检验是否为中文
    if Inspection.search(text_name):
        chinese_long(text_name)
    else:
        english(text_name)
