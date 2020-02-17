import shutil

# 高级的 文件、文件夹、压缩包 处理模块

\将文件内容拷贝到另一个文件中
# 注意！fsrc, fdst都是文件对象，需要打开后才能进行复制import shutil
f1 = open('name', 'r')
f2 = open('name_copy', 'w+') # 复制生成的文件，无需提前存在
shutil.copyfileobj(f1, f2, length=16*1024)

\拷贝文件
# shutil.copyfile(src, dst)
shutil.copyfile('f1.log', 'f2.log') #目标文件无需存在

\仅拷贝权限。内容、组、用户均不变
# shutil.copymode(src, dst)
shutil.copymode('f1.log', 'f2.log') #目标文件必须存在

\仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copystat(src, dst)
shutil.copystat('f1.log', 'f2.log') #目标文件必须存在

\拷贝文件和权限
# shutil.copy(src, dst)
shutil.copy('f1.log', 'f2.log')

\拷贝文件和状态信息
# shutil.copy2(src, dst)
shutil.copy2('f1.log', 'f2.log')

\递归的去拷贝文件夹
# shutil.ignore_patterns(*patterns)
# shutil.copytree(src, dst, symlinks=False, ignore=None)
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*')) #目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除

\递归的去删除文件
# shutil.rmtree(path[, ignore_errors[, onerror]])
shutil.rmtree('folder1')

\递归的去移动文件，它类似mv命令，其实就是重命名。
# shutil.move(src, dst)
shutil.move('folder1', 'folder3')

\打包压缩：day5_bak.tar.gz
# shutil.make_archive(base_name, format,...)
# ============> 打包参数
base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径。
    如 data_bak                       =>保存至当前路径
    如：/tmp/data_bak =>保存至/tmp/
format：压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir：要压缩的文件夹路径（默认当前目录）
owner：用户，默认当前用户
group：组，默认当前组
logger：用于记录日志，通常是logging.Logger对象

# ============> 打包
shutil.make_archive('day5_bak','gztar',root_dir=r'xxxxxxxxx路径') # 会在当前目录生产day5_bak.tar.gz的文件
\目录打包压缩:day5_bak.tar.gz
shutil.make_archive('day5_bak','gztar',root_dir=r'C:\Users\Administrator\PycharmProjects\19期\day5')

#将 /data下的文件打包放置当前程序目录
import shutil
ret = shutil.make_archive("data_bak", 'gztar', root_dir='/data')

#将 /data下的文件打包放置 /tmp/目录
import shutil
ret = shutil.make_archive("/tmp/data_bak", 'gztar', root_dir='/data') 

\shutil 对压缩包的处理（解压）是调用 zipfile 和 tarfile 两个模块来进行的，详细

# zipfile
import zipfile

# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()

# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall(path='.')
z.close()

# tarfile
import tarfile

# 打包，没有压缩功能。
>>> t=tarfile.open('/tmp/egon.tar','w')
>>> t.add('/test1/a.py',arcname='a.bak')
>>> t.add('/test1/b.py',arcname='b.bak')
>>> t.close()


# 解压
>>> t=tarfile.open('/tmp/egon.tar','r')
>>> t.extractall('/egon')
>>> t.close()

# ============> 解压缩包
import tarfile

obj=tarfile.open('day5_bak.tar.gz')
obj.extractall('aaa')
obj.close()