
# python基础之文件处理
# http://www.cnblogs.com/linhaifeng/articles/5984922.html

# 文件处理


# 读

# f=open('a.txt','r',encoding='utf-8')  #打开文件
# res=f.read()   #read 以光标读取文件所有内容
# print(res)
# print('第二次',f.read()) # 第一次read光标已经读到文件末尾，所以光标无法继续读取

# print(f.readline(),end='') #一行一行的读取文件
# print(f.readlines(),end='') #把文件所有行读取出来 组成列表
#,end='' 取消读取文件末尾的换行符

# f.close() #打开文件操作后，如果不关闭 ，会一直占用资源，一定要关闭文件
          #close掉的是操作系统的资源 f 变量依然存在，但是不能发起读写操作了

# del f #回收应用程序 中的 f ， 并没有关闭操作系统的打开文件

#打开 操作 单个或者多个文件，操作完后 自动 close 文件
# with open('a.txt','r',encoding='utf-8') as f,open('b.txt') as f1:
#     pass

# r 文本模式的读，在文件不存在，不会创建新文件
# f=open('a.txt','r',encoding='utf-8')  #应用程序指定一个f 变量(对象), 操作系统打开一个文件
# f.read() #应用程序发起读取文件指令，操作系统来操作去硬盘读取内容然后返回给 f
# print(f.read())
# f.readline() #读取一行
# f.readlines() #把所有行取出来，放入列表
# print(f.readable()) #判断文件是否 可读
# print(f.writable()) #判断问价是否 可写
# f.close()


# 写

# f=open('a.txt','w',encoding='utf-8') # w 写  如果文件不存在就创建文件，如果存在就清空文件
# f.write('1111\n')   #每次写都是先清空在 重新写
# f.write('2222\n')   #每次写都是先清空在 重新写
# f.write('3333\n4444\n')  #每次写都是先清空在 重新写
# f.writelines(['a\n','b\n','c\n'])
# f.write()
# f.close()

# w 文本模式的写,文件存在则清空，不存在则创建
# f=open('a.txt','w',encoding='utf-8')
# print(f.readable()) #判断文件是否 可读
# print(f.writable()) #判断问价是否 可写
# f.write('哈哈哈哈\n') #一行 添加
# f.write('哈哈哈哈\n')
#
# f.writelines(['1111\n','2222\n']) #列表添加
# f.close()


# 追加

# a 文本模式的追加,文件存在光标跳到文件末尾，文件不存在创建，
# f=open('b.txt','a',encoding='utf-8')
# # print(f.writable()) #判断问价是否 可写
# # print(f.tell()) #查看文件光标的位置
# f.write('333\n')
# f.write('4444\n')
# f.close()


# r+,w+,a+  不常用的模式


# rb

# rb 模式即直接从硬盘中读取bytes ，不用指定编码
# f=open('a.txt','rb')
# # print(f.read())
# print(f.read().decode('utf-8'))
# f.close()


# wb

# wb 模式，一定不用指定编码
# f=open('a.txt','wb')
# f.write('你好啊'.encode('utf-8'))
# f.close()


# ab 模式，每次写都要 encode


#回收、关闭文件

# f.close() #打开文件操作后，如果不关闭 ，会一直占用资源，一定要关闭文件
          #close掉的是操作系统的资源 f 变量依然存在，但是不能发起读写操作了

# del f #回收应用程序 中的 f ， 并没有关闭操作系统打开的文件
# f.close() #关闭操作系统打开的文件
# close之后 f 依然存在
# close之后 f.read 是无法操作的，因为read是往操作系统发请求，而系统已经关闭这个文件


#打开 操作 单个或者多个文件，操作完后 自动 close 文件

# with open('a.txt','r',encoding='utf-8') as f,open('b.txt') as f1:
#     pass

# with open('file.txt','w',encoding='utf-8') as f:
#     f.write('111\n')

#文本格式以外的文件
# f=open('test.jpg','rb')
# print(f.read())
#
# with open('test.jpg','rb') as read_f,open('test1.jpg','wb') as write_f:
#     # write_f.write(read_f.read())
#     for line in read_f:
#         write_f.write(line)




# 修改文件

