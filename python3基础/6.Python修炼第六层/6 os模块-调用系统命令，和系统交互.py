import os # os模块是与操作系统交互的一个接口

\os模块函数功能
os.access(path, mode)           # 检验权限模式   
os.chdir(path)                  # 改变当前工作目录
os.chflags(path, flags)         # 设置路径的标记为数字标记。
os.chmod(path, mode)            # 更改权限
os.chown(path, uid, gid)        # 更改文件所有者
os.chroot(path)                 # 改变当前进程的根目录
os.close(fd)                    # 关闭文件描述符 fd
os.closerange(fd_low, fd_high)  # 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
os.curdir                       # 返回当前目录：（'.'）
os.dup(fd)                      # 复制文件描述符 fd
os.dup2(fd, fd2)                # 将一个文件描述符 fd 复制到另一个 fd2
os.environ                      # 获取系统环境变量
os.fchdir(fd)                   # 通过文件描述符改变当前工作目录
os.fchmod(fd, mode)             # 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
os.fchown(fd, uid, gid)         # 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
os.fdatasync(fd)                # 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
os.fdopen(fd[, mode[, bufsize]])  # 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
os.fpathconf(fd, name)          # 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
os.fstat(fd)                    # 返回文件描述符fd的状态，像stat()。
os.fstatvfs(fd)                 # 返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
os.fsync(fd)                    # 强制将文件描述符为fd的文件写入硬盘。
os.ftruncate(fd, length)        # 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
os.getcwd()                     # 返回当前工作目录
os.getcwdu()                    # 返回一个当前工作目录的Unicode对象
os.isatty(fd)                   # 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
os.lchflags(path, flags)        # 设置路径的标记为数字标记，类似 chflags()，但是没有软链接
os.lchmod(path, mode)           # 修改连接文件权限
os.lchown(path, uid, gid)       # 更改文件所有者，类似 chown，但是不追踪链接。
os.link(src, dst)               # 创建硬链接，名为参数 dst，指向参数 src
os.listdir(path)                # 返回path指定的文件夹包含的文件或文件夹的名字的列表。
os.lseek(fd, pos, how)          # 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
os.lstat(path)                  # 像stat(),但是没有软链接
os.linesep                      # 当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.major(device)                # 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
os.makedev(major, minor)        # 以major和minor设备号组成一个原始设备号
os.makedirs(path[, mode])       # 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
os.minor(device)                # 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
os.mkdir(path[, mode])          # 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
os.mkfifo(path[, mode])         # 创建命名管道，mode 为数字，默认为 0666 (八进制)
os.mknod(filename[, mode=0600, device])  # 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
os.open(file, flags[, mode])    # 打开一个文件，并且设置需要的打开选项，mode参数是可选的
os.openpty()                    # 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
os.pathconf(path, name)         # 返回相关文件的系统配置信息。
os.pathsep                      # 用于分割文件路径的字符串
os.pardir                       # 获取当前目录的父目录字符串名：('..')
os.pipe()                       # 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
\os.popen(command[, mode[, bufsize]])  # 从一个 command 打开一个管道
os.path.abspath(path)           # 返回path规范化的绝对路径
os.path.split(path)             # 将path分割成目录和文件名二元组返回
os.path.dirname(path)           # 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)          # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)            # 如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)             # 如果path是绝对路径，返回True
os.path.isfile(path)            # 如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)             # 如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)          # 返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)          # 返回path所指向的文件或者目录的最后修改时间
os.name                         # 字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.read(fd, n)                  # 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
os.readlink(path)               # 返回软链接所指向的文件
os.remove(path)                 # 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
os.removedirs(path)             # 递归删除目录。若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.rename(src, dst)             # 重命名文件或目录，从 src 到 dst
os.renames(old, new)            # 递归地对目录进行更名，也可以对文件进行更名。
os.rmdir(path)                  # 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
os.sep                          # 操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.stat(path)                   # 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
os.stat_float_times([newvalue]) # 决定stat_result是否以float对象显示时间戳
os.statvfs(path)                # 获取指定路径的文件系统统计信息
os.symlink(src, dst)            # 创建一个软链接
\os.system("bash command")       # 运行shell命令，直接显示执行结果。
os.tcgetpgrp(fd)                # 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
os.tcsetpgrp(fd, pg)            # 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
os.tempnam([dir[, prefix]])     # 返回唯一的路径名用于创建临时文件。
os.tmpfile()                    # 返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
os.tmpnam()                     # 为创建一个临时文件返回一个唯一的路径
os.ttyname(fd)                  # 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
os.unlink(path)                 # 删除文件路径
os.utime(path, times)           # 返回指定的path文件的访问和修改的时间。
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])  # 输出在文件夹中的文件名通过在树中游走，向上或者向下。
os.write(fd, str)               # 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度


