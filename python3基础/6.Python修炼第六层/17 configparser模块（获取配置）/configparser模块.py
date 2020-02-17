\python配置文件读取
在代码实现的过程中，我们经常选择将一些固定的参数值写入到一个单独的配置文件中。在python中读取配置文件官方提供了configParser方法。

项目中使用的常量，我们把它收集在一个文件中，这就是配置文件。配置文件在项目中是非常必要的，它避免了项目中文件对常量的分散使用，让常量可以统一修改，避免造成修改不全面的问题。
常用的配置文件后缀是.ini、.conf、.py，当然还有使用.json、.txt的，推荐使用常用的.ini、.py，配置文件的名字一般是config便于理解和使用。
.ini 文件是Initialization File的缩写，即初始化文件，是windows的系统配置文件所采用的存储格式，统管windows的各项配置；.py的配置文件，在python项目中是作为一个包导入，严格来说不是配置文件，而是扩展包。
下面将介绍两类配置文件的使用，一类是.ini、.txt，另一类是.py。
.ini、.txt配置文件使用方法是一致的，只是一个后缀的区别，这里以ini配置文件来介绍，这类配置文件我们使用内置configparser库来使用，它可以实现配置文件的写入、更新、删除、读取等操作非常方便，建议使用这种方式。


\使用方法如下
import configparser
config = configparser.ConfigParser()
config.read(configFilePath)
config.get(section=section, option=option)
# 写的比较简单，详细使用可以查看python安装目录doc下面的官文。

\使用示例
config.ini配置内容如下: 
[mysql]
host = 127.0.0.1
port = 3306
user = root
password = Zhsy08241128
database = leartd

现在假设我们要取出文件中的port值，实现过程为: 
# -*- coding:utf-8 -*-
import os
import configparser
 
# 项目路径
rootDir = os.path.split(os.path.realpath(__file__))[0]
# config.ini文件路径
configFilePath = os.path.join(rootDir,'config.ini')
 
def get_config_values(section,option):
    """
    根据传入的section获取对应的value
    :param section: ini配置文件中用[]标识的内容
    :return:
    """
    config = configparser.ConfigParser()
    config.read(configFilePath)
    # return config.items(section=section)
    return config.get(section=section,option=option)
 
if __name__ == '__main__':
    result = get_config_values('mysql','port')
    print(result)

\其他方法
新建一个config.ini的配置文件内容如下：
[mysql]
name = admin
host = 255.255.255.0
proxy = 6037
password = 123456
pool = true
time = 3

其中[]中的是section节点，该节点下的等式是option即键=值
config.sections()  # 获取section节点
['mysql']

config.options('mysql')             # 获取指定section 的options即该节点的所有键
['name', 'host', 'proxy', 'password', 'pool', 'time']

config.get("mysql", "name")         # 获取指定section下的options
'admin'

config.getint("mysql", "proxy")     # 将获取到值转换为int型
6037

config.getboolean("mysql", "pool")  # 将获取到值转换为bool型
True

config.getfloat("mysql", "time")    # 将获取到值转换为浮点型
3.0

config.items("mysql")               # 获取section的所用配置信息
[('name', 'admin'), ('host', '255.255.255.0'), ('proxy', '6037'), ('password', '123456'), ('pool', 'true'), ('time', '3')]

config.set("mysql", "name", "root")  # 修改db_port的值为69
config.get("mysql", "name") 
'root'

config.has_section("mysql")          # 是否存在该section
True

config.has_option("mysql", "password")  # 是否存在该option
True

config.add_section("redis")          # 添加section节点
config.set("redis", "name", "redis_admin")  # 设置指定section 的options
config.items('redis')
[('name', 'redis_admin')]

\常用方法如下
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read("Config.ini", encoding="utf-8")

config.sections()                       # 获取section节点

config.options('mysql')                 # 获取指定section 的options即该节点的所有键

config.get("mysql", "name")             # 获取指定section下的options
config.getint("mysql", "proxy")         # 将获取到值转换为int型
config.getboolean("mysql", "pool")      # 将获取到值转换为bool型
config.getfloat("mysql", "time")        # 将获取到值转换为浮点型

