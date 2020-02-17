import re

'''
海峰老师常用模块博客
http://www.cnblogs.com/linhaifeng/articles/6384466.html#_label13

一：什么是正则？

　正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）来描述字符或者字符串的方法。或者说：正则就是用来描述一类事物的规则。（在Python中）它内嵌在Python中，并通过 re 模块实现。正则表达式模式被编译成一系列的字节码，然后由用 C 编写的匹配引擎执行。
生活中处处都是正则：
    比如我们描述：4条腿
    　　你可能会想到的是四条腿的动物或者桌子，椅子等
    继续描述：4条腿，活的
          就只剩下四条腿的动物这一类了

二：常用匹配模式(元字符)
http://images2015.cnblogs.com/blog/1036857/201705/1036857-20170529203214461-666088398.png

http://blog.csdn.net/yufenghyc/article/details/51078107

re正则模块
模式     描述
\w       匹配字母数字及下划线
\W       匹配非字母数字及下划线
\s       匹配任意空白字符，等价于[\t\n\r\f]
         [\t\n\r\f]  \t一个制表符(几个空格)  \n换行  \r回到行首 \f空
\S       匹配任意非空字符
\d       匹配任意数字，等价于[0-9]
\D       匹配任意非数字
\A       匹配字符串开始
\Z       匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串
\z       匹配字符串结束
\G       匹配最后匹配完成的位置
\n       匹配一个换行符
\t       匹配一个制表符
^        匹配字符串的开头
$        匹配字符串的末尾
.        匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[...]    用来表示一组字符，单独列出：[amk]匹配'a','m'或'k'
[^...]   不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*        匹配0个或多个的表达式
+        匹配1个或多个的表达式
?        匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}      精准匹配n个前面表达式
{n,m}    匹配n到m次由前面的正则表达式定义的片段，贪婪方式
a|b      匹配a或b
()       匹配括号内的表达式，也表示一个组



'''



import re

# print(re.findall('\w','hello_ | egon 123'))
# print(re.findall('\W','hello_ | egon 123'))
# print(re.findall('\s','hello_ | egon 123 \n \t'))
# print(re.findall('\S','hello_ | egon 123 \n \t'))
# print(re.findall('\d','hello_ | egon 123 \n \t'))
# print(re.findall('\D','hello_ | egon 123 \n \t'))
# print(re.findall('h','hello_ | hello h egon 123 \n \t'))
# # print(re.findall('\Ahe','hello_ | hello h egon 123 \n \t'))
# print(re.findall('^he','hello_ | hello h egon 123 \n \t'))
# # print(re.findall('123\Z','hello_ | hello h egon 123 \n \t123'))
# print(re.findall('123$','hello_ | hello h egon 123 \n \t123'))
# print(re.findall('\n','hello_ | hello h egon 123 \n \t123'))
# print(re.findall('\t','hello_ | hello h egon 123 \n \t123'))


# . [] [^]

#.本身代表任意一个字符
# print(re.findall('a.c','a a1c a*c a2c abc a c aaaaaac aacc'))
#                       #   a.c a.c a.c a.c a.c     a.c a.c
#
# print(re.findall('a.c','a a1c a*c a2c abc a\nc'))
# print(re.findall('a.c','a a1c a*c a2c abc a\nc',re.DOTALL))
# print(re.findall('a.c','a a1c a*c a2c abc a\nc',re.S))

# []内部可以有多个字符，但本身只配多个字符中的一个
# print(re.findall('a[1 23]c','a a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[1\n23]c','a a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[0-9][0-9]c','a a12c a*c a2c a c a\nc',re.S))
# print(re.findall('a[a-zA-Z]c','aac abc aAc a12c a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[^a-zA-Z]c','aac abc aAc a12c a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[\+\/\*\-]c','a-c a+c a/c aac abc aAc a12c a*c a2c a c a\nc',re.S))

# \:转义
# print(re.findall('a\\\\c','a\c abc'))
# print(re.findall(r'a\\c','a\c abc')) #rawstring  原生字符串


# ? * + {}: 左边有几个字符，如果有的话，贪婪匹配
# ? 左边那一个字符有0个或者1个
# print(re.findall('ab?','aab a ab abb aaaa abbb abbbbb bbbbb'))
                #      a,ab a ab ab  aaaa ab   ab

# * 左边那一个字符有0个或者无穷个
# print(re.findall('ab*','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{0,}','a ab abb abbb abbbb bbbbbb'))

# + 左边那一个字符有1个或者无穷个
# print(re.findall('ab+','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{1,}','a ab abb abbb abbbb bbbbbb'))

# {n,m} 左边的字符有n-m次
# print(re.findall('ab{3}','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{4}','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{2,3}','a ab abb abbb abbbb bbbbbb'))


# .* .*?
# .* 贪婪匹配
# print(re.findall('a.*c','a123c456c'))
# .*? 非贪婪匹配
# print(re.findall('a.*?c','a123c456c'))


# | :或运算
# print(re.findall('company|companies','Too many companies have gone bankrupt, and the next one is my company'))
# print(re.findall('compan|companies','Too many companies have gone bankrupt, and the next one is my company'))
                                      # company|companies
# print(re.findall('compan(?:ies|y)','Too many companies have gone bankrupt, and the next one is my company'))

# () :分组
# print(re.findall('ab+','abababab123'))
# print(re.findall('ab+123','abababab123'))
# print(re.findall('ab','abababab123'))
# print(re.findall('(ab)','abababab123'))
# print(re.findall('(a)b','abababab123'))
# print(re.findall('a(b)','abababab123'))

# print(re.findall('(ab)+','abababab123'))
# print(re.findall('(?:ab)+','abababab123'))

# print(re.findall('(ab)+123','abababab123'))
# print(re.findall('(?:ab)+123','abababab123'))

# print(re.findall('(ab)+(123)','abababab123'))

# print(re.findall('compan(y|ies)','Too many companies have gone bankrupt, and the next one is my company'))
# print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company'))



# re 的其他方法

# re.search 搜索
# print(re.findall('ab','abababab123'))
# print(re.search('ab','abababab123').group())
# print(re.search('ab','12aasssdddsssssssss3'))
# print(re.search('ab','12aasssdddsssssssssab3ssssss').group())

# print(re.search('ab','123ab456'))  #从头开始找，一直找到为止
# print(re.match('ab','123ab456'))   #print(re.search('^ab','123ab456'))

# re.split 切分
# print(re.split('b','abcde'))
# print(re.split('[ab]','abcde'))

# re.sub 替换
# print(re.sub('alex','SB','alex make love alex alex',1))
# print(re.subn('alex','SB','alex make love alex alex'))
# print(re.subn('alex','SB','alex make love alex alex',1))

# print(re.sub('(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','alex make love'))
# print(re.sub('(\w+)( .* )(\w+)',r'\3\2\1','alex make love'))
# print(re.sub('(\w+)(\W+\w+\W+)(\w+)',r'\3\2\1','alex make love'))

# re.compile 把正则表达式 编译 得到对象
# obj=re.compile('\d{2}')  #匹配数字2次
#
# print(obj.search('abc123eeee').group()) #12
# print(obj.findall('abc123eeee')) #12

# 过滤中文
# print(re.findall('[\u4e00-\u9fa5]','haha a b 4b 5 9 = 哈哈'))

