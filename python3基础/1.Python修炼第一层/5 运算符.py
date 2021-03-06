计算机可以进行的运算有很多种，可不只加减乘除这么简单，运算按种类可分为:
  1、算数运算、
  2、比较运算、
  3、逻辑运算、
  4、赋值运算、
  5、成员运算、
  6、身份运算、
  7、位运算，
  8、运算符优先级

\算数运算
以下假设变量：a=10，b=20
#运算符  描述                                                实例
  +     加 - 两个对象相加                                a + b输出结果30  
  -     减 - 得到负数或是一个数减去另一个数                 a - b输出结果-10 
  *     乘 - 两个数相乘或是返回一个被重复若干次的字符串       a * b输出结果200
  /     除 - x除以y                                     a / b输出结果2
  %     取模 - 返回除法的余数                             a % b输出结果0
  **    幂等 - 返回x的y次方                              a ** b为10的20次方，输出结果100000000000000000...
  //    取整数 - 返回商的整数部分                          9//2 输出结果4，9.0//2.0输出结果4.0

# a=100
# b=31
# res=a+b

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #真正的除法，有整数，有小数
# print(a//b) #地板除，只取整数部分
# a=10
# b=3
# print(a%b) #取模，返回除法的余数
# print(3**2) 
‘’‘
131
69
3100
3.225806451612903
3
1
9
’‘’

\比较运算
以下假设变量：x=10，y=20
#运算符  描述                                                                  实例
  ==    等于 - 比较对象是否相等。                                               （x == y）返回False
  !=    不等于 - 比较两个对象是否不相等。                                        （x != y）返回True
  <>    不等于 - 比较两个对象是否不相等。                                         (x <> y)返回True。这个运算符类似!=。
  >     大于 - 返回x是否大于y。                                                 (x > y)返回False。
  <     小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的   (x < y) 返回True。
              变量True和False等价。注意，这些变量名的大些。
  >=    大于等于 - 返回x是否大于等于y。                                          (x >= y)返回False.
  <=    小于等于 - 返回x是否小于等于y。                                          (x <= b)返回true。

# age=73

# print(age > 30)
# print(age < 30)
# print(age != 30)
# print(age != 73)
# print(age == 73)

\赋值运算
以下假设变量：a=10，b=20
#运算符          描述                   实例
  =             简单的赋值运算符         c=a+b 将a+b的运算结果赋值为c
  +=            加法赋值运算符           c+=a  等效于 c=c+a
  -=            减法赋值运算符           c-=a  等效于 c=c-a            
  *=            乘法赋值运算符           c*=a  等效于 c=c*a
  /=            除法赋值运算符           c/=a  等效于 c=c/a
  %=            取模法赋值运算符          c%=a  等效于 c=c%a
  **=           幂法赋值运算符           c**=a  等效于 c=c**a
  //=           取整法赋值运算符          c//=a  等效于 c=c//a

# height=180
# height+=1 #height=height+1
# print(height)

\逻辑运算
#运算符    描述                                                           实例
  and     布尔“与” - 如果x为False，x and y返回False，否则它返回y的计算值。     (a and b)都为真才返回True   
  or      布尔“或” - 如果x为True，它返回True。否则它返回y的计算值。             (a or b)有一个为真就返回True
  not     布尔“非” - 如果x为True，它返回False。如果x为False，它返回True。取反   not(a and b)返回False

# age=11
# name='egon'
# print(age > 10 and name == 'ego111111n')
# print(age > 10 or name == 'ego111111n')
# print(not age >10) # 将结果取反

\身份运算（判断id）
# 运算符	     描述	                                          实例
is	      is 是判断两个标识符是不是引用自一个对象。       	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	  is not 是判断两个标识符是不是引用自不同对象。   	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
#is比较的是id,而==比较的是值。
>>> x=1234567890
>>> y=1234567890
>>> id(x)
140206023973008
>>> id(y)
140206023972960 
if x is y:
  print('id不同')

if x == y:
  print('值相同') # id不同，值可以相同。id如果相同值肯定相同。

\成员运算
# 运算符	          描述	                                           实例
in	    如果在指定的序列中找到值返回 True，否则返回 False。	   x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

\运算符优先级
以下表格列出了从最高到最低优先级的所有运算符：
# 运算符	      描述
**	         # 指数 (最高优先级)
~ + -	       # 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //	   # 乘，除，取模和取整除
+ -	         # 加法减法
>> <<	       # 右移，左移运算符
&	           # 位 'AND'
^ |	         # 位运算符
<= < > >=	   # 比较运算符
<> == !=	   # 等于运算符
= %= /= //= -= += *= **=	# 赋值运算符
is is not	   # 身份运算符
in not in	   # 成员运算符
and or not	 # 逻辑运算符

python基础之数据类型与变量：https://www.cnblogs.com/linhaifeng/articles/5935801.html#_label34