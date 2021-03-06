import re

'''
思路

+-
*/
()
优先级处理

思路一：正则表达式+递归

思路二：堆栈的方式，先进后出

    队列：先进先出
        台阶电梯-->> 队列
        上电梯(入队123)：第三个人，第二个人，第一个人
        下电梯(出队123)：第一个人，第二个人，第三个人

    堆栈：先进后出，后进先出
        衣服箱子-->> 堆栈
        装衣服(入栈123)：第三件衣服，第二件衣服，第一间衣服
        取衣服(出栈321)：第三件衣服，第二件衣服，第一间衣服


队列
进队：l.insert(0,'元素')
出队：l.pop()

进队：l.append('元素')
出队：l.pop(0)

堆栈：
进栈：l.insert(0,'元素')
出栈: l.pop(0)

进栈：l.append('元素')
出栈：l.pop()

'''


# # 队列
#
# # insert实现队列  往指定位置添加
# l=[]
# l.insert(0,'p1')
# l.insert(0,'p2')
# l.insert(0,'p3')
# print(l)
# print(l.pop())
# print(l.pop())
# print(l.pop())
# # ['p3', 'p2', 'p1']
# # p1,p2,p3
#
# # append实现队列  在列表右边添加
# l=[]
# l.append('p1')
# l.append('p2')
# l.append('p3')
# print(l)
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))


# # 堆栈  列表insert实现
# l=[]
# l.insert(0,'a1')
# l.insert(0,'a2')
# l.insert(0,'a3')
# print(l)
# print(l.pop(0))
# print(l.pop(0))
# print(l.pop(0))


'''
# -1-2*((-60+30+(-40/5)*(-9-2*-5/30-7/3*99/4*2998+10/-568/14))-(-4*-3)/(16-3*2))+3


-1-2*(-60+30+(-3+2-1-40/5)*(-9-2*-5/20))-3
-111-3
-114

分析数学表达式
从左往右匹配
区分负数与运算符
读一个 数字 一个运算符 一个数字
表达式单元执行与否与下一个运算符的到来有关系
括号的优先级最高
    匹配到左括号时，继续往右匹配
    当匹配到右括号，应该从右往左运算，直到遇到括号，
    括号内的运算符优先级 右边是最高的
    括号内的 表达式已经按照之前的规则排好序，+和-在左边，*和/在右边，
    当括号内的表达式 运算完毕 去掉括号

定义两个栈 (先进后出，后进先出)
处理是按照 提取数字 提取运算符 拿后一个运算符去跟前一个运算符比较

-1-2*(-6+3*2)-1

数字栈(0-9)

运算符栈(+-*/)



'''















