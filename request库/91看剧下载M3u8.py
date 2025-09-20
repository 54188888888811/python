import re
import requests
from concurrent.futures import ThreadPoolExecutor   #线程池的库

url = 'https://v.cdnlz9.com/20240217/21841_d5271836/2000k/hls/mixed.m3u8'
resp = requests.get(url)


with open('91.m3u8','wb')as f:   #wb以二进制写入文件
    f.write(resp.content)
    print('over')
# m3u8_list = []
# m3u8_list.append(resp.text)
# print(m3u8_list)
