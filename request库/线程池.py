from concurrent.futures import ThreadPoolExecutor
def frc():
    for i in range(10000):
        print('frc{}次'.format(i))
    for d in range(10000):
        print('ger{}次'.format(d))
def Jap():
    for z in range(10000):
        print('jap{}次'.format(z))
def USA():
    for s in range(10000):
        print('USA{}次'.format(s))
# def vcr():
#
if __name__ == '__main__':
    with ThreadPoolExecutor(500)as t:
        t.submit(frc)
        t.submit(Jap)
        t.submit(USA)
        for o in range(10000):
            print('vcr{}次'.format(o))