一\递归调用的定义
# 函数递归调用:递归调用是函数嵌套调用的一种特殊形式，函数在调用时，直接或间接调用了自身，就是递归调用。

import sys
print(sys.getrecursionlimit()) # 默认为1000
sys.setrecursionlimit(2000)    # 修改递归深度
print(sys.getrecursionlimit()) # 修改后为2000

n=1
def func1():
    global n  
    print('from func1',n)
    n+=1  # 局部作用域可以读取全局作用域的名字，但是如果想要修改全局名字的值需要global 声明为全局变量。
    func1()  # 直接调用函数本身
func1()


def func():
    print('from func')
    bar()    # 间接调用本身

def bar():
    func()

func()

# 调用函数会产生局部的名称空间，占用内存，因为上述这种调用会无需调用本身，python解释器的内存管理机制为了防止其无限制占用内存，对函数的递归调用做了最大的层级限制。
可以修改递归最大深度

import sys
sys.getrecursionlimit()
sys.setrecursionlimit(2000)

def f1(n):
    print('from f1',n)
    f1(n+1)
f1(1)
# 虽然可以设置，但是因为不是尾递归，仍然要保存栈，内存大小一定，不可能无限递归，而且无限制地递归调用本身是毫无意义的，递归应该分为两个明确的阶段，递推与回溯.


二\递归调用应该分为两个明确的阶段：递推，回溯
回溯阶段必须要有一个明确地结束条件，每进入下一次递归时，问题的规模都应该有所减少（否则，单纯地重复调用自身是毫无意义的）
因为不是一下子得到结果的，每一次递归的结果在内存中保存着，决定着递归的效率不高。

递归分为两个重要的阶段：递推+回溯
递推：一层一层往下找, 每次一层都在依赖下一层给返回的结果自己才有有明确的结果.
回溯：当在某一层找到了结果，或者终止条件触发了，再一层层往回退，一层层返回结果.

# 有五个人，问第五个人的年纪时他说他比第四个人大2岁，以此类推。当问到最后一个人时他说他18岁。
# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18

# 此递归的结束条件，避免死循环。
# n!=1 # age(n)=age(n-1)+2
# n=1  # age(n)=18

def age(n):
    if n == 1:
        res = 18
        return res 
        # return 18 # 简写
    res = age(n-1)+2
    return res      # res=age(4)+2 、res=age(3)+2、res=age(2)+2、res=age(1) ，执行完所有的递推+回溯后将返回值return
    # return age(n-1)+2  # 简写

print(age(5)) # 26岁


\总结递归调用：
#1：进入下一次递归时，问题的规模必须降低。每递归一次规模就少一次。
#2：递归调用必须要有一个明确的结束条件
#3：在python中没有尾递归优化，递归调用的效率就是不高.

案例; 取出多层列表中的每个值
l=[1,2,[3,[4,[5,[6,7,[8,9,[10,[11,[12,]]]]]]]]]
def get(l):
    for item in l:
        # get(item) if isinstance(item,list)  else print(item) # 用一行三元表达式代替下面的if判断
        if isinstance(item,list):  # 判断item是不是list类型，isinstance可以判断所有数据类型。
            get(item)
        else:
            print(item)

get(l)


# 示例
def bar():
    import time
    time.sleep(3)
    return 4

def foo():
    res=bar()+3 # 都执行完才return
    return res

print(foo()) # 7














