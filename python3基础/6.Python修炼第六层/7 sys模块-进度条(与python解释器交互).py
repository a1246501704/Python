import sys  # sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python运行时的环境。

sys.argv             # 接收命令行参数，生成一个List，第一个元素是程序本身路径。检测脚本后面传入的参数，实现从程序外部向程序传递参数。
sys.exc_info()       # 获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
sys.exit(n)          # 退出程序，退出程序引发SystemExit异常，可以捕获异常执行些清理工作。n值默认为0，表示正常退出，其他都是非正常退出。
sys.hexversion       # 获取Python解释程序的版本值，16进制格式如：0x020403F0
sys.version          # 获取Python解释程序的版本信息
sys.version_info     # 获取Python解释程序的版本信息
sys.maxint           # 最大的Int值
sys.maxunicode       # 最大的Unicode值
sys.modules          # 返回系统导入的模块字段，key是模块名，value是模块
sys.modules.keys()   # 返回所有已经导入的模块列表
sys.path             # sys.path 返回的是一个列表！获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。sys.path.append()
sys.platform         # 返回操作系统平台名称
sys.stdout           # 标准输出。sys.stdout.write('please:')
sys.stdin            # 标准输入。sys.stdin.readline()[:-1]
sys.stderr           # 错误输出
sys.exc_clear()      # 用来清除当前线程所出现的当前的或最近的错误信息
sys.exec_prefix      # 返回平台独立的python文件安装的位置
sys.byteorder        # 本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
sys.copyright        # 记录python版权相关的东西
sys.api_version      # 解释器的C的API版本
sys.getrecursionlimit()     # 获取最大递归深度
sys.setrecursionlimit(1500) # 修改递归最大深度
sys.getdefaultencoding()    # 获取解释器默认编码
sys.getfilesystemencoding() # 获取内存数据存在文件的默认编码
# 其他方法: https://blog.csdn.net/swinfans/article/details/85780302

\sys.argv
cat /opt/python.py  # 给python程序传递参数
#!/usr/local/bin/python
# -*- coding:utf-8 -*-

import sys

print(sys.argv[0])          #sys.argv[0] 类似于shell中的$0,但不是脚本名称，而是脚本的路径   
print(sys.argv[1])          #sys.argv[1] 表示传入的第一个参数，既 hello

#运行结果：
[root@Test ~]               # python /opt/python.py hello
/opt/python.py              #打印argv[0]  脚本路径
hello                       #打印argv[1]  传入的参数 hello


import sys
# filename：argv_test.py
for i in range(len(sys.argv)):
      print('argv{0}: type is {1}, value is {2}'.format(i, type(sys.argv[i]), sys.argv[i]))

python argv_test.py 1 a 2 b 3 c
'''
argv0: type is <class 'str'>, value is argv_test.py
argv1: type is <class 'str'>, value is 1
argv2: type is <class 'str'>, value is a
argv3: type is <class 'str'>, value is 2
argv4: type is <class 'str'>, value is b
argv5: type is <class 'str'>, value is 3
argv6: type is <class 'str'>, value is c
'''

\sys.exit(n)
功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）
示例：exit.py
#!/usr/bin/env python

import sys

def exitfunc(value):
    print value
    sys.exit(0)

print "hello"

try:
    sys.exit(1)
except SystemExit,value:
    exitfunc(value)

print "come?"

运行：
# python exit.py
hello
1

\sys.path
功能：获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。
示例：
>>> import sys
>>> sys.path
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages/PILcompat', '/usr/lib/python2.7/dist-packages/gtk-2.0', '/usr/lib/python2.7/dist-packages/ubuntu-sso-client']
sys.path.append("自定义模块路径")

print(sys.path[0]) # 表示当前脚本所在目录

# 初始化环境变量: 一个项目内部的多个目录结构不通的.py文件之间import时很适用
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

