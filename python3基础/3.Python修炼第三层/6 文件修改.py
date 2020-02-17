文件的数据是存放于硬盘上的，因而只存在覆盖、不存在修改这么一说，我们平时看到的修改文件，都是模拟出来的效果，具体的说有两种实现方式：
方式一：将硬盘存放的该文件的内容全部加载到内存，在内存中是可以修改的，修改完毕后，再由内存覆盖到硬盘（word，vim，nodpad++等编辑器）

# 方式一（占用内存过大，仅适用于小文件）：把硬盘中文件的数据全部读入内存，然后在内存里进行修改，最后保存
import os
with open('e.txt','r',encoding='utf-8') as read_f,\
     open('.e.txt.swap','w',encoding='utf-8') as write_f:
    data=read_f.read()
    # print(type(data))
    data=data.replace('alex','SB')
    write_f.write(data)  # 写到新文件

os.remove('e.txt')
os.rename('.e.txt.swap','e.txt')

# 方式二：适用于大文件。将硬盘存放的该文件的内容一行一行地读入内存一行一行地改，修改完毕就写入新文件，最后用新文件覆盖源文件.
import os
with open('e.txt','r',encoding='utf-8') as read_f,\
        open('.e.txt.swap','w',encoding='utf-8') as write_f:
    for line in read_f:
        line=line.replace(' ',',')
        write_f.write(line)

os.remove('e.txt')
os.rename('.e.txt.swap','e.txt')



