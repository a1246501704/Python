\这个是无参装饰器的例子(包一层)
# 添加认证功能
import time

current_status={'user':None,'login_status':False} # 保存认证状态

#不要一步到位就写好装饰器，一步一步的写。否则就写蒙了。
def auth(func):
    def inner(*args,**kwargs):
        if current_status['user'] and current_status['login_status']: # 判断user有值并且状态是true
            res = func(*args,**kwargs)
            return res
        name=input('username>>:').strip()
        pwd=input('password>>:').strip()
        if name == 'egon' and pwd == '123':
            print('login successfull') # 登陆成功后修改字典
            current_status['user']=name
            current_status['login_status']=True
            res=func(*args,** kwargs)
            return res
    return inner

@auth # 根本原理 index=auth(index)
def index():
    time.sleep(3)
    print('welcome to index page')
    return 123

@auth # 根本原理 home=auth(home(name))
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)
    return 456

index()
home('egon')




\下面是有参装饰器的例子(包两层)

# 有参装饰器（调用auth装饰器函数时传参）
def auth(driver='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            name=input("user: ")
            pwd=input("pwd: ")
            if driver == 'file':
                if name == 'egon' and pwd == '123':
                    print('login successful')
                    res=func(*args,**kwargs)
                    return res
            elif driver == 'ldap':
                print('ldap')
        return wrapper
    return auth2

@auth(driver='file')  #给装饰器传参,本质 foo=auth(egine='file')(foo)。实际就是 @auth2 # foo=auth2(foo('egon')) 
def foo(name):
    print(name)

foo('egon') # wrapper()




import time

current_status={'user':None,'login_status':False}

# 装饰器基本最多三层就能满足需求了（一层传参、一层传被装饰器的内存地址、最内层接收被装饰对象的参数并执行被装饰对象函数）
def auth(egine='file'): # 本层用于接收被装饰对象的参数,将传的参数包给wrapper函数。需要什么参数都可以在这层传，在这层可以传多个参数。
    # egine='file'
    def wrapper(func):  # 本层接收被装饰函数的内存地址
        def inner(*args,**kwargs): # 本层接收被装饰对象的参数，怎么接的就怎么传过来。
            if current_status['user'] and current_status['login_status']:
                res = func(*args, **kwargs)
                return res
            if egine == 'file':
                print('file')
                u = 'egon'
                p = '123'
            elif egine == 'mysql':
                print('mysql auth')
                u = 'egon'
                p = '123'
            elif egine == 'ldap':
                print('ldap auth')
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

@auth(egine='ldap') # 结果得到 @wrapper -----> index=wrapper(index) 
                    # 同等于 index = auth(egine='ldap')(index) # 执行auth函数拿到 wrapper函数 ，相当于index=wrapper(index) 而index就是内部的inner函数
def index(): # 根据规律来看 被装饰对象最后都是在装饰器最内部那层去执行的 
    time.sleep(3)
    print('welcome to index page')
    return 123

index() # 实际就是在执行inner()函数

# 最原始的函数在装饰器函数的最内层，无参装饰器在最原始的函数上包了一层，有参装饰器在无参装饰器又包了一层。


