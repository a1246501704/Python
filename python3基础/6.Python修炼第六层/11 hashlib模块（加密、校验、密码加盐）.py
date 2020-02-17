# 1、什么叫hash:hash是一种算法（3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法）
# ，该算法接受传入的内容，经过运算得到一串hash值。
# 2、hash值的特点是：
    # 2.1 只要传入的内容一样，得到的hash值必然一样。 -----> 要用明文传输密码文件完整性校验.
    # 2.2 不能由hash值返解成内容（不可逆推）。 -----> 把密码做成hash值，不应该在网络传输明文密码.
    # 2.3 只要使用的hash算法是一样的，无论校验的内容有多大，得到的hash值长度是固定的.
hash算法就像一座工厂，工厂接收你送来的原材料（可以用m.update()为工厂运送原材料），经过加工返回的产品就是hash值.
原材料 -----> hash工厂 -----> hash值

import hashlib

m=hashlib.md5()

\将hello world分两次校验
m.update('hello'.encode('utf-8')) # encode成bytes类型后update提交
m.update('world'.encode('utf-8')) # hello和world分开提交和一起提交得到的hash值是一样的，保证大文件校验时无误。
print(m.hexdigest())              # 查看生成的hash值，fc5e038d38a57032085441e7fe7010b0

\将hello world一次校验
n=hashlib.md5()
n.update('helloworld'.encode('utf-8')) # 提交一次和上面提交两次得到的hash值是一样的
print(n.hexdigest())                   # fc5e038d38a57032085441e7fe7010b0


\校验文件内容
# 一次校验（文件内容过大时不适用）
with open(r'C:\Users\Administrator\PycharmProjects\19期\day6\7_sys模块.py','rb') as f:
    m=hashlib.md5()
    m.update(f.read())
    print(m.hexdigest()) # 267214cb9601ca23ebd9dd604b74a20f

# 一行一行校验（文件大小都适用）
with open(r'C:\Users\Administrator\PycharmProjects\19期\day6\7_sys模块.py','rb') as f:
    m=hashlib.md5()
    for line in f:
        m.update(line)
    print(m.hexdigest()) # 267214cb9601ca23ebd9dd604b74a20f  结果是一样的


\密文传输
s='alex3714'

m=hashlib.md5()
m.update(s.encode('utf-8'))
s_hash=m.hexdigest()

print(s_hash) # hash值外人无法反解，但是可以暴力破解。服务端就存hash值。

\暴力破解（撞库原理）
passwds=[
    'alex3714',
    '123456',
    'alex123',
    '123alex',
    'Alex@3012'
]

def make_dic(passwds):
    dic={}
    for passwd in passwds:
        m=hashlib.md5() # 还要猜中用的是哪种加密算法
        m.update(passwd.encode('utf-8'))
        dic[passwd]=m.hexdigest()
    return dic
# print(make_dic(passwds)) # 这样就拿到新的密码和hash对应的字典了。

def break_code(s1,dic):
    for p in dic:
        if s1 == dic[p]:
            return p

s1='aee949757a2e698417463d47acac93df' # 截获的hash值

dic=make_dic(passwds)
res=break_code(s1,dic)

print(res)



\密码加盐（避免撞库风险）

import hashlib

m=hashlib.md5('天王盖地虎'.encode('utf-8')) # 开头加加盐（天王盖地虎）
# # m=hashlib.sha512('天王盖地虎'.encode('utf-8')) # 更长的加密
m.update('alex3714'.encode('utf-8')) # 真正的密码
m.update('宝塔镇河妖'.encode('utf-8')) # 结尾加盐（宝塔镇河妖）
print(m.hexdigest()) # b74c5a073f1faf83dbc7b3c30a10ef4d，服务端只存加密值，不用去去除盐。


\比hash高级的加密
import hmac
# 要想保证俩次校验的结果是一样的，处理内容必须以外，key必须一样。

m1=hmac.new('哈了个哈'.encode('utf-8')) # 强制加盐，必须加。
m1.update('alex3714'.encode('utf-8'))
m1.update('个哈'.encode('utf-8'))
print(m1.hexdigest())


m2 = hmac.new('哈'.encode('utf-8'))
m2.update('了个哈alex3714'.encode('utf-8'))
print(m2.hexdigest()) # 这样的加密值是不一样的，不能这样使用。


m3 = hmac.new('哈了个哈'.encode('utf-8'))
m3.update('alex'.encode('utf-8'))
m3.update('3714'.encode('utf-8'))
print(m3.hexdigest()) # 这样的加密值是一样的。

















