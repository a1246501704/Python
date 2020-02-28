# 作用：名字，性别，国籍，地址等描述信息
# 定义：在单引号\双引号\三引号内，由一串字符组成、不可变

name='egon' # name=str('egon')
print(id(name),type(name),name)

\优先掌握的操作：
1、按索引取值(正向取+反向取) ：只能取
2、切片(顾头不顾尾，步长)
3、长度len
4、成员运算in和not in
5、移除空白strip
6、切分split
7、循环

\按索引取值(正向取+反向取) ：只能取
print(name[0],type(name[0])) # e <class 'str'>
print(name[-2])
name[0]='E'  # 不能按字符串索引赋值

\切片(使用索引切片，顾头不顾尾，可以指定步长)
print(name[1:3]) # go
msg='hello world'
print(msg[1:7])   # ello w
print(msg[1:7:2]) # el ，步长为2,取头

msg='abcdefg' 
print(msg[1:6:2]) # bdf
print(msg[:])     # abcdefg,冒号左边是起始右边是结束
print(msg[::2])   # acdf，从头开始到最后结束，步长为2。
print(msg[6::-1]) # gfedcba，6是起始位置。意思是从6的位置倒着往前取，步为1。

\长度len，注意：数字没有长度。
msg='ab c '
print(len(msg)) # 5

\成员运算: in和not in，对应上连续的才会返回True，否则返回False。
msg='hello alex'
print('a' in msg)      # True
print('alex' in msg)   # True
print('ae' not in msg) # False

\移除空白: strip、lstrip、rstip
password='   alex3714        '  # 去除前后空格
password=password.strip()
print(password)
print(password.strip())        # 简便写法

msg='***egon***********'        # 去除前后*字符
print(msg.strip('*'))

msg='***eg**on***********'      # 中间的去不掉，也不能去掉。属于用户输入的内容。
print(msg.strip('*'))

print(name.lstrip('*'))         # 去除左边的*
print(name.rstrip('*'))         # 去除右边的*

\切分: split、rsplit、partition
user_info='root:x:0:0::/root:/bin/bash'
print(user_info[0:4])             # 用切片不合适，如果过长无法获取。
print(user_info.split(':'))       # 以冒号切分，切分成列表。
print(user_info.split(':')[0])    # 以冒号切分，切分成列表,取第0个值。默认以空格切分。
print(user_info.split(':',1))     # 以冒号切分，切分成列表。切分次数1次,['root', 'x:0:0::/root:/bin/bash']
# 连续多次切分
cmd='put       a.txt' 
print(cmd.split())     # ['put','a.txt'],默认以空格切分,不管中间有多少个空格。
print(cmd.split(' '))  # 这个意思是以空字符串切分，并不是空格的意思。['put', '', '', '', '', '', '', 'a.txt']

filepath='put /a/b/c/d/a.txt'
print(filepath.split()) # ['put','/a/b/c/d/a.txt']

msg='alex say i have on tesla'
print(msg.split(maxsplit=1)[0])  # maxsplit指定最大切分几次，切1次取第0个值。

filepath='/a/b/c/d/a.txt'
print(filepath.rsplit('/',1))    # 从右开始切分,['/a/b/c/d', 'a.txt']
name='a|b|c'
print(name.rsplit('|',1))        # 从右开始切分,['a|b', 'c']

str = "http://www.w3cschool.cc/"
print(str.rpartition("www"))     # 用来根据指定的分隔符将字符串进行分割。('http://', 'www', '.w3cschool.cc/')
print(str.partition("www"))      # 结果一样，('http://', 'www', '.w3cschool.cc/')

\列表转成字符串: join   
# 可迭代对象必须都是字符串
user_info='root:x:0:0::/root:/bin/bash'
l=user_info.split(':') # 切分后是个列表,['root', 'x', '0', '0', '', '/root', '/bin/bash']
print(':'.join(l))     # 用join再还原回字符串的形式,root:x:0:0::/root:/bin/bash
print(''.join(l))      # rootx00/root/bin/bash
print(' '.join(l))     # root x 0 0  /root /bin/bash

tag=' '
print(tag.join(['egon','say','hello','world']))  # egon say hello world

l=[]
l.append("sum(case when visit_date = 1 then cnt end) as 2")
l1=', '.join(l)
print(l1)
print(type(l1))

\isdigit: 用来判断字符串str是否由纯数字组成（bytes，unicode）
# 可以判断bytes和unicode类型,是最常用的用于于判断字符是否为"数字"的方法
age=input('>>: ')
print(age.isdigit())

\匹配开头和结尾: startswith,endswith
msg='alex_SB'
print(msg.startswith('alex')) # True
print(msg.endswith('SB'))     # True

