\一、日志级别
NOTSET   = 0  # 不设置
DEBUG    = 10
INFO     = 20
WARNING  = 30 # WARN = WARNING
ERROR    = 40
CRITICAL = 50 # FATAL = CRITICAL
'''
notset=0
debug=10
info=20
warning=30
error=40
critical=50
'''
\二、默认级别为warning，默认的输出目标是：终端
import logging

logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重critical')

'''  输出：日志级别是自上而下匹配的，因为默认的是warning，所以info和debug默认不显示。
WARNING:root:警告warn
ERROR:root:错误error
CRITICAL:root:严重critical
'''
# logging模块处理流程
1、判断日志的等级是否大于Logger对象的等级，如果大于，则往下执行，否则，流程结束。
2、产生日志。第一步，判断是否有异常，如果有，则添加异常信息。第二步，处理日志记录方法(如debug，info等)中的占位符，即一般的字符串格式化处理。
3、使用注册到Logger对象中的Filters进行过滤。如果有多个过滤器，则依次过滤；只要有一个过滤器返回假，则过滤结束，且该日志信息将丢弃，不再处理，而处理流程也至此结束。否则，处理流程往下执行。
4、在当前Logger对象中查找Handlers，如果找不到任何Handler，则往上到该Logger对象的父Logger中查找；如果找到一个或多个Handler，则依次用Handler来处理日志信息。但在每个Handler处理日志信息过程中，会首先判断日志信息的等级是否大于该Handler的等级，如果大于，则往下执行(由Logger对象进入Handler对象中)，否则，处理流程结束。
5、执行Handler对象中的filter方法，该方法会依次执行注册到该Handler对象中的Filter。如果有一个Filter判断该日志信息为假，则此后的所有Filter都不再执行，而直接将该日志信息丢弃，处理流程结束。
6、使用Formatter类格式化最终的输出结果。 注：Formatter同上述第2步的字符串格式化不同，它会添加额外的信息，比如日志产生的时间，产生日志的源代码所在的源文件的路径等等。
7、真正地输出日志信息(到网络，文件，终端，邮件等)。至于输出到哪个目的地，由Handler的种类来决定。

\三、为logging模块指定全局配置，针对所有logger有效，控制日志打印到文件中，并且自己定制日志的输出格式。
# ====================>介绍
可在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
    filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
    filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
    format：指定handler使用的日志显示格式。
    datefmt：指定日期时间格式。
    level：设置rootlogger（后边会讲解具体概念）的日志级别
    stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

format参数中可能用到的格式化串:
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s 用户输出的消息

# ====================> 使用
# 控制日志打印到文件中，并且自己定制日志的输出格式。
import logging

logging.basicConfig( # basicConfig方式不能实现即往文件打日志又往文件打印
    filename='access.log',
    # filemode='w', #默认是a模式，a模式时此参数可以不写。
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=10,
)

logging.debug('调试debug')
logging.info('消息info')
logging.warning('警告warn')
logging.error('错误error')
logging.critical('严重critical')
#========结果
access.log内容:
2017-07-28 20:32:17 PM - root - DEBUG   -test:  调试debug
2017-07-28 20:32:17 PM - root - INFO    -test:  消息info
2017-07-28 20:32:17 PM - root - WARNING -test:  警告warn
2017-07-28 20:32:17 PM - root - ERROR   -test:  错误error
2017-07-28 20:32:17 PM - root - CRITICAL-test:  严重critical

part2: 可以为logging模块指定模块级的配置,即所有logger的配置

# 待解决的问题：
    # 1：既往终端打印，又往文件中打印吗？
    # 2：控制输出到不同的目标（终端+文件）的日志，有各自的配置信息。






# 正确的logging模块使用方式
\四、logging模块的Logger，Handler，Filter，Formatter对象。
import logging
流水线：Logger(产生日志)————> Handler（发送到终端或文件）<———— Formatter（把Formatter对象绑定给Handler对象确定日志输出时的格式）

