\为什么要序列化？序列化两个功能。
1：持久保存状态
    在断电或重启程序之前将程序当前内存中所有的数据都保存下来（保存到文件中），以便于下次程序执行能够从文件中载入之前的数据，然后继续执行，这就是序列化。
2：跨平台数据交互
    序列化之后，不仅可以把序列化后的内容写入磁盘，还可以通过网络传输到别的机器上，如果收发的双方约定好实用一种序列化的
    格式，那么便打破了平台/语言差异化带来的限制，实现了跨平台数据交互。过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。


\如何序列化之json和pickle：
\json（内存结构化数据 <----> 格式json <----> 字符串 <----> 保存至文件或者基于网络传输）
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为
# JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且
# 比XML更快，而且可以直接在Web页面中读取，非常方便。而且json只能识别双引号，不能识别单引号。

# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
#     JSON类型（跨平台交互）: {}、[]、"string"（只识别双引号）、1234.56、true/false、null
#     Python类型（Pickle支持所有python数据类型）: dict、list、str、int或float、true/false、None

user={'name':'egon','pwd':'123'}
with open('db.txt','w',encoding='utf-8') as f:
    f.write(str(user)) # 将字典转为字符串存进文件中，而且写入的都是单引号的。
'''
{'name': 'egon', 'pwd': '123'}
'''

