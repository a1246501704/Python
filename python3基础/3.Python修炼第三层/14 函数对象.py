\一、函数对象

\1.1 函数是第一类对象：函数可以当做数据来使用
    # 1 可以被引用
    # 2 可以当作参数传递
    # 3 返回值可以是函数
    # 4 可以当作容器类型的元素

## 可以被引用
def foo():
    print('from foo')

f=foo  # 此处的foo函数不能把（）加上，否则就成把foo的结果赋值给f变量了。
# print(f)
f()

## 可以当做参数传入一个函数（高阶函数）
def foo():
    print('from foo')

def wrapper(x):
    # print(x)
    x()  # 调wrapper后里面又执行了foo函数
wrapper(foo)

## 可以当做函数的返回值
def foo():
    print('from foo')

def wrapper():
    return foo # 返回值是另外一个函数

f=wrapper()  # 将wrapper函数的返回值foo函数赋值给f，此时f=foo
print(f is foo)

## 可以当做容器类型的一个元素
def foo():
    print('from foo')

l=[foo,1,2]
l[0]()   # 调用函数foo（即是l列表中的第0个）

\1.2 利用该特性，优雅的取代多分支的if
def foo():
    print('from foo')

def bar():
    print('from bar')

dic={
    'foo':foo,
    'bar':bar,
}
while True:
    choice=input('>>: ').strip()
    if choice in dic:
        dic[choice]()


\案例
# 用函数实现一个查询数据库的功能
data_dir='/usr/local/mysql/data'
def select(sql):
    print('select功能: ',sql)

def insert(sql):
    print('insert功能: ', sql)

def update(sql):
    print('update功能: ', sql)

def delete(sql):
    print('delete功能: ', sql)

def alter(sql):
    print('alter功能：',sql)

# 每个函数可以当做容器(字典、列表等)类型的一个元素，有了这个字典main函数体内的if判断就可以不用了。
func_dic={
    'select':select,
    'update':update,
    'insert':insert,
    'delete':delete,
    'alter':alter
}

def main():
    while True:
        inp=input('>>: ').strip()
        if not inp:continue
        sql=inp.split()
        cmd=sql[0]
        # if cmd == 'select':
        #     select(sql)
        # elif cmd == 'update':
        #     update(sql)
        # elif cmd == 'insert':
        #     insert(sql)
        # elif cmd == 'delete':
        #     delete(sql)
        if cmd in func_dic:
            func_dic[cmd](sql)
        else:
            print('command not found')

main()



