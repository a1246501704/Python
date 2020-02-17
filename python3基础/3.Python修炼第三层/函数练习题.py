
# 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
#1
# def modify_file(filename,old,new):
#     import os
#     with open(filename,'r',encoding='utf-8') as read_f,\
#         open('.bak.swap','w',encoding='utf-8') as write_f:
#         for line in read_f:
#             if old in line:
#                 line=line.replace(old,new)
#             write_f.write(line)
#     os.remove(filename)
#     os.rename('.bak.swap',filename)
#
# modify_file('/xxxx/xxxx/a.txt','alex','sb')

# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
#2
# def check_str(msg):
#     res={
#         'num':0,
#         'string':0,
#         'space':0,
#         'other':0,
#     }
#     for s in msg:
#         if s.isdigit():
#             res['num']+=1
#         elif s.isalpha():
#             res['string']+=1
#         elif s.isspace():
#             res['space']+=1
#         else:
#             res['other']+=1
#     return res
# res=check_str('hello name:aSB password:alex3714')
# print(res)

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#4
# def func1(seq):
#     if len(seq) > 2:
#         seq=seq[0:2]
#     return seq
# print(func1([1,2,3,4]))

# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
#5
# def func2(seq):
#     return seq[::2]
# print(func2([1,2,3,4,5,6,7]))

# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

#6
# def func3(dic):
#     d={}
#     for k,v in dic.items():
#         if len(v) > 2:
#             d[k]=v[0:2]
#     return d
# print(func3({'k1':'abcdef','k2':[1,2,3,4],'k3':('a','b','c')}))




