\sys.stdin/sys.stdout/sys.stderr
print('Hi, %s!' %input('Please enter your name: '))
# 等同于:
print('Please enter your name:')
name=sys.stdin.readline()[:-1]
print('Hi, %s!' %name)

# 标准输出
print('Hello World!\n')
# 等同于:
sys.stdout.write('output resule is good!\n')

for i in (sys.stdin, sys.stdout, sys.stderr):
    print(i)
'''
Please enter your name: zhanghongyang
Hi, zhanghongyang!
Please enter your name: 
zhanghongyang
Hi, zhanghongyang!
Hello World!

output resule is good!
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
<_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>
'''

\打印进度条
#=========知识储备==========
#有没有进度条的感觉？
[#             ]
[##            ]
[###           ]
[####          ]

#指定宽度
print('[%-15s]' %'#')
print('[%-15s]' %'##')
print('[%-15s]' %'###')
print('[%-15s]' %'####')

#打印%
print('%s%%' %(100)) #两个%号代表取消了后面%的特殊意义，后面的%就是一个普通的%

#传参来控制宽度
print('[%%-%ds]' %50) #[%-50s]
print(('[%%-%ds]' %50) %'#') # 先给d传50，括号外面再给s传#号 
print(('[%%-%ds]' %50) %'##')
print(('[%%-%ds]' %50) %'###')

#======实现打印进度条函数======
import sys
import time

def progress(percent,width=50): # 进度条应该按照下载进度或者安装进度打印
    if percent >= 1: # 每次加1024会导致percent的值比1大
        percent=1
    show_str=('[%%-%ds]' %width) %(int(width*percent)*'#') # width*percent*#  警号的个数应该是宽度*百分比*#  ，int取整数
    print('\r%s %s%%' %(show_str,int(percent*100)),end='',file=sys.stdout,flush=True)
    \r代表每次跳到行首  file=sys.stdout打印到终端  flush=True每次立马打印不要有延迟  end=''不要有换行  int(percent*100)将小数转成整数
 
#===========应用=============
data_size=1025
recv_size=0
while recv_size < data_size:
    time.sleep(0.1) # 模拟数据的传输延迟
    recv_size+=1024 # 每次收1024
    percent=recv_size/data_size # 接收的比例，是个小数。为了防止data_size是1025大小而造成percent的值所以上面加了个if判断。
    progress(percent,width=70)  # 进度条的宽度70




\自制一个python下载文件的进度条模块
import  requests
import time

def downloader(url,path):
    start_time = time.time() # 开始时间
    size = 0
    response = requests.get(url,stream=True) # stream属性不许带上
    chunk_size = 1024 # 每次下载的数据大小
    content_size = int(response.headers['content-length']) # 数据总大小
    if response.status_code == 200:
        print('[文件大小]%0.2f MB' %(content_size / chunk_size / 1024)) # 换算单位并打印
        with open(path,'wb') as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size +=len(data) # 已下载数据大小
                # \r指定行第一个字符开始，搭配end属性完成覆盖进度条
                print('\r'+'[下载进度]:%s%.2f%%' %('>' * int(size*50 / content_size),float(size / content_size * 100)),end="")
    end_time = time.time() # 结束时间
    print('\n' + "全部下载完成！用时%.2f秒" %(end_time - start_time))

if __name__ == '__main__':
    # url可指定下载的文件的url，name可带路径
    url = 'http://13114864.ch1.unicom.data.tv002.com/down/b5d68c550afa878fdb2da4a7e0a53ff1/WinZip_7.0.4564_xclient.info.dmg?cts=wt-f-D106A39A149A55F1f0f0&ctp=106A39A149A55&ctt=1582558631&limit=1&spd=30000&ctk=b5d68c550afa878fdb2da4a7e0a53ff1&chk=3c99a6980b9d846da8a7785a74328a6f-20068864&mtd=1'
    downloader(url=url,path='aaa.dmg')






















