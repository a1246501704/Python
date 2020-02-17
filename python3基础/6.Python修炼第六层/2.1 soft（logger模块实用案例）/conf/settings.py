import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
os.path.dirname # 获取当前目录路径，即conf目录。再加一层os.path.dirname取到的就是soft目录路径。
os.path.abspath # 获取当前文件绝对路径。
os.path.join    # 拼接文件路径的，不管是否存在。从第一个绝对路径开始拼接。
'''

#DB_PATH='%s%s%s%s%s'  %(BASE_DIR,os.sep,'db',os.sep,'db.json')
DB_PATH=os.path.join(BASE_DIR,'db','db.json')
LOG_PATH=os.path.join(BASE_DIR,'log','access.log') # 拼接成soft/log/access.log
COLLECT_PATH=os.path.join(BASE_DIR,'log','collect.log')

# 定义三种日志输出格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字 core.src
simple_format = '[%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '%(message)s'

# 日志的配置信息
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
        'id_simple': {
            'format': id_simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': LOG_PATH,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        'collect': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'id_simple',
            'filename': COLLECT_PATH,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        # l1=logging.getLogger('collect')拿到的logger配置
        # l2=logging.getLogger('l1')拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递(日志继承)
        },
        'collect': {
            'handlers': ['collect', ],  # 这里如果把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递(日志继承)
        },

    },
}

