import requests
import re

header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'}
url ='https://api.bilibili.com/x/v2/reply/wbi/main?oid=1506696886&type=1&mode=3&pagination_str=%7B%22offset%22:%22%22%7D&plat=1&seek_rpid=&web_location=1315875&w_rid=59a6285fc14374853cb686a684e6acc2&wts=1724902703'
resp = requests.get(url,headers=header)
obj = re.compile(r'"uname":.*?,|"message":.*?,',re.S)
result = obj.finditer(resp.text)
for i in result:
    print(i.group())
