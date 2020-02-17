#time与datetime
在Python中，通常有这几种方式来表示时间：
    时间戳(timestamp): 通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。
    格式化的时间字符串(Format String)
    结构化的时间(struct_time): struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天，夏令时)


import time
\时间戳
print(time.time())  # 1487130156.419527,返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

\结构化的时间
print(time.localtime())         # time.struct_time(tm_year=2019, tm_mon=1, tm_mday=29, tm_hour=21, tm_min=45, tm_sec=57, tm_wday=1, tm_yday=29, tm_isdst=0)
print(time.localtime().tm_year) # 只取年
print(time.gmtime())            # 世界标准时间,和上面的localtime差8小时。

\格式化的字符串时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # '2017-02-15 11:40:53'
print(time.strftime('%Y-%m-%d %X'))

\参考“时间转换图2”
# 本地时区的struct_time，可以通过asctime将 结构化的时间 转换成 格式化字符串的时间。接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
print(time.asctime(time.localtime()))  # Sat Feb  1 15:37:22 2020
print(time.asctime(time.localtime(time.time())))

# UTC时区的struct_time，可以通过ctime将 时间戳时间 转换成 格式化字符串的时间。把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。
print(time.ctime(time.time()))  # Sat Feb  1 15:36:09 2020

\了解
print(time.localtime(123123123))                  # localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。
print(time.gmtime(123123123))                     # 世界标准时间，和localtime差8小时。gmtime() 函数将一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970-1-1以来的秒数。其默认值为time.time()，函数返回time.struct_time类型的对象。
print(time.mktime(time.localtime()))              # mktime() 函数执行与gmtime(), localtime()相反的操作，它接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。
print(time.strptime('2017:03-01','%Y:%m-%d'))     # 根据指定的格式把一个时间字符串解析为时间元组。
print(time.strftime('%Y-%m-%d %X',time.gmtime())) # 接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。

\格式化字符串的时间格式
%a    Locale’s abbreviated weekday name.     
%A    Locale’s full weekday name.     
%b    Locale’s abbreviated month name.     
%B    Locale’s full month name.     
%c    Locale’s appropriate date and time representation.     
%d    Day of the month as a decimal number [01,31].     
%H    Hour (24-hour clock) as a decimal number [00,23].     
%I    Hour (12-hour clock) as a decimal number [01,12].     
%j    Day of the year as a decimal number [001,366].     
%m    Month as a decimal number [01,12].     
%M    Minute as a decimal number [00,59].     
%p    Locale’s equivalent of either AM or PM.    (1)
%S    Second as a decimal number [00,61].    (2)
%U    Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
%w    Weekday as a decimal number [0(Sunday),6].     
%W    Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
%x    Locale’s appropriate date representation.     
%X    Locale’s appropriate time representation.     
%y    Year without century as a decimal number [00,99].     
%Y    Year with century as a decimal number.     
%z    Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].     
%Z    Time zone name (no characters if no time zone exists).     
%%    A literal '%' character.

其中计算机认识的时间只能是'时间戳'格式，而程序员可处理的或者说人类能看懂的时间有: '格式化的时间字符串'，'结构化的时间' ，于是有了下图的转换关系.

\参考“时间转换图1”
    结构化的时间struct_ime ——> mktime ——> 时间戳 timestamp
    结构化的时间struct_ime ——> strftime ——> 格式化的字符串时间 format string

    格式化的字符串时间 format string ——> strptime ——> 结构化的时间struct_ime
    时间戳 timestamp ——> localtime/gmtime ——>  结构化的时间struct_ime

    时间戳 timestamp ——> print(time.strftime('%Y-%m-%d %X',time.localtime(time.time()))) ——> 结构化的时间struct_ime
    结构化的时间struct_ime  ——>  print(time.mktime(time.strptime('2011-05-05 16:37:06','%Y-%m-%d %X'))) ——> 时间戳 timestamp

#--------------------------按图1转换时间
# localtime([secs])
# 将一个 时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。
print(time.localtime()) # time.struct_time(tm_year=2020, tm_mon=2, tm_mday=1, tm_hour=15, tm_min=44, tm_sec=44, tm_wday=5, tm_yday=32, tm_isdst=0)
print(time.localtime(1473525444.037215)) # time.struct_time(tm_year=2016, tm_mon=9, tm_mday=11, tm_hour=0, tm_min=37, tm_sec=24, tm_wday=6, tm_yday=255, tm_isdst=0)
 
print(time.gmtime(1473525444.037215)) # 和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。
 
# mktime(t) : 将一个struct_time转化为时间戳。
print(time.mktime(time.localtime()))  # 1473525749.0

