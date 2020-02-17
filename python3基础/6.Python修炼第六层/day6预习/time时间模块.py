import time

# 时间戳  1970年到目前时间的秒数
# print(time.time())

# 格式化时间  当前时间 年月日 时分秒
# print(time.strftime('%Y-%m-%d %X'))

# 结构化时间  元组形式的当前时间
# print(time.localtime())
# print(time.localtime().tm_mon)

# 结构化时间  UTC 标准时间的时区  跟中国时间相差8个小时
# print(time.gmtime())

# 把接收秒数转成 结构化时间
# print(time.localtime(123123123))

# 把接收秒数转成 转成UTC格式的时间
# print(time.gmtime(123123123))

# 把当前的结构化时间 转成 时间戳
# print(time.mktime(time.localtime()))

# 把结构化时间 转格式化时间
# print(time.strftime('%Y',time.localtime()))
# print(time.strftime('%Y',time.gmtime()))

# '2017-10-16' #把格式化时间 转成结构化时间
# print(time.strptime('2017-10-16','%Y-%m-%d'))

# Mon Oct 16 23:00:58 2017
# print(time.ctime())
# print(time.asctime())
# print(time.ctime(123123))
# print(time.asctime(time.gmtime()))

# 休眠
# print(time.sleep(3))