\替换: replace
msg='alex say i have one telsa, my name is alex'
print(msg.replace('alex','SB'))   # 全部替换，会得到一个新的字符串并不改变原来的值。
print(msg.replace('alex','SB',1)) # 替换次数
k8s_deploy_yaml.replace('app: {}'.format(old_namespace),'app: {}'.format(new_namespace))
k8s_deploy_yaml.replace(('app: %s' %old_namespace),('app: %s' %new_namespace))

\字符串格式化: format
print('my name is %s my age is %s' %('egon',18))
print('my name is {} my age is {}'.format('egon',18))
print('my age is {1},{0} age is {1} too'.format('egon',18))
# 上面传值是按照索引位置传的，下面的方法就可以打破位置关系，类似于字典的形式。
print('my name is {x} my age is {y}'.format(y=18,x='egon'))


\字符串填充: center,ljust,rjust,zfill
=================egon===================
print('egon'.center(30,'='))  # 宽度30，其余的用=号填充。
print('egon'.rjust(30,'='))   # 右对齐，不够用=号填充。
print('egon'.ljust(30,'='))   # 左对齐，不够用=号填充。
print('egon'.zfill(30))       # 用0填充
'''
=============egon=============
==========================egon
egon==========================
00000000000000000000000000egon
'''

\查找字符串索引起始位置、计数。count、find、rfind、index、rindex
msg='hello world'
print(msg.find('ell'))         # 从左到右找，如果有，则返回第一个字符的索引起始位置
print(msg.find('l',0,3))       # 顾头不顾尾,从左到右找，指定查找范围，如果有l，返回第一个字符的索引，没有返回-1.
print(msg.find('easdfasdf'))   # 从左到右找，如果没有，返回-1

print(msg.index('d',0,3))      # 从左到右找，如果有，则返回第一个字符的索引。
print(msg.index('x'))          # 从左到右找，如果没有，会报错。和find对比，find会更好一些。

print(msg.count('l',0,4))      # 查找l出现的次数。顾头不顾尾,如果不指定范围则查找所有。
print(msg.count('l',0,3))

\制表符: \t、expandtabs
msg='abc\tdeft'
print(msg.expandtabs(3)) # abc   deft, 控制制表符\t宽度为3。

\capitalize、upper、lower、title、swapcase 大小写转换:
msg='alex Say hello'
print(msg.capitalize())  # 首字母大些
print(msg.upper())       # 全部大些
print(msg.lower())       # 全部变小写
print(msg.title())       # 每个单词首字母大些
print(msg.swapcase())    # 大小写反转。用于对字符串的大小写字母进行转换,返回大小写字母转换后生成的新字符串。

\is系列-判断字符串，返回True或False。
# msg='Alex Say Hello'
print(msg.isupper())  # 判断字符串是否全部大写
print(msg.islower())  # 判断字符串是否全部小写
print(msg.istitle())  # 判断字符串每个字符首字母是否大些
print(name.isspace()) # 判断字符串是否全部是空格
print(name.isidentifier()) # 判断字符串中是否有python关键字
print(name.isalpha()) # 判断字符串只由字母组成
print(name.isalnum()) # 判断字符串由字母或数字组成

\is数字系列-判断数字
#在python3中
num1=b'4' # bytes
num2=u'4' # unicode,python3中无需加u就是unicode
num3='四' # 中文数字
num4='Ⅳ' # 罗马数字
num5='壹'

\判断数字: isdigt、isdecimal、isnumberic
age=10
inp=input('>>: ').strip()
if inp.isdigit():
    inp=int(inp)
    if inp > age:
        print('ok')
else:
    print('必须输入数字')

isdigt: bytes,unicode # 判断字符串是否由纯数字组成
print(num1.isdigit()) #True
print(num2.isdigit()) #True
print(num3.isdigit()) #False
print(num4.isdigit()) #False
print(num5.isdigit()) #False

isdecimal: uncicode 
# bytes类型无isdecimal方法
print(num2.isdecimal()) #True
print(num3.isdecimal()) #False
print(num4.isdecimal()) #False
print(num5.isdecimal()) #False

isnumberic: unicode,中文数字,罗马数字、汉字数字
# bytes类型无isnumberic方法
print(num2.isnumeric()) #True
print(num3.isnumeric()) #True
print(num4.isnumeric()) #True
print(num5.isnumeric()) #True

# 三者不能判断浮点数
num5='4.3'
print(num5.isdigit())   #False
print(num5.isdecimal()) #False
print(num5.isnumeric()) #False
'''
总结:
    最常用的是isdigit,可以判断bytes和unicode类型,这也是最常见的数字应用场景
    如果要判断中文数字或罗马数字,则需要用到isnumeric
'''