os.name()                               # 返回当前使用平台的代表字符，Windows用'nt'表示，Linux用'posix'表示
os.getcwd()                             # 获取当前工作目录，即当前python脚本工作的目录路径
os.getpid()
os.getcwdb()
os.getcwdu()
os.getegid()
os.geteuid()
os.getpid()
os.getppid()
os.getenv()
os.getenvb()
os.abort()
os.chmod()
os.chown()
os.close()
os.cpu_count()
os.kill()
os.open()
os.getgid()
os.chdir("dirname")                     # 改变当前脚本工作目录；相当于shell下cd
os.curdir()                             # 返回当前目录: ('.')
os.pardir()                             # 获取当前目录的父目录字符串名：('..')
os.mkdir('dirname')                     # 生成单级目录；相当于shell中mkdir dirname
os.makedirs('dirname1/dirname2')        # 可生成多层递归目录
os.rmdir('dirname')                     # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.removedirs('dirname1')               # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.listdir('dirname')                   # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove('1.txt')                      # 删除一个文件
os.rename("oldname","newname")          # 重命名文件/目录/移动目录/，只能同设备（在同一块磁盘，不同设备看下面shutil模块）。
os._exit(n)                             # 直接推出，不抛异常，不执行相关清理工作。常用在子进程中
os.stat('path/filename')                # 获取文件/目录信息
    # l = os.stat('path/filename')
    # print(list(l))
    # print(list(l)[2])
os.sep()                                # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep()                            # 输出当前平台使用的行分隔符，win下为"\t\n",Linux下为"\n"
os.pathsep()                            # 输出用于分割文件路径的字符串 win下为;,Linux下为:
os.environ()                            # 获取系统环境变量
\os.system("bash command")              # 运行shell命令，直接显示，无法直接保存结果。os.system('ls')
os.system(cmd + "> /dev/null 2>&1")     # 将输出丢入黑洞
\os.popen()                             # 打开命令cmd或从命令cmd打开管道，返回值是连接到管道的文件对象
    # res = os.popen("free -m").read()
    #                 # 或readlines()    # 运行shell命令，获取执行结果赋值给变量。
    # print(res)
    res=os.popen("cat /etc/issue").read()
    res=res.split()[0]
    print(res)

os.path.abspath("/usr/bin")                   # 返回path的绝对路径
os.path.split("/usr/bin")                     # 将path分割成目录和文件名元组返回
os.path.dirname("/usr/bin")                   # 返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename("/usr/bin")                  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.isabs("/usr/bin")                     # 如果path是绝对路径，返回True
os.path.exists("/usr/bin")                    # 判断path是否存在，存在返回True,不存在返回False
os.path.isfile("/usr/bin")                    # 判断path是否为文件，是返回True,不是返回False
os.path.isdir("/usr/bin")                     # 判断path是否目录，是返回True，不是返回False
os.path.join(path1[, path2[, ...]])           # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
    # seq1 = ['hello','good','jesse']
    # print(' '.join(seq1)) # hello good jesse

    #seq2 = ['/hello/','/good/','/jesse/']
    #print(list(seq2))
    #print(os.path.join('/hello/','/good/','jesse'))
    #/good/jesse

