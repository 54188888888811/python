import threading
import time
import requests

#分3个线程，一个负责个位数，一个负责两位数，https://svip.high21-playback.com/20240410/29426_a85828cc/2000k/hls/mixed.m3u8
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
date = {'user_name': '54188888888811',
    'user_pwd': '@0987456tang'}
t = 0
a = 10
c = 100
def two(a):
    for n in range(10,100):
        url = 'https://svip.high21-playback.com/20240410/29426_a85828cc/2000k/hls/dea93ec60370000{}.ts'.format(a)
        obj = session.get(url, headers=header)

        with open(file="C:\pythonProject\ls\{}.ts".format(a),mode='a+b')as j:
         j.write(obj.content)
         a += 1
         print('over')
         time.sleep(0.1)
def three(c):
    for n in range(100,354):
        url = 'https://svip.high21-playback.com/20240410/29426_a85828cc/2000k/hls/dea93ec6037000{}.ts'.format(c)
        obj1 = session.get(url, headers=header)
        with open(file="C:\pythonProject\ls\{}.ts".format(c),mode='a+b')as k:
         k.write(obj1.content)
         c += 1
         print(obj1)
         time.sleep(0.1)

num1 = threading.Thread(target=two,args=(a,))   #多线程无法处理带参数的，需要用args=加上元组代替
num2 = threading.Thread(target=three,args=(c,))
for i in range(0,10):
    uil = 'https://www.jcydm.cc/index.php/user/login.html'
    session = requests.session()
    session.post(uil,data=date)
    url = 'https://svip.high21-playback.com/20240410/29426_a85828cc/2000k/hls/dea93ec603700000{}.ts'.format(t)
    resp = session.get(url,headers=header)
    with open(file="C:\pythonProject\ls\{}.ts".format(t),mode='a+b')as f:
        f.write(resp.content)
        t += 1
        time.sleep(0.1)
        print('over')
    num1.start()
    num2.start()
