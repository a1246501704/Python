
#item系列把 对象做成了 跟字典对象一样(增删改查)

class Foo:
    def __getitem__(self, item):
        print('=====>get')
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key]=value
        # setattr(self,key,value)

    def __delitem__(self, key):
        self.__dict__.pop(key)


f=Foo()
# f.x=1
# print(f.x)
# print(f.__dict__)

f['x']=123123123123

# del f['x']

print(f['x'])
