import time
from functools import wraps
def timmer(func):
    #func=最原始的home函数的内存地址
    @wraps(func)
    def inner(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)
        stop_time=time.time()
        print('run time is :[%s]' %(stop_time-start_time))
        return res
    return inner

@timmer #home=inner
def home(name):
    '''
    这是home函数的注释信息
    :param name:
    :return:
    '''
    time.sleep(2)
    print('welcome %s to home page' %name)
    return 456


# home('egon') #inner('egon')

# print(home.__doc__)
print(help(home))
