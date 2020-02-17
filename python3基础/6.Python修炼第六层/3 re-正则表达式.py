一、简介
什么是正则？
　正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法。或者说：正则就是用来描述一类事物的规则。（在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。
生活中处处都是正则：
    比如我们描述：4条腿
    　　你可能会想到的是四条腿的动物或者桌子，椅子等
    继续描述：4条腿，活的
          就只剩下四条腿的动物这一类了

正则表达式本身是一种小型的、高度专业化的编程语言，而在python中，通过内嵌集成re模块，程序媛们可以直接调用来实现正则匹配。
正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行。

二、常用匹配模式(元字符)
\w  :匹配字母数字及下划线
\W  :匹配非字母数字下划线
\s  :匹配任意空白字符，[\t\n\r\f]都属于空，都可以被\s匹配
\S  :匹配任意非空字符
\d  :匹配任意数字，等价于[0-9]
\D  :匹配任意非数字
\A  :匹配字符串开始
\Z  :匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
\z  :匹配字符串结束
\G  :匹配最后匹配完成的位置
\n  :匹配一个换行符
\t  :匹配一个制表符
^   :匹配字符串的开头
$   :匹配字符串的末尾
.   :匹配任意字符，除换行符，当配合re.DOTALL或者re.S标记使用时，则可以匹配包括换行符的任意字符。
[...]   :用来表示一组字符，单独列出：[amk]匹配'a','m'和'k'
[^...]  :不在[]中的字符：[^abc]匹配除了a，b，b之外的字符
*   :匹配0个或多个的表达式
+   :匹配1个或多个的表达式
?   :匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式。
{n} :精确匹配n个前面表达式
{n,}:必须匹配n次或无穷次前面表达式
{n,m}:匹配n到m次由前面的正则表达式定义的片段，贪婪方式。
a|b :匹配a或b
()  :匹配括号内的表达式，也表示一个组。


import re

print(re.findall('alex','12a3 alex say hello alex sb 123 _ 4%5*6')) # ['alex', 'alex']
                #                            alex
print(re.findall('aaa','12a1aaa')) # ['aaa']
                #          aaa

\w 匹配字母数字及下划线
print(re.findall('\w','alex 123 _ 4%5*')) # ['a', 'l', 'e', 'x', '1', '2', '3', '_', '4', '5']
\W 匹配非字母数字下划线
print(re.findall('\W','alex 123 _ 4%5*')) # [' ', ' ', ' ', '%', '*']

\s 匹配任意空白字符,[\t\n\r\f]都属于空，都可以被\s匹配
print(re.findall('\s','al\te\nx sb 123 _ 4%5*')) # ['\t', '\n', ' ', ' ', ' ', ' ']
\S 匹配任意非空字符
print(re.findall('\S','al\te\nx sb 123 _ 4%5*')) # ['a', 'l', 'e', 'x', 's', 'b', '1', '2', '3', '_', '4', '%', '5', '*']

\d 匹配任意数字，等价于[0-9]。
print(re.findall('\d','al\te\nx hello alex sb 123 _ 4%5*')) # ['1', '2', '3', '4', '5']
\匹配两个连续的两个数字
print(re.findall('\d\d','al\te\nx hel12345lo alex sb 123 _ 4%5*')) # ['12', '34', '12']
\D 匹配任意非数字
print(re.findall('\D','al\te\nx  sb 123 _ 4%5*')) # ['a', 'l', '\t', 'e', '\n', 'x', ' ', ' ', 's', 'b', ' ', ' ', '_', ' ', '%', '*']

\A 匹配字符串开始
print(re.findall('\Al','alex say hello'))   # []
print(re.findall('\Al','lalex lsay hello')) # ['l']
\Z 匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
print(re.findall('llo\Z','alex say hello')) # ['llo']
\匹配字符串的开头,同等\A
print(re.findall('^l','alex say hello')) # []
\匹配字符串的末尾，同等\Z
print(re.findall('llo$','alex say hello')) # ['llo']

\匹配一个换行符
print(re.findall('\n','al\te\nx sb 123 _ 4%5*')) # ['\n']
\匹配一个制表符
print(re.findall('\t','al\te\nx sb 123 _ 4%5*')) # ['\t']


