# /usr/local/bin/python3
# -*- encoding: utf-8 -*-

'''
# @Time    : 2020/11/5 10:42 上午
# @Author  : zhanghongyang
# @Site    : 
# @Email   : zhy_linux@sina.com
# @File    : test.py.py
# @Software: PyCharm
# @docs    : 
'''


# a =123
# print(id(a))
# a =456
# print(id(a))

# name = '******egon******'
# # print(name[6::-1])
# # print(len(name))
#
# # print(name.rstrip('*'))
# user_info='root:x:0:0::/root:/bin/bash'
# print(user_info.partition(':'))
# tag=' '
# a=tag.join(['egon','say','hello','world'])

#

# name-age = 18

x='Info Egon:18'
# y='Info Egon:18'
# print(id(x))
# print(id(y))
#
# print(type(x))
# print(locals().keys())
# # print('x' in locals().keys())
# print(dir())
# print(vars().keys())
# print(globals().keys())
# n1 = 'aaa'
# n2 = 10
# n3 = '10'
# print(str(n1) + str(n2) + 'bbb')
# print(n1 *  n2)
# print(n1 + n2)

# name = input('plase input your name:>>')
# # print(name)
# print(id(name),type(name),name)
# print('您的用户名为:',name,'您的密码为:',name)
# age = 1.823234
# print(type(age))
# name = """aaaa"""
# print(type(name))
# name='egon'
# msg='hello'
# age=18
# print(name+msg+str(age))
# hobbies='play read music movie'
# print(hobbies)
# print(hobbies.split()[0])
# hobbies=['play','read','music','movie']
# hobbies[0]='11111'
# print(hobbies[0])
# del hobbies[0]
# print(hobbies)

# list1 = [1,2,3]
# list2 = [4,5,6]
# print(list1 + list2)
# print(len([1, 2, 3]))
# print('','name',sep="''",end='')
# set1 = ('1','2')
# print(list(set1))
# list1 = [1,2,3,4,4,5,1,2,3,4]
# print(list1.index(4))
# print(list1.count(4))

# a = [[1,2],[3,4]]
# print(a[:][0])
# print(a[0][:])
# print(a[:-1])
# print(a[0][0])
# l=[1,1.3,'egon',['a','b'],{'name':'zhy'}]
#
# print(l)
# print(l[4]["name"])
# list=[]
# for i in range(1,101):
#     list.append(i)
#
# # print(list)
# templist = []
# newlist  = []
#
# while True:
#     num = 0
#     for i in list:
#         templist.append(i)
#         num+=1
#         if num == 3:
#             newlist.append(templist)
#             templist = []
#             num =0
#             continue
#     if i == 100:
#         newlist.append(templist)
#         break
# print(newlist)

# list = []
#
# for number in range(1,101):
#     list.append(number)
#
# templist = []
# newlist  = []
#
# while True:
#     num = 0
#     for temp in list:
#         templist.append(temp)
#         num+=1
#         if num == 3:
#             newlist.append(templist)
#             templist = []
#             num = 0
#             continue
#     if temp == 100:
#         newlist.append(templist)
#         break
#

# print(newlist)

# print('天风请加审批')
# egg_list = ['我是egg%s' %i for i in range(10)]
# reason = input('plase input your reason >>:')
# print('同意请加' if reason in egg_list else '罚款20元')

# class A:
#     country = 'China'
#
#     def func(self):
#         self.name= 'alex'
#
#     def c_method(self):
#         print('in class method')
#
#     def s_method(self):
#         print('in static method')

# class A(object):
#     bar = 1
#
#     def func1(self):
#         print('foo')
#
#     @classmethod
#     def func2(cls):
#         print('func2')
#         print(cls.bar)
#         cls().func1()  # 调用 foo 方法


# A.func2()


# a = 123
# print(type(a))