# Vim 原理 修改文件   vim就是一次全部读取文件
# import os
# with open('old.txt','r',encoding='utf-8') as read_f,\
#     open('.old.txt.swap','w',encoding='utf-8') as write_f:
#     msg=read_f.read()
#     # print(msg,type(msg))
#     msg=msg.replace('alex','SB')
#     # print(msg)
#     write_f.write(msg)
# os.remove('old.txt')
# os.rename('.old.txt.swap','old.txt')
# 如果文件过大 推荐一行一行的读取

# 换成读取文件时  一行一行读取文件 再修改
# import os
# with open('old.txt','r',encoding='utf-8') as read_f,\
#     open('.old.txt.swap','w',encoding='utf-8') as write_f:
#     for line in read_f:
#         if 'SB' in line:
#             line=line.replace('SB','alex')
#         write_f.write(line)
# os.remove('old.txt')
# os.rename('.old.txt.swap','old.txt')


# 文件读取 写入列表 转成字典
# l={}
# f = open('a.txt','r',encoding='utf-8')
# u = f.readlines()
# print(u,type(u))
# for i in u:
#     i = i.strip()
#     print(i)
#     # print(i.split(' ')[0])
#     # print(i.split(' ')[1])
#     l[i.split(' ')[0]]={'金额':i.split(' ')[1]}
# print(l)
# print(l['www']['金额'])



# 脚本传参实现拷贝文件

# import sys
#
# #python3 copy.py source.file target.file
# if len(sys.argv) < 3:
#     print('usage:python3 copy.py source.file target.file')
#     sys.exit()
#
# #r'D:\python编码\py_s19\day3\old.txt' windows路径问题加r r是原生字符串
# with open(r'%s' %sys.argv[1],'rb') as read_f,\
#         open(r'%s' %sys.argv[2],'wb') as write_f:
#
#     for line in read_f:
#         write_f.write(line)





# 文件其他操作

# f=open('a.txt','r',encoding='utf-8')
# print(f.read(3)) #  读3个字符

# f=open('a.txt','rb')
# print(f.read(3)) #  读3个字节
# print(f.read(3).decode('utf-8')) # 解码读 unicode 3个字节存的中文

# f=open('a.txt','r',encoding='utf-8')
# print(f.read())
# # f.seek(0)  # 定义光标位置 重置到0
# f.seek(3)
# print(f.tell())  #以字节显示光标位置
# print(f.read())

# seek有三种移动方式0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的

# 0
# f=open('a.txt','rb')
# print(f.read(3))
# print(f.tell())
# f.seek(3,0)
# print(f.tell())
# print(f.read(3).decode('utf-8'))

# 1
# f=open('a.txt','rb')
# print(f.read(3))
# print(f.tell())
# f.seek(3,1)
# print(f.tell())
# print(f.read().decode('utf-8'))

# 2
# f=open('a.txt','rb')
# f.seek(0,2) #光标移动至末尾
# print(f.tell())


# python3 tail.py -f access.log
# import time
# import sys
#
# with open(r'%s' %sys.argv[2],'rb') as f:
#     f.seek(0,2)
#
#     while True:
#         line=f.readline()
#         if line:
#             print(line.decode('utf-8'),end='')
#         else:
#             time.sleep(0.2)

#模拟文件追加
# with open('access.log','a') as f:
#     f.write('1111\n')


# truncate是截断文件，所以文件的打开方式必须可写，但是不能用w或w+等方式打开，因为那样直接清空文件了，所以truncate要在r+或a或a+等模式下测试效果
# with open('a.txt','r+',encoding='utf-8') as f:
#     f.truncate(9) #以字节 截取  截取从0到9以内

# 直接循环  一行一行读  内存里面只会存一行
# with open('a.txt','r',encoding='utf-8') as f:
#     # l=f.readlines()
#     # print(l)
#     # for line in l:
#     #     print(line,end='')
#     for line in f:
#         print(line)

# l=[1,2,3,4,5]
# for index in range(len(l)):
#     # print(index)
#     print(l[index])


# for itme in l:
#     # print(index)
#     print(itme)


l=[1,2,3,'a','b']

print(l[7],'123')
