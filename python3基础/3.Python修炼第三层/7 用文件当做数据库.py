


with open('db.txt','r',encoding='utf-8') as f:
    for line in f:
        user_l=line.split(',') # split后每行都是一个列表
        print(user_l[1],int(user_l[2]))
 