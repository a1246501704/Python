
# 字符串练习题
# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
# name = " aleX"
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip())
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# print(name.startswith('al'))
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# print(name.endswith('X'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace('l','p'))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split('l'))
# 6)    将 name 变量对应的值变大写,并输出结果 
# print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果 
# print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[0:3])
# 10)    请输出 name 变量对应的值的后 2 个字符? 
# print(name[-2:])
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# print(name.index('e'))
# 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# name = " aleX"
# a=name[:-1]
# print(a)

# 列表练习题

# 1. 有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
#
# 2. 用列表模拟队列
    # 列：先进先出
    # ppend，pop
    # l1=[]
    # l1.append('first')
    # l1.append('second')
    # l1.append('third')
    #
    # print(l1.pop(0))
    # print(l1.pop(0))
    # print(l1.pop(0))
# 3. 用列表模拟堆栈
    # l1=[]
    # l1.insert(0,'first')
    # l1.insert(0,'second')
    # l1.insert(0,'third')
    # print(l1)
    # print(l1.pop(0))
    # print(l1.pop(0))
    # print(l1.pop(0))
# 4. 有如下列表，请按照年龄排序（涉及到匿名函数）
# l=[
#     {'name':'alex','age':84},
#     {'name':'oldboy','age':73},
#     {'name':'egon','age':18},
# ]
# 答案：
# l.sort(key=lambda item:item['age'])
# print(l)

# 元组练习题
#简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入　　

# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
# goods_1=[]
#
# while True:
#     for key in msg_dic:
#         print(key,msg_dic[key])
#     choice = input("商品>>: ")
#     if choice not in msg_dic:
#         print("没有",choice,"此商品")
#         continue
#     count = input("个数>>: ")
#     if count.isdigit():
#         goods_1.append((choice,msg_dic[choice],int(count)))
#         print(goods_1)


# 字典练习题
# 1 有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
# l1=[11,22,33,44,55,66,77,88,99,90]
# l2={'k1':[],'k2':[]}
# for i in l1:
#     if i > 66:
#         l2['k1'].append(i)
#     if i < 66:
#         l2['k2'].append(i)
# print(l2)

# 2 统计s='hello alex alex say hello sb sb'中每个单词的个数
# 结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
# s='hello alex alex say hello sb sb'
# l=s.split()
# dic={}
# for item in l:
#     print(item)
#     if item in dic:
#         dic[item]+=1
#     else:
#         dic[item]=1
# print(dic)


# # 集合练习题
# # 一.关系运算
# # 有如下两个集合，pythons是报名python课程的学员名字集合，linuxs是报名linux课程的学员名字集合
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
# # 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# # 求出所有报名的学生名字集合
# print(pythons | linuxs)
# # 求出只报名python课程的学员名字
# print(pythons - linuxs)
# # 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)

#  　　二.去重
# 　　 1. 有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
# 　　 2.在上题的基础上，保存列表原来的顺序
# 　　 3.去除文件中重复的行，肯定要保持文件内容的顺序不变
# 　　 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
# l=[
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'alex','age':73,'sex':'male'},
#     {'name':'egon','age':20,'sex':'female'},
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'egon','age':18,'sex':'male'},
# ]
# s=set()
# l1=[]
# for item in l:
#     val=(item['name'],item['age'],item['sex'])
#     if val not in s:
#         s.add(val)
#         l1.append(item)
# print(l1)

# #去重,无需保持原来的顺序
# l=['a','b',1,'a','a']
# print(set(l))


























