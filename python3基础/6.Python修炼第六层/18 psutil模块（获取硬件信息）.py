# psutil是一个跨平台库（http://code.google.com/p/psutil/），能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。
# 它主要应用于系统监控，分析和限制系统资源及进程的管理。它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、
# free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。目前支持32位和64位的Linux、Windows、OS X、FreeBSD和Sun Solaris等操作系统

import Psutil

\cpu
1 psutil.cpu_percent(interval,percpu) #返回CPU利用率
2 psutil.cpu_times_percent(interval=None, percpu=False)
3 psutil.cpu_count(logical=True)   #返回系统逻辑CPU
4 psutil.cpu_stats()              #返回CPU的统计信息
5 psutil.cpu_freq(percpu=False)   #返回CPU的频率

查看cpu逻辑个数
>>> psutil.cpu_count()
1

查看cpu物理个数
>>> psutil.cpu_count(logical=False)
1

\内存
系统总计内存
>>> mem.total
1040662528

查看系统虚拟内存
>>> mem = psutil.virtual_memory()

系统已经使用内存
>>> mem.used
965718016

系统空闲内存
>>> mem.free
112779264

\磁盘
磁盘利用率使用psutil.disk_usage方法获取，

磁盘IO信息包括read_count(读IO数)，write_count(写IO数)
read_bytes(IO写字节数)，read_time(磁盘读时间)，write_time(磁盘写时间),这些IO信息用
psutil.disk_io_counters()

获取磁盘的完整信息
psutil.disk_partitions()

获取分区表的参数
psutil.disk_usage('/')   #获取/分区的状态

获取硬盘IO总个数
psutil.disk_io_counters()

获取单个分区IO个数
psutil.disk_io_counters(perdisk=True)    #perdisk=True参数获取单个分区IO个数

\网络
网络信息与磁盘IO信息类似,涉及到几个关键点，包括byes_sent(发送字节数),byte_recv=xxx(接受字节数),
pack-ets_sent=xxx(发送字节数),pack-ets_recv=xxx(接收数据包数),这些网络信息用

获取网络总IO信息
psutil.net_io_counters()  

输出网络每个接口信息
psutil.net_io_counters(pernic=True)     #pernic=True

获取当前系统用户登录信息
psutil.users()

psutil.net_io_counters(pernic=False)        #返回系统网络IO统计信息
psutil.net_connections(kind='inet')         #返回系统socket连接
psutil.net_if_addrs()                       #返回网卡绑定的IP、子网掩码、广播地址
psutil.net_if_stats()                       #返回网卡的相关信息


\获取开机时间
psutil.boot_time() #以linux时间格式返回
datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S") #转换成自然时间格式

\查看单个进程
p = psutil.Process(2423) 
psutil.pids() #查看系统全部进程
p.name()   #进程名
p.exe()    #进程的bin路径
p.cwd()    #进程的工作目录绝对路径
p.status()   #进程状态
p.create_time()  #进程创建时间
p.uids()    #进程uid信息
p.gids()    #进程的gid信息
p.cpu_times()   #进程的cpu时间信息,包括user,system两个cpu信息
p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
p.memory_percent()  #进程内存利用率
p.memory_info()    #进程内存rss,vms信息
p.io_counters()    #进程的IO信息,包括读写IO数字及参数
p.connectios()   #返回进程列表
p.num_threads()  #进程开启的线程数
听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
p.name()
p.username()

\传感器
1 psutil.sensors_temperatures(fahrenheit=False)       #返回硬件的温度
2 psutil.sensors_fans()                               #返回硬件风扇速度
3 psutil.sensors_battery()                            #返回电池状态