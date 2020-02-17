# 1、为何要用循环
# 上节课我们已经学会用if .. else 来猜年龄的游戏啦，但是只能猜一次就中的机率太小了，如果我想给玩家3次机会呢？
# 就是程序启动后，玩家最多可以试3次，这个怎么弄呢？你总不会想着把代码复制3次吧。。。
AGE_OF_OLDBOY=73
# 第一次
guess=int(input('>>: '))
if guess > AGE_OF_OLDBOY:
    print('太大了')
elif guess < AGE_OF_OLDBOY:
    print('太小了')
else:
    print('蒙对了')
# 第二次
guess=int(input('>>: '))
if guess > AGE_OF_OLDBOY:
    print('太大了')
elif guess < AGE_OF_OLDBOY:
    print('太小了')
else:
    print('蒙对了')
# 第三次
guess=int(input('>>: '))
if guess > AGE_OF_OLDBOY:
    print('太大了')
elif guess < AGE_OF_OLDBOY:
    print('太小了')
else:
    print('蒙对了')
# 即使是小白的你，也觉得的太low了是不是，以后要修改功能还得修改3次，因此记住，写重复的代码是程序员最不耻的行为。
# 那么如何做到不用写重复代码又能让程序重复一段代码多次呢？循环语句就派上用场啦.

# for语句以遍历对象的方式构造循环，有时却需要构造一种类似无限循环的程序控制结构或某种不确定运行次数的循环，就需要使用while语句
\1、while语句结构：
　　while语句的基本形式如下：
     　　while<条件>：
         　　 <语句1>
     　　else：
          　　<语句2>
　　与for循环不同的是，while语句只有在测试条件为假时才会停止。

\break语句、continue语句、pass语句
　　break语句：用在while和for循环中，break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。
　　continue语句：用在while和for循环中，continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。 continue 语句跳出本次循环，而break跳出整个循环。
　　pass是空语句：是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句。

\2、条件循环：while，语法如下
while: 条件循环
# while 条件
#     循环体
      # 如果条件为真，那么循环体则执行，执行完毕后再次循环，重新判断条件。。。
      # 如果条件为假，那么循环体不执行,循环终止

# 打印0-3
count=0
while count  < 3:
    print('loop',count)
    count+=1

# 打印0-100
    # break: 跳出本层循，如果外层还有循环需要写多个(循环控制)
count=0
while True:
    if count > 100:
        break
    print(count)
    count+=1

# 打印0-10
    # continue: 跳出本次循环,继续下一次循环。（循环控制）
count=0
while True:
    if count > 10:
        break
    print(count)
    count+=1

count=0
while count <= 10:
    print(count)
    count+=1

# 打印从0-10，但是7不打印。
count=0
while count <= 10:
    if count == 7:
        count+=1  # 进入下一次循环之前把count加1.
        continue  # 跳出本次循环，本次循环后面的不执行了，进入下一次循环。
    print(count)
    count+=1

\打印0-10之间的偶数
count=0
while count <= 10:
    if count%2 == 0:
        print('loop',count)
    count+=1

\打印0-10之间的奇数
count=0
while count <= 10:
    if count%2 == 1:
        print('loop',count)
    count+=1

\while+else: while在没有被break时才会执行else
count=0
while count <= 10:
    if count == 3:
        break
    print(count)
    count+=1
else:      ## 中途没有被break打断才会执行。
    print('while正常结束了，没有被break打断，才会执行这里的代码')

\注意一: countinue加在循环的末尾没有意义
count=0
while count <= 5:
    print(count)
    count+=1
    #continue #加到这里没意义，加在中间才会有意义。

\注意二: 
name='egon'
password='alex3714'
count=0
while count < 3:   ## 登陆超过3次退出
    u=input('u>>:')
    p=input('p>>:')
    if u == name and p == password:
        print('login sucessful')
        break       ## 登陆成功就退出
    else:
        print('user nor password err')
        count+=1

\while嵌套if:
name='egon'
password='alex3714'
count=0
while True:
    if count == 3:
       print('尝试次数太多')
       break
    u=input('u>>:')
    p=input('p>>:')

    if u == name and p == password:
        print('login sucessful')
        break       ## 登陆成功就退出
    else:
        print('user nor password err')
        count+=1
\while嵌套：登陆成功后不要退出，输入操作命令并打印输入的命令，当输入quit时退出。
name='egon'
password='alex3714'
count=0
while True:
    if count == 3:
        break
    u = input('u>>:')
    p = input('p>>:')

    if u == name and p == password:
        print('login sucessful')
        while True:
            cmd = input('>>: ')
            if cmd == 'quit':
               break               ## 结束本层循环（把本层while退出掉了）
            print('run %s' % cmd)
        break                      ## 跳出最外层的while。
    else:
        print('user nor password err')
        count += 1

