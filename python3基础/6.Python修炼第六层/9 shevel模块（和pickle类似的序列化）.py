

\shelve模块比pickle模块简单，只有一个open函数，返回类似字典的对象，可读可写;key必须为字符串，而值可以是python所支持的数据类型.


import shelve # 序列化时就像操作字典一样

f=shelve.open(r'sheve.txt') # 打开一个文件
f['stu1_info']={'name':'egon','age':18,'hobby':['piao','smoking','drinking']} # 写数据
f['stu2_info']={'name':'gangdan','age':53}                                    # 写数据
f['school_info']={'website':'http://www.pypy.org','city':'beijing'}           # 写数据

print(f['stu1_info']['hobby']) # 查数据
f.close()                      # 关闭文件
########################################




import shelve

dic={'a':1,'b':2}
# 存数据
d=shelve.open(r'db.shl')  # 创建这个文件，实际对应着三个文件。
d['egon']={'pwd':'123','age':18} # 存数据
d['alex']={'pwd':'123465','age':18} # 存数据
d['x']=dic  # 也可将字典存进去，x当key。

d.close()

# 取数据
obj=shelve.open(r'db.shl') # 打开
print(obj['x']['a'])       # 取数据，取1

obj.close()