# 叠加多个装饰器
# 1. 加载顺序(outter函数的调用顺序):自下而上
# 2. 执行顺序(wrapper函数的执行顺序):自上而下
# 装饰器装饰正下方的函数，多个装饰器同时使用时有顺序一说。

总结：装饰器就是闭包函数，一个内部函数外面包了一层外部函数。


\案例一
import time
current_status={'user':None,'login_status':False}

# 装饰器1
def timmer(func):
    def inner(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
        return res
    return inner

# 装饰器2
def auth(egine='file'):
    # egine='file'
    def wrapper(func):
        def inner(*args,**kwargs):
            if current_status['user'] and current_status['login_status']:
                res = func(*args, **kwargs)
                return res
            if egine == 'file':
                u = 'egon'
                p = '123'
            elif egine == 'mysql':
                u = 'egon'
                p = '123'
            elif egine == 'ldap':
                u = 'egon'
                p = '123'
            else:
                pass
            name = input('username>>:').strip()
            pwd = input('password>>:').strip()
            if name == u and pwd == p:
                print('login successfull')
                current_status['user'] = name
                current_status['login_status'] = True
                res = func(*args, **kwargs)
                return res
        return inner
    return wrapper

# 装饰index函数
@auth(egine='ldap') # 执行步骤2：执行auth拿到@wrapper，index=wrapper(timmer_inner)。  ## auth装饰timmer函数，timmer函数装饰index函数。
@timmer             # 执行步骤1：timmer_inner=timmer(index)。## timmer装饰不能在auth装饰器上面，否则统计的是auth函数的执行时间。
def index():
    time.sleep(3)
    print('welcome to index page')
    return 123

index() # inner()



\案例二
def outter1(func1): #func1=wrapper2的内存地址
    print('加载了outter1')
    def wrapper1(*args,**kwargs):
        print('执行了wrapper1')
        res1=func1(*args,**kwargs)
        return res1
    return wrapper1

def outter2(func2): #func2=wrapper3的内存地址
    print('加载了outter2')
    def wrapper2(*args,**kwargs):
        print('执行了wrapper2')
        res2=func2(*args,**kwargs)
        return res2
    return wrapper2

def outter3(func3): # func3=最原始的那个index的内存地址
    print('加载了outter3')
    def wrapper3(*args,**kwargs):
        print('执行了wrapper3')
        res3=func3(*args,**kwargs)
        return res3
    return wrapper3

@outter1 # outter1(wrapper2的内存地址)======>index=wrapper1的内存地址
@outter2 # outter2(wrapper3的内存地址)======>wrapper2的内存地址
@outter3 # outter3(最原始的那个index的内存地址)===>wrapper3的内存地址
def index():
    print('from index')

print('======================================================')
index()

