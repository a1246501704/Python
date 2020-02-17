

\1、无参：应用场景仅仅只是执行一些操作，比如与用户交互，打印
\2、有参：需要根据外部传进来的参数，才能执行相应的逻辑，比如统计长度，求最大值最小值
\3、空函数：设计代码结构时使用。在设计程序时先设计流程图，定义功能再逐个实现。


# 无参函数
def main():
    while True:
        user=input('>>: ').strip()
        # if len(user) == 0:continue
        if not user:continue
        password=input('>>: ')
        res=auth(user,password) # 调用auth有参函数
        if res:
            print('login successful')
        else:
            print('logon err')

# 有参：函数体的代码依赖外部传入的值。
def auth(user,pwd):
    if user == 'egon' and pwd == '123':
        return True
    else:
        return False
main()  # 调用主函数，


def my_max(x,y):
    if x > y:
        return x  # 使用return返回x的值
    else:
        return y
res=my_max(1,3)   # 这一次的调用结果就是return的返回值，赋值给变量将结果保存下来。
print(res)


\结论：
1、定义时无参，意味着调用时也无需传入参数
2、定义时有参，意味着调用时则必须传入参数

\# 空函数(重点)
# 程序的体系结构，用于写程序前制定整体结构。然后再一个一个功能去实现。
def select(sql):
    '''
    查询功能
    :param sql: 格式后的sql
    :return: xxxx
    '''
    pass

def update():
    pass

def insert():
    pass

def delete():
    pass












