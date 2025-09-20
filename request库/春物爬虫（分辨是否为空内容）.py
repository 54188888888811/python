import requests
import re
import time
print("""最好不要爬这个良心网站""")
o = 67686
y = 1
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}
def big(o):
    while o <= 68835:
        for p in range(1,20):
            url = 'https://m.wenkuchina.com/lightnovel/169/{}_{}.html'.format(o,p)
            resp = requests.get(url,headers=header)
            if len(resp.text) > 6000:
                obj = re.compile(r"chaptername:(?P<flag>.*?),",re.S)
                obj1 = re.compile(r'<p>(?P<ject>.*?)</p>',re.S)
                result = obj.finditer(resp.text)
                result1 = obj1.finditer(resp.text)
                print('yes')
                time.sleep(1)
                for i in result:
                    with open('chun_wu.txt'.format(o, p),'a',newline='\n',encoding='utf-8') as f:
                        f.write(i.group('flag'))
                        f.write('\n')
                    for a in result1:
                        with open('chun_wu.txt'.format(o,p),'a',newline='\n',encoding='utf-8')as f:
                            f.write(a.group('ject'))
                            f.write('\n')
                print('over')
                time.sleep(1.2)
            else:
                print('no')
                o += 1
            p+=1
        o += 1

if input('你确定要爬吗？（yes/on）') == 'yes':
    big(o)