# class A:
#     country = 'China'
#     def func1(self):
#         self.name = 'alex'
#
#     def func2(self):
#         print('funrc 2')
#
#     def func3():
#         print('in func3')
#
#     @classmethod       # 类方法：就是不需要传具体的对象self，但是可以使用类的属性、静态属性、方法。可以使用一些公共变量，但不能使用对象的变量，因为没有给c_method传self。
#     def c_method(cls): # cls固定传，就是自己这个类 A。被装饰的对象不需要实例化，直接使用 类名.方法名()  就可以调用。
#         print('in class method')
#         print(cls.country)
#         cls().func2()
#
#     @staticmethod      # 静态方法，不可以使用类里的其他变量。
#     def s_method():
#         print('in static method')
#         # print(country) # 加了@staticmethod 装饰器后就无法调用类里面的 属性和方法了,加cls也不行。
#
#
#
# aaa = A()
# aaa.s_method()

# import  random
# print(random.randrange(1,13))
# DNS_REGION = 'sanddpace.com'
#
# data = "($http_origin ~* 'https?://(localhost|.*\.mdprd\.cn)/?')"
#
# data = data.replace('mdprd\.cn','%s\.%s') %(DNS_REGION.split('.')[0],DNS_REGION.split('.')[1])
# print(data)
# import os
# DNS_HEAD = 'qas-test'
# DNS_REGION = 'mxjcloud.com'
#
# def nginx_data_edit():
#     old_list = ['test.txt']
#     new_conf = '.nginx_conf_template'
#     for old_conf in old_list:
#         with open(old_conf, 'r', encoding='utf-8') as read_f, open(new_conf, 'w', encoding='utf-8') as write_f:
#             data = read_f.read()
#             data = data.replace('devs-test', DNS_HEAD)
#             data = data.replace('mdprd.cn', DNS_REGION)
#             #data = data.replace('mdprd\.cn','%s\.%s') %(DNS_REGION.split('.')[0],DNS_REGION.split('.')[1])
#             data = data.replace('mdprd\.cn', ('%s\.%s' % (DNS_REGION.split('.')[0], DNS_REGION.split('.')[1])))
#             write_f.write(data)
#         os.remove(old_conf)
#         os.rename(new_conf, old_conf)
#
# nginx_data_edit()
#
# import  requests
# wx_access_token = "37_dpGO04_oO0UpiytqQI-zodO05uU2qA1tPGd4jnpNg-6oO54kZtvZ-ZjnQcB0v_XhweyvgDtGAqCYmiOSkQ9xVoxT9-1H0aJvkququ-dUdRHDxB-Kh-j0UFV64X8zUm2RVQK4_kKSo4ecv2duIFMeABAYVC"
# scene_list = ['sub_meetingroom', 'sub_member', 'sub_activity']
# config_dict = "37_dpGO04_oO0UpiytqQI-zodO05uU2qA1tPGd4jnpNg-6oO54kZtvZ-ZjnQcB0v_XhweyvgDtGAqCYmiOSkQ9xVoxT9-1H0aJvkququ-dUdRHDxB-Kh-j0UFV64X8zUm2RVQK4_kKSo4ecv2duIFMeABAYVC"
# # 准备qrcode
# def prepare_qrcode_ticket(wx_access_token, scene_list, config_dict):
#     url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % (wx_access_token)
#     for i in range(0, len(scene_list)):
#         scene_str = scene_list[i].strip()
#         if len(scene_str) == 0:
#             continue
#         request_body = '''{"action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": "%s"}}}''' % (scene_str)
#         response = requests.post(url, data=request_body,headers={'Method': 'POST', "Content-Type": "application/json"})
#         print("我来了")
#         # response = urllib2.urlopen(request)
#         print(response.text,type(response.text)) #<class 'str'>  {"ticket":"gQHz8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAydndlZjAwWmlmeDIxMDAwMGcwN2wAAgSl_iNeAwQAAAAA","url":"http:\/\/weixin.qq.com\/q\/02vwef00Zifx210000g07l"}
#         print(response.status_code)
#         if response.status_code == 200:
#             response_data = response.json()
#             print("我是response_data",response_data,type(response_data))
#             if  len(response_data['ticket'])  and len(response_data["url"]) >0:
#             # if not response_data.has_key("errcode") and len(response_data["url"]) > 0:
#                 config_dict[scene_str] = response_data["ticket"].__str__()
#             else:
#                 print("Failed to generate qrcode url for %s: %s %d" %(scene_str, response_data["errmsg"], response_data["errcode"]))
#         else:
#             print("Failed to generate qrcode url for %s" %(scene_str))
#     print("获取到的微信ticket是：", config_dict)
#     return config_dict
#
# prepare_qrcode_ticket(wx_access_token,scene_list,config_dict)

