\方式一、为对象初始化自己独有的特征
class People:
    country='China'
    x=1
    def run(self):
        print('----->', self)

# 实例化出三个空对象
obj1=People()
obj2=People()
obj3=People()

# 为对象定制自己独有的特征
obj1.name='egon'
obj1.age=18
obj1.sex='male'

obj2.name='lxx'
obj2.age=38
obj2.sex='female'

obj3.name='alex'
obj3.age=38
obj3.sex='female'

# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj3.__dict__)
# print(People.__dict__)


\方式二、为对象初始化自己独有的特征
class People:
    country='China'
    x=1
    def run(self):
        print('----->', self)

# 实例化出三个空对象
obj1=People()
obj2=People()
obj3=People()

# 为对象定制自己独有的特征
def chu_shi_hua(obj, x, y, z): #obj=obj1,x='egon',y=18,z='male'
    obj.name = x
    obj.age = y
    obj.sex = z

chu_shi_hua(obj1,'egon',18,'male')
chu_shi_hua(obj2,'lxx',38,'female')
chu_shi_hua(obj3,'alex',38,'female')


\方式三、为对象初始化自己独有的特征
class People:
    country='China'
    x=1

    def chu_shi_hua(obj, x, y, z): #obj=obj1,x='egon',y=18,z='male'
        obj.name = x
        obj.age = y
        obj.sex = z

    def run(self):
        print('----->', self)


obj1=People()
# print(People.chu_shi_hua)
People.chu_shi_hua(obj1,'egon',18,'male')

obj2=People()
People.chu_shi_hua(obj2,'lxx',38,'female')

obj3=People()
People.chu_shi_hua(obj3,'alex',38,'female')


\方式四、为对象初始化自己独有的特征
class People:
    country='China'
    x=1

    def __init__(obj, x, y, z): #obj=obj1,x='egon',y=18,z='male'
        obj.name = x
        obj.age = y
        obj.sex = z

    def run(self):
        print('----->', self)

obj1=People('egon',18,'male') #People.__init__(obj1,'egon',18,'male')
obj2=People('lxx',38,'female') #People.__init__(obj2,'lxx',38,'female')
obj3=People('alex',38,'female') #People.__init__(obj3,'alex',38,'female')


\__init__方法
# 强调：
#   1、该方法内可以有任意的python代码
#   2、一定不能有返回值
class People:
    country='China'
    x=1

    def __init__(obj, name, age, sex): #obj=obj1,x='egon',y=18,z='male'
        # if type(name) is not str:
        #     raise TypeError('名字必须是字符串类型')
        obj.name = name
        obj.age = age
        obj.sex = sex


    def run(self):
        print('----->', self)


# obj1=People('egon',18,'male')
obj1=People(3537,18,'male')

# print(obj1.run)
# obj1.run() #People.run(obj1)
# print(People.run)

！！！__init__方法之为对象定制自己独有的特征


\！！！补充说明：从代码级别看面向对象 ！！！
#1、在没有学习类这个概念时，数据与功能是分离的
def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx


def exc2(host,port,db,charset,proc_name)
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx

#每次调用都需要重复传入一堆参数
exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
exc2('127.0.0.1',3306,'db1','utf8','存储过程的名字')


#2、我们能想到的解决方法是，把这些变量都定义成全局变量
HOST=‘127.0.0.1’
PORT=3306
DB=‘db1’
CHARSET=‘utf8’

def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx


def exc2(host,port,db,charset,proc_name)
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx

exc1(HOST,PORT,DB,CHARSET,'select * from tb1;')
exc2(HOST,PORT,DB,CHARSET,'存储过程的名字')


#3、但是2的解决方法也是有问题的，按照2的思路，我们将会定义一大堆全局变量，这些全局变量并没有做任何区分，即能够被所有功能使用，然而事实上只有HOST，PORT，DB，CHARSET是
# 给exc1和exc2这两个功能用的。言外之意：我们必须找出一种能够将数据与操作数据的方法组合到一起的解决方法，这就是我们说的类了

class MySQLHandler:
    def __init__(self,host,port,db,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.charset=charset
    def exc1(self,sql):
        conn=connect(self.host,self.port,self.db,self.charset)
        res=conn.execute(sql)
        return res


    def exc2(self,sql):
        conn=connect(self.host,self.port,self.db,self.charset)
        res=conn.call_proc(sql)
        return res


obj=MySQLHandler('127.0.0.1',3306,'db1')
obj.exc1('select * from tb1;')
obj.exc2('存储过程的名字')


#改进
class MySQLHandler:
    def __init__(self,host,port,db,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.charset=charset
        self.conn=connect(self.host,self.port,self.db,self.charset)
    def exc1(self,sql):
        return self.conn.execute(sql)

    def exc2(self,sql):
        return self.conn.call_proc(sql)


obj=MySQLHandler('127.0.0.1',3306,'db1')
obj.exc1('select * from tb1;')
obj.exc2('存储过程的名字')

数据与专门操作该数据的功能组合到一起