# 作用：存多个值,key-value存取，取值速度快.消耗性能。
# 定义：key必须是不可变类型，value可以是任意类型.
# 可变类型

\字典方法
dict.get     # 查询，没有时不报错
dict.items   # 查询所有的key:value
dict.keys    # 查询所有的key
dict.values  # 查询所有的value
dict.fromkeys
dict.copy
dict.pop     # 指定ke已删除
dict.popitem # 随机删除
dict.setdefault # 设置默认值
dict.update
dict.clear   # 清除

d={'a':1}
d={0:1}
d={[1,2,3]:1}      # 列表不能当做字典的key,可以当作value
d={(0,'mac'):3000} # 元组可以当作字典的key
print(d[(0,'mac')])

\优先掌握的操作：
# 按key存取值：可存可取
info={'name':'egon','age':18,'sex':'male'} #本质info=dict({....})

print(info['sex']) # 取
info['hobbies']=['read','music','play','sleep','eat'] # 存列表
print(info)
info['pig']=('eat','drink','sleep')  # 存元组
print(info)

# 长度len
print(len(info))

# 成员运算 in 和 not in，指的是key值。
成员运算用的是字典的key

# 删除，按照key值删除
print(info.pop('name')) # 返回被删除key的值
print(info.pop('name1213','确实是没有的，我的哥')) # 没有这个key时指定一个默认输出，否则会报错。
print(info.pop('name1213',None)) # 如果没有值就返回None。

# 键keys()，值values()，键值对items()，返回结果是个可以直接被for循环in的可迭代类型。
print(info.keys())  # dict_keys(['name', 'age', 'sex']) ，以看似列表的形式输出所有key
print(info.values())# dict_values(['egon', 18, 'male']) ，以看似列表的形式输出所有value
print(info.items()) # dict_items([('name', 'egon'), ('age', 18), ('sex', 'male')]) ,以看似列表的形式输出所有key:value。

# 取出来的用途可以用于for循环
for key in info.keys():
    print(key)
'''
name 
age
sex
'''
for val in info.values():
    print(val)
'''
egon
18
male
'''
for item in info.items():
    print(item)            # 直接print(item)打印的是元组
'''
('name', 'egon')
('age', 18)
('sex', 'male')
'''
for item in info.items():
    print(item[0],item[1])  
'''
name egon
age 18
sex male
'''
for k,v in info.items(): # 解压赋值
    print(k,v)  
'''
name egon
age 18
sex male
'''
# 循环


\常用方法
info={'name':'egon','age':18,'sex':'male'}
# 查询一个不存在的key时会报错
print(info['name']) 
print(info['name123']) 
# 查询字典中的key
print(info.get('name123'))     # None，值不存在不会报错
print(info.get('name123',123)) # 使用get当key值不存在时默认会输出None,还可以指定返回值。如123.
# 删除item，一个item由（一对key/value）组成
print(info.popitem()) # 随机删除字典中的key，不能指定。以元组的形式返回剩下的key。
# ('sex', 'male')

\update: 更新 
info_new={'a':1,'age':19}
info.update(info_new)
print(info) # {'name': 'egon', 'age': 19, 'sex': 'male', 'a': 1} ,没有的key会添加加进去，已有的key将值覆盖。

\fromkeys: 快速初始化一个字典 
dice1={}.fromkeys(['name','age','hobbies'],None) # 可以带入列表、元组
print(dice1) # {'name': None, 'age': None, 'hobbies': None}

\setdefault: 设置默认值
# 语法: result = dict.setdefault(key, default=None)
    # key: 查找的键值
    # default: 键不存在时，设置的默认键值
    # result: 键存在返回键值， 否则返回default
In [1]: kwargs = {'name': 'Lilei'}
In [2]: item = kwargs.setdefault('name', 'zhangsan')
#取到对应的键值 item-->Lilei
In [3]: item
Out[3]: 'Lilei'

In [5]: new = kwargs.setdefault('info', {})
#没有对应的键 item-->default-->{}
In [6]: new
Out[6]: {}

In [7]: kwargs
Out[7]: {'info': {}, 'name': 'Lilei'}
#向字典中插入info，值为{}
In [8]: new.setdefault('score', '90')
Out[8]: '90'

In [9]: new
Out[9]: {'score': '90'}
#new对应的是kwargs中info的值{}， 然后给它赋值{'score': '90'}
In [10]: kwargs
Out[10]: {'info': {'score': '90'}, 'name': 'Lilei'}


info={'name':'egon','age':18,'sex':'male'}
print(info.setdefault('age',19))  # 如果字典中已经存在这个key，则不修改,返回这个key的值。如果不存在则添加。
print(info.setdefault('hobbies',['read','music'])) # 有则不改，返回已经有的值，没有则从末尾新增，返回新增的值
print(info)

print(id(info.setdefault('hobbies',[]))) 
print(info)
print(id(info['hobbies']))
'''
4401483656
{'name': 'egon', 'age': 18, 'sex': 'male', 'hobbies': []}
4401483656
'''

