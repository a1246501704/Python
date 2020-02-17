

#应用场景
#在对象中的 python占用资源被释放后，触发 __del__ 方法 关闭操作系统占用资源

class Foo:
    def __init__(self,x):
        self.x=x

    def __del__(self): # 在对象资源被释放时触发
        print('-----del------')
        print(self)

f=Foo(100000)
del f
print('=======================>')





