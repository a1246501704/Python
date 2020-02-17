\一、read(3)
1. 文件打开方式为文本模式时，代表读取3个字符.
2. 文件打开方式为b模式时，代表读取3个字节.
#以文本的模式读文件，n代表的是字符的个数
with open('a.txt','r',encoding='utf-8') as f:
    data=f.read(3) # 你好啊
    print(data)

#以b的模式读文件，n代表的是字节的个数
with open('a.txt','rb') as f:
    data=f.read(3)  # b'\xe4\xbd\xa0'
    print(f.tell())
    print(data.decode('utf-8')) # 你

\二: 其余的文件内光标移动都是以字节为单位如:seek，tell，truncate、
注意:
1. seek有三种移动方式 0，1，2，其中1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
2. truncate是截断文件，所以文件的打开方式必须可写，但是不能用w或w+等方式打开，因为那样直接清空文件了，
   所以truncate要在r+或a或a+等模式下测试效果。
# tell:告诉当前光标的位置
with open('a.txt','r',encoding='utf-8') as f:
    data=f.read(3)
    print(f.tell())
    print(data)

# seek：移动光标
with open('a.txt','r',encoding='utf-8') as f:
    data1=f.read()
    print('first: ',data1)
    print(f.tell())
    f.seek(0)    # 将光标再移动到行首。
    data2 = f.read()
    print('second: ',data2)


# 0:文件开头
# 1:当前位置，文件的打开模式要是rb模式。
# 2:文件末尾,文件的打开模式要是rb模式。
with open('a.txt','r',encoding='utf-8') as f:
    f.seek(3,0)  # 第二个参数表示3以谁做参照物移动，可以写0、1、2。其中的0是从文件开头移动。
    print(f.read())

with open('a.txt', 'rb',) as f:
    f.read(3)
    f.seek(3,1)
    # print(f.read())
    print(f.read().decode('utf-8'))

with open('a.txt', 'rb',) as f:
    f.seek(-3,2) # 倒着seek,2模式光标到文件末尾。0到末尾
    print(f.read())


# tail -f access.log，查看tail.py文件
with open('access.log','a',encoding='utf-8') as f:
    f.write('11111\n')




# truncate截断文件，只能在a模式下使用。保留从开头到x，其余部分删除。以字节为单位从文件开头开始。
with open('a.txt','a',encoding='utf-8') as f:
    f.truncate(2)




file.read([size])      # size 未指定则返回整个文件，如果文件大小 >2 倍内存则有问题，f.read()读到文件尾时返回""(空字串)。
file.readline()        # 读取一行。
file.readable          # 判断文件是否可读
file.readlines([size]) # 返回包含size行的列表, size 未指定则读取所有内容放入列表中。
for line in f: print line # 通过迭代器访问。
f.write("hello\n")     # 如果要写入字符串以外的数据,先将他转换为字符串。
f.writelines           # 写多行
f.writable             # 判断文件是否可写
f.tell()               # 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数)。
f.seek(偏移量,[起始位置]) # 用来移动文件指针。偏移量: 单位为比特，可正可负。起始位置: 0 - 文件头, 默认值; 1 - 当前位置; 2 - 文件尾
f.close()              # 关闭文件

