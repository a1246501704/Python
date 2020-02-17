# sys模块

import sys

'''

sys.argv           命令行参数List，第一个元素是程序本身路径
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称

sys.stdout         标准输出
'''

# #=========知识储备==========
# #进度条的效果
# [#             ]
# [##            ]
# [###           ]
# [####          ]

# #指定宽度
# print('[%-15s]' %'#')
# print('[%-15s]' %'##')
# print('[%-15s]' %'###')
# print('[%-15s]' %'####')

# #打印%
# print('%s%%' %(100)) #第二个%号代表取消第一个%的特殊意义

# #可传参来控制宽度
# print('[%%-%ds]' %50) #[%-50s]
# print(('[%%-%ds]' %50) %'#')
# print(('[%%-%ds]' %50) %'##')
# print(('[%%-%ds]' %50) %'###')


# #=========实现打印进度条函数==========
# import sys
# import time
#
# def progress(percent,width=50):
#     if percent >= 1:
#         percent=1
#     show_str=('[%%-%ds]' %width) %(int(width*percent)*'#')
#     print('\r%s %d%%' %(show_str,int(100*percent)),file=sys.stdout,flush=True,end='')


# #=========应用==========
# data_size=1025
# recv_size=0
# while recv_size < data_size:
#     time.sleep(0.1) #模拟数据的传输延迟
#     recv_size+=1024 #每次收1024
#
#     percent=recv_size/data_size #接收的比例
#     progress(percent,width=70) #进度条的宽度70
#


# #进度条
# import sys,time
#
# for i in range(1,10):
#     sys.stdout.write('\r%s' %('#'*i))
#     sys.stdout.flush()
#     time.sleep(0.5)
#
# import sys,time
# for i in range(1,10):
#     print('\r%s' %('#'*i),file=sys.stdout,flush=True,end='')
#     time.sleep(0.5)







# # 进度条
# # print(('[%%-%ds]' %50) %(20*'#'))
# # print('[%%-%ds]' %50 %(30*'#'))
#
# import sys,time
#
# def progress(percent,width=50): #51
#     if percent >= 100:
#         # print('\r[%s] 100%%' %(width*'#'))
#         # return
#         percent=100
#     show_str=('[%%-%ds]' %width) %(int(width*percent/100)*'#')
#     print('\r%s %d%%' %(show_str,percent),file=sys.stdout,flush=True,end='')
#
# total_size=1026
# recv_size=0
#
# while recv_size < total_size:
#     time.sleep(0.01) #模拟下载的网络延迟
#     recv_size+=1024
#     recv_per=int(100*recv_size/total_size)
#     progress(recv_per,width=30)