##重复匹配：. ?  *  +  {n,m}  []  () |  .*  .*?  
\.:来匹配任意一个字符，可以写多个点。配合re.S匹配任意非空字符。
print(re.findall('a.c','a1c a%c abc accc acccc'))       # ['a1c', 'a%c', 'abc', 'acc', 'acc']
print(re.findall('a.c','a1c a%c a\nc accc acccc'))      # ['a1c', 'a%c', 'acc', 'acc']
print(re.findall('a.c','a1c a%c a\nc accc acccc',re.S)) # ['a1c', 'a%c', 'a\nc', 'acc', 'acc'] ,re.S或re.DOTALL代表把\n和\t也算作字符来匹配。

\?:左边那个字符出现0次或1次，非贪婪匹配。
print(re.findall('ab?','a ab abb abbb abbbbbb'))     # ['a', 'ab', 'ab', 'ab', 'ab']
print(re.findall('ab{0,1}','a ab abb abbb abbbbbb')) # ['a', 'ab', 'ab', 'ab', 'ab']
print(re.findall('ab{2}','a ab abb abbb abbbbbb'))   # ['abb', 'abb', 'abb']

\*:左边那个字符出现0次或无穷次，贪婪匹配。
print(re.findall('ab*','a ab abb abbb abbbbbb abbc123bbbb'))    # ['a', 'ab', 'abb', 'abbb', 'abbbbbb', 'abb']
print(re.findall('ab{0,}','a ab abb abbb abbbbbb abbc123bbbb')) # ['a', 'ab', 'abb', 'abbb', 'abbbbbb', 'abb']

\+:左边那个字符必须出现1次或无穷次，贪婪匹配。
print(re.findall('ab+','a ab abb abbb abbbbbb abbc123bbbb'))    # ['ab', 'abb', 'abbb', 'abbbbbb', 'abb']
print(re.findall('ab{1,}','a ab abb abbb abbbbbb abbc123bbbb')) # ['ab', 'abb', 'abbb', 'abbbbbb', 'abb']

\{n,m}:左边那个字符出现n到m次,{3,}表示前面的字符必须出现3次或更多次的匹配。
print(re.findall('ab{3}','a ab abb abbb abbbbbb abbc123bbbb'))   # ['abbb', 'abbb']
print(re.findall('ab{3,}','a ab abb abbb abbbbbb abbc123bbbb'))  # ['abbb', 'abbbbbb']
print(re.findall('ab{0,1}','a ab abb abbb abbbbbb abbc123bbbb')) # ['a', 'ab', 'ab', 'ab', 'ab', 'ab']
print(re.findall('ab{0,}','a ab abb abbb abbbbbb abbc123bbbb'))  # ['a', 'ab', 'abb', 'abbb', 'abbbbbb', 'abb']
print(re.findall('ab{1,}','a ab abb abbb abbbbbb abbc123bbbb'))  # ['ab', 'abb', 'abbb', 'abbbbbb', 'abb']

\[]:用来表示一组字符，单独列出：[amk]匹配'a'、'm'或'k'任意一个
print(re.findall('a[0-9]c','a1c a%c a\nc accc acccc',re.S))                # ['a1c']
print(re.findall('a[a-z]c','a1c a%c a\nc accc acccc',re.S))                # ['acc', 'acc']
print(re.findall('a[A-Z]c','a1c a%c a\nc accc acccc aAc aAAc',re.S))       # ['aAc']
print(re.findall('a[0-9a-zA-Z]c','a1c a%c a\nc accc acccc aAc aAAc',re.S)) # ['a1c', 'acc', 'acc', 'aAc']
print(re.findall('^1[35789]\d{9}','18514006261 a%c a\nc accc ac18514006261ccc',re.S)) # ['18514006261'] 匹配手机号

\匹配a%c和a c
print(re.findall('a[% ]c','a c a1c a%c a+c a-c a/c a*c',re.S))  # ['a c', 'a%c']
\[^]:取反
print(re.findall('a[^% ]c','a c a1c a%c a+c a-c a/c a*c',re.S)) # ['a1c', 'a+c', 'a-c', 'a/c', 'a*c']