\其他方法
user_info.splitlines # 按\n切分成列表
# 默认splitelines参数keepends为False，意思是不保留每行结尾的\n, 而keepends为True时，分割的每一行里尾部会有\n。
u = "www.jeapedu.com\nwww.chinagame.me\nwww.quanzhan.org"
print(u.splitlines())
['www.jeapedu.com', 'www.chinagame.me', 'www.quanzhan.org'] # splitlines是按行分割字符串，返回值也是个列表。


\字符串方法

count(sub[, start[, end]])	  # 返回 sub 在字符串里边出现的次数，start 和 end 参数表示范围，可选。
join(sub)	                  # 以字符串作为分隔符，插入到 sub 中所有的字符之间。
expandtabs([tabsize=8])	      # 把字符串中的 tab 符号（\t）转换为空格，如不指定参数，默认的空格数是 tabsize=8。
encode(encoding=’utf-8’, errors=’strict’)	# 以 encoding 指定的编码格式对字符串进行编码。

# 字符串大小写反转
capitalize() # 把字符串的第一个字符改为大写。
casefold()	 # 把整个字符串的所有字符改为小写。
lower()	     # 转换字符串中所有大写字符为小写。
swapcase()	 # 翻转字符串中的大小写。
title()	     # 返回标题化（所有的单词都是以大写开始，其余字母均小写）的字符串。
upper()	     # 转换字符串中的所有小写字符为大写。

# 移除空白
strip([chars])	# 删除字符串前边和后边所有的空格，chars 参数可以定制删除的字符，可选。
lstrip()	    # 去掉字符串左边的所有空格。
rstrip()	    # 删除字符串末尾的空格。

# 字符串填充
center(width)# 将字符串居中，并使用空格填充至长度 width 的新字符串。
rjust(width) # 返回一个右对齐的字符串，并使用空格填充至长度为 width 的新字符串。
ljust(width) # 返回一个左对齐的字符串，并使用空格填充至长度为 width 的新字符串。
zfill(width) # 返回长度为 width 的字符串，原字符串右对齐，前边用 0 填充。

# 字符串判断
isalnum()	 # 如果字符串至少有一个字符并且所有字符都是字母或数字则返回 True，否则返回 False。
isalpha()	 # 如果字符串至少有一个字符并且所有字符都是字母则返回 True，否则返回 False。
isdecimal()	 # 如果字符串只包含十进制数字则返回 True，否则返回 False。
isdigit()	 # 如果字符串只包含数字则返回 True，否则返回 False。
islower()	 # 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回 True，否则返回 False。
isnumeric()	 # 如果字符串中只包含数字字符，则返回 True，否则返回 False。
isspace()	 # 如果字符串中只包含空格，则返回 True，否则返回 False。
istitle()	 # 如果字符串是标题化（所有的单词都是以大写开始，其余字母均小写），则返回 True，否则返回 False。
isupper()	 # 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回 True，否则返回 False。

# 字符串查找
find(sub[, start[, end]])	# 检测 sub 是否包含在字符串中，如果有则返回索引值，否则返回 -1，start 和 end 参数表示范围，可选。
rfind(sub[, start[, end]])	# 类似于 find() 方法，不过是从右边开始查找。
index(sub[, start[, end]])	# 跟 find 方法一样，不过如果 sub 不在 string 中会产生一个异常。
rindex(sub[, start[, end]])	# 类似于 index() 方法，不过是从右边开始。
partition(sub)	# 找到子字符串 sub，把字符串分成一个 3 元组 (pre_sub, sub, fol_sub)，如果字符串中不包含 sub 则返回 (‘原字符串’, ”, ”)
rpartition(sub)	# 类似于 partition() 方法，不过是从右边开始查找。
endswith(sub[, start[, end]])       # 检查字符串是否以 sub 子字符串结束，如果是返回 True，否则返回 False。start 和 end 参数表示范围，可选。
startswith(prefix[, start[, end]])	# 检查字符串是否以 prefix 开头，是则返回 True，否则返回 False。start 和 end 参数可以指定范围检查，可选。

# 字符串替换
replace(old, new[, count])	# 把字符串中的 old 子字符串替换成 new 子字符串，如果 count 指定，则替换不超过 count 次。
translate(table)            # 根据 table 的规则（可以由 str.maketrans(‘a’, ‘b’) 定制）转换字符串中的字符。把a用b替换掉。

# 字符串切分
split(sep=None, maxsplit=-1)# 不带参数默认是以空格为分隔符切片字符串，如果 maxsplit 参数有设置，则仅分隔 maxsplit 个子字符串，返回切片后的子字符串拼接的列表。
splitlines(([keepends]))	# 在输出结果里是否去掉换行符，默认为 False，不包含换行符；如果为 True，则保留换行符。







