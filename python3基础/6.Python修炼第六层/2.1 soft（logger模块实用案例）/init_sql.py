import json

#初始化数据库
# dic={
#     'egon':{'password':'123','balance':3000},
#     'alex':{'password':'alex3714','balance':4000},
#     'ysb':{'password':'dsb','balance':5000},
# }

# json.dump(dic,open(r'C:\Users\Administrator\PycharmProjects\19期\day6\soft\db\db.json','w'))




#连接上数据，拿到数据对象
dic=json.load(open(r'C:\Users\Administrator\PycharmProjects\19期\day6\soft\db\db.json','r'))


print(dic.get('egon'))
print(dic.get('egon123123')) # 用get的方式取字典里的值没有不会报错。