print(re.findall('a[+\-*/]c','a c a1c a%c a+c a-c a/c a*c',re.S)) # ['a+c', 'a-c', 'a/c', 'a*c'],减号放在中间就成了运算了，所以转义一下。
print(re.findall('a[-+*/]c','a c a1c a%c a+c a-c a/c a*c',re.S))  # ['a+c', 'a-c', 'a/c', 'a*c'],把减号放在最前面也可以避免成为运算
print(re.findall('a[+*/-]c','a c a1c a%c a+c a-c a/c a*c',re.S))  # ['a+c', 'a-c', 'a/c', 'a*c'],或者放最后
print(re.findall('a.*?c','a c a1c a%c a+c a-c a/c a*c',re.S))     # ['a c', 'a1c', 'a%c', 'a+c', 'a-c', 'a/c', 'a*c']

\贪婪匹配: .* 匹配所有字符
print(re.findall('a.*b','a123b456b'))  # 匹配a开头b结尾，找到最右最长的。 ['a123b456b']

\非贪婪匹配: .*? 
print(re.findall('a.*?b','a123b456b')) # 匹配a开头b结尾，找到第一个就停止了。['a123b']

\分组: () ,匹配以<imag href=\"开头，以/>结尾的，两者中间的字符取出来。
# 用分组取出图片的url，保留的是组内的内容。
print(re.findall('<imag href=\"(.*)\" />',
                 '<h1>hello</h1><a href="http://www.baidu.com"></a><imag href="http://www.baidu.com/a.jpg" />')) # ['http://www.baidu.com/a.jpg']
# 不使用分组，取出整个匹配内容。
print(re.findall('<imag href=\"(?:.*)\" />',
                 '<h1>hello</h1><a href="http://www.baidu.com"></a><imag href="http://www.baidu.com/a.jpg" />')) # ['<imag href="http://www.baidu.com/a.jpg" />']

\ |: 或者的意思
# 前面固定匹配，后面要么ies或者是y，然后结合?:取出所有。不单单取分组内的内容。
print(re.findall('compan(?:ies|y)','Too many companies have gone bankrupt, and the next one is my company')) # ['companies', 'company']

\r: 告诉python解释器，这是原生字符串，不需要转义。
print(re.findall('a\\\\c','a\c a12 a2c'))  # ['a\\c']，python结束起需要使用一层转义，所有需要多加一份转义。
print(re.findall(r'a\\c','a\c a12 a2c'))   # ['a\\c'],用r声明字符串中的内容都是原生字符串，原生表示字符串中的所有特殊字符没有任何意义。



\===========================re模块提供的方法介绍===========================
\findall 从头找到尾
# re.findall(pattern, string, flags=0) 找到RE匹配的所有字符串，并把他们作为一个列表返回
print(re.findall('alex','alex say hello alex')) # ['alex', 'alex']

\search与findall用法完全一致，不一样的地方在于search匹配一次就结束。
# re.search(pattern, string, flags=0) 扫描整个字符串并返回第一个成功的匹配
只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。
print(re.search('alex','alex say hello alex').group()) # alex

\match代表从头匹配,同search,不过在字符串开始处进行匹配,完全可以用search+^代替match
# re.match(pattern, string, flags=0) 从字符串的起始位置匹配，如果起始位置匹配不成功的话，match()就返回none
print(re.match('alex','alex say hello alex').group())   # alex,匹配不成功返回None
print(re.search('^alex','alex say hello alex').group()) # alex

\re.split() 切割
print(re.split(':','root:x:0:0:/root::/bin/bash')) # ['root', 'x', '0', '0', '/root', '', '/bin/bash']
print(re.split('[ab]','abcd'))     #['', '', 'cd']，先按'a'分割得到''和'bcd',再对''和'bcd'分别按'b'分割

\re.sub() 替换,数字1表示只替换一次，后面再有也不替换了。
# re.sub(pattern, repl, string, count=0, flags=0) 替换匹配到的字符串
print(re.sub('alex','SB','alex say i have one telsa my name is alex',1))  # SB say i have one telsa my name is alex，不指定n，默认替换所有
\替换位置
# 将alex和SB替换位置
print(re.sub(r'(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','alex-love: SB')) # SB-love: alex
                                                        #  1 2  3  4 5
print(re.sub(r'^al',r'AAAAAAAAA','alex-love: SB alex')) # AAAAAAAAAex-love: SB alex

\re.subn() ，替换并统计替换次数
print(re.subn('alex','SB','alex say i have one telsa my name is alex')) # ('SB say i have one telsa my name is SB', 2)

