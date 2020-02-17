#cp source_file dst_file
import sys  # argv用来给脚本传参数

sfile=sys.argv[1] # 源文件
dfile=sys.argv[2] # 目标文件

# 使用两个with实现
with open(sfile,'rb') as read_f:
    data=read_f.read()

with open(dfile,'wb') as write_f:
    write_f.write(data)


# 使用一个with实现，多个open，一个读一个写。
with open(sfile,'rb') as read_f,open(dfile,'wb') as write_f:
    # data=read_f.read()   # 读所有，如果文件过大会有性能问题
    # write_f.write(data)
    for line in read_f:    # 一行一行读
        write_f.write(line)
        write_f.flush()


# 练习，利用b模式，编写一个cp工具，要求如下：
　　1. 既可以拷贝文本又可以拷贝视频，图片等文件
　　2. 用户一旦参数错误，打印命令的正确使用方法，如usage: cp source_file target_file
　　提示：可以用import sys，然后用sys.argv获取脚本后面跟的参数

import sys
if len(sys.argv) != 3: # 判断传参的个数
    print('usage: cp source_file target_file')
    sys.exit()

source_file,target_file=sys.argv[1],sys.argv[2]
with open(source_file,'rb') as read_f,open(target_file,'wb') as write_f:
    for line in read_f:
        write_f.write(line)