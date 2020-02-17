# 我们几乎可以在任何操作系统上通过命令行指令与操作系统进行交互，比如Linux平台下的shell。那么我们如何通过Python来完成这些命令行指令的执行呢？
# 另外，我们应该知道的是命令行指令的执行通常有两个我们比较关注的结果：
#     命令执行的状态码 -- 表示命令执行是否成功
#     命令执行的输出结果 -- 命令执行成功后的输出
# 早期的Python版本中，我们主要是通过os.system()、os.popen().read()等函数来执行命令行指令的，另外还有一个很少使用的commands模块。
# 但是从Python 2.4开始官方文档中建议使用的是subprocess模块.

# 当我们在执行python程序的时候想要执行系统shell可以使用subprocess，这时可以新起一个进程来执行系统的shell命令，python3常用的有subprocess.run()和subprocess.Popen，
# 两者的区别是前者是调用的后者，相当于是subprocess.run是subprocess.Popen的又一层封装，前者必须要等待子进程运行结束才会返回，python主进程会被阻塞，而后者已运行则立即返回对象，
# 不用等待子进程运行结束，也可以使用wait()方法等待子进程运行结束，后期可以使用返回的对象调用子进程运行的结果。

使用subprocess这个模块来产生子进程，并连接到子进程的标准输入/输出/错误中去，还可以得到子进程的返回值。

\1. subprocess模块中的常用函数
subprocess.run()	               # Python 3.5中新增的函数。执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
subprocess.call()	               # 执行指定的命令，返回命令执行状态，其功能类似于os.system(cmd)。
subprocess.check_call()	         # 执行指定的命令，如果执行成功则返回状态码，否则抛出异常。其功能等价于subprocess.run(..., check=True)。
subprocess.check_output()	       # 执行指定的命令，如果执行状态码为0则返回命令执行结果，而不是打印，否则抛出异常。
subprocess.getoutput(cmd)	       # 接收字符串格式的命令，执行命令并返回执行结果，其功能类似于os.popen(cmd).read()和commands.getoutput(cmd)。
subprocess.getstatusoutput(cmd)	 # 接受字符串形式的命令，返回 一个元组形式的结果，第一个元素是命令执行状态，第二个为执行结果。
subprocess.Popen()               # 在一些复杂场景中，我们需要将一个进程的执行输出作为另一个进程的输入。在另一些场景中，我们需要先进入到某个输入环境，然后再执行一系列的指令等。这个时候我们就需要使用到suprocess的Popen()方法。
  该方法有以下参数：
    args：   # shell命令，可以是字符串，或者序列类型，如list,tuple。
    bufsize：# 缓冲区大小，可不用关心
    stdin,stdout,stderr：# 分别表示程序的标准输入，标准输出及标准错误
    shell：  # 与上面方法中用法相同
    cwd：    # 用于设置子进程的当前目录
    env：    # 用于指定子进程的环境变量。如果env=None，则默认从父进程继承环境变量
    universal_newlines：不同系统的的换行符不同，当该参数设定为true时，则表示使用\n作为换行符

\2. 上面各函数的定义及参数说明
函数参数列表：
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None, check=False, universal_newlines=False)
subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None)
subprocess.getstatusoutput(cmd)

subprocess.getoutput(cmd)
参数说明：
  args  # 要执行的shell命令，默认应该是一个字符串序列，如['df', '-Th']或('df', '-Th')，也可以是一个字符串，如'df -Th'，但是此时需要把shell参数的值置为True。
  shell # 如果shell为True，那么指定的命令将通过shell执行。如果我们需要访问某些shell的特性，如管道、文件名通配符、环境变量扩展功能，这将是非常有用的。当然，python本身也提供了许多类似shell的特性的实现，如glob、fnmatch、os.walk()、os.path.expandvars()、os.expanduser()和shutil等。
  check # 如果check参数的值是True，且执行命令的进程以非0状态码退出，则会抛出一个CalledProcessError的异常，且该异常对象会包含 参数、退出状态码、以及stdout和stderr(如果它们有被捕获的话)。
  stdout, stderr：
      run()函数默认不会捕获命令执行结果的正常输出和错误输出，如果我们向获取这些内容需要传递subprocess.PIPE，然后可以通过返回的CompletedProcess类实例的stdout和stderr属性或捕获相应的内容；
      call()和check_call()函数返回的是命令执行的状态码，而不是CompletedProcess类实例，所以对于它们而言，stdout和stderr不适合赋值为subprocess.PIPE；
      check_output()函数默认就会返回命令执行结果，所以不用设置stdout的值，如果我们希望在结果中捕获错误信息，可以执行stderr=subprocess.STDOUT。
  input # 该参数是传递给Popen.communicate()，通常该参数的值必须是一个字节序列，如果universal_newlines=True，则其值应该是一个字符串。
  universal_newlines # 该参数影响的是输入与输出的数据格式，比如它的值默认为False，此时stdout和stderr的输出是字节序列；当该参数的值设置为True时，stdout和stderr的输出是字符串。

