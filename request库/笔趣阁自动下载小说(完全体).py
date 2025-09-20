import re
import requests

#完美实现
a = 1


def book_down(a, x):
    url = 'https://www.bqgui.cc/book/875/{}.html'.format(a)  #想下哪本填网址
    heaners = {
        'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 '
            'Safari/537.36 Edg/127.0.0.0'
    }
    resp = requests.get(url, headers=heaners)
    resp.encoding = resp.apparent_encoding
    #print(resp.text)
    topic_obj = re.compile(r'class="Readarea ReadAjax_content">\s\s(?P<topic>.*?)<br /><br />', re.S)
    #实现小说主体的开头一句的re
    obj = re.compile(r'(<br /><br />\s\s(?P<book>.*?)<br /><br />)', re.S)
    #小说剩余部分的re
    book_topic = topic_obj.finditer(resp.text)
    books = obj.finditer(resp.text)
    for i in books:
        books_s = i.group('book')
        for d in book_topic:
            book_t = d.group('topic')
            with open('{}.txt'.format(x), 'a', encoding='utf-8') as b:
                b.write(book_t)
                print('over')
                #为小说添加开头一句
        with open('{}.txt'.format(x), 'a', encoding='utf-8') as b:
            b.write(books_s)
            print('over')
            #小说的后文


c = eval(input('请输入要下载到的章节（数字）'))
while a < c:    #实现下载章节的变化
    book_down(a, 1)
    a += 1