\re.compile() 
print(re.findall('^alex','alex say hello alex'))        # ['alex']
print(re.search('^alex','alex say hello alex').group()) # alex
\正则表达式重用
obj=re.compile(r'^alex')
print(obj.findall('alex say hello alex'))        # ['alex']
print(obj.search('alex say hello alex').group()) # alex

\re.finditer()
# re.finditer(pattern, string, flags=0) 找到RE匹配的所有字符串，并把他们作为一个迭代器返回
pattern = re.compile(r"\d+")
p = pattern.finditer("abc1def2rst3xyz")
for i in p:
    print(i.group())
# 输出结果：
1
2
3

函数参数说明：
pattern:匹配的正则表达式
string：要匹配的字符串
flags：标记为，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
repl：替换的字符串，也可作为一个函数
count：模式匹配后替换的最大次数，默认0表示替换所有匹配

\补充：
#补充二
import re

#使用|，先匹配的先生效，|左边是匹配小数，而findall最终结果是查看分组，所有即使匹配成功小数也不会存入结果

#而不是小数时，就去匹配(-?\d+)，匹配到的自然就是，非小数的数，在此处即整数
print(re.findall(r"-?\d+\.\d*|(-?\d+)","1-2*(60+(-40.35/5)-(-4*3))")) #找出所有整数['1', '-2', '60', '', '5', '-4', '3']
# r"-?\d+\.\d*|(-?\d+)" | 左边不成立才会匹配右边

#找到所有数字:
print(re.findall('\D?(\-?\d+\.?\d*)',"1-2*(60+(-40.35/5)-(-4*3))")) # ['1','2','60','-40.35','5','-4','3']

#计算器作业参考：http://www.cnblogs.com/wupeiqi/articles/4949995.html
expression='1-2*((60+2*(-3-40.35/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
content=re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)',expression).group() #(-3-40.35/5),先算括号里的，在算乘除后算加减。每次匹配时中间不能有括号，匹配完一次计算出结果后替换进去再匹配再计算。


