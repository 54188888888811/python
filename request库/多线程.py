from threading import Thread
a = 1
def frc():
    for i in range(10000):
        print('frc{}次'.format(i))
    for d in range(10000):
        print('ger{}次'.format(d))
t = Thread(target=frc)  #创建一个多线程（子线程）
for n in range(1000):   #主线程
    t.start()   #子线程开始
    print('jap{}次'.format(n))