with open('db.txt','r',encoding='utf-8') as f:
    data=f.read()
    print(type(data) # 文件中看着是字典，其实是字符串类型。这样就取出来就不是字典了，怎么办？
'''
SyntaxError: unexpected EOF while parsing
'''

# 解决办法: 使用json模块实现序列化
import json

\dumps和loads对应使用（dumps是将dict转化成str格式，loads是将str转化成dict格式。）
# 写（存）: 序列化
user={'name':'egon','pwd':'123','age':18}
with open('db.json','w',encoding='utf-8') as f:
    f.write(json.dumps(user)) # 存入的虽然也是str类型，但是是json可识别的格式的str，并且是双引号的。

# 读（取）: 反序列化
with open('db.json','r',encoding='utf-8') as f:
    data=f.read()
    print(data,type(data)) # 虽然也是str但是是json可以识别的str。
    dic=json.loads(data)   # json识别的str，取出来就还是字典。
    print(dic['name'])
'''
{"name": "egon", "pwd": "123", "age": 18} <class 'str'>
egon
'''

\注意： json序列化时，默认遇到中文会转换成unicode，如果想要保留中文在序列化时，在dumps函数中添加参数ensure_ascii=False即可解决。
\无论数据是怎样创建的，只要满足json格式，就可以json.loads出来,不一定非要dumps的数据才能loads
# 写: 序列化
user={'name':'张洪洋','pwd':'123','age':18}
with open('db.json','w',encoding='utf-8') as f:
    f.write(json.dumps(user))
# 读: 反序列化
with open('db.json','r',encoding='utf-8') as f:
    data=f.read()
    print(data,type(data)) 
    dic=json.loads(data)
    print(dic['name'])
'''
{"name": "\u5f20\u6d2a\u6d0b", "pwd": "123", "age": 18} <class 'str'>
张洪洋
'''

# 写: 序列化
user={'name':'张洪洋','pwd':'123','age':18}
with open('db.json','w',encoding='utf-8') as f:
    f.write(json.dumps(user,ensure_ascii=False)) # dumps时保留中文
# 读: 反序列化
with open('db.json','r',encoding='utf-8') as f:
    data=f.read()
    print(data,type(data)) 
    dic=json.loads(data)
    print(dic['name'])
'''
{"name": "张洪洋", "pwd": "123", "age": 18} <class 'str'>
张洪洋
'''

\与dump的区别，dumps()是将字典转换为json，可以不用通过文件，举个栗子
import json

data = {
    'name' : 'soap',
    'shares' : 90,
    'price' : 542.23
}
json_str = json.dumps(data) 
print(json_str) # {"name": "soap", "shares": 90, "price": 542.23}

\json.dump()是通过文件的形式进行处理，举个栗子：
import json

 my_dict = dict()
 with open('labels.txt', 'r', encoding='utf-8') as f:
     contents = f.readlines()
     for content in contents:
        key = content.split(':')[0]
        label_1 = content.split(':')[1].split(',')[0]
        label_2 = content.split(':')[1].split(',')[1]
        value = [label_1, label_2]
        my_dict[key] = value

with open('./filename.json', 'w', encoding='utf-8') as f:
    json.dump(my_dict, f)

'''
label.txt内容如下：

2:'地地意同了H', 'rreree'
4:'3YP65G', 'ybbreb'
'''

\dump和load对应使用（也是类似dumps和loads的功能，只是必须与文件操作结合起来了。）
user={'name':'egon','pwd':'123','age':18}
# 写: 序列化
json.dump(user,open('db1.json','w',encoding='utf-8')) 
'''
{"name": "egon", "pwd": "123", "age": 18}
'''
# 读: 反序列化
dic=json.load(open('db1.json','r',encoding='utf-8'))
print(dic,type(dic),dic['name']) # 写进去的是什么，拿出来的还是什么。没变化还是个字典。
'''
{'name': 'egon', 'pwd': '123', 'age': 18} <class 'dict'> egon
'''


import json
 
dic={'name':'alvin','age':23,'sex':'male'}
print(type(dic))#<class 'dict'>
 
# 写: 序列化
j=json.dumps(dic)
print(type(j)) #<class 'str'>
 
 
f=open('序列化对象','w')
f.write(j)  # 等价于json.dump(dic,f)
f.close()

# 读: 反序列化
import json
f=open('序列化对象')
data=json.loads(f.read()) #  等价于data=json.load(f)


\如果有多行需要写入一个文件怎么办？
d1 = {'1':2, '2':3, '3':4}
d2 = {'1':3, '2':4, '3':5}

with open('data.json', 'w') as f:
    f.write(json.dumps(d1) + '\n' + json.dumps(d2) + '\n') # 用换行分开

# 读取时自己分开
with open('data.json', 'r') as f:
    print(json.loads(f.readline())) # 读的时候要一行一行的读
    print(json.loads(f.readline()))

\将序列化写成功能函数
import json

dic={'name':'alvin','age':23,'sex':'male'}

def write_json(obj):
    with open('db.json','w',encoding='utf-8',) as f:
        f.write(json.dumps(obj))

def read_json():
    with open('db.json','r',encoding='utf-8') as f:
        data=f.read()
        return json.loads(data)

write_json(dic)
dic_1 = read_json()
print(dic_1)
dic_1['play']='book'
print(dic_1)
write_json(dic_1)

def write_json(jlist):
    # 将bx列表写入json文件
    with open('bx_list.json', 'w') as f_obj:  
        json.dump(jlist, f_obj)

def read_json():
    # 读取存储于json文件中的列表
    with open('bx_list.json', 'r') as f_obj:
        jlist = json.load(f_obj)
    return jlist

if __name__ == "__main__":
    list0=['bx-1', 'bx-2', 'bx-3', 'bx-4']
    write_json(list0)
    list1 = read_json()
    print(list1)
    list1.append('bx-5')
    print(list1)
    write_json(list1)
    print(read_json())
'''
['bx-1', 'bx-2', 'bx-3', 'bx-4']
['bx-1', 'bx-2', 'bx-3', 'bx-4', 'bx-5']
['bx-1', 'bx-2', 'bx-3', 'bx-4', 'bx-5']
'''


\pickel（内存结构化数据 <----> 格式pickel <----> bytes类型 <----> 保存至文件或者基于网络传输）
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
import pickle
 
dic={'name':'alvin','age':23,'sex':'male'}
print(type(dic)) #<class 'dict'>

#-------------------------序列化 
j=pickle.dumps(dic)
print(type(j)) #<class 'bytes'>
f=open('序列化对象_pickle','wb') # 注意是w是写入str,wb是写入bytes,j是'bytes'
f.write(j)  #-------------------等价于pickle.dump(dic,f)
f.close()

#-------------------------反序列化
import pickle
f=open('序列化对象_pickle','rb')
data=pickle.loads(f.read()) # 等价于data=pickle.load(f)
print(data['age'])