#! /usr/bin/env python3
#-*- coding:utf-8 -*-

abc = '''
backend.smartdevice,
internal-qrcode,
iot,
internal-backendsmartdevice,
backendcnb,
backendseat,
cloudprinter,
crm-for-dream,
devicedata,
fan-coil-web,
frontdashboard,
frontseat,
backendsmartdevice,
iotregister,
main-event-handle,
mdp-qrcode-event,
mdp-query-front,
mdp-report-archive,
meeting-screen-web,
meetingservice,
mgw,
m,
ops,
printer,
qrcodefront,
qrcode,
qrcodepublic,
qrcode-read,
quota,
ra,
record-screen,
report,
rsync,
rsyncworkwx,
sms,
test-platform-backend,
test-platform,
thirdparty,
uidevice,
web-meeting,
webrtc,
websocket,
worksheet,
www,
wxhub,
zoom-meeting-service,
cloudprinterweb,
eventbackend,
fu,
hrdatasyncserver,
iotscene,
meeting,
order,
qna,
qrcodesaas,
questionnaire,
quota,
report,
so,
sso,
wxhub,
smart-visitor,
visitor-door-control,
balance,
ldapsyncvpn,
xxl-job,
xxl-so,
'''

# print(abc.replace('\n',''))


# print(aaa)


# a =123
# print(id(a))
# a =456
# print(id(a))

# name = '******egon******'
# # print(name[6::-1])
# # print(len(name))
#
# # print(name.rstrip('*'))
# user_info='root:x:0:0::/root:/bin/bash'
# print(user_info.partition(':'))
# tag=' '
# a=tag.join(['egon','say','hello','world'])

#

# name-age = 18

# x = 'Info Egon:18'
# y='Info Egon:18'
# print(id(x))
# print(id(y))
#
# print(type(x))
# print(locals().keys())
# # print('x' in locals().keys())
# print(dir())
# print(vars().keys())
# print(globals().keys())
# n1 = 'aaa'
# n2 = 10
# n3 = '10'
# print(str(n1) + str(n2) + 'bbb')
# print(n1 *  n2)
# print(n1 + n2)

# name = input('plase input your name:>>')
# # print(name)
# print(id(name),type(name),name)
# print('您的用户名为:',name,'您的密码为:',name)
# age = 1.823234
# print(type(age))
# name = """aaaa"""
# print(type(name))
# name='egon'
# msg='hello'
# age=18
# print(name+msg+str(age))
# hobbies='play read music movie'
# print(hobbies)
# print(hobbies.split()[0])
# hobbies=['play','read','music','movie']
# hobbies[0]='11111'
# print(hobbies[0])
# del hobbies[0]
# print(hobbies)

# list1 = [1,2,3]
# list2 = [4,5,6]
# print(list1 + list2)
# print(len([1, 2, 3]))
# print('','name',sep="''",end='')
# set1 = ('1','2')
# print(list(set1))
# list1 = [1,2,3,4,4,5,1,2,3,4]
# print(list1.index(4))
# print(list1.count(4))

