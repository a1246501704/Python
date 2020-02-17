import random # 随机

print(random.random())      # (0,1)----float 大于0且小于1之间的小数，0和1都取不到。
print(random.uniform(1,3))  # 指定一个范围来取之间的小数。大于1小于3的小数，如1.927109612082716
print(random.randint(1,3))  # [1,3] 大于等于1且小于等于3之间的整数，1和3也都能取到。
print(random.randrange(1,3))# [1,3) 大于等于1且小于3之间的整数，1能取到，3取不到。range顾头不顾尾。
print(random.choice([1,'23',[4,5]]))   # 1或者23或者[4,5]，随机任意取一个元素。
print(random.sample([1,'23',[4,5]],2)) # 列表元素任意取2个组合 

item=[1,3,5,7,9]
random.shuffle(item) # 打乱item的顺序,相当于"洗牌"。
print(item)  # 会更改原来的列表中元素的顺序。


\生成随机验证码
def make_code(n):
    res=''
    for i in range(n):
        s1=str(random.randint(0,9))     # 随机取个整数，数字要想和字符串拼接需要用str转换一下。
        s2=chr(random.randint(65,90))   # 随机取大写字母，ascii码表中65～90这个范围内的是大写字母，然后用chr转换成字母。
        s3=chr(random.randint(97,122))  # 随机取大写字母，ascii码表中97～122这个范围内的是小写字母，然后用chr转换成字母。
        s4=chr(random.randint(33,47))   # 特殊符号,设置随机密码时使用
        s5=chr(random.randint(58,64))   # 特殊符号,设置随机密码时使用
        s6=chr(random.randint(91,96))   # 特殊符号,设置随机密码时使用
        s7=chr(random.randint(123,126)) # 特殊符号,设置随机密码时使用
        res+=random.choice([s1,s2,s3,s4,s5,s6,s7])  # 然后从数字和字母中随机取一个赋值给res。
    return res


print(make_code(16)) # <^bR8c;X,](ZU}p\







