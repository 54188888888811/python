import requests

#accept-language是api的关键
#pape = 1429时停止
def down_noval():
    pape = 1429
    a = {
         "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'}
    uil = "https://www.pdske.com/247695/{}.html".format(pape)
    obj = requests.get(uil, headers=a)
    print(obj.text)


down_noval()