\3. subprocess.CompletedProcess类介绍
需要说明的是，subprocess.run()函数是Python3.5中新增的一个高级函数，其返回值是一个subprocess.CompletedPorcess类的实例，
因此，subprocess.completedPorcess类也是Python 3.5中才存在的。它表示的是一个已结束进程的状态信息，它所包含的属性如下：
    args：      用于加载该进程的参数，这可能是一个列表或一个字符串
    returncode：子进程的退出状态码。通常情况下，退出状态码为0则表示进程成功运行了；一个负值-N表示这个子进程被信号N终止了
    stdout：    从子进程捕获的stdout。这通常是一个字节序列，如果run()函数被调用时指定universal_newlines=True，则该属性值是一个字符串。如果run()函数被调用时指定stderr=subprocess.STDOUT，那么stdout和stderr将会被整合到这一个属性中，且stderr将会为None
    stderr：    从子进程捕获的stderr。它的值与stdout一样，是一个字节序列或一个字符串。如果stderr灭有被捕获的话，它的值就为None
    check_returncode()： 如果returncode是一个非0值，则该方法会抛出一个CalledProcessError异常。
\subprocess.Popen类
该类用于在一个新的进程中执行一个子程序。前面我们提到过，上面介绍的这些函数都是基于subprocess.Popen类实现的，通过使用这些被封装后的高级函数可以很方面的完成一些常见的需求。由于subprocess模块底层的进程
创建和管理是由Popen类来处理的，因此，当我们无法通过上面哪些高级函数来实现一些不太常见的功能时就可以通过subprocess.Popen类提供的灵活的api来完成。

# subprocess.Popen的构造函数
  参数说明：
  args：    # 要执行的shell命令，可以是字符串，也可以是命令各个参数组成的序列。当该参数的值是一个字符串时，该命令的解释过程是与平台相关的，因此通常建议将args参数作为一个序列传递。
  bufsize： # 指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
  stdin, stdout, stderr： # 分别表示程序标准输入、输出、错误句柄。
  preexec_fn： # 用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
  close_fds：  # 如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭。
  shell： # 该参数用于标识是否使用shell作为要执行的程序，如果shell值为True，则建议将args参数作为一个字符串传递而不要作为一个序列传递。
  cwd：   # 如果该参数值不是None，则该函数将会在执行这个子进程之前改变当前工作目录。
  env：   # 用于指定子进程的环境变量，如果env=None，那么子进程的环境变量将从父进程中继承。如果env!=None，它的值必须是一个映射对象
  universal_newlines： # 如果该参数值为True，则该文件对象的stdin，stdout和stderr将会作为文本流被打开，否则他们将会被作为二进制流被打开。
  startupinfo和creationflags： # 这两个参数只在Windows下有效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如主窗口的外观，进程优先级等。

# subprocess.Popen类的实例可调用的方法
  Popen.poll()	 # 用于检查子进程（命令）是否已经执行结束，没结束返回None，结束后返回状态码。
  Popen.wait(timeout=None)	# 等待子进程结束，并返回状态码；如果在timeout指定的秒数之后进程还没有结束，将会抛出一个TimeoutExpired异常。
  Popen.communicate(input=None, timeout=None)	# 该方法可用来与进程进行交互，比如发送数据到stdin，从stdout和stderr读取数据，直到到达文件末尾。
  Popen.send_signal(signal)	# 发送指定的信号给这个子进程。
  Popen.terminate()	# 停止该子进程。
  Popen.kill()	# 杀死该子进程。
  Popen.returncode # 获取进程的返回码。如果进程未结束，将返回None。