config.items("mysql")                   # 获取section的所用配置信息

config.set("mysql", "name", "root")     # 修改db_port的值为69

config.has_section("mysql")             # 是否存在该section
config.has_option("mysql", "password")  # 是否存在该option

config.add_section("redis")             # 添加section节点
config.set("redis", "name", "redis_admin")  # 设置指定section 的options

config.remove_section("redis")          # 整个section下的所有内容都将删除
config.remove_option("mysql", 'time')   # 删除section下的指定options

config.write(open("Config", "w"))       # 保存config


\补充
# 一、ConfigParser简介
ConfigParser 是用来读取配置文件的包。配置文件的格式如下：中括号“[ ]”内包含的为section。section 下面为类似于key-value 的配置内容。
[db]
db_host = 127.0.0.1
db_port = 69
db_user = root
db_pass = root
host_port = 69

[concurrent]
thread = 10
processor = 20

括号“[ ]”内包含的为section。紧接着section 为类似于key-value 的options 的配置内容。

# 二、ConfigParser 初始化对象
使用ConfigParser 首选需要初始化实例，并读取配置文件：

import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")

# 三、ConfigParser 常用方法
1、获取所用的section节点
# 获取所用的section节点
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
print(config.sections())
#运行结果
# ['db', 'concurrent']

2、获取指定section 的options。即将配置文件某个section 内key 读取到列表中：
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
r = config.options("db")
print(r)
#运行结果
# ['db_host', 'db_port', 'db_user', 'db_pass', 'host_port']

3、获取指点section下指点option的值
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
r = config.get("db", "db_host")
# r1 = config.getint("db", "k1") #将获取到值转换为int型
# r2 = config.getboolean("db", "k2" ) #将获取到值转换为bool型
# r3 = config.getfloat("db", "k3" ) #将获取到值转换为浮点型
print(r)
#运行结果
# 127.0.0.1

4、获取指点section的所用配置信息
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
r = config.items("db")
print(r)
#运行结果
#[('db_host', '127.0.0.1'), ('db_port', '69'), ('db_user', 'root'), ('db_pass', 'root'), ('host_port', '69')]


5、修改某个option的值，如果不存在则会出创建
# 修改某个option的值，如果不存在该option 则会创建
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
config.set("db", "db_port", "69")  #修改db_port的值为69
config.write(open("ini", "w"))

[db]
db_host = 127.0.0.1
db_port = 69
db_user = root
db_pass = root

[concurrent]
thread = 10
processor = 20

6、检查section或option是否存在，bool值
import configparser
config = configparser.ConfigParser()
config.has_section("section") #是否存在该section
config.has_option("section", "option")  #是否存在该option

7、添加section 和 option
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
if not config.has_section("default"):  # 检查是否存在section
    config.add_section("default")
if not config.has_option("default", "db_host"):  # 检查是否存在该option
    config.set("default", "db_host", "1.1.1.1")
config.write(open("ini", "w"))

[db]
db_host = 127.0.0.1
db_port = 69
db_user = root
db_pass = root

[concurrent]
thread = 10
processor = 20

[default]
db_host = 1.1.1.1


8、删除section 和 option
import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
config.remove_section("default") #整个section下的所有内容都将删除
config.write(open("ini", "w"))

[db]
db_host = 127.0.0.1
db_port = 69
db_user = root
db_pass = root

[concurrent]
thread = 10
processor = 20


9、写入文件
以下的几行代码只是将文件内容读取到内存中，进过一系列操作之后必须写回文件，才能生效。

import configparser
config = configparser.ConfigParser()
config.read("ini", encoding="utf-8")
写回文件的方式如下：（使用configparser的write方法）

config.write(open("ini", "w"))


\正式代码
import os
import configparser

rootDir = os.path.split(os.path.realpath(__file__))[0]
configFilePath = os.path.join(rootDir, 'config.ini')

def get_config_values(section,option):
    config = configparser.ConfigParser()
    config.read(configFilePath)
    return config.get(section=section,option=option)

if __name__ == '__main__':
    result = get_config_values('mysql','error_status')
    print(result)


