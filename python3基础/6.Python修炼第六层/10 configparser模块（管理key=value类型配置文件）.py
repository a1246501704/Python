
# ConfigParser模块在python中用来读取配置文件，配置文件的格式跟windows下的ini配置文件相似，可以包含一个或多个节(section), 
# 每个节可以有多个参数（键=值）。使用的配置文件的好处就是不用在程序员写死，可以使程序更灵活。 
# 注意：在python 3 中ConfigParser模块名已更名为configparser


\针对的是xxx.cnf内容类型的配置文件，例如 mysql的配置文件my.cof文件。见my.cnf文件内容。
'''
# “[ ]”包含的为 section，section 下面为类似于 key - value 的配置内容；
# configparser 默认支持 '=' '：' 两种分隔。
# [mysql]和[mysqld]在configparser模块中叫sections
# password等在configparser模块中都叫options,options属于sections

[mysql]
user=root
password = 123

[mysqld]
character-server-set=utf-8
port=3306
x=True
y=1.3
'''


import configparser

obj=configparser.ConfigParser()
obj.read('my.cnf')

print(obj.sections())       # ['mysql', 'mysqld']
print(obj.options('mysql')) # 看mysql这个sections下有哪些options,['user', 'password']
print(obj.items('mysql'))   # 看mysql这个sections每个options的key和值,[('user', 'root'), ('password', '123')]

key=obj.keys()
for i in key:
    print(i)
'''
DEFAULT
mysql
mysqld
'''


# 读取
\get 方法
print(obj.get('mysql','user')) # 取值 root。取mysql这个sections下的user这个options的值。拿到的结果是字符串类型。
x=obj.get('mysqld','port')     # 取端口
print(x,type(x))               # 都是字符串类型,3306 <class 'str'>

\getint、getboolean、getfloat 方法
print(type(obj.getint('mysqld','port')))  # 拿到的是整型
print(type(obj.getboolean('mysqld','x'))) # 拿到布尔值
print(type(obj.getfloat('mysqld','y')))   # 拿到浮点型

###########################################################
[section1]
k1 = v1
k2:v2
user=egon
age=18
is_admin=true
salary=31

[section2]
k1 = v1
###########################################################
import configparser

config=configparser.ConfigParser()
config.read('a.cfg')

#查看所有的标题
res=config.sections() #['section1', 'section2']
print(res)

#查看标题section1下所有key=value的key
options=config.options('section1')
print(options) #['k1', 'k2', 'user', 'age', 'is_admin', 'salary']

#查看标题section1下所有key=value的(key,value)格式
item_list=config.items('section1')
print(item_list) #[('k1', 'v1'), ('k2', 'v2'), ('user', 'egon'), ('age', '18'), ('is_admin', 'true'), ('salary', '31')]

#查看标题section1下user的值=>字符串格式
val=config.get('section1','user')
print(val) #egon

#查看标题section1下age的值=>整数格式
val1=config.getint('section1','age')
print(val1) #18

#查看标题section1下is_admin的值=>布尔值格式
val2=config.getboolean('section1','is_admin')
print(val2) #True

#查看标题section1下salary的值=>浮点型格式
val3=config.getfloat('section1','salary')
print(val3) #31.0

------------------------> 改写 <------------------------
import configparser

config=configparser.ConfigParser()
config.read('a.cfg',encoding='utf-8')

#删除整个标题section2
config.remove_section('section2')

#删除标题section1下的某个k1和k2
config.remove_option('section1','k1')
config.remove_option('section1','k2')

#判断是否存在某个标题
print(config.has_section('section1'))

#判断标题section1下是否有user
print(config.has_option('section1','user'))

#添加一个标题
config.add_section('egon')

#在标题egon下添加name=egon,age=18的配置
config.set('egon','name','egon')
config.set('egon','age',18)     # 报错,必须是字符串'18'

#最后将修改的内容写入文件,完成最终的修改
config.write(open('a.cfg','w'))


\判断是否存在
import configparser
obj=configparser.ConfigParser()
obj.read('my.cnf')

print(obj.has_section('mysql')) # 返回布尔值
print(obj.has_option('alex','is_sbxxxxxxxxxxx'))


\修改操作
# 添加
import configparser

obj=configparser.ConfigParser()
obj.read('my.cnf')

obj.add_section('alex')           # 添加标题
obj.set('alex','password','123')  # 给标题里添加内容
obj.set('alex','is_sb','True')    # 给标题里添加内容
obj.write(open('my.cnf','w'))     # 将修改写入到文件(是将原文件读出来的内容+修改的内容=原文件新内容[清空重写])

# 删除
obj.remove_section('mysqld')      # 删除标题,删除section会将其下的key一并删除。
obj.remove_option('mysql','user') # 删除mysql标题下的user
obj.write(open('my.cnf','w'))     # 将修改写入文件


\初始化文件（类似字典的操作方式）
import configparser #引入模块

config = configparser.ConfigParser()    # 类中一个方法 #实例化一个对象

config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }	# 类似于操作字典的形式

config['bitbucket.org'] = {'User':'Atlan'} # 添加section和option，类似于操作字典的形式。
config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'} # 添加section和option，类似于操作字典的形式。
with open('example.ini', 'w') as configfile:
   config.write(configfile)	# 将对象写入文件

''' 生成的example.ini文件内容如下
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = Atlan

[topsecret.server.com]
host port = 50022
forwardx11 = no
'''
# 读取
print('bytebong.com' in config)         # False
print('bitbucket.org' in config)        # True
print(config['bitbucket.org']["user"])  # Atlan
print(config['DEFAULT']['Compression']) # yes
print(config['topsecret.server.com']['ForwardX11'])  # no
print(config['bitbucket.org'])          # <Section: bitbucket.org>
for key in config['bitbucket.org']:     # 注意,有default会默认default的键
    print(key)

print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
print(config.items('bitbucket.org'))    # 找到'bitbucket.org'下所有键值对
print(config.get('bitbucket.org','compression')) # yes  get方法Section下的key对应的value

\read_dict方式
parser = configparser.ConfigParser()
parser.read_dict({'section1': {'key1': 'value1',
                               'key2': 'value2',
                               'key3': 'value3'},
                  'section2': {'keyA': 'valueA',
                               'keyB': 'valueB',
                               'keyC': 'valueC'},
                  'section3': {'foo': 'x',
                               'bar': 'y',
                               'baz': 'z'}
                  })

print(parser.sections()) # ['section1', 'section2', 'section3']