wait() ：等待命令执行完成，并且返回结果状态
>>> obj = subprocess.Popen("sleep 10;echo 'hello'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
>>> obj.wait()
# 中间会一直等待
0

terminate()：结束进程
import subprocess
>>> res = subprocess.Popen("sleep 20;echo 'hello'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
>>> res.terminate() # 结束进程
>>> res.stdout.read()
b''

pid：获取当前执行子shell的程序的进程号
import subprocess
>>> res = subprocess.Popen("sleep 5;echo 'hello'",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
>>> res.pid # 获取这个linux shell 的 进程号
2778



\4. 实例
# subprocess.Popen的构造函数
import subprocess

cmd = input(">>>: ")
res = subprocess.Popen(
    cmd,  # 字符串指令,如dir 或 ipconfig等等
    shell=True,  # 使用shell,就相当于使用cmd窗口
    stderr=subprocess.PIPE,  # 标准错误输出,PIPE为管道，也就是将正确输出放到一个管道中，管道中的数值只能取一次，取走了就没有了。
    stdout=subprocess.PIPE,  # 将标准输出#错误输出丢到一个管道中，跟上边不是同一个管道。
)

print(res.stdout.read().decode("utf-8"))  # 将标准输出从管道拿出，输出打印出来。
print(res.stderr.read().decode("utf-8"))  # stdout.read()读出来的数据是bytes类型。将错误输出从管道拿出，输出打印出来。


# stdin  stdout
import subprocess
obj1=subprocess.Popen('ps -ef',shell=True,
                      stdout=subprocess.PIPE)

obj2=subprocess.Popen('grep tomcat',shell=True,
                      stdin=obj1.stdout,  # obj1的标准输出就是obj2的标准输入
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)

print(obj2.stdout.read().decode('utf-8'))

# subprocess.run() : 执行指定的命令，等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例。
>>> subprocess.run(["ls", "-l"])) 
'''
total 328
-rw-r--r--  1 zhanghongyang  staff      8 Feb  1 22:57 1.json
drwxr-xr-x  3 zhanghongyang  staff     96 Jan 27 17:58 __pycache__
-rw-r--r--  1 zhanghongyang  staff      9 Dec 21 22:29 a.txt
CompletedProcess(args=['ls', '-l'], returncode=0)
'''

>>> subprocess.run("exit 1", shell=True, check=True) # check=True 捕获进程以非0状态码退出，则会抛出一个CalledProcessError的异常
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')

# subprocess.call() :执行指定的命令，返回命令执行状态。
>>> subprocess.call(['ls',  '-l'])
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.call('ls -l', shell=True)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.call(['ls',  '-l'], stdout=subprocess.DEVNULL)
0
>>> subprocess.call(['ls',  '-l', '/test'])
ls: 无法访问/test: 没有那个文件或目录
2

# suprocess.check_call() :执行指定的命令，如果执行成功则返回状态码，否则抛出异常。
>>> subprocess.check_call(['ls',  '-l'])
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.check_call('ls -l', shell=True)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
0
>>> subprocess.check_call('ls -l /test', shell=True)
ls: 无法访问/test: 没有那个文件或目录
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.4/subprocess.py", line 557, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command 'ls -l /test' returned non-zero exit status 2

# sbuprocess.check_output() :执行指定的命令，如果执行状态码为0则返回命令执行结果，否则抛出异常。
>>> ret = subprocess.check_output(['ls',  '-l'])
>>> print(ret)
b' \xe5\x85\xac\xe5\x85\xb1\xe7\x9a\x84\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe6\xa8\xa1\xe6\x9d\xbf\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe8\xa7\x86\xe9\xa2\x91\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe5\x9b\xbe\xe7\x89\x87\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe6\x96\x87\xe6\xa1\xa3\ndrwxr-xr-x  2 wader wader   4096  4\xe6\x9c\x88 13  2016 \xe4\xb8\x8b\xe8\xbd\xbd\ndrwxr-xr-x  2 wader wader   4096 12\xe6\x9c\x88  7  2015 \xe9\x9f\xb3\xe4\xb9\x90\ndrwxr-xr-x  7 wader wader   4096  5\xe6\x9c\x88 26  2016 \xe6\xa1\x8c\xe9\x9d\xa2\n'
>>> ret = subprocess.check_output(['ls',  '-l'], universal_newlines=True)
>>> print(ret)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面

# subprocess.getoutput()与subprocess.getstatusoutput()
>>> ret = subprocess.getoutput('ls -l')
>>> print(ret)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面
>>> retcode, output = subprocess.getstatusoutput('ls -l')
>>> print(retcode)
0
>>> print(output)
总用量 160
drwxr-xr-x  2 wader wader   4096 12月  7  2015 公共的
drwxr-xr-x  2 wader wader   4096 12月  7  2015 模板
drwxr-xr-x  2 wader wader   4096 12月  7  2015 视频
drwxr-xr-x  2 wader wader   4096 12月  7  2015 图片
drwxr-xr-x  2 wader wader   4096 12月  7  2015 文档
drwxr-xr-x  2 wader wader   4096  4月 13  2016 下载
drwxr-xr-x  2 wader wader   4096 12月  7  2015 音乐
drwxr-xr-x  7 wader wader   4096  5月 26  2016 桌面

>>> retcode, output = subprocess.getstatusoutput('ls -l /test')
>>> print(retcode)
2
>>> print(output)
ls: 无法访问/test: 没有那个文件或目录

# 比如我想杀appium的进程，可以用下面的代码
import os
import subprocess

PIDS=subprocess.getstatusoutput('ps -ef |grep appium ')

pidlist=[]
for i in PIDS[1].split("\n"):
    try:
        pidlist.append(i.split()[1])
    except Exception as e:
        pass

print(pidlist)

for i in pidlist:
    os.system("kill -9 "+i)