\1、创建Logger对象: 负责产生日志信息，然后交给Filter过滤，然后交给不同的Handler输出。
logger=logging.getLogger('root')

\2、Filter对象：过滤日志的对象，略。不怎么用。

\3、创建Handler对象: 负责接收Logger对象传来的日志内容，控制打印到终端or文件。Handler对象有两类，文件的FileHandler和终端的StreamHandler。
h1=logging.FileHandler('t1.log') #打印到文件
h2=logging.FileHandler('t2.log') #打印到文件
h3=logging.StreamHandler()       #打印到终端

\4、创建Formmater对象: 日志输出格式
# 给文件
formatter1=logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
# 给终端
formatter2=logging.Formatter(
    '%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

\5、为handler对象绑定Foratter对象的日志格式和设置日志级别。
#给文件：绑定到Filehandler对象
h1.setFormatter(formatter1)
h2.setFormatter(formatter1)
#给终端：绑定到Streamhandler对象
h3.setFormatter(formatter2)

#设置日志级别
h1.setLevel(30) # 第二道日志级别关卡，因为Logger设置的20级别，所以能够放行30级别的warning日志。
h2.setLevel(30)
h3.setLevel(30)

\6、把Handler对象h1,h2,h3都add给logger对象，这样logger对象才能把自己的日志交给他们三个Handler对象负责输出。
logger.addHandler(h1)
logger.addHandler(h2)
logger.addHandler(h3)
logger.setLevel(20) # 第一道日志级别关卡，这里设置的20（即info,能够通过的日志级别是20和20以上的级别）。括号的数字一定要<=Hanlder对象的数字。

\7、测试
logger.debug('debug')
logger.info('info')
logger.warning('warn123') # 级别30，设置Logger对象的日志级别为20时（info）能放行warning日志。
logger.error('error')
logger.critical('critical')
'''
执行结果： t1.log t2.log中有日志内容，同时终端也打印了一份。
'''

\强调: 如果想要日志成功打印
# 日志内容的级别 >= Logger对象的日志级别  <= Handler对象的日志级别

\五、Logger与Handler的级别
logger是第一级过滤，然后才能到handler，我们可以给logger和handler同时设置level，但是需要注意的是。
Logger也是第一个根据级别过滤消息的,如果您将Logger设置为INFO，并将所有处理程序设置为DEBUG，您仍然不会收到处理程序上的调试消息————它们将被日志程序本身拒绝。
如果您将logger设置为DEBUG，但是将所有处理程序设置为INFO，那么您也不会收到任何调试消息——因为当logger说“ok, processing this”时，处理程序会拒绝它(DEBUG < INFO)。

# 验证
import logging

form=logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    )

ch=logging.StreamHandler()

ch.setFormatter(form)
# ch.setLevel(10)
ch.setLevel(20) # 放行20级别以上的日志，debug日志级别不够直接被屏蔽了。

l1=logging.getLogger('root')
# l1.setLevel(20)
l1.setLevel(10) # 放行10级别以上的日志
l1.addHandler(ch)

l1.debug('l1 debug') # 级别为10


\六、Logger的继承（了解）
#了解知识点：Logger对象的继承

import logging

# 实例化了多个logger对象
logger1=logging.getLogger('a')
logger2=logging.getLogger('a.b') # 继承关系a.b，实际最后用的是a下面的b。a是b的父级。
logger3=logging.getLogger('a.b.c')

h3=logging.StreamHandler()

