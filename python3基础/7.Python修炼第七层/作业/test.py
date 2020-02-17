
#随机身份证ID
# import uuid
# import hashlib
# import time
#
# def create_uuid():
#     return str(uuid.uuid1())
#
# def create_md5():
#     m=hashlib.md5()
#     m.update(bytes(str(time.time()),encoding='utf-8'))
#     return m.hexdigest()
#
#
# if __name__ == '__main__':
#     print(create_uuid())
#     print(create_uuid())
#     print(create_uuid())
#     print(create_uuid())
#
#     print(create_md5())
#     print(create_md5())
#     print(create_md5())
#     print(create_md5())


School
身份证
#/home/db/shool/
s1---->/home/db/shool/file
s2---->/home/db/shool/file
s3---->/home/db/shool/file



Teacher
身份证
#/home/db/reacher/
t1---->/home/db/reacher/file
t2---->/home/db/reacher/file
t3---->/home/db/reacher/file


员公工牌
部门
工号
姓名
性别

class 部门类:
    def __init__(self,部门,工号,姓名):
        self.部门=部门
        self.工号=工号
        self.姓名=姓名

class 员工类:
    pass

李杰=员工类(it部门,工号,姓名,性别)

it部门=部门类(id,it部门)



class SchoolNid:
    def __init__(self):
        self.uuid=create_uuid()

    def get_obj_by_uuid(self):
        return pickle.load(open('/home/db/school/c1.学校','rb'))


class CourselNid:
    def __init__(self):
        self.uuid=create_uuid()

    def get_obj_by_uuid(self):
        return pickle.load(open('/home/db/school/c1.学校','rb'))


class School:
    def __init__(self,name,addr):
        self.nid=SchoolNid()
        self.name=name
        self.addr=addr


class Course:
    def __init__(self,name,学校nid):
        self.nid=CourselNid()
        self.name=name
        self.学校=学校nid

# class Student:
#     def __init__(self,name,学校nid):
#         self.nid=SchoolNid()
#         self.name=name
#         self.学校=学校nid

s1=School(老男孩,北京)
s1.save() #----->s1.nid=12345
# s1---->/home/db/school/12345

c1=Course(python,12345)
c1.save()
# c1-->12345-->s1

s1=pickle.load(open('/home/db/school/c1.学校','rb'))

s1=c1.学校.get_obj_by_uuid()

# stu1=Student('alex',12345)
#
# stu1=--->12345--->s1
# s1=pickle.load(open('/home/db/school/c1.学校','rb'))


ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"











