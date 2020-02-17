#与匿名函数结合使用
#max,min,sorted


# # max min  #比较大小

# salaries={
# 'egon':3000,
# 'alex':100000000,
# 'wupeiqi':10000,
# 'yuanhao':2000
# }

# print(max(salaries))
# print(max(salaries.values()))

# t1=(1,'h',3,4,5,6)
# t2=(1,'y',3)
# print(t1>t2)

# t1=(100000000,'alex')
# t2=(3000,'egon')
# print(t1 > t2)

# print(max(zip(salaries.values(),salaries.keys()))[1])
# print(list(zip(salaries.values(),salaries.keys())))

# def get_value(name):
#     return salaries[name]
# print(max(salaries,key=get_value))
# l=[]
# for name in salaries:
#     # print(name)
#     res=get_value(name)
#     # print(res)
#     l.append(res)
# print(max(l))


# lambda name:salaries[name]

# print(max(salaries,key=lambda name:salaries[name]))
# print(min(salaries,key=lambda name:salaries[name]))


# # sorted
#
# salaries={
# 'egon':3000,
# 'alex':100000000,
# 'wupeiqi':10000,
# 'yuanhao':2000
# }
#
# # def get_value(name):
# #     return salaries[name]
# # print(sorted(salaries)) #按照人名排序
# # print(sorted(salaries,key=get_value)) #按照薪资排序，升序
# # print(sorted(salaries,key=get_value,reverse=True)) #按照薪资排序，降序
#
# # print(sorted(salaries,key=lambda name:salaries[name])) #按照薪资排序，升序
# # print(sorted(salaries,key=lambda name:salaries[name],reverse=True)) #按照薪资排序，降序



#filter,map,reduce

# map  #映射
# names=['alex','wupeiqi','yuanhao','yanglei','egon']
# res=map(lambda x:x+'_SB',names)
# # res=map(lambda x:x if x == 'egon' else x+'_SB',names)
# print(list(res))
#

#没必要自己写
# def my_map(func,seq):
#     for item in seq:
#         yield func(item)
#
# res1=my_map(lambda x:x+'_SB',names)
# print(next(res1))
# print(next(res1))
# print(next(res1))


# # reduce  #合并
# from functools import reduce
# print(reduce(lambda x,y:x+y,range(101)))
# # print(reduce(lambda x,y:x+y,range(101),100))


# # filter # 过滤
# names=['alex_SB','wupeiqi_SB','yuanhao_SB','yanglei_SB','egon']
# print(list(filter(lambda name:name.endswith('SB'),names)))



