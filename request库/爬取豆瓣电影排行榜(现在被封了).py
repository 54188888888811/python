import re
import requests

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'
ig = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 '
        'Safari/537.36 Edg/127.0.0.0'
}
rect = requests.get(url, headers=ig)
print()
# with open('douban.html','w',encoding='utf-8')as f:
#     f.write(rect.text,)
# print('over')
obj = re.compile('"rank":(?P<top>.*?),"cover_url":.*?","types":(?P<type>.*?),"regions":.*?,"title":"(?P<name>.*?)"')
tect = obj.finditer(rect.text)
for i in tect:
    print(i.group('name','type','top'))