
import pickle
import uuid   #生成随机身份证号 str(uuid.uuid1())



#基类
class BashModel:

    # 数据存储，把对象用pickle序列化保存到文件
    def save(self):
        pickle.dump(self, open('/home/db/%s' %self.身份证, 'wb'))

    # 查询数据，pickle读物文件
    @classmethod  # @classmethod 定义一个类方法 @staticmethod 定义一个静态方法
    def get_all_obj_list(cls):
        ret = []
        for file_name in 循环/home/db/文件名:
            obj = pickle.load(open(/home/db/file_name, 'rb'))
            ret, append(obj)
        return ret


#学校
class School(BashModel):

    #初始化函数
    def __init__(self,name,addr):
        self.身份证 = 身份证号
        self.name = name
        self.addr = addr

    #打印对象名，直接调用此方法
    def __str__(self):
        return self.name



s1=School('老男孩','北京')
s1.save()  #pickle.dump(s1,open(/home/db/老男孩,'wb'))
#/home/db/老男孩

s2=School('北大青鸟','北京')
s2.save() #pickle.dump(s1,open(/home/db/北大青鸟,'wb'))
#/home/db/北大青鸟


s3=School('老男孩','上海')
s3.save() #pickle.dump(s1,open(/home/db/老男孩,'wb'))

School.get_all_obj_list() #定义了类方法后，直接通过类名调用，不需要再借助具体对象调用
#打印所有的学校信息
for school_obj in School.get_all_obj_list():
    print('学校名字 %s ' %shcool_obj.name)


#教师
class Teacher(BashModel):
    pass

#课程
class Course(BashModel):
    pass

#班级
class Classes(BashModel):
    pass

#学生
class Student(BashModel):
    pass