\追加: append方法（不方便）,setdefault方便。
# 使用if判断追加
info={'name':'egon','age':18,'sex':'male',}
if 'hobbies' not in info:
    info['hobbies']=[]
    info['hobbies'].append('music')
else:
    info['hobbies'].append('read')

if 'hobbies' not in info:
    info['hobbies'] = []
    info['hobbies'].append('music')
else:
    info['hobbies'].append('read')

print(info)
{'name': 'egon', 'age': 18, 'sex': 'male', 'hobbies': ['music', 'read']}

# 使用setdefault添加更为简便
# hobbies不在info里则新添加一个key并添加一个空值，然后追加了一个新值。
info.setdefault('hobbies',[]).append('music') 
print(info) # {'name': 'egon', 'age': 18, 'sex': 'male', 'hobbies': ['music', ]}
# 继续为名为hobbies的key添加value，因为hobbies已经在info中存在，所以直接append
info.setdefault('hobbies',[]).append('read') #['music', ].append('read')
print(info) # {'name': 'egon', 'age': 18, 'sex': 'male', 'hobbies': ['music', 'read']}

\补充两种赋值方式：
# 一：链式赋值
x=10
y=x
x=y=z=10
print(id(x),id(y),id(z))

# 交换两个变量的值
m=10
n=20
temp=n # 先把n的值存起来
n=m #n=10
m=temp
print(m,n) 
# 太麻烦，python提供了简便的方法
m,n=n,m
print(m,n)

# 二：从一个数据类型中解压出我们想要的值，支持元组、列表、字符串
t=(10.3,11.2,12.1,14.3,3.1)

x,y,z,a,b=t      # 解压赋值,数量要和t元组中一致，不能只解压其中某个。
print(x,y,z,a,b)
print(x,b)

x,_,_,_,b=t
print(x,b)
print(_) # 取到"_"最后一次的值

x,*_,b=t # 中间任意长度都匹配_
print(x,b)

x,*_='hello'
print(x) # h

x,y,z={'a':1,'b':2,'c':3}
print(x,y,z)  # 对于字典取的是key, a b c


\练习
# 1、有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于66的值
# 保存至第二个key的值中即：{'k1': 大于66的所有值, 'k2': 小于66的所有值}
a={'k1':[],'k2':[]}
c=[11,22,33,44,55,66,77,88,99,90]
for i in c:
    if i>66:
        a['k1'].append(i)
    else:
        a['k2'].append(i)
print(a) # {'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55, 66]}

# 2、统计s='hello alex alex say hello sb sb'中每个单词的个数
# 结果如：{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
s='hello alex alex say hello sb sb'
l=s.split()
dic={}
for item in l:
    if item in dic:
        dic[item]+=1   # 改变字典中key的值
    else:
        dic[item]=1
print(dic) # {'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}

# 3、其他做法（重点看setdefault的用法）
s='hello alex alex say hello sb sb'
dic={}
words=s.split()
print(words)
for word in words: # word='alex'
    dic[word]=s.count(word) # 统计每个单词在列表中的个数,字典里没有则新加个值
    print(dic)
'''
['hello', 'alex', 'alex', 'say', 'hello', 'sb', 'sb']
{'hello': 2}
{'hello': 2, 'alex': 2}
{'hello': 2, 'alex': 2}
{'hello': 2, 'alex': 2, 'say': 1}
{'hello': 2, 'alex': 2, 'say': 1}
{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
'''

# 利用setdefault解决重复赋值
'''
setdefault的功能
1：key存在，则不赋值，key不存在则设置默认值
2：key存在，返回的是key对应的已有的值，key不存在，返回的则是要设置的默认值
d={}
print(d.setdefault('a',1)) # 返回1

d={'a':2222}
print(d.setdefault('a',1)) # 返回2222
'''
s='hello alex alex say hello sb sb'
dic={}
words=s.split()
print(words)
for word in words: #word='alex'
    dic.setdefault(word,s.count(word))
    print(dic)
'''
['hello', 'alex', 'alex', 'say', 'hello', 'sb', 'sb']
{'hello': 2}
{'hello': 2, 'alex': 2}
{'hello': 2, 'alex': 2}
{'hello': 2, 'alex': 2, 'say': 1}
{'hello': 2, 'alex': 2, 'say': 1}
{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
{'hello': 2, 'alex': 2, 'say': 1, 'sb': 2}
'''

# 利用集合，去掉重复，减少循环次数
s='hello alex alex say hello sb sb'
dic={}
words=s.split()
print(words)
words_set=set(words) 
print(words_set)
# set 和 dict 类似，也是一组 key 的集合，但是不存储 value。 
# 由于 key 不重复，所以，在 set 中，没有重复的 key 集合是可变类型。
for word in words_set:
    dic[word]=s.count(word)
    print(dic)
'''
['hello', 'alex', 'alex', 'say', 'hello', 'sb', 'sb']
{'say', 'hello', 'sb', 'alex'}
{'say': 1}
{'say': 1, 'hello': 2}
{'say': 1, 'hello': 2, 'sb': 2}
{'say': 1, 'hello': 2, 'sb': 2, 'alex': 2}
'''

