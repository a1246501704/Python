一：编写函数，（函数执行的时间是随机的）
二：编写装饰器，为函数加上统计时间的功能
三：编写装饰器，为函数加上认证的功能

四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果

七：为题目五编写装饰器，实现缓存网页内容的功能：
具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中

八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作

九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
注意：时间格式的获取
import time
time.strftime('%Y-%m-%d %X')

====================================================================================================================
#题目一:略（已实现）
#题目二:略（已实现）
#题目三:略（已实现）
#题目四：
db='db.txt'
login_status={'user':None,'status':False}
def auth(auth_type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args,**kwargs)
            if auth_type == 'file':
                with open(db,encoding='utf-8') as f:
                    dic=eval(f.read())
                name=input('username: ').strip()
                password=input('password: ').strip()
                if name in dic and password == dic[name]:
                    login_status['user']=name
                    login_status['status']=True
                    res=func(*args,**kwargs)
                    return res
                else:
                    print('username or password error')
            elif auth_type == 'sql':
                pass
            else:
                pass
        return wrapper
    return auth2

@auth()
def index():
    print('index')

@auth(auth_type='file')
def home(name):
    print('welcome %s to home' %name)


# index()
# home('egon')

#题目五
import time,random
user={'user':None,'login_time':None,'timeout':0.000003,}

def timmer(func):
    def wrapper(*args,**kwargs):
        s1=time.time()
        res=func(*args,**kwargs)
        s2=time.time()
        print('%s' %(s2-s1))
        return res
    return wrapper


def auth(func):
    def wrapper(*args,**kwargs):
        if user['user']:
            timeout=time.time()-user['login_time']
            if timeout < user['timeout']:
                return func(*args,**kwargs)
        name=input('name>>: ').strip()
        password=input('password>>: ').strip()
        if name == 'egon' and password == '123':
            user['user']=name
            user['login_time']=time.time()
            res=func(*args,**kwargs)
            return res
    return wrapper

@auth
def index():
    time.sleep(random.randrange(3))
    print('welcome to index')

@auth
def home(name):
    time.sleep(random.randrange(3))
    print('welcome %s to home ' %name)

index()
home('egon')

#题目六:略(已实现)
#题目七：简单版本
import requests
import os
cache_file='cache.txt'
def make_cache(func):
    def wrapper(*args,**kwargs):
        if not os.path.exists(cache_file):
            with open(cache_file,'w'):pass

        if os.path.getsize(cache_file):
            with open(cache_file,'r',encoding='utf-8') as f:
                res=f.read()
        else:
            res=func(*args,**kwargs)
            with open(cache_file,'w',encoding='utf-8') as f:
                f.write(res)
        return res
    return wrapper

@make_cache
def get(url):
    return requests.get(url).text


# res=get('https://www.python.org')

# print(res)

#题目七:扩展版本
import requests,os,hashlib
engine_settings={
    'file':{'dirname':'./db'},
    'mysql':{
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'password':'123'},
    'redis':{
        'host':'127.0.0.1',
        'port':6379,
        'user':'root',
        'password':'123'},
}

def make_cache(engine='file'):
    if engine not in engine_settings:
        raise TypeError('egine not valid')
    def deco(func):
        def wrapper(url):
            if engine == 'file':
                m=hashlib.md5(url.encode('utf-8'))
                cache_filename=m.hexdigest()
                cache_filepath=r'%s/%s' %(engine_settings['file']['dirname'],cache_filename)

                if os.path.exists(cache_filepath) and os.path.getsize(cache_filepath):
                    return open(cache_filepath,encoding='utf-8').read()

                res=func(url)
                with open(cache_filepath,'w',encoding='utf-8') as f:
                    f.write(res)
                return res
            elif engine == 'mysql':
                pass
            elif engine == 'redis':
                pass
            else:
                pass

        return wrapper
    return deco

@make_cache(engine='file')
def get(url):
    return requests.get(url).text

# print(get('https://www.python.org'))
print(get('https://www.baidu.com'))


#题目八
route_dic={}

def make_route(name):
    def deco(func):
        route_dic[name]=func
    return deco
@make_route('select')
def func1():
    print('select')

@make_route('insert')
def func2():
    print('insert')

@make_route('update')
def func3():
    print('update')

@make_route('delete')
def func4():
    print('delete')

print(route_dic)


#题目九
import time
import os

def logger(logfile):
    def deco(func):
        if not os.path.exists(logfile):
            with open(logfile,'w'):pass

        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            with open(logfile,'a',encoding='utf-8') as f:
                f.write('%s %s run\n' %(time.strftime('%Y-%m-%d %X'),func.__name__))
            return res
        return wrapper
    return deco

@logger(logfile='aaaaaaaaaaaaaaaaaaaaa.log')
def index():
    print('index')

index()