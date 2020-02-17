#coding:utf-8
# 请将python版本切换至2.x版本执行代码
class A:pass
    # def func(self):
    #     print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class C(A):
    def func(self):
        print('C')

class D(B,C):pass

# d = D()
# d.func() # 深度优先查找顺序: 一条路走到黑再走另一条路。
# class A1(object): # 新式类：广度优先（继承了object类的类才是新式类）
#     pass



class A:pass
    # def func(self):
    #     print('A')

class B(A):pass
    # def func(self):
    #     print('B')

class C(A):
    def func(self):
        print('C')

class D(B):pass
    # def func(self):
    #     print('D')

class E(C):
    def func(self):
        print('E')

class F(D,E):pass
    # def func(self):
    #     print('F')

f = F()
f.func()