\打开文件的模式
文件句柄 = open('文件路径', '模式')

模式可以是以下方式以及他们之间的组合:
# ‘r'	open for reading (default)
# ‘w'	open for writing, truncating the file first
# ‘a'	open for writing, appending to the end of the file if it exists
# ‘b'	binary mode
# ‘t'	text mode (default)
# ‘+'	open a disk file for updating (reading and writing)
# ‘U'	universal newline mode (for backwards compatibility; should not be used in new code)

# 1. 打开文件的模式有(默认为文本模式)：
r，只读模式【默认模式，文件必须存在，不存在则抛出异常】
w，只写模式【不可读；不存在则创建；存在则清空内容】
a，之追加写模式【不可读；不存在则创建；存在则只追加内容】

# 2. 对于非文本文件，我们只能使用b模式，"b"表示以字节的方式操作（而所有文件也都是以字节的形式存储的，
# 使用这种模式无需考虑文本文件的字符编码、图片文件的jgp格式、视频文件的avi格式）
rb 
wb
ab
# 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码

# 3. 了解部分，没什么太大意义。
"+"  表示可以同时读写某个文件
r+， 读写【可读，可写】
w+， 写读【可读，可写】
a+， 写读【可读，可写】
x，  只写模式【不可读；不存在则创建，存在则报错】
x+， 写读【可读，可写】

\字符串数据类型（text，r、w、a实际上是rt、wt、at，只是把t省略了）
# r：默认的打开模式，实际是rt。只读，文件不存在则报错。
f=open('a.txt',encoding='utf-8')
print('===>',f.read())     # 读所有，bytes---decode('utf-8')--->str(unicode)，编辑器自动给做了decode。
print('===>',f.read())     # 光标从第一行开始移动读取，当第二次再读的时候已经没有了。读完了。
print(f.readline(),end='') # 一次读一行，print在打印时end=\n。添加end=''即可。
print(f.readline(),end='')
print(f.readline(),end='')
print(f.readline(),end='') # 当读第四行的时候就没有内容了。
print(f.readlines())       # 读所有行，结果放入列表中。大文件时不使用这个，费内存。

for line in f.readlines(): # 去除readlines列表中的换行符。
    line=line.strip('\n')
f.close()

# w:只写模式，实际是wt。不能读。如果文件存在则清空，如果文件不存在则新建。
f=open('b.txt',mode='w',encoding='utf-8')  # utf-8是告诉操作系统用什么编码打开
f.write('11111\n') # 要自己加换行符，unicode---encode-->bytes 
f.write('2222\n')
f.write('333333\n')

l=['444\n','55555\n','66666\n']  # 为 writelines铺垫
for line in l:
    f.write(line)

f.writelines(['444\n','55555\n','66666\n']) # 以列表、元组、集合（乱序）的形式都可以，就不用循环了。本质原理就是一个for循环写。
f.close()

# a：追加写模式，实际是at。如果文件存在则把光标移动到文件末尾，如果文件不存在则新建。存在则追加。
f=open('c.txt','a',encoding='utf-8')  # 指定模式时可以不用写mode关键字，直接写模式。适用所有权限。
f.write('333333\n')
f.write('444444\n')
f.write('1111\n222\n') #针对文本模式的写,需要自己写换行符
f.write('1111\n222\n'.encode('utf-8')) #针对b模式的写,需要自己写换行符
f.writelines(['333\n','444\n']) #文件模式
f.writelines([bytes('333\n',encoding='utf-8'),'444\n'.encode('utf-8')]) #b模式
f.close()


# 遍历文件
with open('a.txt',encoding='utf-8') as f:
#     #不推荐使用
     lines=f.readlines() # readlins将文件所有内容读到一个列表中，可迭代对象。
     for line in lines:
        #  print(line,end='') # end=''是去掉print函数自带的换行符
#     #推荐使用，不依赖索引也不依赖key使用for循环比较好。
     for line in f:
         print(line,end='') # 此时line是str类型，字符串就和字符编码有关系。属于文本文件，r、w、a模式实际上后面都省略了个t（text）。

\二进制数据类型（bytes，r、w、a实际上是rb、wb、ab，只是把t省略了）
# b: open时是以bytes的形式去操作文件内容,不能指定字符编码。

with open('yuanhao.jpg',mode='rb') as f: # 不能使用text形式操作（rt、wt、at），bytes格式也不能encoding
    print(f.read())  # b类型
    print(f.read().decode('utf-8'))  # 图片、视频等非text的的bytes类型不能decode，读出的内容是bytes类型没错，但不是unicode encode后的结果。

with open('a.txt',mode='rb') as f:   
    data=f.read()
    print(data.decode('utf-8')) # decode解码成python3的str(unicode)类型，utf-8是怎么存的怎么显示。rb格式也可以打开text文本文件，直接取到原始的bytes。a.txt写中文测试

with open('d.txt',mode='wb') as f:
    f.write('哈哈哈hello'.encode('utf-8')) # str(unicode)————>encode————>bytes（存到硬盘），utf-8是告诉操作系统以什么编码写入。

with open('d.txt', mode='ab') as f:
    f.write('\n哈哈哈hello'.encode('utf-8'))


\了解
f.read       # 读取文件全部，光标移动到文件内容最后。
f.readline   # 一次读一行
f.readlines  # 全读出来，将结果放入列表中（带有\n换行符）
f.write      # 写文件，文件有则覆盖内容，文件没有则新建。
f.writelines # 实现类似for循环写入
f.readable() # 判断文件是否可读，返回True或False。
f.writable() # 判断文件是否可写，返回True或False。
f.close      # 关闭文件
f.closed     # 文件是否关闭
f.encoding   # 如果文件打开模式为b,则没有该属性
f.flush()    # 立刻将文件内容从内存刷到硬盘
f.name       # 如果使用open()创建文件，则为文件名称，否则，它将是一个表示文件来源的字符串
f.isatty     # 是否是终端设备文件
f.reconfigure # 
f.seek       # 用于移动文件读取指针到指定位置
f.seekable   # 
f.tell       # 返回当前文件指针
f.truncate   # 将文件截断为最多n个字符
f.detach     # 
f.fileno     # 返回文件描述符