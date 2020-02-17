\1. 文件操作
# open 打开
f = open(文件路径, mode="模式", encoding="编码格式")  # 最最底层操作的就是bytes,打开一个文件的时候获取到的是一个文件句柄.
# 绝对路径:从磁盘根目录开始寻找
# 相对路径:相对于当前程序所在的文件夹

f= open("D:\西游记\金角大王吧.txt", mode="r", encoding="gbk")
print(f.read())
f.close()

\2. mode:

\r: 读取,只读.
读取文件的相关操作
1. read()
    默认: 读取文件内容(全部)
    read(n) 读取n个字符
2. readline() 读取一行
3. readlines() 读取全部. 返回列表
4. for line in f: 每次读取一行内容(最重要)

f = open("moder.txt", mode="r", encoding="utf-8")
print(f.read(5))  # 读取5个字符
print(f.read(5))  # 继续读5个
print(f.readline().strip())  # 换行符为分割,strip()可以去掉换行. 读取到的内容第一件事就是去掉空白
print(f.readline())
f.close()
print(f.readlines()) # 一次性把文件中的内容读取到列表中,注意是列表

#文件句柄是一个可迭代对象
#优点:相对来说节省内存,操作相对简单一点
for line in f:  # 从文件中读取到每一行给前面的line
    print(line.strip())
f.close()


\w:写入. 只写、创建文件、会清空文件
# 每次用w模式打开文件,都会清空这个文件(坑)
f = open('胡辣汤', mode='w', encoding="utf-8")  # 可以帮我们创建文件

f.write('河南特色\n')
f.write("东北特色\n")
f.write("陕西特色\n")
# 好习惯
f.flush()  # 刷新管道, 把数据写入文件
f.close()

\a:也可以创建文件、追加写
f = open("葫芦小金刚", mode="a", encoding="utf-8") # a, append 追加, 在文件末尾写入内容
f.write("你叫什么名字阿?")
# f.read() # not readable
f.flush()
f.close()

\r+: 对于文件而言. 应该有的操作就两个:读, 写
读写操作
f = open("葫芦小金刚", mode="r+", encoding="utf-8")
content = f.read()  # 顺序必须先读,后写
# r+特有的深坑:不论读取内容的是多少,只要你读了.写就是在末尾
f.write('五娃')
print(content)

\w+: 写读操作
# 一上来会清空文件, 没人用
f = open("葫芦小金刚", mode="w+", encoding="utf-8")
content = f.read()  # 顺序必须先读,后写
# r+特有的深坑:不论读取内容的是多少,只要你读了.写就是在末尾
f.write('五娃')
f.write("有能吐火的, 有能吐水的")
# 移动光标
f.seek(0)  # 移动到开头
s = f.read()
print("========>", s)

\a+: 追加写读
所有带b的表示直接操作的是bytes, 当处理非文本文件的时候.

# 追加写读, 光标在末尾. 所有的写都是在末尾
f = open("葫芦小金刚", mode="a+", encoding="utf-8")
f.write("机械葫芦娃召唤神龙, 高喊. 我代表月亮消灭你!")
f.seek(0)
s =f.read()
print("=====>", s)
rb
wb

ab: 断点续传

r+b
w+b
a+b


\3.文件复制
f1 = open("E:/1.png", mode="rb")

f2 = open("D:/1.png", mode="wb")

for line in f1:  # line是从f1中读取的内容
    f2.write(line)  # 把读取的内容原封不动的写出去

f1.close()
f2.flush()
f2.close()


\4.seek和tell
f = open("胡辣汤", mode="r+", encoding="utf-8")
f.seek(0, 2)  # 移动到末尾
# content = f.read()
# print(content)
# f.seek(0)  # 移动到开头
# print(f.read())
# print(f.tell())  # 字节

f.seek(3)
print(f.read())


\5.文件修改
f1 = open("夸一夸alex", mode="r", encoding="utf-8")
f2 = open("夸一夸alex_副本", mode="w", encoding="utf-8")

for line in f1:
    if "好人" in line:
        line = line.replace("好人", "sb")
    f2.write(line)
f1.close()
f2.flush()
f2.close()
os.remove("夸一夸alex")
os.rename("夸一夸alex_副本", "夸一夸alex")


with open("夸一夸alex", mode="r", encoding="utf-8") as f, \
        open("夸一夸alex_副本", mode="w", encoding="utf-8") as  f2:
    for line in f:
        if "好人" in line:
            line = line.replace("好人", "sb")
        f2.write(line)

os.remove("夸一夸alex")
os.rename("夸一夸alex_副本", "夸一夸alex")