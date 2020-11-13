\SQLAlchemy
SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，
简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

见图

图中Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作，如：
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
 
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
 
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
 
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
 
更多详见：http://docs.sqlalchemy.org/en/latest/dialects/index.html

\步骤一：
使用图中的 Engine/ConnectionPooling/Dialect 进行数据库操作，Engine使用ConnectionPooling连接数据库，然后再通过Dialect执行SQL语句。
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)
engine.execute("INSERT INTO ts_test (a, b) VALUES ('2', 'v1')")
engine.execute("INSERT INTO ts_test (a, b) VALUES (%s, %s)",((555, "v1"),(666, "v1"),))
engine.execute("INSERT INTO ts_test (a, b) VALUES (%(id)s, %(name)s)",id=999, name="v1")
result = engine.execute('select * from ts_test')
result.fetchall()

\ 事务操作
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)

# 事务操作
with engine.begin() as conn:
    conn.execute("insert into table (x, y, z) values (1, 2, 3)")
    conn.execute("my_special_procedure(5)")
conn = engine.connect()
# 事务操作 
with conn.begin():
       conn.execute("some statement", {'x':5, 'y':10})

注：查看数据库连接：show status like 'Threads%';


\步骤二：
使用 Schema Type/SQL Expression Language/Engine/ConnectionPooling/Dialect 进行数据库操作。Engine使用Schema Type创建一个特定的结构对象，
之后通过SQL Expression Language将该对象转换成SQL语句，然后通过 ConnectionPooling 连接数据库，再然后通过 Dialect 执行SQL，并获取结果。
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
 
metadata = MetaData()
user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
 
color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)
metadata.create_all(engine)
# metadata.clear()
# metadata.remove()




#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
)
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)

conn = engine.connect()


\增删改查
# 创建SQL语句，INSERT INTO "user" (id, name) VALUES (:id, :name)
conn.execute(user.insert(),{'id':7,'name':'seven'})
conn.close()

# sql = user.insert().values(id=123, name='wu')
# conn.execute(sql)
# conn.close()

# sql = user.delete().where(user.c.id > 1)

# sql = user.update().values(fullname=user.c.name)
# sql = user.update().where(user.c.name == 'jack').values(name='ed')

# sql = select([user, ])
# sql = select([user.c.id, ])
# sql = select([user.c.name, color.c.name]).where(user.c.id==color.c.id)
# sql = select([user.c.name]).order_by(user.c.name)
# sql = select([user]).group_by(user.c.name)

# result = conn.execute(sql)
# print result.fetchall()
# conn.close()


\更多内容详见：
    http://www.jianshu.com/p/e6bba189fcbd
    http://docs.sqlalchemy.org/en/latest/core/expression_api.html
注：SQLAlchemy无法修改表结构，如果需要可以使用SQLAlchemy开发者开源的另外一个软件Alembic来完成。


\步骤三：
使用 ORM/Schema Type/SQL Expression Language/Engine/ConnectionPooling/Dialect 所有组件对数据进行操作。根据类创建对象，对象转换成SQL，执行SQL。
#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)
Base = declarative_base()
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
 
# 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
# Base.metadata.create_all(engine)
 
Session = sessionmaker(bind=engine)
session = Session()
 
 
# ########## 增 ##########
# u = User(id=2, name='sb')
# session.add(u)
# session.add_all([
#     User(id=3, name='sb'),
#     User(id=4, name='sb')
# ])
# session.commit()
 
# ########## 删除 ##########
# session.query(User).filter(User.id > 2).delete()
# session.commit()
 
# ########## 修改 ##########
# session.query(User).filter(User.id > 2).update({'cluster_id' : 0})
# session.commit()
# ########## 查 ##########
# ret = session.query(User).filter_by(name='sb').first()
 
# ret = session.query(User).filter_by(name='sb').all()
# print ret
 
# ret = session.query(User).filter(User.name.in_(['sb','bb'])).all()
# print ret
 
# ret = session.query(User.name.label('name_label')).all()
# print ret,type(ret)
 
# ret = session.query(User).order_by(User.id).all()
# print ret
 
# ret = session.query(User).order_by(User.id)[1:3]
# print ret
# session.commit()





\pymysql
#  linux下安装方法：
1.tar包下载及解压

下载tar包
wget https://pypi.python.org/packages/29/f8/919a28976bf0557b7819fd6935bfd839118aff913407ca58346e14fa6c86/PyMySQL-0.7.11.tar.gz#md5=167f28514f4c20cbc6b1ddf831ade772
解压并展开tar包
tar xf PyMySQL-0.7.11.tar.gz

2.安装
[root@localhost PyMySQL-0.7.11]# python36 setup.py instal


\数据库的连接
本次测试创建的数据及表：
#创建数据库及表，然后插入数据
mysql> create database dbforpymysql;
mysql> create table userinfo(id int not null auto_increment primary key,username varchar(10),passwd varchar(10))engine=innodb default charset=utf8;
mysql> insert into userinfo(username,passwd) values('frank','123'),('rose','321'),('jeff',666);