# a = [[1,2],[3,4]]
# print(a[:][0])
# print(a[0][:])
# print(a[:-1])
# print(a[0][0])
# l=[1,1.3,'egon',['a','b'],{'name':'zhy'}]
#
# print(l)
# print(l[4]["name"])
# list=[]
# for i in range(1,101):
#     list.append(i)
#
# # print(list)
# templist = []
# newlist  = []
#
# while True:
#     num = 0
#     for i in list:
#         templist.append(i)
#         num+=1
#         if num == 3:
#             newlist.append(templist)
#             templist = []
#             num =0
#             continue
#     if i == 100:
#         newlist.append(templist)
#         break
# print(newlist)

# list = []
#
# for number in range(1,101):
#     list.append(number)
#
# templist = []
# newlist  = []
#
# while True:
#     num = 0
#     for temp in list:
#         templist.append(temp)
#         num+=1
#         if num == 3:
#             newlist.append(templist)
#             templist = []
#             num = 0
#             continue
#     if temp == 100:
#         newlist.append(templist)
#         break
#

# print(newlist)

# print('天风请加审批')
# egg_list = ['我是egg%s' %i for i in range(10)]
# reason = input('plase input your reason >>:')
# print('同意请加' if reason in egg_list else '罚款20元')

# class A:
#     country = 'China'
#
#     def func(self):
#         self.name= 'alex'
#
#     def c_method(self):
#         print('in class method')
#
#     def s_method(self):
#         print('in static method')

# class A(object):
#     bar = 1
#
#     def func1(self):
#         print('foo')
#
#     @classmethod
#     def func2(cls):
#         print('func2')
#         print(cls.bar)
#         cls().func1()  # 调用 foo 方法


# A.func2()


# a = 123
# print(type(a))

# class A:
#     country = 'China'
#     def func1(self):
#         self.name = 'alex'
#
#     def func2(self):
#         print('funrc 2')
#
#     def func3():
#         print('in func3')
#
#     @classmethod       # 类方法：就是不需要传具体的对象self，但是可以使用类的属性、静态属性、方法。可以使用一些公共变量，但不能使用对象的变量，因为没有给c_method传self。
#     def c_method(cls): # cls固定传，就是自己这个类 A。被装饰的对象不需要实例化，直接使用 类名.方法名()  就可以调用。
#         print('in class method')
#         print(cls.country)
#         cls().func2()
#
#     @staticmethod      # 静态方法，不可以使用类里的其他变量。
#     def s_method():
#         print('in static method')
#         # print(country) # 加了@staticmethod 装饰器后就无法调用类里面的 属性和方法了,加cls也不行。
#
#
#
# aaa = A()
# aaa.s_method()