formatter2=logging.Formatter(
    '%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

h3.setFormatter(formatter2)
h3.setLevel(10)

# 同一个Handler对象可以给多个logger对象绑定，同一个logger对象可以add多个handler对象。
logger1.addHandler(h3) 
logger1.setLevel(10)

logger2.addHandler(h3)
logger2.setLevel(10)

logger3.addHandler(h3)
logger3.setLevel(10)

logger1.debug('logger1 debug')
logger2.debug('logger2 debug')  # 执行此条会打印两条日志，父级一条，自己一条。
logger3.debug('logger3 debug')  # 执行此条会打印两条日志，父父级一条，父级一条，自己一条。
'''
2020-01-30 23:30:10 PM - logger1 debug
2020-01-30 23:30:10 PM - logger2 debug
2020-01-30 23:30:10 PM - logger2 debug
2020-01-30 23:30:10 PM - logger3 debug
2020-01-30 23:30:10 PM - logger3 debug
2020-01-30 23:30:10 PM - logger3 debug
'''

\七、应用（在项目中正式使用logging模块方法）
\1、logging配置文件（详细阅读logger模块实用案例）
# 使用logging.config.dictConfig加载配置
import os
import logging.config

# 定义三种日志输出格式 开始
standard_format  = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
simple_format    = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录
logfile_name = 'all2.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'              # 绑定上面formatters字典中的simple
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',   # 绑定上面formatters字典中的standard
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,   # 日志大小 5M，每5M切割一份
            'backupCount': 5,          # 最大保留份数
            'encoding': 'utf-8',       # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置,同等于下面的''logger对象。
        '': { # 这里单引号里是空，表明使用的是默认的logger。
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕。
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)  # 加载上面定义的logging配置
    logger = logging.getLogger(__name__)    # 生成一个log实例
    logger.info('It works!')  # 记录该文件的运行状态

if __name__ == '__main__':
    load_my_logging_cfg()

\2、使用
import time
import logging
import my_logging  # 导入自定义的logging配置

logger = logging.getLogger(__name__)  # 生成logger实例

def demo():
    logger.debug("start range... time:{}".format(time.time()))
    logger.info("中文测试开始。。。")
    for i in range(10):
        logger.debug("i:{}".format(i))
        time.sleep(0.2)
    else:
        logger.debug("over range... time:{}".format(time.time()))
    logger.info("中文测试结束。。。")

if __name__ == "__main__":
    my_logging.load_my_logging_cfg()  # 在你程序文件的入口加载自定义logging配置
    demo()

\3、！！！关于如何拿到logger对象的详细解释！！！
注意注意注意：
#1、有了上述方式我们的好处是：所有与logging模块有关的配置都写到字典中就可以了，更加清晰，方便管理
#2、我们需要解决的问题是：
    1、从字典加载配置：logging.config.dictConfig(settings.LOGGING_DIC)

    2、拿到logger对象来产生日志
    logger对象都是配置到字典的loggers 键对应的子字典中的，按照我们对logging模块的理解，要想获取某个东西都是通过名字，也就是key来获取的。
    于是我们要获取不同的logger对象就是logger=logging.getLogger('loggers子字典的key名')

    但问题是：如果我们想要不同logger名的logger对象都共用一段配置，那么肯定不能在loggers子字典中定义n个key   
 'loggers': {    
        'l1': {
            'handlers': ['default', 'console'],  #
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'l2: {
            'handlers': ['default', 'console' ], 
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
        'l3': {
            'handlers': ['default', 'console'],  #
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
}

#我们的解决方式是，定义一个空的key
    'loggers': {
        '': {
            'handlers': ['default', 'console'], 
            'level': 'DEBUG',
            'propagate': True, 
        },

}

\这样我们再取logger对象时
logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，但是拿着该名字去loggers里找key名时却发现找不到，于是默认使用key=''的配置

\另外一个django的配置，瞄一眼就可以，跟上面的一样。
#logging_config.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 3,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        #打印到文件的日志:收集错误及以上的日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        #打印到文件的日志
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console', 'error'],
            'level': 'DEBUG',
            'propagate': True,
        },
        #logging.getLogger('collect')拿到的logger配置
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        }
    },
}

# -----------
# 用法:拿到俩个logger

logger = logging.getLogger(__name__) #线上正常的日志
collect_logger = logging.getLogger("collect") #领导说,需要为领导们单独定制领导们看的日志



