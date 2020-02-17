# 简单的if判断
name=input('>>: ')
if name == 'alex':
    print('SB')
else:
    print('NB')

# 将上述简单的if判断使用三元表达式的形式写在一行里:
name = input('>>: ')
print('SB' if name == 'alex' else 'NB') # 判断成功执行的放左边，失败的放右边。


name = input('>>: ')
user=('SB' if name == 'alex' else 'NB') # 也可以复职给一个变量
print(user)


# 函数return里也可以这样使用:
def my_max(x,y):
    return x if x > y else y

\注：只支持简单的if判断



