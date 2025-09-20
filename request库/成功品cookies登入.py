import re
import requests

url = 'https://login2.scrape.center/login?next=/'
session = requests.session()
date = {
    'username': 'admin',
    'password': 'admin'
}
session.post(url,data=date)

obj = session.get('https://login2.scrape.center/detail/2')
with open('llq.html','w',encoding='utf-8')as f:
    f.write(obj.text)