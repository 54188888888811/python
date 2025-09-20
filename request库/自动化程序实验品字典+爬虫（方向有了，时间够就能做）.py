import re
import requests

url = 'https://bizhi.cheetahfun.com/dn/c3d/'
hander = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 '
        'Safari/537.36'
        'Edg/127.0.0.0'
}
resp = requests.get(url, headers=hander)
a = 1
yq = re.compile(r'/div> <div data-classify-id.*?data-detail=(?P<name>.*?)data-wallpaper-type="1"', re.S)

result = yq.finditer(resp.text)
women = {}
for i in result:
    print(i.group('name'))
    women[a] = i.group('name')
    a += 1
if eval(input('请输入要下载的壁纸序号')) == 1:
    print(women[1])
#后续只需要获得每张壁纸的HTML地址后就能做出来
