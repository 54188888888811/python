import re
import requests
from concurrent.futures import ThreadPoolExecutor

#不足：没有实现自动翻页，但有了思路。其次，re的内容抓取还不熟练，以后应当补足
i = 1
hander = {'user-agent':
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 '
              'Safari/537.36'
              'Edg/127.0.0.0',
          'referer':
              'http://www.shucai123.com/price/'
          }


def fer():  #给多线程安排的任务
    uil = 'http://www.shucai123.com/price/t2'
    fer_want = requests.get(uil, headers=hander)
    fer_few = re.compile(
        r'bgcolor="#ffffff">.*?href="(?P<place>.*?)</a></td><td><a .*? &nbsp; </p><p style="color:#669900', re.S)
    result = fer_few.finditer(fer_want.text)
    for v in result:
        with open('llq.html', 'a', encoding='utf-8') as f:
            f.write(v.group('place'))


url = 'http://www.shucai123.com/price/t3'
resp = requests.get(url, headers=hander)
obj = re.compile(r'bgcolor="#ffffff">.*?href="(?P<place>.*?)</a></td><td><a .*? &nbsp; </p><p style="color:#669900',
                 re.S)              #地址^
request = obj.finditer(resp.text)
for i in request:
    with ThreadPoolExecutor(50) as t:
        t.submit(fer)   #多线程启动！
    op = i.group('place')
    obj1 = re.compile('[\u4e00-\u9fa5]')
    adj = obj1.findall(op)
    print(adj)