#为何同样的表达式search与findall却有不同结果:
print(re.search('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))").group()) #(-40.35/5)
print(re.findall('\(([\+\-\*\/]*\d+\.?\d*)+\)',"1-12*(60+(-40.35/5)-(-4*3))"))        #['/5', '*3']

#看这个例子:(\d)+相当于(\d)(\d)(\d)(\d)...,是一系列分组
print(re.search('(\d)+','123').group()) # 123    group的作用是将所有组拼接到一起显示出来
print(re.findall('(\d)+','123'))        # ['3']  findall结果是组内的结果,且是最后一个组的结果

print(re.findall(r'<.*?>.*?</.*?>','<h1>hello</h1>'))           # ['<h1>hello</h1>']
print(re.findall(r'<(.*?)>.*?</(.*?)>','<h1>hello</h1>'))       # [('h1', 'h1')]  取分组内的字符
print(re.findall(r'<(.*?)>.*?</(\1)>','<h1>hello</h1>'))        # [('h1', 'h1')]  第二个分组(.*?)重用第一个分组的代码直接使用\1即可
print(re.findall(r'<(?P<k>.*?)>.*?</(?P=k)>','<h1>hello</h1>')) # ['h1']    将第一个匹配到的结果赋值给k，后面直接用k


#取数字
print(re.findall('\-?\d+\.?\d*',"1-12*(60+(-40.35/5)-(-4*3))"))

print(re.findall('\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))
print(re.findall('\-?\d+\.\d+',"1-12*(60+(-40.35/5)-(-4*3))"))

#取整数
print(re.findall('\-?\d+\.\d+|(\-?\d+)',"1-12*(60+(-40.35/5)-(-4*3))"))
print(re.findall('(\-?\d+\.\d+)|\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))


作业
# expression='1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
# print(re.search(r'\(([-+*/]?\d+\.?\d*)+\)',expression).group())
# print(eval(expression))

\视图代码
# 在线正则表达式测试:tool.oschina.net/regex/#
import re

\re模块 re.compile、re.match、 re.search :推荐使用 re.match
正则匹配的时候，第一个字符是 r，表示 raw string 原生字符，意在声明字符串中间的特殊字符不用转义。
比如表示 ‘\n'，可以写 r'\n'，或者不适用原生字符 ‘\n'。

\re.compile() 函数
编译正则表达式模式，返回一个对象。可以把常用的正则表达式编译成正则表达式对象，方便后续调用及提高效率。
# re.compile(pattern, flags=0)
    # pattern 指定编译时的表达式字符串
    # flags 编译标志位，用来修改正则表达式的匹配方式。支持 re.L|re.M 同时匹配
    # flags 标志位参数

re.I(re.IGNORECASE)
使匹配对大小写不敏感

re.L(re.LOCAL) 
做本地化识别（locale-aware）匹配

re.M(re.MULTILINE) 
多行匹配，影响 ^ 和 $

re.S(re.DOTALL)
使 . 匹配包括换行在内的所有字符

re.U(re.UNICODE)
根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.

re.X(re.VERBOSE)
该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

示例：
import re
content = 'Citizen wang , always fall in love with neighbour，WANG'
rr = re.compile(r'wan\w', re.I) # 不区分大小写
print(type(rr))
a = rr.findall(content)
print(type(a))
print(a)

# findall 返回的是一个 list 对象
<class '_sre.SRE_Pattern'>
<class 'list'>
['wang', 'WANG']

\re.match : 总是从字符串‘开头去匹配'，并返回匹配的字符串的 match 对象 <class '_sre.SRE_Match'>。
# re.match(pattern, string[, flags=0])
    # pattern 匹配模式，由 re.compile 获得
    # string 需要匹配的字符串

例如：
pattern = re.compile(r'hello')
a = re.match(pattern, 'hello world')
b = re.match(pattern, 'world hello')
c = re.match(pattern, 'hell')
d = re.match(pattern, 'hello ')
if a:
  print(a.group())
else:
  print('a 失败')
if b:
  print(b.group())
else:
  print('b 失败')
if c:
  print(c.group())
else:
  print('c 失败')
if d:
  print(d.group())
else:
  print('d 失败')
'''
hello
b 失败
c 失败
hello
'''

#最常规匹配
content='Hello 123 456 World_This is a Regex Demo'
res=re.match('Hello\s\d\d\d\s\d{3}\s\w{10}.*Demo',content)
print(res)
print(res.group()) # 使用group可以取到结果
print(res.span())
'''
<re.Match object; span=(0, 40), match='Hello 123 456 World_This is a Regex Demo'>
Hello 123 456 World_This is a Regex Demo
(0, 40)
'''

#泛匹配
content='Hello 123 456 World_This is a Regex Demo'
res=re.match('^Hello.*Demo',content)
print(res.group())
'''
Hello 123 456 World_This is a Regex Demo
'''

#匹配目标,获得指定数据
content='Hello 123 456 World_This is a Regex Demo'
res=re.match('^Hello\s(\d+)\s(\d+)\s.*Demo',content)
print(res.group()) #取所有匹配的内容
print(res.group(1)) #取匹配的第一个括号内的内容
print(res.group(2)) #取匹配的第二个括号内的内容
'''
Hello 123 456 World_This is a Regex Demo
123
456
'''

#贪婪匹配:.*代表匹配尽可能多的字符
content='Hello 123 456 World_This is a Regex Demo'
res=re.match('^He.*(\d+).*Demo$',content)
print(res.group(1)) #只打印6,因为.*会尽可能多的匹配,然后后面跟至少一个数字


#非贪婪匹配:?匹配尽可能少的字符
content='Hello 123 456 World_This is a Regex Demo'
res=re.match('^He.*?(\d+).*Demo$',content)
print(res.group(1)) #123,因为.*?找到第一个连续数字就停止了


#匹配模式:.不能匹配换行符
content='''Hello 123456 World_This
is a Regex Demo
'''
res=re.match('He.*?(\d+).*?Demo$',content)
print(res) # 输出None

res=re.match('He.*?(\d+).*?Demo$',content,re.S) #re.S让.可以匹配换行符
print(res)
print(res.group(1))
'''
<re.Match object; span=(0, 39), match='Hello 123456 World_This\nis a Regex Demo'>
123456
'''
# match 的方法和属性
str = 'hello world! hello python'
pattern = re.compile(r'(?P<first>hell\w)(?P<symbol>\s)(?P<last>.*ld!)') # 分组，0 组是整个 hello world!, 1组 hello，2组 ld!
match = re.match(pattern, str)
print('group 0:', match.group(0)) # 匹配 0 组，整个字符串
print('group 1:', match.group(1)) # 匹配第一组，hello
print('group 2:', match.group(2)) # 匹配第二组，空格
print('group 3:', match.group(3)) # 匹配第三组，world!
print('groups:', match.groups())  # groups 方法，返回一个包含所有分组匹配的元组
print('start 0:', match.start(0), 'end 0:', match.end(0)) # 整个匹配开始和结束的索引值
print('start 1:', match.start(1), 'end 1:', match.end(1)) # 第一组开始和结束的索引值
print('start 2:', match.start(1), 'end 2:', match.end(2)) # 第二组开始和结束的索引值
print('pos 开始于：', match.pos)
print('endpos 结束于：', match.endpos) # string 的长度
print('lastgroup 最后一个被捕获的分组的名字：', match.lastgroup)
print('lastindex 最后一个分组在文本中的索引：', match.lastindex)
print('string 匹配时候使用的文本：', match.string)
print('re 匹配时候使用的 Pattern 对象：', match.re)
print('span 返回分组匹配的 index （start(group),end(group))：', match.span(2))
'''
group 0: hello world!
group 1: hello
group 2: 
group 3: world!
groups: ('hello', ' ', 'world!')
start 0: 0 end 0: 12
start 1: 0 end 1: 5
start 2: 0 end 2: 6
pos 开始于： 0
endpos 结束于： 25
lastgroup 最后一个被捕获的分组的名字： last
lastindex 最后一个分组在文本中的索引： 3
string 匹配时候使用的文本： hello world! hello python
re 匹配时候使用的 Pattern 对象： re.compile('(?P<first>hell\\w)(?P<symbol>\\s)(?P<last>.*ld!)')
span 返回分组匹配的 index （start(group),end(group))： (5, 6)
'''
\re.search 函数 :对整个字符串进行搜索匹配，返回第一个匹配的字符串的 match 对象。
# re.search(pattern, string[, flags=0])
#     pattern 匹配模式，由 re.compile 获得
#     string 需要匹配的字符串
str = 'say hello world! hello python'
pattern = re.compile(r'(?P<first>hell\w)(?P<symbol>\s)(?P<last>.*ld!)') # 分组，0 组是整个 hello world!, 1组 hello，2组 ld!
search = re.search(pattern, str)
print('group 0:', search.group(0)) # 匹配 0 组，整个字符串
print('group 1:', search.group(1)) # 匹配第一组，hello
print('group 2:', search.group(2)) # 匹配第二组，空格
print('group 3:', search.group(3)) # 匹配第三组，world!
print('groups:', search.groups())  # groups 方法，返回一个包含所有分组匹配的元组
print('start 0:', search.start(0), 'end 0:', search.end(0)) # 整个匹配开始和结束的索引值
print('start 1:', search.start(1), 'end 1:', search.end(1)) # 第一组开始和结束的索引值
print('start 2:', search.start(1), 'end 2:', search.end(2)) # 第二组开始和结束的索引值
print('pos 开始于：', search.pos)
print('endpos 结束于：', search.endpos) # string 的长度
print('lastgroup 最后一个被捕获的分组的名字：', search.lastgroup)
print('lastindex 最后一个分组在文本中的索引：', search.lastindex)
print('string 匹配时候使用的文本：', search.string)
print('re 匹配时候使用的 Pattern 对象：', search.re)
print('span 返回分组匹配的 index （start(group),end(group))：', search.span(2))
'''
group 0: hello world!
group 1: hello
group 2: 
group 3: world!
groups: ('hello', ' ', 'world!')
start 0: 4 end 0: 16
start 1: 4 end 1: 9
start 2: 4 end 2: 10
pos 开始于： 0
endpos 结束于： 29
lastgroup 最后一个被捕获的分组的名字： last
lastindex 最后一个分组在文本中的索引： 3
string 匹配时候使用的文本： say hello world! hello python
re 匹配时候使用的 Pattern 对象： re.compile('(?P<first>hell\\w)(?P<symbol>\\s)(?P<last>.*ld!)')
span 返回分组匹配的 index （start(group),end(group))： (9, 10)
'''

#转义:\

# content='price is $5.00'
# res=re.match('price is $5.00',content)
# print(res)
#
# res=re.match('price is \$5\.00',content)
# print(res)


#总结:尽量精简,详细的如下
    # 尽量使用泛匹配模式.*
    # 尽量使用非贪婪模式:.*?
    # 使用括号得到匹配目标:用group(n)去取得结果
    # 有换行符就用re.S:修改模式