strftime(format[, t]) : 把一个代表时间的元组或者struct_time（如由time.localtime()和
# time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。
print(time.strftime("%Y-%m-%d %X", time.localtime()))           # 2016-09-11 00:49:56  将结构化时间 转换成 格式化时间字符串
print(time.strftime('%Y-%m-%d %X',time.localtime(time.time()))) # 2020-02-01 15:54:19  将时间戳 转换成 格式化时间字符串
 
# 把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
print(time.strptime('2011-05-05 16:37:06', '%Y-%m-%d %X')) # time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6,tm_wday=3, tm_yday=125, tm_isdst=-1)
#在这个函数中，format默认为："%a %b %d %H:%M:%S %Y"。


\时间加减
import datetime
# 取当前时间
print(datetime.datetime.now()) # 返回格式化时间 2016-08-19 12:47:03.941925

# 3天以后的时间
print(datetime.datetime.now()+datetime.timedelta(days=3)) # 时间戳直接转成日期格式 2016-08-19

# 3天以前
print(datetime.datetime.now()-datetime.timedelta(days=3)) # 当前时间+3天
# 3天以前
print(datetime.datetime.now()+datetime.timedelta(days=-3))# 当前时间-3天

# 小时
print(datetime.datetime.now()+datetime.timedelta(hours=3))

# 分钟....等更细的时间
print(datetime.datetime.now()+datetime.timedelta(minutes=3))

# 时间戳 转换成 格式化的字符串时间
print(datetime.datetime.fromtimestamp(123123123)) # 1973-11-26 08:52:03
 
# 修改时间，修改年，月，日，时，分，秒
print(datetime.datetime.now().replace(hour=22))  # 2020-02-01 22:59:34.015982

# 修改时间，修改年，月，日，时，分，秒
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))  # 2020-02-01 02:03:29.854853

\常用时间转换及处理函数：
import datetime
# 获取当前时间
d1 = datetime.datetime.now()
print(d1)

# 当前时间加上半小时
d2 = d1 + datetime.timedelta(hours=0.5)
print(d2)

# 格式化字符串输出
d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
print(d3)

# 将字符串转化为时间类型
d4 = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
print(d4)

# 获取本周和本月第一天的日期：
# -*- coding:utf-8 -*-
import datetime

def first_day_of_month():
    '''
    获取本月第一天
    :return:
    '''
    # now_date = datetime.datetime.now()
    # return (now_date + datetime.timedelta(days=-now_date.day + 1)).replace(hour=0, minute=0, second=0,
    # microsecond=0)
    return datetime.date.today() - datetime.timedelta(days=datetime.datetime.now().day - 1)

def first_day_of_week():
    '''
    获取本周第一天
    :return:
    '''
    return datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())

if __name__ == "__main__":
    this_week = first_day_of_week()
    last_week = this_week - datetime.timedelta(days=7)
    this_month = first_day_of_month()
    last_month = this_month - datetime.timedelta(days=(this_month - datetime.timedelta(days=1)).day)
    print(this_week) 
    print(last_week)
    print(this_month)
    print(last_month)
'''
2020-01-27
2020-01-20
2020-02-01
2020-01-01
'''

import datetime

"""
datetime的功能强大
能支持0001年到9999年
"""

# 当前时间。返回的是一个datetime类型。now方法有个参数tz，设置时区类型。如果没有和方法today的效果一样
now = datetime.datetime.now()
# UTC时间
datetime.datetime.utcnow()

attrs = [
    ("year", "年"), ('month', "月"), ("day", "日"), ('hour', "小时"), ('minute', "分"), ('second', "秒"),
    ('microsecond', "毫秒"), (
        'min', "最小"), ('max', "最大"),
]
for k, v in attrs:
    "now.%s = %s #%s" % (k, getattr(now, k), v)


# 返回一个time结构
now.timetuple()

# 返回一个date类型
now.date()

# 返回一个time类型
now.time()

# 当前星期几。星期一是0，星期于是6。注意这里是方法，不是属性哦。
now.weekday()

# 当前星期几。星期一是1，星期于是7。注意这里是方法，不是属性哦。
now.isoweekday()

# 修改当前时间。比如修改成当月1号
now.replace(day=1)
past = datetime.datetime(2010, 11, 12, 13, 14, 15, 16)

# 行比较运算.返回的是timedelta类型
now - past

# 转成字符串。详细规则见Time篇
strdatetime = now.strftime("%Y-%m-%d %H:%M:%S")

# 字符串生成datetime对象
datetime.datetime.strptime(strdatetime, "%Y-%m-%d %H:%M:%S")