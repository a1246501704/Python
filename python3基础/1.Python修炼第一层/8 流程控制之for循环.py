for循环语句

\1、for语句的结构：
　　Python语言中的for语句与其他高级程序设计语言有很大的不同，其他高级语言for语句要用循环控制变量来控制循环。Python中for语句是通过循环遍历某一序列对象（字符串、列表、元组等）来构建循环，循环结束的条件就是对象被遍历完成。
　　for语句的形式如下：
     　　for <循环变量> in <循环对象>：
          　　<语句1>
     　　else:
          　　<语句2>
　　else语句中的语句2只有循环正常退出（遍历完所有遍历对象中的值）时执行。

# 迭代式循环：for，语法如下
# 　　for i in range(10):
# 　　　　缩进的代码块
# break与continue（同上）
# 循环嵌套

\实例
for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num/i
            print("%d等于%d*%d" % (num,i,j))
            break
    else:
        print("%d是一个质数" % num) # for在没有被break时才会执行else


for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s' %(i,j,i*j),end=' ')
    print()


\2、range()函数
　　for语句的循环对象可以是列表、元组以及字符串，可以通过range()函数产生一个迭代值，以完成计数循环。
　　range( [start,]  stop [, step])
实例：
for i in range(5):
    print(i)
'''
0
1
2
3
4
'''
for i in range(0,10,3):
    print(i)
'''
0
3
6
9
'''
for语句使用range()函数可以构建基于已知循环次数的循环程序，也可以以range()生成的数字作为索引来访问列表、元组、字符串中的值。
　　需要注意的是，range() 函数返回的对象表现为它是一个列表，但事实上它并不是，range()函数并不是在调用时一次生成整个序列，而是遍历一次才产生一个值，以减少内存的占用，其本质是一个迭代器。
如：
>>>range(10)
range(0, 10)
>>> type(range(10))
<class 'range'>
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

\循环嵌套
循环嵌套是指：在一个循环体里面嵌入另一循环。
实例1：通过while循环打印99乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print('%d*%d=%d' % (i, j, i*j), end='\t')
        i += 1
    print()
    j += 1

实例2：通过for循环打印99乘法表
for j in range(1, 10):
    for i in range(1, j+1):
        print('%d*%d=%d' % (i, j, i*j), end='\t')
        i += 1
    print()
    j += 1
'''
1*1=1   
1*2=2   2*2=4   
1*3=3   2*3=6   3*3=9   
1*4=4   2*4=8   3*4=12  4*4=16  
1*5=5   2*5=10  3*5=15  4*5=20  5*5=25  
1*6=6   2*6=12  3*6=18  4*6=24  5*6=30  6*6=36  
1*7=7   2*7=14  3*7=21  4*7=28  5*7=35  6*7=42  7*7=49  
1*8=8   2*8=16  3*8=24  4*8=32  5*8=40  6*8=48  7*8=56  8*8=64  
1*9=9   2*9=18  3*9=27  4*9=36  5*9=45  6*9=54  7*9=63  8*9=72  9*9=81
'''

实例3:打印金字塔
#分析
'''
             #max_level=5
    *        #current_level=1，空格数=4，*号数=1
   ***       #current_level=2,空格数=3,*号数=3
  *****      #current_level=3,空格数=2,*号数=5
 *******     #current_level=4,空格数=1,*号数=7
*********    #current_level=5,空格数=0,*号数=9

#数学表达式
空格数=max_level-current_level
*号数=2*current_level-1
'''

#实现
max_level=5
for current_level in range(1,max_level+1):
    for i in range(max_level-current_level):
        print(' ',end='') #在一行中连续打印多个空格
    for j in range(2*current_level-1):
        print('*',end='') #在一行中连续打印多个空格
    print()