#查看表内容
mysql> select * from userinfo;
+----+----------+--------+
| id | username | passwd |
+----+----------+--------+
|  1 | frank    | 123    |
|  2 | rose     | 321    |
|  3 | jeff     | 666    |
+----+----------+--------+
3 rows in set (0.00 sec)

\连接数据库：
import pymysql

#连接数据库
db = pymysql.connect("localhost","root","LBLB1212@@","dbforpymysql")

#使用cursor()方法创建一个游标对象
cursor = db.cursor()

#使用execute()方法执行SQL语句
cursor.execute("SELECT * FROM userinfo")

#使用fetall()获取全部数据
data = cursor.fetchall()

#打印获取到的数据
print(data)

#关闭游标和数据库的连接
cursor.close()
db.close()

#运行结果
((1, 'frank', '123'), (2, 'rose', '321'), (3, 'jeff', '666'))

\要完成一个MySQL数据的连接，在connect中可以接受以下参数：
# 参数
def __init__(self, host=None, user=None, password="",
             database=None, port=0, unix_socket=None,
             charset='', sql_mode=None,
             read_default_file=None, conv=None, use_unicode=None,
             client_flag=0, cursorclass=Cursor, init_command=None,
             connect_timeout=10, ssl=None, read_default_group=None,
             compress=None, named_pipe=None, no_delay=None,
             autocommit=False, db=None, passwd=None, local_infile=False,
             max_allowed_packet=16*1024*1024, defer_connect=False,
             auth_plugin_map={}, read_timeout=None, write_timeout=None,
             bind_address=None):
# 参数解释：
host:           # 主机名或者主机地址
user:           # 用户名
password:       # 密码
database:       # 指定的数据库
port:           # 端口，默认是3306
bind_address:   # 当客户端有多个网络接口的时候，指点连接到数据库的接口，可以是一个主机名或者ip地址
unix_socket:    # 指定字符编码
sql_mode:       # 默认使用SQL_MODE


\数据库操作
# 一、数据库增删改操作
commit()方法：在数据库里增、删、改的时候，必须要进行提交，否则插入的数据不生效。
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES('jack','123')"
cursor.execute(sql)
db.commit()  # 提交数据
cursor.close()
db.close()

#或者在execute提供插入的数据
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"
cursor.execute(sql,("bob","123"))  # 带入数据
# res = cursor.execute(sql,("bob","123"))  # 获取返回结果
db.commit()  #提交数据
cursor.close()
db.close()


\小知识点，mysql的注入问题：
在mysql中使用"--"代表注释，比如现在来实现一个用户登录的小程序：
用户名和密码都存在表userinfo中，表内容如下：
mysql> select * from userinfo;
+----+----------+--------+
| id | username | passwd |
+----+----------+--------+
|  1 | frank    | 123    |
|  2 | rose     | 321    |
|  3 | jeff     | 666    |
+----+----------+--------+
3 rows in set (0.00 sec)

小程序代码如下：
import pymysql
user = input("username:")
pwd = input("password:")
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = "select * from userinfo where username='%s' and passwd='%s'" %(user,pwd)
result=cursor.execute(sql)
cursor.close()
db.close()
if result:
    print('登录成功')
else:
    print('登录失败')
#正确登录的运行结果
username:frank
password:123
result: 1
登录成功

#错误登录的运行结果
username:frank
password:1231231
result: 0
登录失败
看起来没有什么问题，但是试试下面的方式吧
----------------------------------------------
username:' or 1=1 -- 
password:123
result: 3
登录成功
----------------------------------------------
咦~也登录成功了.
为什么呢？可以看一下现在的执行的sql语句：
select * from userinfo where username='' or 1=1 -- ' and passwd='123'
这里--后面的会被注释，所以where一定会成功，这里等于查看了所有行的内容，返回值也不等于0，所以就登录成功了。
解决方法就是将变量或者实参直接写到execute中即可：
result=cursor.execute(sql,(user,pwd))
在键入类似' or 1=1 -- 的时候就不会登录成功了。 


# executemany()：用来同时插入多条数据：
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"
cursor.executemany(sql,[("tom","123"),("alex",'321')])
db.commit()  #提交数据
cursor.close()
db.close()


# execute()和executemany()都会返回受影响的行数：
sql = "delete  from  userinfo where username=%s"
res = cursor.executemany(sql,("jack",))
print("res=",res)
#运行结果
res= 1

# 当表中有自增的主键的时候，可以使用lastrowid来获取最后一次自增的ID：
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"
cursor.execute(sql,("zed","123"))
print("the last rowid is ",cursor.lastrowid)
db.commit()  #提交数据
cursor.close()
db.close()

#运行结果
the last rowid is  10


