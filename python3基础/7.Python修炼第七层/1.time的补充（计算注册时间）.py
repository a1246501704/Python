#上传时间：时间戳
#当前的时间
# 时差 = 当前的时间戳时间 - 上传的时间戳时间
# 时差转换为结构化时间 1970-1-1 = 1972-1-1
# 真正的时差 = 时差转换为结构化时间 - 1970 -1 - 1
# import time
# timestamp_before = time.mktime(time.strptime('2015-11-20 20:20:10','%Y-%m-%d %H:%M:%S'))
# time_now = time.time()
# def time_sub(timestamp_before,time_now = time.time()):
#     sub_time = time_now - timestamp_before
#     res = time.gmtime(sub_time)
#     return res
# print(res.tm_year-1970)
# print(res.tm_mon-1)
# print(res.tm_mday-1)

import time
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time
struct_time=time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))