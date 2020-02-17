#_*_coding:utf-8_*_
import sys
# sys.path.append(r'/Users/zhuzhiwen/Downloads/py_s19/day7/作业/Elec')

import time
import pickle
import os
from src import identifier
from conf import settings


#基类
class BaseModel:
    #存储用户信息
    def save(self):
        file_path=os.path.join(self.db_path,self.nid)
        pickle.dump(self,open(file_path,'wb'))

    #读取用户信息
    @classmethod
    def get_all_obj_list(cls):
        ret=[]
        for filename in os.listdir(cls.db_path):
            file_path=os.path.join(cls.db_path,filename)
            obj=pickle.load(opne(file_path,'rb'))
            ret.append(obj)
        return ret

#a1=Admin('alex','123')
#a1.db_path
#a1.save()-->a1.db_path
#a2_obj a3_obj a4_obj a5_obj
#Admin.get_all_obj_list() --->[a1_obj,a2_obj,a3_obj]

#管理员 信息
class Admin(BaseModel):
    db_path=settings.ADMIN_DB
    def __init__(self,username,password):
        self.nid=identifier.AdminNid(self.db_path)
        self.username=username
        self.password=password
        self.create_time=time.strftime('%Y-%m-%d')

    @staticmethod
    def login():
        try:
            name=input('请输入用户名： ').strip()
            pas=input('请输入密码： ').strip()
            for obj in Admin.get_all_obj_list():
                if obj.username == name and obj.password == pas:
                    status = True
                    error=''
                    data='\033[45;1m登录成功\033[0m'
                    break
                else:
                    raise Exception('\033[43;1m用户名或密码错误\033[0m' %name)

        except Exception as e:
            status=False
            error=str(e)
            data=''
        return {'status':status,'error':error,'data':data}



#学校
class School(BaseModel):
    db_path=settings.SCHOOL_DB
    def __init__(self,name,sddr):
        self.nid=identifier.SchoolNid(self.db_path)
        self.name=name
        self.addr=addr
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.__income=0

    def __str__(self):
        return self.name


#老师
class Teacher(BaseModel):
    db_path=settings.TEACHER_DB
    def __init__(self,name,level):
        self.nid=identifier.TeacherNid(self.db_path)
        self.name=name
        self.level=level
        self.__account=0
        self.create_time = time.strftime('%Y-%m-%d %X')


#s1=School('老男孩','北京')
#c1=Course('python','14400','4m',s1.nid)
#c1.school_nid.get_obj_by_uuid() --->s1
#课程
class Course(BaseModel):
    db_path=settings.COURSE_DB
    def __init__(self,name,price,period,school_nid):
        self.nid = identifier.CourseNid(self.db_path)
        self.name=name
        self.price=price
        self.period=period
        self.school_nid=school_nid


#alex --> python
#alex --> 语文
#alex --> 体育
#course.get_all_obj_list()
#课程和老师的对应关系
class Coure_to_teacher(BaseModel):
    db_path=settings.COURSE_TO_TEACHER_DB
    def __init__(self,course_nid,teacher_nid):
        self.nid=identifier.Course_to_teacherNid(self.db_path)
        self.course_nid=course_nid
        self.teacher_nid=teacher_nid

    def get_coure_to_teacher_list(self):
        ret=self.get_all_obj_list()
        if ret:
            return [ret.course_nid.get_obj_by_uuid(),ret.classes_nid.get_obj_by_uuid()]
        return [None,None]
        # res=[(obj.course_nid.get_obj_by_uuid(),obj.teacher_nid.get_obj_by_uuid()) \
        #      for obj in ret]
        # return res


#班级
class Classes(BaseModel):
    db_path=settings.CLASSES_DB
    def __init__(self,name,tuition,school_nid,course_to_teacher_list):
        self.nid=identifier.ClassesNid(self.db_path)
        self.name=name
        self.tuition=tuition
        self.school_nid=school_nid
        self.course_to_teacher_list=course_to_teacher_list


#分数(学生使用)
class Score:
    def __init__(self,nid):
        self.nid=nid
        self.score_dict={}

    def set(self,course_to_teacher_nid,number):
        self.score_dict[course_to_teacher_nid]=number

    def get(self,course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)

#学生
class Student(BaseModel):
    db_path=settings.STUDENT_DB
    def __init__(self,name,age,qq,classes_nid):
        self.nid=identifier.StudentNid(self.db_path)
        self.name=name
        self.age=age
        self.qq=qq
        self.classes_nid=classes_nid
        self.score=Score(self.nid)





