# 为什么要用序列化:
    数据存储
    网络传输

# json    主流，跨平台数据交互，能识别python的数据类型有限。
# pickle  不跨平台数据交互，支持python所有数据。
# shaevel 把数字当成一个字典操作、操作简单


import json,pickle


\json
d={'a':1}

print(type(json.dumps(d))) # <class 'str'>
print(json.dumps(d))       # {"a": 1} 
with open('1.json','w') as f:
    f.write(json.dumps(d)) # dumps 是把json格式数据以字符串的形式写如到文件中。

with open('2.json','r') as f:
    data=f.read()
    print(json.loads(data)['a']) # loads 是把文件中的json格式的字符串反解成字典。

print(json.loads('{"name":1}')['name']) # 1  只要传参是json格式的字符串就行，不一定是存放在文件中的json的字符串。

l=[1,2,3,'a'] # json不识别单引号
print(json.loads('[1,2,3,"a"]')[1]) # 将单引号改成双引号直接传给loads

# dump序列化、load反序列化
json.dump(d,open('3.json','w')) # d为要序列化的对象、open打开一个文件、w写的方式
print(json.load(open('3.json','r'))['a'])


# 遍历json字符串
json_str = {"name":"lisi",
            "age":27}
# json解析并按key排序
json_str = json.dumps(params, sort_keys=True)
# 将 JSON 对象转换为 Python 字典
params_json = json.loads(json_str)

items = params_json.items()
for key, value in items:
    print(str(key) + '=' + str(value))



\pickle 
d={'a':1}

# 序列化
d_pkl=pickle.dumps(d)
print(d_pkl,type(d_pkl)) # 序列化后是 bytes 类型
with open('1.pkl','wb') as f:
    f.write(d_pkl)

pickle.dump(d,open('2.pkl','wb')) # 上面的简写成一步

# 反序列化
x=pickle.load(open('2.pkl','rb'))
print(x,type(x))


\证明pickle能序列化所有的python类型
import json,pickle
# 序列化
def func():
    print('from 序列表.py')

json.dumps(func) # 报错，json不支持函数序列化。

print(pickle.dumps(func)) # 不报错，说明pickel支持。func对应的是内存地址，序列化是将这个地址序列化了。
pickle.dump(func,open('3.pkl','wb'))

# 反解
def func():
    print('==================>') # 反解前先把func函数定义，函数体内容无所谓。序列化函数没什么意义，只是在单纯的证明可以序列化此类型。

f=pickle.load(open('3.pkl','rb'))
f()