# import  random
# print(random.randrange(1,13))
# DNS_REGION = 'sanddpace.com'
#
# data = "($http_origin ~* 'https?://(localhost|.*\.mdprd\.cn)/?')"
#
# data = data.replace('mdprd\.cn','%s\.%s') %(DNS_REGION.split('.')[0],DNS_REGION.split('.')[1])
# print(data)
# import os
# DNS_HEAD = 'qas-test'
# DNS_REGION = 'mxjcloud.com'
#
# def nginx_data_edit():
#     old_list = ['test.txt']
#     new_conf = '.nginx_conf_template'
#     for old_conf in old_list:
#         with open(old_conf, 'r', encoding='utf-8') as read_f, open(new_conf, 'w', encoding='utf-8') as write_f:
#             data = read_f.read()
#             data = data.replace('devs-test', DNS_HEAD)
#             data = data.replace('mdprd.cn', DNS_REGION)
#             #data = data.replace('mdprd\.cn','%s\.%s') %(DNS_REGION.split('.')[0],DNS_REGION.split('.')[1])
#             data = data.replace('mdprd\.cn', ('%s\.%s' % (DNS_REGION.split('.')[0], DNS_REGION.split('.')[1])))
#             write_f.write(data)
#         os.remove(old_conf)
#         os.rename(new_conf, old_conf)
#
# nginx_data_edit()
#
# import  requests
# wx_access_token = "37_dpGO04_oO0UpiytqQI-zodO05uU2qA1tPGd4jnpNg-6oO54kZtvZ-ZjnQcB0v_XhweyvgDtGAqCYmiOSkQ9xVoxT9-1H0aJvkququ-dUdRHDxB-Kh-j0UFV64X8zUm2RVQK4_kKSo4ecv2duIFMeABAYVC"
# scene_list = ['sub_meetingroom', 'sub_member', 'sub_activity']
# config_dict = "37_dpGO04_oO0UpiytqQI-zodO05uU2qA1tPGd4jnpNg-6oO54kZtvZ-ZjnQcB0v_XhweyvgDtGAqCYmiOSkQ9xVoxT9-1H0aJvkququ-dUdRHDxB-Kh-j0UFV64X8zUm2RVQK4_kKSo4ecv2duIFMeABAYVC"
# # 准备qrcode
# def prepare_qrcode_ticket(wx_access_token, scene_list, config_dict):
#     url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % (wx_access_token)
#     for i in range(0, len(scene_list)):
#         scene_str = scene_list[i].strip()
#         if len(scene_str) == 0:
#             continue
#         request_body = '''{"action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": "%s"}}}''' % (scene_str)
#         response = requests.post(url, data=request_body,headers={'Method': 'POST', "Content-Type": "application/json"})
#         print("我来了")
#         # response = urllib2.urlopen(request)
#         print(response.text,type(response.text)) #<class 'str'>  {"ticket":"gQHz8DwAAAAAAAAAAS5odHRwOi8vd2VpeGluLnFxLmNvbS9xLzAydndlZjAwWmlmeDIxMDAwMGcwN2wAAgSl_iNeAwQAAAAA","url":"http:\/\/weixin.qq.com\/q\/02vwef00Zifx210000g07l"}
#         print(response.status_code)
#         if response.status_code == 200:
#             response_data = response.json()
#             print("我是response_data",response_data,type(response_data))
#             if  len(response_data['ticket'])  and len(response_data["url"]) >0:
#             # if not response_data.has_key("errcode") and len(response_data["url"]) > 0:
#                 config_dict[scene_str] = response_data["ticket"].__str__()
#             else:
#                 print("Failed to generate qrcode url for %s: %s %d" %(scene_str, response_data["errmsg"], response_data["errcode"]))
#         else:
#             print("Failed to generate qrcode url for %s" %(scene_str))
#     print("获取到的微信ticket是：", config_dict)
#     return config_dict
#
# prepare_qrcode_ticket(wx_access_token,scene_list,config_dict)

# ! /usr/bin/env python3
# -*- coding:utf-8 -*-

abc = '''
backend.smartdevice,
internal-qrcode,
iot,
internal-backendsmartdevice,
backendcnb,
backendseat,
cloudprinter,
crm-for-dream,
devicedata,
fan-coil-web,
frontdashboard,
frontseat,
backendsmartdevice,
iotregister,
main-event-handle,
mdp-qrcode-event,
mdp-query-front,
mdp-report-archive,
meeting-screen-web,
meetingservice,
mgw,
m,
ops,
printer,
qrcodefront,
qrcode,
qrcodepublic,
qrcode-read,
quota,
ra,
record-screen,
report,
rsync,
rsyncworkwx,
sms,
test-platform-backend,
test-platform,
thirdparty,
uidevice,
web-meeting,
webrtc,
websocket,
worksheet,
www,
wxhub,
zoom-meeting-service,
cloudprinterweb,
eventbackend,
fu,
hrdatasyncserver,
iotscene,
meeting,
order,
qna,
qrcodesaas,
questionnaire,
quota,
report,
so,
sso,
wxhub,
smart-visitor,
visitor-door-control,
balance,
ldapsyncvpn,
xxl-job,
xxl-so,
'''

# print(abc.replace('\n',''))


# aaa = '''aaaa/aaa:aa.aa
# bbbb
# cccc
# dddd
# '''
#
# # print(aaa)
#
# # l1 = []
# #
# # bbb = aaa.splitlines()
# # print(bbb)
# import os
#
# res=os.popen("cat /tmp/test").read()
# res=res.split()
# print(res)

