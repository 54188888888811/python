import re
import requests


number = 0
def range(number):
    obj = {0: '5f685274073b',1 : '279fcd874c72',2: '8a3d4d640516',3:'fbd076c39d28'}
    down(obj[number])
    number += 1



def down(name):
    url = 'https://www.spiderbuf.cn/playground/h03/{}'.format(name)
    a = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0'}
    resp = requests.get(url,headers=a)
    print(resp.text)
    with open('nuber_name.txt','a',encoding='utf-8') as f:
        f.write(resp.text)
while number < 4:
    range(number)
    number += 1