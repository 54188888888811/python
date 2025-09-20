import re

import requests
#每次使用需要重写cooki
#分了三步骤，先在主网站查找需求，然后进入需求链接，寻找下载地址
url = 'https://www.dytt89.com'
ig = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 '
        'Safari/537.36 Edg/127.0.0.0',
    "cookie": "guardok=GH7Zm6p4cr+1fJEeSMkYyUzNKDaSm7X+FEAP0ToAh8hgvx0I1Rio4FkEAiO8X3p0gperhQ0D05HYbCa4whpP9Q==;"
}
resp = requests.get(url, headers=ig, verify=False)
resp.encoding = resp.apparent_encoding
rect = re.compile(r"""2024必看热片.*?<ul>(?P<uil>.*?)</ul>""", re.S)
result = rect.finditer(resp.text)
for i in result:
    obj1 = i.group('uil')
recs = re.compile(r"""<li><a href='(?P<name>.*?)'(?P<al>.*?)">""", re.S)
result_ture = recs.finditer(obj1)
for i in result_ture:
    print(i.group('name', 'al'))
ruls = url + i.group('name')
aw = requests.get(ruls, headers=ig, verify=False)
aw.encoding = aw.apparent_encoding
who = re.compile(r'<!--xunleiDownList Start-->.*?bgcolor="#fdfddf"><a.*?href="(?P<llq>.*?)&tr=.*?</a></td>', re.S)
where = who.finditer(aw.text)
for it in where:
    print(it.group('llq'))  #这仅是一部电影的下载链接，但是框架主体例子全都完成
