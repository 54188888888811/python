class A:
    def __init__(self,name='李狗蛋',age=18):
        self.n = name
        self.a = age
p = A('李华',20)#class中的self形参等于classA（）中的赋值
a = A()
print(p.n,p.a)
print(a.n ,a.a)