\循环嵌套与tag:使用tag=True tag=False 管理多层嵌套循环
# tag=True 
# 　　while tag:
# 　　　　......
# 　　　　while tag:
# 　　　　　　........
# 　　　　　　while tag:
# 　　　　　　　　tag=False
name='egon'
password='alex3714'
count=0
tag=True
while tag:
    if count == 3:
        break
    u = input('u>>:')
    p = input('p>>:')
    if u == name and p == password:
        print('login sucessful')
        while tag:
            cmd = input('>>: ')
            if cmd == 'quit':
                tag=False   # 控制此变量的变化会使得使用这个变量的while都会跳出循环。
                continue
            print('run %s' % cmd)
    else:
        print('user nor password err')
        count += 1

\练习，要求如下：
    1 循环验证用户输入的用户名与密码
    2 认证通过后，运行用户重复执行命令
    3 当用户输入命令为quit时，则退出整个程序
#实现一：
name='egon'
password='123'
while True:
    inp_name=input('用户名: ')
    inp_pwd=input('密码: ')
    if inp_name == name and inp_pwd == password:
        while True:
            cmd=input('>>: ')
            if not cmd:continue
            if cmd == 'quit':
                break
            print('run <%s>' %cmd)
    else:
        print('用户名或密码错误')
        continue
    break

#实现二：使用tag
name='egon'
password='123'
tag=True
while tag:
    inp_name=input('用户名: ')
    inp_pwd=input('密码: ')
    if inp_name == name and inp_pwd == password:
        while tag:
            cmd=input('>>: ')
            if not cmd:continue
            if cmd == 'quit':
                tag=False
                continue
            print('run <%s>' %cmd)
    else:
        print('用户名或密码错误')

break与continue:
#break用于退出本层循环.
while True:
    print "123"
    break
    print "456"

#continue用于退出本次循环，继续下一次循环.
while True:
    print "123"
    continue
    print "456"

while+else:
# 与其它语言else 一般只与if 搭配不同，在Python 中还有个while ...else 语句，while 后面的else 作用是指，当while 
# 循环正常执行完，中间没有被break 中止的话，就会执行else后面的语句.
count = 0
while count <= 5 :
    count += 1
    print("Loop",count)
else:
    print("循环正常执行完啦")
print("-----out of while loop ------")
输出
Loop 1
Loop 2
Loop 3
Loop 4
Loop 5
Loop 6
循环正常执行完啦
-----out of while loop ------

#如果执行过程中被break啦，就不会执行else的语句啦
count = 0
while count <= 5 :
    count += 1
    if count == 3:break
    print("Loop",count)
else:
    print("循环正常执行完啦")
print("-----out of while loop ------")
输出
Loop 1
Loop 2
-----out of while loop ------

while循环练习题
#1. 使用while循环输出1 2 3 4 5 6     8 9 10
#2. 求1-100的所有数的和
#3. 输出 1-100 内的所有奇数
#4. 输出 1-100 内的所有偶数
#5. 求1-2+3-4+5 ... 99的所有数的和
#6. 用户登陆（三次机会重试）
#7：猜年龄游戏
要求：
    允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出
#8：猜年龄游戏升级版 
要求：
    允许用户最多尝试3次
    每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
    如何猜对了，就直接退出 
#题一
count=1
while count <= 10:
    if count == 7:
        count+=1
        continue
    print(count)
    count+=1
count=1
while count <= 10:
    if count != 7:
        print(count)
    count+=1
#题目二
res=0
count=1
while count <= 100:
    res+=count
    count+=1
print(res)
#题目三
count=1
while count <= 100:
    if count%2 != 0:
        print(count)
    count+=1
#题目四
count=1
while count <= 100:
    if count%2 == 0:
        print(count)
    count+=1
#题目五
res=0
count=1
while count <= 5:
    if count%2 == 0:
        res-=count
    else:
        res+=count
    count+=1
print(res)
#题目六
count=0
while count < 3:
    name=input('请输入用户名：')
    password=input('请输入密码：')
    if name == 'egon' and password == '123':
        print('login success')
        break
    else:
        print('用户名或者密码错误')
        count+=1
#题目七
age_of_oldboy=73
count=0
while count < 3:
    guess=int(input('>>: '))
    if guess == age_of_oldboy:
        print('you got it')
        break
    count+=1
#题目八
age_of_oldboy=73
count=0
while True:
    if count == 3:
        choice=input('继续(Y/N?)>>: ')
        if choice == 'Y' or choice == 'y':
            count=0
        else:
            break
    guess=int(input('>>: '))
    if guess == age_of_oldboy:
        print('you got it')
        break
    count+=1