\二、数据库的查询操作
# 这里主要介绍三个绑定方法：
    fetchone():获取下一行数据，第一次为首行；
    fetchall():获取所有行数据源
    fetchmany(4):获取下4行数据

# 先来查看表的内容：
mysql> select * from userinfo;
+----+----------+--------+
| id | username | passwd |
+----+----------+--------+
|  1 | frank    | 123    |
|  2 | rose     | 321    |
|  3 | jeff     | 666    |
|  5 | bob      | 123    |
|  8 | jack     | 123    |
| 10 | zed      | 123    |
+----+----------+--------+
6 rows in set (0.00 sec)


# 使用fetchone()：
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "SELECT * FROM userinfo"
cursor.execute(sql)
res = cursor.fetchone() #第一次执行
print(res)
res = cursor.fetchone() #第二次执行
print(res)
cursor.close()
db.close()

#运行结果
(1, 'frank', '123')
(2, 'rose', '321')


# 使用fetchall()：
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor()
sql = "SELECT * FROM userinfo"
cursor.execute(sql)
res = cursor.fetchall() #第一次执行
print(res)
res = cursor.fetchall() #第二次执行
print(res)
cursor.close()
db.close()
#运行结果
((1, 'frank', '123'), (2, 'rose', '321'), (3, 'jeff', '666'), (5, 'bob', '123'), (8, 'jack', '123'), (10, 'zed', '123'))
()

可以看到，第二次获取的时候，什么数据都没有获取到，这个类似于文件的读取操作。

\将结果转换为字典类型
默认情况下，我们获取到的返回值是元组，只能看到每行的数据，却不知道每一列代表的是什么，这个时候可以使用以下方式来返回字典，每一行的数据都会生成一个字典：
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 在实例化的时候，将属性cursor设置为pymysql.cursors.DictCursor
使用fetchall获取所有行的数据，每一行都被生成一个字典放在列表里面：
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
sql = "SELECT * FROM userinfo"
cursor.execute(sql)
res = cursor.fetchall()
print(res)
cursor.close()
db.close()
#运行结果
[{'id': 1, 'username': 'frank', 'passwd': '123'}, {'id': 2, 'username': 'rose', 'passwd': '321'}, {'id': 3, 'username': 'jeff', 'passwd': '666'}, {'id': 5, 'username': 'bob', 'passwd': '123'}, {'id': 8, 'username': 'jack', 'passwd': '123'}, {'id': 10, 'username': 'zed', 'passwd': '123'}]

这样获取到的内容就能够容易被理解和使用了！

\移动指针获取数据
在获取行数据的时候，可以理解开始的时候，有一个行指针指着第一行的上方，获取一行，它就向下移动一行，所以当行指针到最后一行的时候，就不能再获取到行的内容，
所以我们可以使用如下方法来移动行指针：
cursor.scroll(1,mode='relative')  # 相对当前位置移动
cursor.scroll(2,mode='absolute')  # 相对绝对位置移动
第一个值为移动的行数，整数为向下移动，负数为向上移动，mode指定了是相对当前位置移动，还是相对于首行移动
# 例如：
sql = "SELECT * FROM userinfo"
cursor.execute(sql)
res = cursor.fetchall()
print(res)
cursor.scroll(0,mode='absolute') #相对首行移动了0，就是把行指针移动到了首行
res = cursor.fetchall()  #第二次获取到的内容
print(res)

#运行结果
[{'id': 1, 'username': 'frank', 'passwd': '123'}, {'id': 2, 'username': 'rose', 'passwd': '321'}, {'id': 3, 'username': 'jeff', 'passwd': '666'}, {'id': 5, 'username': 'bob', 'passwd': '123'}, {'id': 8, 'username': 'jack', 'passwd': '123'}, {'id': 10, 'username': 'zed', 'passwd': '123'}]
[{'id': 1, 'username': 'frank', 'passwd': '123'}, {'id': 2, 'username': 'rose', 'passwd': '321'}, {'id': 3, 'username': 'jeff', 'passwd': '666'}, {'id': 5, 'username': 'bob', 'passwd': '123'}, {'id': 8, 'username': 'jack', 'passwd': '123'}, {'id': 10, 'username': 'zed', 'passwd': '123'}]

\上下文管理器
在python的文件操作中支持上下文管理器，在操作数据库的时候也可以使用：
import pymysql
config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"LBLB1212@@",
    "database":"dbforpymysql"
}
db = pymysql.connect(**config)
with db.cursor(cursor=pymysql.cursors.DictCursor) as cursor:  # 获取数据库连接的对象
    sql = "SELECT * FROM userinfo"   
    cursor.execute(sql)
    res = cursor.fetchone()
    print(res)
    cursor.scroll(2,mode='relative')
    res = cursor.fetchone()
    print(res)
    cursor.close()
db.close()

#运行结果
{'id': 1, 'username': 'frank', 'passwd': '123'}
{'id': 5, 'username': 'bob', 'passwd': '123'}

上下文管理器可以使代码的可读性更强。