os.path.getmtime("/usr/bin")                  # 返回文件或目录的最后修改时间，结果为秒数
os.path.getatime("/usr/bin")                  # 返回文件或目录的最后访问时间，结果为秒数
os.path.getctime("/usr/bin")                  # 返回文件或目录得创建时间，结果为秒数
os.path.getsize("/usr/bin")                   # 返回文件的大小，若是目录则返回0


\res=os.system('tasklist')                   # tasklist是windows查看进程命令
print('==========================?>',res)   # 上一步的输出直接打印到终端上了，只返回了一个0.
cmd = "df -hT"
os.system(cmd)

print(os.path.split(r'a\b\c\d.txt') )       # 切分目录路径和文件名
print(os.path.dirname(r'a\b\c\d.txt') )     # 取目录名
print(os.path.basename(r'a\b\c\d.txt') )    # 取文件名

print(os.stat(os.stat(os.path.abspath(__file__)).st_size) # os.stat看文件状态，接着调.st_size就是文件大小。
print(os.path.getsize(os.path.abspath(__file__))) # 直接调文件大小


# 在Linux和Mac平台上，该函数会原样返回path
# 在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。
print(os.path.normcase('c:/Windows\\system32\\')) # c:/Windows\system32\

# 不区分系统，规范化路径，如..和/
print(os.path.normpath('c://windows\\System32\\../Temp/')) # c:/windows\System32\../Temp

\文件操作
# 关于open的模式
w 写方式
a 追加模式打开（从EOF开始，必要时创建新文件）
r+ 以读写模式打开
w+ 以读写模式打开
a+ 以读写模式打开
rb 以二进制读模式打开
wb 以二进制写模式打开 (参见 w )
ab 以二进制追加模式打开 (参见 a )
rb+ 以二进制读写模式打开 (参见 r+ )
wb+ 以二进制读写模式打开 (参见 w+ )
ab+ 以二进制读写模式打开 (参见 a+ )
# 用法
os.mknod("text.txt")：创建空文件
fp = open("text.txt",w):直接打开一个文件，如果文件不存在就创建文件

fp.read([size])         # size为读取的长度，以byte为单位
fp.readline([size])     # 读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])    # 把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
fp.write(str)           # 把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)      # 把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
fp.close()              # 关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。 如果一个文件在关闭后还对其进行操作会产生ValueError
fp.flush()              # 把缓冲区的内容写入硬盘
fp.fileno()             # 返回一个长整型的”文件标签“
fp.isatty()             # 文件是否是一个终端设备文件（unix系统中的）
fp.tell()               # 返回文件操作标记的当前位置，以文件的开头为原点
fp.next()               # 返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[,whence])  # 将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
fp.truncate([size])     # 把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。


\目录操作
os.mkdir("file")                        # 创建目录
shutil.copyfile("oldfile","newfile")    # 复制文件:oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")        # oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
shutil.copytree("olddir","newdir")      # 复制文件夹.olddir和newdir都只能是目录，且newdir必须不存在。可以跨设备。
os.rename("oldname","newname")          # 重命名文件（目录）.文件或目录都是使用这条命令
shutil.move("oldpos","newpos")          # 移动文件（目录）
os.rmdir("dir")                         # 只能删除空目录
shutil.rmtree("dir")                    # 空目录、有内容的目录都可以删
os.chdir("path")                        # 转换目录，换路径

\取当前执行文件的绝对路径
# django中的处理方式
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# openstack中使用如下方式处理
# print(os.path.normpath(os.path.join(os.path.abspath(__file__),'..','..')))
print(os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    '..',
    '..'
)
))


os路径处理
#方式一：不推荐使用
import os
#具体应用
import os,sys
possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(__file__),
    os.pardir, #上一级
    os.pardir,
    os.pardir
))
sys.path.insert(0,possible_topdir)


#方式二：推荐使用
os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

