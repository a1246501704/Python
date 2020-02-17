#海峰老师 模块博客：
# http://www.cnblogs.com/linhaifeng/articles/6384466.html#_label12

import logging

'''
#用于便捷记录日志且线程安全的模块

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

日志设定级别，则拥有本级别之上的所有级别
'''

'''
可在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有:
    filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
    filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
    format：指定handler使用的日志显示格式。
    datefmt：指定日期时间格式。
    level：设置rootlogger（后边会讲解具体概念）的日志级别
    stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。
            若同时列出了filename和stream两个参数，则stream参数会被忽略。


#logger：产生日志的对象
#Filter：过滤日志的对象
#Handler：接收日志然后控制打印到不同的地方，FileHandler用来打印到文件中，StreamHandler用来打印到终端
#Formatter对象：可以定制不同的日志格式对象，然后绑定给不同的Handler对象使用，以此来控制不同的Handler的日志格式

'''

# # import logging
# # logging.basicConfig(filename='access.log',
# #                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
# #                     datefmt='%Y-%m-%d %H:%M:%S %p',
# #                     level=10)
# #
# #
# # logging.debug('debug') #调试信息
# # logging.info('info') #正常信息
# # logging.warning('warning') #警告信息
# # logging.error('error') #错误信息
# # logging.critical('critical') #紧急信息
#
#
# #Formater,handler,logger,filter
# import logging
#
# #定义日志格式
# formatter1=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',)
#
# # fh1=logging.FileHandler('test1.log')  #接收日志内容到文件
# ch=logging.StreamHandler()  #接收日志内容到终端
#
# ch.setFormatter(formatter1) #接收日志的终端添加日志格式
#
# logging1=logging.getLogger('egon')  #产生日志，传给Handler
# logging1.setLevel(10)   #定义日志级别
# logging1.addHandler(ch) #把产生的日志 传给指定Handler
#
# logging1.debug('debug') #打印日志内容
# # logging1.info('info')
# # logging1.error('error')
# # logging1.warning('warning')
# # logging1.critical('critical')


import logging
import my_log_settings
my_log_settings.load_my_logging_cfg()

logging1=logging.getLogger(__name__)
logging2=logging.getLogger('collect')

logging1.debug('默认日志的debug')
logging2.debug('给老板的一封信')




