import requests
import re
o = 148856
y = 1
p = 1
def big(o,p):
    while o <= 149203:
        for p in range(1,10):
            url = 'https://m.wenkuchina.com/lightnovel/530/{}_{}.html'.format(o,p)
            resp = requests.get(url)
            obj = re.compile(r"chaptername:(?P<flag>.*?),",re.S)
            obj1 = re.compile(r'<p>(?P<ject>.*?)</p>',re.S)
            result = obj.finditer(resp.text)
            result1 = obj1.finditer(resp.text)
            for i in result:
                with open('sqing.txt'.format(o, p),'a',newline='\n',encoding='utf-8') as f:
                    f.write(i.group('flag'))
                    f.write('\n')
                for a in result1:
                    with open('sqing.txt'.format(o,p),'a',newline='\n',encoding='utf-8')as f:
                        f.write(a.group('ject'))
                        f.write('\n')
                        print('over')
            p+=1
        o += 1
big(o,p)